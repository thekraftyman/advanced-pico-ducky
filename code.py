import digitalio
from ducky_engine import DuckyEngine
from board import *
from rp2040_boards import Tiny2040

def main():
    engine = DuckyEngine()
    rp_board = Tiny2040()
    prog_status = bool(engine.get_programming_status())

    # run the payload
    if not prog_status:
        payload = select_payload()
        print("Running ", payload)
        engine.run_file( payload )
        print( "Done" )
    else:
        print( "Update payload" )

    rp_board.led_breathe()

def select_payload():
    payload = "payload.dd"
    # check switch status
    # payload1 = GPIO4 to GND
    # payload2 = GPIO5 to GND
    # payload3 = GPIO10 to GND
    # payload4 = GPIO11 to GND
    payload1Pin = digitalio.DigitalInOut(GP4)
    payload1Pin.switch_to_input(pull=digitalio.Pull.UP)
    payload1State = not payload1Pin.value
    payload2Pin = digitalio.DigitalInOut(GP5)
    payload2Pin.switch_to_input(pull=digitalio.Pull.UP)
    payload2State = not payload2Pin.value
    payload3Pin = digitalio.DigitalInOut(GP10)
    payload3Pin.switch_to_input(pull=digitalio.Pull.UP)
    payload3State = not payload3Pin.value
    payload4Pin = digitalio.DigitalInOut(GP11)
    payload4Pin.switch_to_input(pull=digitalio.Pull.UP)
    payload4State = not payload4Pin.value

    if(payload1State == True):
        payload = "payload.dd"
    elif(payload2State == True):
        payload = "payload2.dd"
    elif(payload3State == True):
        payload = "payload3.dd"
    elif(payload4State == True):
        payload = "payload4.dd"
    else:
        # if all pins are high, then no switch is present
        # default to payload1
        payload = "payload.dd"

    return payload

main()
