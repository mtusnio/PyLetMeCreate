#!/usr/bin/env python3
"""Python binding of Lora wrapper of LetMeCreate library."""

import ctypes

LORA_CLICK_AUTO_FREQ_BAND_250KHZ = 0
LORA_CLICK_AUTO_FREQ_BAND_125KHZ = 1
LORA_CLICK_AUTO_FREQ_BAND_62_5KHZ = 2
LORA_CLICK_AUTO_FREQ_BAND_31_3KHZ = 3
LORA_CLICK_AUTO_FREQ_BAND_15_6KHZ = 4
LORA_CLICK_AUTO_FREQ_BAND_7_8KHZ = 5
LORA_CLICK_AUTO_FREQ_BAND_3_9KHZ = 6
LORA_CLICK_AUTO_FREQ_BAND_200KHZ = 7
LORA_CLICK_AUTO_FREQ_BAND_100KHZ = 8
LORA_CLICK_AUTO_FREQ_BAND_50KHZ = 9
LORA_CLICK_AUTO_FREQ_BAND_25KHZ = 10
LORA_CLICK_AUTO_FREQ_BAND_12_5KHZ = 11
LORA_CLICK_AUTO_FREQ_BAND_6_3KHZ = 12
LORA_CLICK_AUTO_FREQ_BAND_3_1KHZ = 13
LORA_CLICK_AUTO_FREQ_BAND_166_7KHZ = 14
LORA_CLICK_AUTO_FREQ_BAND_83_3KHZ = 15
LORA_CLICK_AUTO_FREQ_BAND_41_7KHZ = 16
LORA_CLICK_AUTO_FREQ_BAND_20_8KHZ = 17
LORA_CLICK_AUTO_FREQ_BAND_10_4KHZ = 18
LORA_CLICK_AUTO_FREQ_BAND_5_2KHZ = 19
LORA_CLICK_AUTO_FREQ_BAND_2_6KHZ = 20

LORA_CLICK_CODING_RATE_4_5 = 0
LORA_CLICK_CODING_RATE_4_6 = 1
LORA_CLICK_CODING_RATE_4_7 = 2
LORA_CLICK_CODING_RATE_4_8 = 3

LORA_CLICK_BANDWIDTH_125KHZ = 0
LORA_CLICK_BANDWIDTH_250KHZ = 1
LORA_CLICK_BANDWIDTH_500KHZ = 2

class LoraClickConfig(ctypes.Structure):
    _fields_ = [("frequency", c_uint32),
                ("spreading_factor", c_uint8),
                ("auto_freq_band", c_uint),
                ("coding_rate", c_uint),
                ("bandwidth", c_uint),
                ("power", c_int8),
                ("bitrate", c_uint16),
                ("freq_deviation", c_uint16),
                ("preamble_length", c_uint16),
                ("enable_crc_header", c_bool)]

_LIB = ctypes.CDLL('libletmecreate_click.so')

def get_default_configuration():
    """
        Returns default configuration.
    """
    return _LIB.lora_click_get_default_configuration()

def init(mikrobus_index, config):
    pass

def configure(config):
    pass

def send(data):
    pass

def receive(data):
    pass

def write_eeprom(start_address, data):
    pass

def read_eeprom(start_address, data):
    pass

def get_eui(eui):
    pass
