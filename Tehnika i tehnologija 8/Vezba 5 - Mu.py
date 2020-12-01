from microbit import *
crveni_pin = pin0
žuti_pin = pin1
zeleni_pin = pin2
while True:
    žuti_pin.write_digital(0)
    crveni_pin.write_digital(1)
    sleep(8000)
    crveni_pin.write_digital(0)
    žuti_pin.write_digital(1)
    sleep(2000)
    žuti_pin.write_digital(0)
    zeleni_pin.write_digital(1)
    sleep(8000)
    zeleni_pin.write_digital(0)
    žuti_pin.write_digital(1)
    sleep(2000)
