
def setup():
    size(640, 380)
    
A = 0
x = 100
l = 60
r = 40
l_max = l
r_max = r

def draw():
    global A,x,l,r
    translate(width/4, height/2)
    rotate(radians(180))
    background(255)
    
    # Position of Momentum
    x = r*cos(A) + sqrt(l**2 - r**2 * sin(A)**2)
    
    # Length of Rod
    l = sqrt(r**2 + x**2 - 2*r*x*cos(A))
    
    # R
    line(0, 0, r*sin(A), r*cos(A))
    # L
    line(r*sin(A), r*cos(A), 0, x)
    
    
    # postion of piston
    #x = r*cos(A) + sqrt(l**2 - r**2 * sin(A)**2)
    #line(0, 0, 0, x)
    #print(x)
    fill(0)
    rect(-30, x, 60, 10)
    noFill()
    
    beginShape()
    vertex(-30, r_max)
    vertex(-30, l_max+r_max+30)
    vertex(30, l_max+r_max+30)
    vertex(30, r_max)
    endShape()
    
    A += 0.1
