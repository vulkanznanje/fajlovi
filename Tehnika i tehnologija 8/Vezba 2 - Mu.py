from microbit import *

while True:
    if button_a.is_pressed():
        LightsOn = Image("05050:"
                         "00000:"
                         "00500:"
                         "50005:"
                         "05550")
    elif button_b.is_pressed():
        display.scroll("Zdravo, svete!")
