# import modules
from microbit import *
import radio
#import log    # debug/comment

data = ""
uart.init(9600)
encoding = "utf-8"

display.show(Image.DIAMOND)

while True:
    ulaz = uart.read()
    if ulaz == None:
        continue
    else:
        Time = str(ulaz, encoding).split(" ")
        break

hour = int(Time[0])
minute = int(Time[1])
second = int(Time[2])
day = int(Time[3])
month = int(Time[4])
year = int(Time[5])
limit = int(Time[6])
display.clear()

# set radio group and turn radio on
radio.config(group=1)
radio.on()

# show SQUARE if micro:bit is ready
display.show(Image.SQUARE)    # debug/comment

# test data logging
# log.set_labels('time', 'id', 'temp')    # debug/comment

# loop repeats forever
while True:

    display.show(Image.HAPPY)
    while True:
            
        #Extracting the data
        if button_b.was_pressed():
            data = data + "Gathered data"
            uart.write(data)
            sleep(2000)
            reset() #resets microbit after data extraction (2 sec delay for saftey)
   
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
            day += 1
            hour = 0
            
        #Changing the month and the year
        if month == 2:
            if year%4 == 0 and day == 29:
                month += 1
                day = 1
            elif day == 28:
                month += 1
                day = 1
            elif month in [1, 3, 5, 7, 8, 10, 12] and day == 31:
                if month == 12:
                    year += 1
                    month = 1
                    day = 1
                else:
                    month += 1
            elif month in [2, 4, 6, 9, 11] and day == 30:
                month += 1

            
        # send request to sub units
        print(str(hour),":",str(minute),":",str(second))   # debug/comment
        if second == 0 and minute%30 == 0:   # production
        #if second % 11 == 0:   # dev/test
            radio.send("+")
            time = str(hour) + ":" + str(minute)
            date = str(day)+"."+str(month)+"."+str(year)+"."
            id = "1"
            temp = temperature()
            if int(temp) >= limit:
                message = str(id) + "," + str(date) + "," + str(time) + "," + str(temp) + "|" + "Warning"
                uart.write(message)
            data = data + str(id) + "," + str(date) + "," + str(time) + "," + str(temp) + "|"
                
            display.show("+")   # debug/comment
            sleep(100)   # debug/comment
            # print("request sent")   # debug/comment
            
        # when response is received
        response = radio.receive()
        if response:
            time = str(hour) + ":" + str(minute)
            date = str(day)+"."+str(month)+"."+str(year)+"."
            id = str(response).split(":")[0]
            temp = str(response).split(":")[1]
            if int(temp) >= limit:
                message = str(id) + "," + str(date) + "," + str(time) + "," + str(temp) + "|" + "Warning"
                uart.write(message)
                    
            data = data + str(id) + "," + str(date) + "," + str(time) + "," + str(temp) + "|"
