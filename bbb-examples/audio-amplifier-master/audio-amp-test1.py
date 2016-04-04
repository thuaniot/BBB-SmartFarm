#!/usr/bin/python

import time
from Adafruit_I2C import Adafruit_I2C

#Create variable called i2c which refers to the address of the TPA2016 amplifier.
i2c = Adafruit_I2C(0x58)

TPA2016_SETUP			= 0x1
TPA2016_SETUP_R_EN		= 0x80
TPA2016_SETUP_L_EN		= 0x40
TPA2016_SETUP_R_FAULT	= 0x10
TPA2016_SETUP_L_FAULT	= 0x08

TPA2016_GAIN            = 0x5
TPA2016_AGC_OFF         = 0x00

# def setup():
# Set up the speakers
setup_speakers = i2c.readS8(TPA2016_SETUP)
print 'Speaker setup value =', setup_speakers

setup_rt_spkr = i2c.readS8(TPA2016_SETUP_R_EN)
# write_rt_spkr = i2c.write8(TPA2016_SETUP_R_FAULT, 1)
i2c.write8(TPA2016_SETUP_R_FAULT, 0)
print 'Right Speaker value =', setup_rt_spkr

# setup_rt_fault = i2c.readS8(TPA2016_SETUP_R_FAULT)
# # write_rt_fault = i2c.write8(TPA2016_SETUP_R_FAULT, 1)
# i2c.write8(TPA2016_SETUP_R_FAULT, 0)
# print 'Right Speaker Fault value =', setup_rt_fault

# Turn off AGC
agc_off = i2c.readS8(TPA2016_AGC_OFF)
print 'Current AGC_Off setting = ', agc_off

# Find out current decibel/gain level. THIS WORKS!!
def gain_change():
    gain_value = i2c.readS8(TPA2016_GAIN)
    g = gain_value
    print 'Current Gain/Decibel level =', gain_value
    if g == 51 :
        i2c.write8(0x5, 10)
        

# TPA2016: set gain to 0
# bit 6 on register 0x58 set to 0
# i2c.write8(0x5, 000111)
# 0x3f
gain_change()
 
