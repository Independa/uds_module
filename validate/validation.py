__author__ = 'wenzou'

from constants import *
from helpers import *
import json

def return_failure(message='Failure'):
    return {'success': False, 'message': message}
    
def return_success(message='Success'):
    return {'success': True, 'message': message}

def validate(value, reading_type, unit=None):
    
    #check if reading_type exists
    if reading_type not in READING_TYPE_SLUG_LIST:
        return return_failure(message='Invalid reading type')
        
    if not unit:
        unit = DEFAULT_UNITS_BY_READING_TYPE[reading_type]

    #check if unit matches the reading_type
    if unit not in ACCEPTED_UNITS_BY_READING_TYPE[reading_type]:
        return return_failure(message='Invalid unit for reading type')
    #check if value within acceptable range of unit
    MIN_INDEX=0
    MAX_INDEX=1
    if unit == BOOLEAN_UNIT_SLUG:
        if value in RANGE_SPEC_BY_UNIT[BOOLEAN_UNIT_SLUG]:
            return return_success(message='Successful')
    else:
        #todo: determine if its a float value based on constants
        range_by_reading_type = RANGE_SPEC_BY_UNIT[reading_type].get(unit, None)
        if range_by_reading_type is None:
            range_value =  RANGE_SPEC_BY_UNIT[reading_type].get(DEFAULT_RANGES)
        else:
            range_value = RANGE_SPEC_BY_UNIT[reading_type].get(unit)
            
        if range_value[MIN_INDEX] < float(value) < range_value[MAX_INDEX]:
            return return_success(message='Successful')

    #return false if anything fails
    return return_failure(message='value range invalid for unit')

def validate_request(request, data=None):
    if data is None:
        data = request.POST.copy()
        
    if DEVICE_ID_KEY not in data:
        return return_failure(message='Device ID is missing')
        
    if is_bulk(request):
        if READINGS_JSON_KEY not in data:
            return return_failure(message='Readings are missing')
        try:
            readings = json.loads(data[READINGS_JSON_KEY])
        except:
            return return_failure(message='The format of the Readings array is invalid')
            
        for reading in readings:
            if type(reading) is not dict:
                return_failure(message='The format of the Extra Fields array is invalid')
            if READING_TYPE_ID_KEY not in reading or not reading[READING_TYPE_ID_KEY]:
                return return_failure(message='Reading Type ID is required.')
            if ORIGINAL_VALUE_KEY not in reading or not reading[ORIGINAL_VALUE_KEY]:
                return return_failure(message='Value is required.')
            reading_type_id = reading['reading_type_id'].lower()
            value = reading['value']
            validation_response = validate(value, reading_type_id, reading.get(ORIGINAL_UNIT_KEY, None))
            if validation_response['success'] is False:
                return validation_response
                   
    else :
        if READING_TYPE_ID_KEY not in data:
            return return_failure(message='Reading Type ID missing')
        if ORIGINAL_VALUE_KEY not in data:
            return return_failure(message='Value is missing')
        reading_type_id = data[READING_TYPE_ID_KEY].lower()
        value = data[ORIGINAL_VALUE_KEY]
        validation_response = validate(value, reading_type_id, data.get(ORIGINAL_UNIT_KEY, None))
        if validation_response['success'] is False:
            return validation_response
    
    return return_success(message='Successful')