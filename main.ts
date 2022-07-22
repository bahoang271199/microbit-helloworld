input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 4; index++) {
        pins.servoWritePin(AnalogPin.P2, 0)
        basic.pause(100)
        pins.servoWritePin(AnalogPin.P2, 44)
        basic.pause(100)
    }
})
music.onEvent(MusicEvent.MelodyEnded, function () {
    pins.digitalWritePin(DigitalPin.P1, 0)
})
input.onButtonPressed(Button.B, function () {
    music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Once)
})
music.onEvent(MusicEvent.MelodyNotePlayed, function () {
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.servoWritePin(AnalogPin.P2, 0)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.servoWritePin(AnalogPin.P2, 44)
    basic.pause(200)
})
basic.showString("Hello!")
pins.digitalWritePin(DigitalPin.P1, 0)
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.No)
})
