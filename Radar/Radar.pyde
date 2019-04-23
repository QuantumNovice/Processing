

def setup():
    global r
    size(600, 400)
    r = sqrt( (width/2)**2 + (height/2)**2)

ctr = 0


def draw():
    global ctr
    background(0)
    polargrid()
    strokeWeight(5)
    theta = radians(ctr)
    stroke(242, 21, 9)
    line(0, 0, r*cos(theta), r*sin(theta))
    ctr -= 5
    

def polargrid():
    stroke(66, 244, 122)
    strokeWeight(2)
    noFill()
    translate(width/2, height/2)
    for theta in range(0, 360, 20):
        circle(0, 0, 2*theta)
        theta = radians(theta)
        line(0, 0, r*cos(theta), r*sin(theta))
    
