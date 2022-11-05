import serial
import serial.tools.list_ports
import datetime
import time

print("Priključite microbit prije nego što započnete")
ulaz = input("Napišite START kako biste započeli: ")

while True:
    if ulaz == "START":

        #sending date and time
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            try:
                ser = serial.Serial(p, 9600, timeout=.1)
                break
            except:
                if ports.index(p) == len(ports)-1:
                    print("Mikrobit nije prikopčan na aktivan port. Ponovo pokrenite program i pokušajte ponovo")
                    quit()
                else:
                    continue
        time.sleep(1)
        slanje = (f"{datetime.datetime.now().hour} {datetime.datetime.now().minute} {datetime.datetime.now().second} {datetime.datetime.now().day} {datetime.datetime.now().month} {datetime.datetime.now().year}")
        ser.write(slanje.encode())

        #waiting for response from microbit
        while True:
            data = ser.readline()
            if data:

                #writing out gathered data from microbit
                if data[-1] == "Gathered data":
                    data.pop(-1)
            else:
                continue
    else:
        while ulaz != "START":
            ulaz = input("Pogreška u unosu, napišite START kako biste započeli")
