def on_button_pressed_a():
    global Osvetljenje
    Osvetljenje += -1
    if Osvetljenje < 0:
        Osvetljenje = 0
    basic.show_number(Osvetljenje)
    pins.analog_write_pin(AnalogPin.P0, Snaga)
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    global Osvetljenje
    Osvetljenje += 1
    if Osvetljenje > 9:
        Osvetljenje = 9
    basic.show_number(Osvetljenje)
    pins.analog_write_pin(AnalogPin.P0, Snaga)
input.on_button_pressed(Button.B, on_button_pressed_b)
Snaga = 0
Osvetljenje = 0
Min = 100
Max = 1023
Korak = Math.idiv(Max - Min, 9)
Osvetljenje = 0
basic.show_number(Osvetljenje)
def on_forever():
    global Snaga
    if Osvetljenje == 0:
        Snaga = 0
    else:
        Snaga = Min + Osvetljenje * Korak
basic.forever(on_forever)
