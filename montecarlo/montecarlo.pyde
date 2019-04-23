

def setup():
    size(400, 400)

inside = 1.0
outside = 1.0

def draw():
    global inside, outside
    translate(width/2, height/2)
    x = random(-100, 100)
    y = random(-100, 100)
    
    if sqrt(x**2 + y**2) <=  100:
        fill(123,123,255)
        circle(x,y, 10)
        inside += 1
    else:
        fill(255 , 124, 140)
        circle(x, y, 10)
        outside += 1
    print( 4*(inside/(inside+outside)) )
