
import fluo


# sketch.py
def setup():
    size(400, 400)
    
def draw():
    background(0)
    stroke(255)
    textSize(32)

    # Get hour, minuites, and seconds    
    h = hour()
    m = minute()
    s = second() 

    translate(200,200)
    
    
    rotate(radians(-90))

    sAngle = map(s,0,60,0,360)
    rotate(radians(sAngle))
    # Diplay on the screen, need to convert integer to string
    text(str(h) + ":" + str(m) + ":" + str(s), 0 , 32)
    
    
    
    
    
     #fluo.showGrid(w = 200,h = 200)
        
    
