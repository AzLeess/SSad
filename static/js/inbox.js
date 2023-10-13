//Date and time
var today = new Date();
var dateDisplay = document.querySelector("#date");
var timeDisplay = document.querySelector("#time");
var weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
var day = weekday[today.getDay()];
var dd = String(today.getDate()).padStart(2,"0");
var months = ["January", "February", "March", "April", "May", "June", "July", "August","September", "October", "November", "December"]
var month = months[today.getMonth()];
var yy = today.getFullYear();
var time = today.getHours() + ":" + today.getMinutes();
dateDisplay.innerHTML = day + " " + dd + " " + month + ", " + yy;
timeDisplay.innerHTML = time;

//Private chat scroll
var items = $(".private-chat li");
var dashboard = document.querySelector(".dashboard-container");

// Event Listeners
$(".nav-link").on("click", (e)=>{
  var tab = e.target;
  $(".nav-link").removeClass("active");
  $(tab).addClass("active");
  changeTab(e.target);
});

$("i").on("mouseenter", (e)=>{
  $(e.target).addClass("fas");
  $(e.target).removeClass("far");
})

$("i").on("mouseout", (e)=>{
  $(e.target).addClass("far");
  $(e.target).removeClass("fas");
})

$("li.notif").on("click", ()=> {

  $(".section").css("display", "none");
  $(".chat-body").css("display", "block");
  //var room = "#room"+$(".inbox li").attr("id");
  //$(room).css("display","block")
})

window.addEventListener("load", callbackFunc);
window.addEventListener("resize", callbackFunc);
window.addEventListener("scroll", callbackFunc);
// $(".private-chat").on("scroll", callbackFunc());

//Functions
function isItemInView(item){
  var rect = item.getBoundingClientRect();
  return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

function callbackFunc() {
    for (var i = 0; i < items.length; i++) {
      if (isItemInView(items[i])) {
        items[i].classList.add("show");
      }
    }
  }

function changeTab(tab){
  if (tab.innerHTML === "More"){
    console.log("more");
  } else {
    $(".section").css("display", "none");
  switch(tab.innerHTML){
    case 'Compose':
      console.log("Compose clicked");
      $(".compose-body").css("display", "block");
      break;
    case 'Inbox':
      console.log("Inbox clicked");
      $(".inbox-body").css("display", "block");
      break;
    case 'Send file':
      console.log("send file clicked");
      $(".send_file-body").css("display", "block");
      break;
    case 'genchat':
      console.log("Sent clicked");
       $(".genchat-body").css("display", "block");
      break;
    case 'Drafts':
      console.log("Drafts clicked");
      $(".drafts-body").css("display", "block");
      break;
    case 'Trash':
      console.log("Trash clicked");
      $(".trash-body").css("display", "block");
      break;
    case 'More':
      console.log("More clicked");
      break;
    default:
  }
  }
  
}