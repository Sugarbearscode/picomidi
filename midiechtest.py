from machine import Pin,UART
import time

#  standard mapping for the UART to MIDI is ..
#  UART 0 = Midi OUT (also mapped to the second MIDI Out)
#  UART 1 = Midi IN
#  There are two MIDI OUTs on the MIDIMUSO, One MIDI IN and one MIDI THRU
#  (The MIDI THRU replicates what comes in the MIDI in to the MIDI THRU)


uart1 = UART(0, baudrate=31250, tx=Pin(0), rx=Pin(1))
uart2 = UART(1, baudrate=31250, tx=Pin(4), rx=Pin(5))
uart1.init(bits=8, parity=None, stop=1)
led = Pin("LED", Pin.OUT)
while True:
    if uart1.any() > 0:
        data = uart1.read(1)
        uart1.write(data)
        uart2.write(data)
        led.toggle()
