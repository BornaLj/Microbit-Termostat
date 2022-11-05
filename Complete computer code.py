import serial
import datetime
import time
import serial.tools.list_ports

print("Priključite microbit prije nego što započnete")
ulaz = input("Napišite START kako biste započeli")

while True:
    if ulaz == "START":

        #determining open serial port
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
        
        #sending date and time
        time.sleep(1)
        slanje = (f"{datetime.datetime.now().hour} {datetime.datetime.now().minute} {datetime.datetime.now().second} {datetime.datetime.now().day} {datetime.datetime.now().month} {datetime.datetime.now().year}")
        ser.write(slanje.encode())

        #waiting for response from microbit
        while True:
            data = ser.readline()
            if data:
                
                #Transforming string data into list
                data = data.split("|")
                data2 = []
                for element in data:
                    element = element.split(",")
                    data2.append(element)
                
                data = data2.copy()

                #writing out gathered data from microbit
                if data[-1][0] == "Gathered data":
                    data.pop(-1)

                    #preparing data in a specific form | data = {id:{date:{time:temp}}}
                    newData = {}
                    newData2 = {}
                    lista = []
                    rječnik = {}
                    rješeno = False
                    
                    #determining the max amount of microbits
                    for x in range(len(data)):
                        lista.append(int(data[x][0]))

                    n = max(lista)

                    #grouping sublists by microbit id
                    for i in range(1, n+1):
                        lista = []
                        for j in data:
                            if int(j[0]) == i:
                                lista.append(j[1:])
                        newData.update({str(i):lista})

                    #making the final dictionary
                    for a,b in newData.items():
                        rječnik = {}
                        zapis = {}
                        for c in range(len(b)):
                            if rješeno == True:
                                rješeno = False
                                continue
                            else:
                                try:
                                    if b[c][0] == b[c+1][0]:
                                        datum = b[c][0]
                                        rješeno = True
                                        zapis = {datum:{b[c][1]:b[c][2], b[c+1][1]:b[c+1][2]}}
                                        rječnik.update(zapis)
                                    else:
                                        datum = b[c][0]
                                        zapis = {datum:{b[c][1]:b[c][2]}}
                                        rječnik.update(zapis)
                                except:
                                    datum = b[c][0]
                                    zapis = {datum:{b[c][1]:b[c][2]}}
                                    rječnik.update(zapis)
                                    continue
                        newData2.update({a:rječnik})

                    #storing the value as "data" in order to avoid confusion
                    data = newData2.copy()
    else:
        #prevention from typing wrong commands
        while ulaz != "START":
            ulaz = input("Pogreška u unosu, napišite START kako biste započeli")
