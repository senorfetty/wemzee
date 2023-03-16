const rmCheck =
document.getElementById('rememberMe'),usernameinput= document.getElementById('username');

if(localStorage.checkbox && localStorage.checkbox !== ''){
    rmCheck.setAttribute('checked','checked');
    usernameinput.value= localStorage.username;
} else {
    rmCheck.removeAttribute('checked');
    usernameinput.value= '';
}
function IsRememberMe(){
    if (rmCheck.checked && usernameinput.value !== '') {
        localStorage.username = usernameinput.value;
        localStorage.checkbox = rmCheck.value;
    } else {
        localStorage.username= '';
        localStorage.checkbox= '';
    }
}


function Show() {
    var pass = document.getElementById('password');
    if (pass.type === 'password') {
        pass.type = 'text';
    } else {
        pass.type = 'password';
    }
}