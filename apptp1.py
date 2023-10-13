
from socket import socket
from flask import Flask , render_template , url_for ,request,session,redirect,make_response
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
from sqlalchemy import delete,create_engine
import os
#from vf import mirroir ,affine,cesar_dg , cesar_gd
from flask_socketio import SocketIO,send,emit
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

import rsa,V2_SSAD,binaire,alphanum,mdp5chiffres,decalage,vff,stenographie,encode,decode,rasame

users ={}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = create_engine("sqlite:///database.db")

#configuration de la bd + de l'application web
app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
socket = SocketIO(app, cors_allowed_origins='*')


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# adding zip fonction to jinja2
@app.template_global(name='zip')
def _zip(*args, **kwargs): #to not overwrite builtin zip in globals
    return __builtins__.zip(*args, **kwargs)


#definition de la classe qui contiendra les users et les mdps


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

#definition de la classe message
class message(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(20), nullable=False)
    receiver = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime,default=datetime.utcnow())
    

#########

@app.route('/')
@login_required
def index():
    return render_template('index.html')

##################register



@ app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        
        hashed_password = bcrypt.generate_password_hash(request.form['pwd'])
        new_user = User(username=rasame.public(request.form['user']), password=hashed_password)
        print(rasame.public(request.form['user']))
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('index'))
    else :
        return render_template('register.html')


### login 
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method =='POST':
        user = User.query.filter_by(username=request.form['user']).first()
        if user:
            if bcrypt.check_password_hash(user.password, request.form['pwd']):
                login_user(user)
                resp = make_response(redirect('/'))
                resp.set_cookie("username",request.form['user'])
                print(request.cookies.get("username"))
                return resp #redirect(url_for('index'))
    return render_template('login.html',action='/login')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

#cryptage et decryptage des messages envoyees entre utilisateurs 



@app.route('/steno-res')
@login_required
def cards():
        #print(os.listdir("static/hidden/"))
        img_list = os.listdir("static/hidden/")
        music_list = os.listdir("static/uploads")
        rmusic =[]
        for music in music_list:
            if music.split(".")[-1] == "mp3":
                rmusic.append(music)
        #print (music_list)
        #print(rmusic)
        slides=[]
        secret = []
        for i in range(1,len(img_list)+1):
           slides.append('side-'+str(i))
        for img in img_list:
            secret.append(stenographie.discover("static/hidden/"+img))
        #print(secret)

        return render_template('steno.html',slides=slides,imgs=img_list,secrets=secret,)


############send message 

@app.route('/msg')
@login_required
def msg():
    #deli = message.query.filter_by(receiver='maya').all()
    db.session.query(message).filter(message.receiver=='maya').delete()
    db.session.commit()
    #db.session.delete(deli)
    #db.session.commit()
    return 'deleted'
@app.route('/c')
@login_required
def c():
    return current_user.username



#creating groupe chat endcoded
@socket.on('message')
def handle_message(msg):
    print(msg)
    if not msg.endswith("connected"):
        msg_cry = V2_SSAD.encode_miroir(msg.split(":")[1])
        msg_cry = " crypted :" + msg_cry
        send(msg_cry.split("_")[0],broadcast=True)
        send(msg,broadcast=True)
    else :
       send(msg,broadcast=True) 

@socket.on('username', namespace='/private')
def receive_username(username):
    print("\n\nusers  : ")
    users[username] = request.sid
    print(users)
    #users.append({username : request.sid})
    #print(users)
    print('Username added!')

@socket.on('private_message', namespace='/private')
def private_message(data):
    users[data['sender']] = request.sid
    print(data)
    recipient_session_id = users[data['username']]
    message = data['message']
    sender = data['sender']
    #phase de cryptage:
    if data["methodecry"]=="decalage" :
        msg_cry =  decalage.encode_decalage(message,data["sens"],int(data["b"]))
        print(msg_cry)
        print(decalage.decryptage(msg_cry))
    elif data["methodecry"]=="miroir" :
        msg_cry = V2_SSAD.encode_miroir(message)
        print(msg_cry)
        print(V2_SSAD.decryptage(msg_cry))
    elif data["methodecry"]=="cesar" :
        msg_cry = V2_SSAD.encode_cesar(message,data["sens"],int(data["b"]))
        print(msg_cry)
        print(V2_SSAD.decryptage(msg_cry))
    elif data["methodecry"]=='affine' :
        if 0 != int(data["a"]):
            msg_cry =vff.code_affine(message,int(data["a"]),int(data["b"]))
        else:
            msg_cry = decalage.encode_decalage(message,data['sens'],int(data["b"]))
        print("here " +msg_cry)
        if 0 ==int(data["a"]):
            print(decalage.decryptage(msg_cry))
        else :
            print(vff.decode_affine(msg_cry))

    


    argu = { 'message' : message , 'sender':sender , 'crypted' :msg_cry  }
    #print(argu)
    emit('new_private_message', argu , room=recipient_session_id)



@app.route("/genchat")
@login_required
def genchat():
    return render_template("genchat.html",username=current_user.username)


@app.route("/attaques",methods=['GET','POST'])
@login_required
def attaques():
    if request.method == 'GET':
        return render_template("attaques.html")
    else : 
        if request.form["type"] == '3-binaires':
            resp = binaire.mdp3(request.form['mdp'])
        elif request.form["type"] == '5-chifres':
            resp = mdp5chiffres.mdp5f(request.form['mdp'])
        else:
            resp = alphanum.md5a(request.form['mdp'])


        return render_template("attaques.html",resp = resp)





#init inbox 
@app.route('/inbox',methods=["POST","GET"])
@login_required
def inbox() :
        if request.method=="GET":
                resp = make_response(render_template('inbox.html'))
                resp.set_cookie("username",current_user.username)
                return resp 
        else :
            print(request.form["hide"])
            if 'file' not in request.files:
                return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            if filename.split(".")[-1] != "mp3":
                stenographie.hide(request.form["hide"],"static/uploads/"+filename,"static/hidden/")
            else : 
                if os.path.exists("static/uploads/"+filename):
                    print("found")
                    #encode.code(request.form["hide"],"static/uploads/steg.PNG","static/uploads/"+filename)
            return redirect(url_for('inbox'))


if __name__ == "__main__" :
    socket.run(app)