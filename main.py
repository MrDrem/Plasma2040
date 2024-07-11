import plasma
from plasma import plasma2040
import time
import random

# Import helpers for RGB LEDs, Buttons, and Analog
from pimoroni import RGBLED, Button, Analog

# Set how many LEDs you have
NUM_LEDS = 89

led = RGBLED(plasma2040.LED_R, plasma2040.LED_G, plasma2040.LED_B)
led.set_rgb(0, 0, 0)
led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT, rgbw=True)
led_strip.set_rgb(0, 0, 0, 0)

bright = 0

user_sw = Button(plasma2040.USER_SW)
button_a = Button(plasma2040.BUTTON_A)
button_b = Button(plasma2040.BUTTON_B)

led_strip.start()

# Define the colors
#randset = (0, 0, 0, 0)
#colours = [(255, 0, 0, 0), (0, 255, 0, 0), (0, 0, 255, 0), (0, 0, 0, 255), randset]

# Initialize the color index
current_color_index = -1

for i in range(NUM_LEDS):
    led_strip.set_rgb(i, 0, 0, 0, 0)

while True:
    if user_sw.read():
        print("Pressed User SW - {}".format(time.ticks_ms()))
        # Cycle to the next color
        randset = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 0)
        colours = [(255, 0, 0, 0), (0, 255, 0, 0), (0, 0, 255, 0), (0, 0, 0, 255), randset]
        current_color_index = (current_color_index + 1) % len(colours)
        r, g, b, w = colours[current_color_index]
        for i in range(NUM_LEDS):
            led_strip.set_rgb(i, r, g, b, w)
        print(f"Color changed to RGBW: {r}, {g}, {b}, {w}")
        time.sleep(0.5)  # Add a delay to avoid rapid color changes        

    if button_a.read():
        bright = bright+.1
        if bright == 1.1:
            bright = 0
        print("Pressed A - {}".format(time.ticks_ms()))
        led.set_rgb(int(0*bright), int(255*bright), int(0*bright))
        for i in range(NUM_LEDS):
            led_strip.set_rgb(i, int(0*bright), int(255*bright), int(0*bright), int(0*bright))
        
    if button_b.read():
        print("Pressed B - {}".format(time.ticks_ms()))
        led.set_rgb(0, 0, 255)
