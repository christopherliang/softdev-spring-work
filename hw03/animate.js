// All the document element variables
var canvas = document.getElementById("playground"),
    circlebtn = document.getElementById("circle"),
    dvdbtn = document.getElementById("dvd"),
    stopbtn = document.getElementById("stop"),
    // Canvas and other variables
    ctx = canvas.getContext("2d"),
    radius = 0,
    growing = true,
    pColor = "red",
    stop = false,
    globalID,
    x = canvas.width/2-40,
    y = canvas.height/2-22.5,
    cx = 1.8,
    cy = -1;

var logo = new Image();
logo.src="logo_dvd.jpg";

// Draw function
var draw = function() {
    if (!stop) {
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
    } else {
        stop = false;
    }
    ctx.clearRect(0,0,canvas.width,canvas.height);
    ctx.beginPath();
    ctx.fillStyle=pColor; 
    ctx.arc(canvas.width/2,canvas.height/2,radius,0,2*Math.PI);
    ctx.closePath();
    ctx.fill();
    globalID = window.requestAnimationFrame(draw);
};

var stopper = function() {
    if (!stop) {
        stop = !stop;
    }
    window.cancelAnimationFrame(globalID);
    window.cancelAnimationFrame(dvd_image);
}

var bounce = function() {
    if (!stop) {
        ctx.clearRect(0,0,canvas.width,canvas.height);
        if ((x >= (canvas.width - 80)) || (x <= 1)) {
            cx = -cx;
        }
        if ((y >= (canvas.height - 45)) || (y <= 1)) {
            cy = -cy;
        }
        x += cx;
        y += cy;
    } else {
        stop = false;
    }
    ctx.drawImage(logo,x,y,80,45);
    dvd_image = window.requestAnimationFrame(bounce);
}


//Event listeners
circlebtn.addEventListener("click", draw);
stopbtn.addEventListener("click", stopper);
dvdbtn.addEventListener("click", bounce);
