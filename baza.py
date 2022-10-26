# import modules
from microbit import *
import radio
#import log    # debug/comment

# set local variables for time as hour, minute, seconds
# change variables for case
hour = 22
minute = 29
second = 50

# set radio group and turn radio on
radio.config(group=1)
radio.on()

# show SQUARE if micro:bit is ready
display.show(Image.SQUARE)    # debug/comment

# test data logging
# log.set_labels('time', 'id', 'temp')    # debug/comment

# loop repeats forever
while True:
    
    # set hours by pressing button A
    if button_a.is_pressed():
        hour += 1
        if hour > 23:
            hour = 0
        display.scroll(hour)
        display.show(":")
        sleep(100)   # debug/comment
    
    # set minutes by pressing button B
    if button_b.is_pressed():
        minute += 1
        if minute > 59:
            minute = 0
        display.scroll(minute)
        display.show(":")
        sleep(100)   # debug/comment

    # switch into send/receive mode by shaking micro:bit
    if accelerometer.was_gesture('shake'):
        while True:
            display.show(Image.CONFUSED)   # display CONFUSED if in send/receive
            sleep(1000)
            # increase seconds, minutes and hours
            second += 1
            if second >= 60:
                minute += 1
                second = 0
            if minute >= 60:
                hour += 1
                minute = 0
            if hour >= 24:
                hour = 0
            
            # send request to sub units
            print(str(hour),":",str(minute),":",str(second))   # debug/comment
            if second == 0 and minute % 30 == 0:   # production
            #if second % 11 == 0:   # dev/test
                radio.send("+")
                display.show("+")   # debug/comment
                sleep(100)   # debug/comment
                # print("request sent")   # debug/comment
            
            # when response is received
            response = radio.receive()
            if response:
                time = str(hour) + ":" + str(minute) + ":" + str(second)
                id = str(response).split(":")[0]
                temp = str(response).split(":")[1]

                # show sub unit's id to confirm received response
                display.show(id)   # debug/comment
                display.scroll(response)   # debug/comment
                display.clear()   # debug/comment
                
                # log responses received
                # log.add({'time': time, 'id' : id, 'temp': temp})