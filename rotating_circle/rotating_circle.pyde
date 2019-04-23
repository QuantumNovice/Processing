
def setup():
    size(600, 480, P3D)
    
theta = 0
def draw():
    background(0)
    global theta
    noFill()
    strokeWeight(15)
    #stroke(random(255),random(255),random(255))
    stroke(128, 210, 24)
    translate(width/2, height/2)
    #rotateY(degrees(theta))
    rotateZ(degrees(theta))
    circle(50, 50, 200)
    theta += 40
    
