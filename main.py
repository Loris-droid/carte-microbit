from microbit import *
import radio
radio.config(group=1)
while True :
        message = radio.receive()
        if message:
            display.scroll(message)
        if button_a.is_pressed():
            display.scroll('A')
        radio.send('A')
        if button_b.is_pressed():
            display.scroll('B')
        radio.send('B') 
