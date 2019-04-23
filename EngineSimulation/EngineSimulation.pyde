
def setup():
    size(840, 600)

def polar_line(x,y, r, theta):
    line(x,y, x+r*cos(radians(theta)), y+r*sin(radians(theta)))
    
    
x = 0
def draw():
    global x
    TDC = -100
    BDC = 100
    background(255)
    noFill()
    
    y = map(cos(radians(x)), -1, 1, TDC, BDC)
    
    # Cylinders
    cylinder_x = 100
    cylinder_y = 250
    rect(width/2 - cylinder_x/2, height/2 - cylinder_y/2, cylinder_x, cylinder_y)
    fill(0)
    
    # Piston
    piston_x = cylinder_x
    piston_y = cylinder_y/3
    rect(width/2 - piston_x/2, height/2 - piston_y/2 - y, piston_x, piston_y)
    
    line(piston_x, piston_y, cylinder_x, cylinder_y)
    
    x += 5
