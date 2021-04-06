var navbarContainer = document.getElementById("nav-bar");
var navbarItems = document.getElementsByClassName("nav-bar-button");
var navbarDots = document.getElementsByClassName("nav-dot");

for (var i = 0 ; i < navbarItems.length; i++) {

    if(i==2){
        navbarItems[i].addEventListener("click", function() {
            var currentNav = document.getElementsByClassName("nav-bar-active");
            if (currentNav[0]) currentNav[0].className = currentNav[0].className.replace(" nav-bar-active", "");
            
            var currentDot = document.getElementsByClassName("nav-dot-active");
            if (currentDot[0]) currentDot[0].className = currentDot[0].className.replace(" nav-dot-active", "");
        }); 
    }else{
        navbarItems[i].addEventListener("click", function() {
            var currentNav = document.getElementsByClassName("nav-bar-active");
            if (currentNav[0]) currentNav[0].className = currentNav[0].className.replace(" nav-bar-active", "");
            this.className += " nav-bar-active";
            
            var currentDot = document.getElementsByClassName("nav-dot-active");
            if (currentDot[0]) currentDot[0].className = currentDot[0].className.replace(" nav-dot-active", "");
            this.children[1].className += " nav-dot-active";
        });
    }

  }
