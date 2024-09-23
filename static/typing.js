// typing.js file
// don' forget to fix the prompt
function check_win(){
    if (words.length < 1){
        return true;
    }
    return false;
}

function timer(x){
    var time = 0 + document.getElementById('timer').innerHTML
    if (time > 0){
        time--;
        document.getElementById('timer').innerHTML = time + ''
    }
    else{
        clearInterval(x)
        document.getElementById("timer").innerHTML = 'Times up!'
        finish()
    }
}

function finish(){
    const h = document.getElementById("started")
    h.innerHTML = 'Play Again!';
    document.getElementById("starter").onclick = function reset (){location.reload();}
    if (check_win()){
        document.getElementById("promt").innerHTML = 'GOOD JOB!'
    }
    else{
        document.getElementById("promt").innerHTML = " Try, Try Again"
    }
}