def on_button_pressed_a():
    for index in range(4):
        pins.servo_write_pin(AnalogPin.P2, 0)
        basic.pause(100)
        pins.servo_write_pin(AnalogPin.P2, 44)
        basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_melody_ended():
    pins.digital_write_pin(DigitalPin.P1, 0)
music.on_event(MusicEvent.MELODY_ENDED, on_melody_ended)

def on_button_pressed_b():
    music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
        MelodyOptions.ONCE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_melody_note_played():
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.servo_write_pin(AnalogPin.P2, 0)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.servo_write_pin(AnalogPin.P2, 44)
    basic.pause(200)
music.on_event(MusicEvent.MELODY_NOTE_PLAYED, on_melody_note_played)

basic.show_string("Hello!")
pins.digital_write_pin(DigitalPin.P1, 0)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.show_icon(IconNames.NO)
basic.forever(on_forever)
