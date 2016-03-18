var data = [4,8,15,16,23,42];
d3.select(".chart")
  .selectAll("div")
    .data(data)
  .enter().append("div")
    .style("width",function(d) { 
	//return d * 10 + "px"; 
	return foo(d) + "px";
    })
    .text(function(d) { 
	return d;
    });

//scale bars
var foo = d3.scale.linear()
    .domain([0, d3.max(data)])
    .range([
