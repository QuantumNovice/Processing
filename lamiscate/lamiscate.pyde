
def setup():
    size(600, 400)
    

def draw():
    background(255)
    translate(width/2, height/2)
    scale(10)
    strokeWeight(0.2)
    p1, p2 = lamiscate()
    list_line(p2+p1)
    fill(255)
    print(p2[-2][0], p2[-2][1], 10)
    


def lamiscate():
    part1 = []
    part2 = []
    for x in range(-100, 100):
        y = sqrt(x**2 - x**4 / 200)
        part1.append((x,y))
    for x in range(-100, 100):
        y = -sqrt(x**2 - x**4 / 200)
        part2.append((x,y))
    return part1,part2

def list_line(Z):
    for i in range(len(Z)):
        if i < len(Z)-1:
            line(Z[i][0],Z[i][1], Z[i+1][0], Z[i+1][1])
