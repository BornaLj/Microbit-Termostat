import serial
import datetime
import time

print("Priključite microbit prije nego što započnete")
ulaz = input("Napišite START kako biste započeli")

while True:
    if ulaz == "START":

        #sending date and time
        ser = serial.Serial("COM3", 9600, timeout=.1)
        time.sleep(1)
        slanje = (f"{datetime.datetime.now().hour} {datetime.datetime.now().minute} {datetime.datetime.now().second} {datetime.datetime.now().day} {datetime.datetime.now().month} {datetime.datetime.now().year}")
        ser.write(slanje)

        #waiting for response from microbit
        while True:
            data = ser.readline()
            if data:

                #writing out gathered data from microbit
                if data[-1] == "Gathered data":
                    data.pop(-1)
    else:
        while ulaz != "START":
            ulaz = input("Pogreška u unosu, napišite START kako biste započeli")
