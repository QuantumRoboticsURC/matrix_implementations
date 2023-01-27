#!/usr/bin/env python3
import rospy
    
import time
import board
import neopixel_spi as neopixel
from std_msgs.msg import Int64 
from geometry_msgs.msg import Twist


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    pixels.fill((0, 0, 0))
    pixels.show()
    #GRB
    # 1 = R, 2 = B, 3 = G
    if data.data == 0:
        pixels.fill((0, 0, 0))
    elif data.data == 1:
        pixels.fill((0, 50, 0))
    elif data.data == 2:
        pixels.fill((0, 0, 50))
    elif data.data == 3:
        for i in range (10):
            pixels.fill((0, 0, 0))
            pixels.show()
            time.sleep(.25)
            pixels.fill((50, 0, 0))
            pixels.show()
            time.sleep(.25)
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(.25)     
        pixels.fill((0, 50, 0))    
    pixels.show()
    
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/autonomous/status_led", Int64, callback, queue_size=1)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()





if __name__ == '__main__':

    NUM_PIXELS = 64
    PIXEL_ORDER = neopixel.RGB
    COLORS = (0x000000, 0xFF0000, 0x00FF00, 0x0000FF)
    DELAY = 0.01

    spi = board.SPI()

    pixels = neopixel.NeoPixel_SPI(spi,
                                NUM_PIXELS,
                                pixel_order=PIXEL_ORDER,
                                auto_write=False)

    listener()
