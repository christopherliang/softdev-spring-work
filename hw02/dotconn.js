// All the document element variables
var canvas = document.getElementById("playground");
var clearbtn = document.getElementById("clear");
var dotCount = document.getElementById("num");
var lastCount = document.getElementById("last");

// Canvas and Int variables
var ctx = canvas.getContext("2d");
var cursorX,cursorY,pColor;
var pX = pY = -1;
var num = last = 0;

// Draw function
var draw = function(e) {
    // Get mouse coordinates
    cursorX = e.offsetX;
    cursorY = e.offsetY;
    // If NOT the first circle, connect new circle to previous circle
    if (pX != -1) 
        connectCircle();
    // Generate random color
    pColor='#'+(Math.random()*0xFFFFFF<<0).toString(16); 
    // Begin path for redrawing of circle.
    // Redrawing of circle overlaps the line connecting this circle
    // to the previous circle.
    ctx.beginPath();
    ctx.fillStyle=pColor; 
    ctx.arc(cursorX,cursorY,20,0,2*Math.PI);
    ctx.closePath();
    ctx.fill();
    // Sets circle coordinates as previous coordinates for the next 
    // circle drawing
    pX = cursorX;
    pY = cursorY;
    // Adds 1 the number of circles
    // Changes score on HTML 
    num++;
    dotCount.innerHTML = num;

    console.log('Circle #' + num + ': ('+cursorX+','+cursorY+')');
};

// Connects previous circle with new circle drawn
var connectCircle = function() {
    ctx.strokeStyle=pColor;
    // Start path for connection line
    ctx.beginPath();
    ctx.moveTo(pX,pY);
    ctx.lineTo(cursorX,cursorY);
    // If "Boring" is checked, connections will be made by a line
    if (document.getElementById("l").checked) {
        ctx.closePath
        ctx.stroke();
    }
    // If "Cool" is checked, connections will be made by a fill
    if (document.getElementById("f").checked) {
        ctx.lineTo(cursorX+10,cursorY+10);
        ctx.closePath();
        ctx.fill();
    }
    // Start path for new circle
    ctx.beginPath();
    ctx.fillStyle=pColor;
    ctx.arc(pX,pY,20,0,2*Math.PI);
    ctx.fill();
    ctx.closePath();
};

// Clear screen function
var clearScreen = function() {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    pX = pY = -1;
    lastCount.innerHTML = last = num;
    num = dotCount.innerHTML = 0;
};

//Event listeners
canvas.addEventListener("click", draw);
clearbtn.addEventListener("click", clearScreen);
