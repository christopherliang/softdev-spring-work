var democrat = 1;
var isInArray = function(d,a) {
    return a.indexOf(d) > -1;
};
var democratNumber = [548, 291, 251, 246, 210, 182, 160, 147, 142, 121, 118, 118, 117, 116, 109, 96, 93, 92, 85, 84, 78, 75, 74, 71, 67, 60, 59, 59, 52, 46, 43, 43, 42, 41, 37, 37, 37, 37, 35, 33, 32, 31, 30, 30, 27, 27, 26, 25, 23, 20, 18, 17, 12, 12, 11, 11, 1];

var democratState = ["California", "New York", "Texas", "Florida", "Pennsylvania", "Illinois", "Ohio", "Michigan", "New Jersey", "North Carolina", "Maryland", "Washington", "Georgia", "Massachussets", "Virginia", "Wisconsin", "Minessota", "Indiana", "Arizona", "Missouri", "Colorado", "Tennessee", "Oregon", "Connecticut", "Puerto Rico", "Alabama", "Kentucky", "Louisiana", "South Carolina", "Iowa", "District of Columbia", "Nevada", "New Mexico", "Oklahoma", "Mississippi", "Arkansas", "Kansas", "Utah", "West Virginia", "Hawaii", "Rhode Island", "New Hampshire", "Delaware", "Maine", "Nebraska", "Idaho", "Montana", "Vermont", "South Dakota", "North Dakota", "Alaska", "Wyoming", "Democrats Abroad", "Guam", "Virgin Islands", "American Samoa", "Northern Marianas", "Unassigned"];

var alloted = ["Iowa", "New Hampshire", "South Carolina", "Nevada", "Alabama", "Alaska", "Arkansas", "Georgia", "Massachussets", "Minnesota", "Oklahoma", "Tennessee", "Texas", "Vermont", "Virginia", "Kansas", "Kentucky", "Louisiana", "Maine", "Puerto Rico", "Hawaii", "Idaho", "Michigan", "Mississippi", "District of Columbia", "Wyoming", "Florida", "Illinois", "Missouri", "North Carolina", "Northern Marianas", "Ohio"];

var democratGraph = function() {
    d3.select("body").select(".chart").selectAll("div").remove();
    d3.select("body").select(".chart").selectAll("div")
        .data(democratNumber)
        .enter()
        .append("div")
        .text(".")
        .style("width",0)
        .style("opacity",0)
        .transition()
            //.delay(function(d,i) { return i * 100})
            .duration(2000)
            .style('width',function(d) { return (d * 2) + "px";}) 
            .style('background-color',function(d) {
                var a = democratNumber.indexOf(d);
                if (isInArray(democratState[a],alloted)) {
                    return 'green';
                } else {
                    return 'red';
                }
            })
        .style("padding","10px")
        .style("border","solid 1px")
        .style("border-bottom-right-radius","2em")
        .text( function(d,i) { 
            return d + " votes in " + democratState[i]; 
        })
        .style("opacity",1);
};

democratGraph();

