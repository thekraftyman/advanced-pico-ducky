# rp2040_boards.py

__author__ = "thekraftyman"

"""
A set of board classes to easily program for multiple specific rp2040 boards
"""

import pwmio
import board

class RP2040Board:
    """
    Base class for all boards
    """
    def __init__( self, led_pin ):
        self._led_pin = led_pin
        self._led = self._led = pwmio.PWMOut( led_pin, frequency=5000, duty_cycle=0 )

    @property
    def led_pin( self ):
        return self._led_pin

    @property
    def led( self ):
        return self._led

    def led_breathe( self ):
        ''' locks into an infinite loop. watch out! '''
        while True:
            self.led_down()
            self.led_up()

    def led_down( self ):
        for i in range( 100 ):
            if i >= 50:
                self.led.duty_cycle = 65535 - int(( i - 50 ) * 2 * 65535 / 100)
            time.sleep( 0.01 )

    def led_up( self ):
        for i in range( 100 ):
            if i < 50:
                self.led.duty_cycle = int( i * 2 * 65535 / 100 )
            time.sleep( 0.01 )


class Tiny2040(RP2040Board):
    """
    The Tiny2040 from pimoroni
    """

    def __init__( self ):
        super().__init__( board.GP20 )
