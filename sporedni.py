from microbit import *
import radio

#Korisnik namjesta id microbita
id = 2
while True:
    if button_a.was_pressed():
        id += 1
    elif button_b.was_pressed():
        break
    
radio.config(group=1)
radio.on()

while True:
    message = radio.receive()
    display.scroll(str(id))   # Provjerava radi li kod
    if message == "+":
        display.show(message)   # Provjerava radi li kod
        sleep(id*100)   # Obavezno treba ostati (microbitu treba vremen)
        response = (str(id) + ":" + str(temperature()))
        radio.send(response)
        display.scroll(str(temperature()))   # debug/comment
