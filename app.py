
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



users ={}

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



############send message 


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


    argu = { 'message' : message , 'sender':sender  }
    #print(argu)
    emit('new_private_message', argu , room=recipient_session_id)



@app.route("/genchat")
@login_required
def genchat():
    return render_template("genchat.html",username=current_user.username)


#init inbox 
@app.route('/inbox',"GET")
@login_required
def inbox() :
        resp = make_response(render_template('inbox.html'))
        resp.set_cookie("username",current_user.username)
        return resp 
        

if __name__ == "__main__" :
    socket.run(app)