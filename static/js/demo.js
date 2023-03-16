let i=0;

function timed(){
    i++;
    postMessage(i);
    setTimeout('timed()',1000);
}
        
export {timed};