from microbit import *
import radio

# !!! change unit id !!!
id = 1   

radio.config(group=1)
radio.on()

while True:
    message = radio.receive()
    display.show(id)   # debug/comment
    if message == "+":
        display.show(message)   # debug/comment
        sleep(id*100)   # do not remove this line
        response = (str(id) + ":" + str(temperature()))
        radio.send(response)
        display.scroll(str(temperature()))   # debug/comment