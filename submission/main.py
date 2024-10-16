import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

while True:
    userColourVal = input("\nMENU: Would you like to use the red(1), green(2) or blue(3) colour?: ")
    if userColourVal == "q" | userColourVal == "Q": # if input is q or Q, 
        break
    try:
        userColourVal = int(userColourVal)
    except:
        print("A number was not entered")
        continue
    if userColourVal == 1:
        pickedColour = (255, 0, 0) # red
    elif userColourVal == 2:
        pickedColour = (0, 255, 0) # green
    elif userColourVal == 3:
        pickedColour = (0, 0, 255) # blue
    else:
        print("Not a valid number (1-3)")
        continue
    while max > 0:
    
        for i in range(10):
            cp.pixels[i] = userColourVal
        cp.pixels.show()
        time.sleep(0.3)

        max = max - 1
