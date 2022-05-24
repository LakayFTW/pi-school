function handleSwitchDarkLight(){
    var body = document.getElementById("body");

    if(body.classList[0] == "light-mode"){
        console.log("test");
        body.classList.replace("light-mode", "dark-mode");
    }
    else{
        body.classList.replace("dark-mode", "light-mode");
    }


    if(body.classList[0] == "dark-mode"){
        document.cookie = "daynight=dark-mode";
    }
    else{
        document.cookie = "daynight=light-mode";
    }
}

function checkForCookies(){
    var daynightcookie = getCookie("daynight");
    var body = document.getElementById("body");
    
    if(document.cookie.indexOf("daynight=") == -1){
        document.cookie = "daynight=light-mode";
    }
    if(daynightcookie == "dark-mode"){
        body.classList.replace("light-mode", "dark-mode");
    }
    if(daynightcookie == "light-mode"){
        body.classList.replace("dark-mode", "light-mode");
    }
}

function getCookie(cname){
    let name = cname + "=";
    let split = document.cookie.split(";");
    for(var j= 0; j < split.length; j++){
        let char = split[j];
        while (char.charAt(0) == ' ') {
            char = char.substring(1);
        }
        if (char.indexOf(name) == 0) {
            return char.substring(name.length, char.length);
        }
    }
    return "";
}