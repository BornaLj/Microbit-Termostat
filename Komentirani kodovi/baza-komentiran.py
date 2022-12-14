# Potrebni moduli za rad s microbitom i microbit radijem
from microbit import *
import radio

#Priprema za komunikaciju između baze i računala
data = ""
uart.init(9600) #Frekvencija prenošenja bitova u određenom vremenu
encoding = "utf-8"

#Provjera radi li kod
display.show(Image.DIAMOND)

#Provjera primanja poruke od računala
while True:
    ulaz = uart.read()
    if ulaz == None:
        continue
    else:
        Time = str(ulaz, encoding).split(" ") #Prima stvarno vrijeme
        break
#Raspoređuje poruku na različite varijable
hour = int(Time[0])
minute = int(Time[1])
second = int(Time[2])
day = int(Time[3])
month = int(Time[4])
year = int(Time[5])
limit = int(Time[6]) #Temperatura koju je korisnik odabrao na početku
display.clear()

# Uključivanje funkcije radija i namještanje na radio liniju 1
radio.config(group=1)
radio.on()



# Zauvijek se ponavlja
while True:

    display.show(Image.HAPPY) #Provjerava radi li kod
    while True:
            
        #Vađenje podataka
        if button_b.was_pressed():
            data = data + "Gathered data"
            uart.write(data)
            sleep(2000)
            reset() #Resetira microbit nakon vađenja podataka (2 sekunde duljina iz sigurnosnih razloga)
   
        display.show(Image.CONFUSED)   # Provjerava radi li kod
        sleep(1000)
        # Povećavanje varijabli za vrijeme (služi za mjerenje vremena)
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
            
        #Mijenjanje mjeseci i godina
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

            
        # Slanje zahtjeva sporednim microbitima
        print(str(hour),":",str(minute),":",str(second))   # Provjera rad li kod
        if second == 0 and minute%30 == 0:   # Zbog ovog se mjeri svakih 30 minuta
            radio.send("+")
            time = str(hour) + ":" + str(minute)
            date = str(day)+"."+str(month)+"."+str(year)+"."
            id = "1"
            temp = temperature()
            if int(temp) >= limit: #Gleda je li temperatura prešla odabranu temperaturu
                message = str(id) + "," + str(date) + "," + str(time) + "," + str(temp) + "|" + "Warning|"
                uart.write(message)
            data = data + str(id) + "," + str(date) + "," + str(time) + "," + str(temp) + "|"
                
            display.show("+")   # Provjera radi li kod
            sleep(100)   
         
            
        # Kada je dobiven odgovor (response) složi novi string
        response = radio.receive()
        if response:
            time = str(hour) + ":" + str(minute)
            date = str(day)+"."+str(month)+"."+str(year)+"."
            id = str(response).split(":")[0]
            temp = str(response).split(":")[1]
            if int(temp) >= limit: #Gleda je li temperatura prešla odabranu temperaturu
                message = str(id) + "," + str(date) + "," + str(time) + "," + str(temp) + "|" + "Warning|"
                uart.write(message)
                    
            data = data + str(id) + "," + str(date) + "," + str(time) + "," + str(temp) + "|"
