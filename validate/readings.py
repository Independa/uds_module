__author__ = 'wenzou'

from constants import *


def get_readings_parameter_dictionary():
    reading_parameters = {
        ACKNOWLEDGE_KEY: None,
        SOURCE_TYPE_KEY: None,
        DEVICE_ID_KEY: None,
        API_KEY_KEY: None,
        ORIGINAL_VALUE_KEY: None,
        READING_TYPE_ID_KEY: None,
        ORIGINAL_UNIT_KEY: None,
        PREFERRED_VALUE_KEY: None,
        PREFERRED_UNIT_KEY: None,
        TAG_KEY: None,
        LATITUDE_KEY: None,
        LONGITUDE_KEY: None,
        DURATION_KEY: None,
        CREATED_READING_KEY: None,
        CREATED_TRANSMISSION_KEY: None,
        DATA_KEY: None,
        USER_EVENT_KEY: None,
        READINGS_JSON_KEY: None
    }
    return reading_parameters