from microbit import *
import random
Ugao = 0
Razlika = 0
Cilj = random.randrange(360)
Smiley = Image("05050:"
               "00000:"
               "00500:"
               "50005:"
               "05550")
compass.calibrate()
display.show(Smiley)
while True:
    while button_a.is_pressed() == False:
        Ugao = compass.heading()
        Razlika = abs(Cilj - Ugao)
        pin0.write_digital(1)
        sleep(Razlika * 5)
        pin0.write_digital(0)
        sleep(Razlika * 5)
    if Razlika < 15:
        display.scroll("Tacan ugao!")
        Cilj = random.randrange(360)
    else:
        display.scroll("Pokusaj ponovo.")
