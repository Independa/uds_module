__author__ = 'wenzou'

from constants import *


def validate(value, reading_type, unit):
    #check if reading_type exists
    if reading_type not in READING_TYPE_SLUG_LIST:
        return {'success': False, 'message': 'Invalid reading type'}

    #check if unit matches the reading_type
    if unit not in ACCEPTED_UNITS_BY_READING_TYPE[reading_type]:
        return {'success': False, 'message': 'Invalid unit for reading type'}
    #check if value within acceptable range of unit
    MIN_INDEX = 0
    MAX_INDEX = 1
    if unit == BOOLEAN_UNIT_SLUG:
        if value == RANGE_SPEC_BY_UNIT[BOOLEAN_UNIT_SLUG][MIN_INDEX] or value == RANGE_SPEC_BY_UNIT[BOOLEAN_UNIT_SLUG][MAX_INDEX]:
            return {'success': True, 'message': 'Successful'}
    else:
        if RANGE_SPEC_BY_UNIT[unit][MIN_INDEX] < value < RANGE_SPEC_BY_UNIT[unit][MAX_INDEX]:
            return {'success': True, 'message': 'Successful'}

    #return false if anything fails
    return {'success': False, 'message': 'value range invalid for unit'}
