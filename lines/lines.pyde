
class atom:
    def __init__(self, w, h):
        self.p = PVector(random(w), random(h))
        self.v = PVector(5*random(1), 5*random(1))
        self.dia = 4
        self.p_last = []
        
    
    def show(self):
        self.boundary()
        #stroke(255)
        strokeWeight(self.dia)
        point(self.p.x, self.p.y)
        
        self.p_last.append((self.p.x, self.p.y, (random(255), random(255), random(255))))
        
        self.p += self.v
        if len(self.p_last) >= 2:
            for i in range(len(self.p_last)-1):
                stroke(self.p_last[-1][0], self.p_last[-1][1]))#, 34)#,self.p_last[-1][2])
                line(self.p_last[i][0], self.p_last[i][1], self.p_last[i+1][0], self.p_last[i+1][1])
        
    def boundary(self):
        if self.p.x > width-10 or self.p.x < 0+10:
            self.v.x *= -1
        if self.p.y > height-10 or self.p.y < 0+10:
            self.v.y *= -1
            
    def is_colliding(self, instance):
        if sqrt((self.p.x - instance.p.x)**2 + (self.p.y - instance.p.y)**2) <= self.dia+10:
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
