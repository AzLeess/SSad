var today = new Date();
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

$(document).ready(function() {
    var socket = io.connect("http://localhost:5000")
    socket.on("connect" , function (){
        console.log(getCookie("username"))
        socket.send(getCookie("username")+" connected");
    });
    socket.on('message',function(msg){
        console.log(msg)
        $(".genchat").append($('<li>').text(msg));
    });
    $("#sendBTN").on('click', function(){
        console.log("cliked");
        socket.send($('#username').val()+ " : " +$('#message').val());
        $("#message").val('');
    });
    $('#smessage').on('click', function() {
        console.log("smessage");
        var message = getCookie("username") + ": "+ $('#message1').val() ;
        $('#message1').val("");
        socket.send( message);
    
    });
})

var private_socket = io('http://127.0.0.1:5000/private')

$('#send_username').on('click', function() {
    console.log("emited username");
    private_socket.emit('username', $('#username').val());
});

$('#send_private_message').on('click', function() {
    console.log("cliked");
    var recipient = $('#send_to_username').val();
    var message_to_send = $('#private_message').val();
    var selectedmethode = $("#methode").children("option:selected").val();
    var slectedsens = $('#sens').children("option:selected").val();
    var parametre_a = $("#numbera").val();
    var parametre_b = $("#numberb").val();

    private_socket.emit('private_message', {'username' : recipient, 'message' : message_to_send , 'sender' : getCookie("username"), methodecry : selectedmethode , sens:slectedsens , a :parametre_a , b:parametre_b});
});

private_socket.on('new_private_message', function(argu) {
    console.log(argu)
    var received_chat = "<li class='show' ><div><p>"+argu['sender'] +"</p><p>"+argu['message'] +"</p><time>"+today.getDate()+"/"+today.getHours()+"/"+today.getMinutes()+"</time></div></li>"
    var received_crypted = "<li class='show' ><div><p>"+argu['sender'] +"</p><p>"+argu['crypted'] +"</p><time>"+today.getDate()+"/"+today.getHours()+"/"+today.getMinutes()+"</time></div></li>"
    var notif ='<li class="notif" ><div class="email unread" ><div class="email-left"><img><div class="email-subject"><p>'+argu['sender'] +'</p><p>Private chat</p></div></div><div class="star"><i class="far fa-star"></i><time>'+today.getHours()+" : "+today.getMinutes()+'</time></div></div></li>'
    console.log(received_chat)
    $(".inbox ul").append(notif)
    $(".private-chat ul").append(received_crypted)
    $(".private-chat ul").append(received_chat)
});


// genchat socket 







 