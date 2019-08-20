console.log("Sketch started");

function setup() {
    console.log("setup");
    document.body.style.userSelect = 'none';
    let c = createCanvas(windowWidth, windowHeight);
    c.position(0, 0);
    c.style('pointer-events', 'none');
    stroke(0);
    strokeWeight(4);
}

function draw() {
    
    if(mouseIsPressed)
        line(mouseX, mouseY, pmouseX, pmouseY);
    
}