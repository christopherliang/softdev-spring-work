// Sets variable "c" to element "c" in HTML (the canvas)
var c = document.getElementById("ftb2maga");

// Gets the 2d surface of the canvas and sets it to the variable
var ctx = c.getContext("2d");

// Sets the color of the fill
ctx.fillStyle = "#0000FF";

// Sets size of filled rectangle using dimensions
// (X-position, Y-position, Length, Width)
ctx.fillRect(50,50,200,200);

// Sets color of stroke (not filled)
ctx.strokeStyle = "blue";

// Sets size and dimensions of stroke rectangle
// (X-position, Y-position, Length, Width)
ctx.strokeRect(10,10,200,200);

// Starts the creation of a shape
ctx.beginPath();

// Sets the origin point for the shape
ctx.moveTo(10,10);

// Moves the endpoint of the line to a new coordinate
ctx.lineTo(50,50);

// New endpoint without connecting it with the last endpoint
ctx.lineTo(50,250);
ctx.lineTo(10,210);
// Connects last point with the starting point
ctx.closePath();
ctx.fillStyle="green";
// Fills in shape created by points
ctx.fill();

ctx.beginPath();
ctx.moveTo(10,10);
ctx.lineTo(210,10);
ctx.lineTo(250,50);
ctx.lineTo(50,50);
ctx.closePath();
ctx.fillStyle="red";
ctx.fill();

ctx.strokeStyle="yellow";
// Draws lines from points that are connected on the same path
ctx.stroke();

ctx.beginPath();
// Draw arc/circle (x center,y center,radius,start angle, end angle)
ctx.arc(150,150,80,0,2*Math.PI);
ctx.fillStyle="black";
ctx.fill();
ctx.closePath();

// Set the font size and font style
ctx.font = "50px trebuchet";
// Sets the text of the font and the x,y coordinates
ctx.fillText("Box with hole",40,300);
