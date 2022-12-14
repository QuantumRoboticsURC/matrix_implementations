

import time
import board
import neopixel_spi as neopixel


NUM_PIXELS = 64
PIXEL_ORDER = neopixel.RGB
COLORS = (0x000000, 0xFF0000, 0x00FF00, 0x0000FF)
DELAY = 0.01

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(spi,
                               NUM_PIXELS,
                               pixel_order=PIXEL_ORDER,
                               auto_write=False)


pixels.fill((50, 30, 10))
pixels.show()
#pixels[0] = (255, 0, 0)
#pixels.show()
