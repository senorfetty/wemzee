



let fem= document.getElementById('prac');
// MODIFY CONTENT
// fem.textContent = 'Welcome TRavs'
// fem.innerHTML= fem.innerHTML + ' ' + 'SASA';
// fem.style.color= 'yellow';

// document.getElementById('prac').innerHTML = 'Date :' + Date();
// document.getElementById('prac').style.color= 'green';
// document.write('Tarehe ya Leo Mwaionaje??');


function validateForm(){
    let x= document.forms['frm1']['first'].value;
    let y= document.forms['frm1']['last'].value;
    let z= document.getElementById('age').value;
    let text
    if (x =='' || y == '' || z == '' && isNaN(z) || z<1|| z>44){ //VALID INPUTS NAME && AGE
        alert('INVALID FORM');
        return false;
    } else{
        text= 'Input OK';
    }
}

function btn(){
    onclick= document.getElementById('first').style.color = 'red'
}


//ANIMATION
function myMove() {
    let id=null;
    elem=document.getElementById('animate');
    selem= document.getElementById('anime');
    let pos= 0;
    clearInterval(id);
    id= setInterval(frame,5);

    function frame() {
        if (pos == 350) {
            clearInterval(id);      //test or animation is finished, end the test
        } else {
            pos++;
            elem.style.top= pos + 'px';
            elem.style.left= pos + 'px';
            selem.style.top= pos + 'px';
            selem.style.right= pos + 'px';
        }
    }
}



function bt() {
    s= document.getElementById('prac');
    s.innerHTML= 'WE MZEE';

}

function display(){
    l=document.getElementById('s')
    l.innerHTML=Date()
}


// onchange to upper
function upper(){
    u= document.getElementById('first');
    u.value= u.value.toUpperCase();
}

// eventlistener



function evnt(){
    m=document.getElementById('mybtn');
    m.addEventListener('mousemove' , shi);
    m.addEventListener('click', shw); //shw is a future function
    m.addEventListener('click', sha); 
   

    function shi(){
        l= document.getElementById('show');
        l.innerHTML += 'FCK YOU'
    }

    function shw(){
        alert('WAS POPPIN MA NIGGAA');
    }
    function sha(){
        l= document.getElementById('show');
        l.innerHTML= 'NIGGA YOU GAAAY'
    }
}



function coll(){
    z= document.getElementsByTagName('label');
    for (i=0; i<z.length; i++){
        z[i].style.color= 'Yellow';
    }
}


function conf(){
    var text;
    if(confirm('Are You Sure you want to Submit?') == true){
        text= 'OK'; 
    } else {
        return false;
    }
}
conf()


m= setInterval(zoea,1000)
function zoea(){
    d= new Date();
    document.getElementById('sauti').innerHTML= d.toLocaleTimeString();
}

function func(){
     const x= document.getElementById('no');
    if( !x.checkValidity()){
        document.getElementById('sh').innerHTML= x.validationMessage;
    } else {
        document.getElementById('sh').innerHTML= 'INPUT SHWARI';
    }
}

let w;
function start(i){
    if (typeof(w) == 'undefined'){
        w= new Worker();
    }
    w.onmessage= function(event) {
        document.getElementById('deadline').innerHTML= event.data;
    };
}

function stop(){
    w.terminate();
    w = undefined;
}

// let s= ('https://editorial.rottentomatoes.com/guide/popular-movies/');

// fetch (s)
// .then(x => x.text())
// .then(y => document.getElementById('dem').innerHTML= y);
// // .then(y => document.getElementById('dem').innerHTML = y);


getText('https://editorial.rottentomatoes.com/guide/popular-movies/');

async function getText(file){
    let x= await fetch(file);
    let y= await x.text();
    console.log(y);
}

// fetch (s)

// .then(x => x.text())
// .then(y => document.getElementById('dem').innerHTML= y);
// .then(y => document.getElementById('dem').innerHTML = y);


x= document.getElementById('loc');
function geo(){
    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(showPosition);
    } else {
        x.innerHTML = 'NOT SUPPORTED'
    }
}
function showPosition() {
    let ll = position.coords.latitude + "," + position.coords.longitude;

    let img_url = "https://maps.googleapis.com/maps/api/staticmap?center="+ll+"&zoom=14&size=400x300&sensor=false&key=YOUR_KEY";
    document.getElementById("loc").innerHTML = "<img src='"+img_url+"'>";
}







// function age(){
//     let z= document.getElementById('age').value;
//     let text;
//     if (isNaN(z) || z<1|| z>44)  {
//         alert('Input INVALID');
//     } else{
//         text= 'Input OK';
//     }
// }