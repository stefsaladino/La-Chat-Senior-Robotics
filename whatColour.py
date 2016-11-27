#written by Daniella Swanepoel, Eamon Farhat, Willem van Gerwen

from read_adc_mcp3008 import *

#number is the max number for the reflective value
BLACK = 80

def whatColour():
    # read the analog pin
    adc_1 = readadc(ch1_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    adc_2 = readadc(ch2_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    adc_3 = readadc(ch3_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    adc_4 = readadc(ch4_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    channels = [adc_1, adc_2, adc_3, adc_4]
    colours = [0,0,0,0]
    
    for i in range(len(channels)):
        if (channels[i] < BLACK):
            colours[i]= "BLACK"
        else:
            colours[i]= "COLOUR"
    return colours
