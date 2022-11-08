#Moduli potrebni za rad s microbitom i microbit radijem
from microbit import *
import radio

#Korisnik namješta id microbita
id = 2
while True:
    if button_a.was_pressed():
        id += 1
    elif button_b.was_pressed():
        break
#Paljenje radija i postavljanje svih microbita na istu radijo vezu     
radio.config(group=1)
radio.on()
#Primanje poruke i slanje povratne informacije (temperatura u tom trenutku)
while True:
    message = radio.receive()
    display.scroll(str(id))   # Provjerava radi li kod
    if message == "+":
        display.show(message)   # Provjerava radi li kod
        sleep(id*100)   # Obavezno treba ostati (microbitu treba vremena da ispuni zadatke)
        response = (str(id) + ":" + str(temperature()))
        radio.send(response)
        display.scroll(str(temperature()))   # debug/comment
