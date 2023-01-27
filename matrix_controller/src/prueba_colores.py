import time
import board
import neopixel_spi as neopixel
from adafruit_pixel_framebuf import PixelFramebuffer

NUM_PIXELS = 64
pixel_width = 8
PIXEL_ORDER = neopixel.RGB
COLORS = (0x000000, 0xFF0000, 0x00FF00, 0x0000FF)
DELAY = 0.1


spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(spi,
                               NUM_PIXELS, brightness = 0.5,
                               pixel_order=PIXEL_ORDER,
                               auto_write=False)
pixels.fill((50, 0, 0))
pixels.show()
time.sleep(1)
pixels.fill((0,0,0))
pixels.show()
# Green
#pixels.fill((50, 30, 10))

# Red
pixels.fill((0, 50, 0))
pixels.show()
time.sleep(1)

pixels.fill((0,0,0))
pixels.show()
# Blue
pixels.fill((0, 0, 50))
pixels.show()
time.sleep(1)


# Turn them off.
pixels.fill((0,0,0))
pixels.show()

#The pixel on the corner down left green
# pixels[0] = (255, 0, 0)

#The pixel on the corner up left green
#pixels[7] = (255, 0, 0)

#pixels.fill(0)
#pixels.show()
#time.sleep(1)

pixels.deinit()



#pixels = PixelFramebuffer(spi,
#			  8,
#			  8,
#                          orientation=VERTICAL,
#                          rotation=2)
#
		
#pixels.text("Try", 3, 4, 0x00FF00)
#pixels.display()
