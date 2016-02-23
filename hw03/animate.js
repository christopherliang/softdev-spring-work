// All the document element variables
var canvas = document.getElementById("playground"),
    circlebtn = document.getElementById("circle"),
    stopbtn = document.getElementById("stop"),
    // Canvas and other variables
    ctx = canvas.getContext("2d"),
    radius = 0,
    stop = false,
    growing = true,
    trails = false,
    pColor = "red",
    globalID;

// Draw function
var draw = function() {
    if (growing == true) {
        if (radius < (canvas.width / 2)) {
            radius++;
        } else {
            growing = false;
            pColor='#'+(Math.random()*0xFFFFFF<<0).toString(16); 
        }
    } else {
        if (radius == 0) {
            growing = true;
            pColor='#'+(Math.random()*0xFFFFFF<<0).toString(16); 
        } else {
            radius--;
        }
    }
    ctx.clearRect(0,0,canvas.width,canvas.height);
    ctx.beginPath();
    ctx.fillStyle=pColor; 
    ctx.arc(canvas.width/2,canvas.height/2,radius,0,2*Math.PI);
    ctx.closePath();
    ctx.fill();
};

var animate = function() {
    draw();
    globalID = window.requestAnimationFrame(animate);
}

var stopper = function() {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    growing = false;
    radius = 0;
    window.cancelAnimationFrame(globalID);
}

//Event listeners
circlebtn.addEventListener("click", animate);
stopbtn.addEventListener("click", stopper);
