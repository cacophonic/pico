import time, random
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28),15)

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Colour variables
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0
pink = 255,20,147
black = 0,0,0

colours = [red, green, blue]

delay = 0.5
state = False
    
def updateState(success):
    global delay
    global state
    if (success == True):
        strip.fill(green)
        delay = delay - 0.05
    else:
        strip.fill(red)
        delay = 0.5
    strip.write()
    time.sleep(1)
    state = False

while True: # Run forever
    print(state)
    if state == False:
        strip.fill(black)
        strip.write()
        colour = colours[random.randint(0,2)]
        position = random.randint(3,14)
        strip[position] = colour
        strip.write()
        state = True
        
    for i in range(0,15):
        
        if i > position:
            updateState(False)
            break
        
        for j in range(0,255,5):
            strip[i] = (j,j,0)
            strip.write()
            time.sleep(0.0025)
            
        time.sleep(delay) # Short Delay
        
        for j in range(255,0,-5):
            strip[i] = (j,j,0)
            strip.write()
            time.sleep(0.0025)
        
        strip[i] = black
        strip.write()
        
        if button1.value() == 1:
            updateState(position == i and colour == red)
            break
            
        if button2.value() == 1: 
            updateState(position == i and colour == green)
            break
            
        if button3.value() == 1: 
            updateState(position == i and colour == blue)
            break
