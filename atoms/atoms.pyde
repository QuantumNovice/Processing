
class atom:
    def __init__(self, w, h):
        self.p = PVector(random(w), random(h))
        self.v = PVector(5*random(1), 5*random(1))
        self.dia = 20
        #print(random(1))
    
    def show(self):
        self.boundary()
        stroke(255)
        strokeWeight(self.dia)
        point(self.p.x, self.p.y)
        self.p += self.v
        
    def boundary(self):
        if self.p.x > width-10 or self.p.x < 0+10:
            self.v.x *= -1
        if self.p.y > height-10 or self.p.y < 0+10:
            self.v.y *= -1
            
    def is_colliding(self, instance):
        if sqrt((self.p.x - instance.p.x)**2 + (self.p.y - instance.p.y)**2) <= self.dia+20:
            return True
        return False

def collision_handler(objects, instance):
    for ball in objects:
        if instance.is_colliding(ball):
            #instance.v.x *= -1
            #ball.v.x *= -1
            # Conservation of momentum
            instance.v.x, ball.v.x = ball.v.x, instance.v.x
        

def setup():
    global atoms
    size(600, 400)
    atoms = [atom(width, height) for i in range(20)]
    
    

def draw():
    background(54)
    for a in atoms:
        collision_handler(atoms, a)
    for a in atoms:
        a.show()
    #print(atoms[-1].is_colliding(a))
