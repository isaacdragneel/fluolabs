# sketch.py
def setup():
    global rcolor,s,ps,x,y
    size(400, 400)
    rcolor = color(random(255),random(255),random(255))
    
    s = second()
    ps = s - 1
    
    
    x = 0
    y = 32
    
def draw():
    global s,ps,rcolor,x,y
    background(0)
    stroke(255)
    textSize(32)

    # Get hour, minuites, and seconds    
    h = hour()
    m = minute()
    s = second()
    
      
    if(s != ps):
        rcolor = color(random(255),random(255),random(255))
        ps = s
        fill(rcolor)
        
        x = random(width)
        y = random(height)
        
    # Diplay on the screen, need to convert integer to string
    text(str(h) + ":" + str(m) + ":" + str(s), x , y)
        
        
