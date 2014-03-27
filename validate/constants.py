__author__ = 'wenzou'

UNLIMITED_POSITIVE = 10000000000000000000000

SYST_CONSTRAINTS = (0,1000)
DIAST_CONSTRAINTS = (0,1000)


TEMPERATURE_UNIT_CELSIUS_SLUG='celsius'
TEMPERATURE_UNIT_FAHRENHEIT_SLUG='fahrenheit'

WEIGHT_UNIT_POUNDS_SLUG = 'pounds'
WEIGHT_UNIT_KILOGRAMS_SLUG = 'kg'
WEIGHT_UNIT_STONES_SLUG = 'stone'

STEPS_UNIT_SLUG = 'steps'
BOOLEAN_UNIT_SLUG = 'boolean'
PPM_UNIT_SLUG = 'ppm'
BPM_UNIT_SLUG = 'beats_per_minute'
ML_CUBED_PER_SECOND_UNIT_SLUG = 'ml3s'
PERCENTAGE_UNIT_SLUG = 'percentage'
MG_PER_DL_UNIT_SLUG = 'mgdl'
MMHG_UNIT_SLUG = 'mmHg'
TIMES_UNIT_SLUG = 'times'

BODY_WEIGHT_SLUG = "body_weight"
GLUCOSE_SLUG = "glucose"
DIASTOLIC_SLUG = "diastolic"
SYSTOLIC_SLUG = "systolic"
OXYGEN_SLUG = "oxygen"
AIRFLOW_SLUG = "airflow"
STEPS_SLUG = "steps"
BODY_TEMP_SLUG = "body_temp"
HEART_RATE_SLUG = "heartrate" # deprecated
PULSE_SLUG = "pulse"
ROOM_TEMP_SLUG = "room_temp"
### 5/6/13 - these slugs are rarely referenced so far (if it should be renamed, then rename them now) ###
CARBON_MONOXIDE_SLUG = "carbon_monoxide"
SCALE_SLUG = "scale"
PANIC_SLUG = "panic"
PRESSURE_SLUG = "pressure_pad"
TOILET_SLUG = "toilet"
DOOR_SENSOR_SLUG = "door"
MOTION_SENSOR_SLUG = "motion"
BED_SLUG = "bed"
SLEEP_SLUG = "sleep"
FIRE_SLUG = "fire"
###

DEFAULT_RANGES = 'DEFAULT_RANGES'
RANGE_SPEC_BY_UNIT = {
    DEFAULT_RANGES: {
        BOOLEAN_UNIT_SLUG: (0, 1, 'True', 'False', '1', '0'),
        WEIGHT_UNIT_KILOGRAMS_SLUG: (27, 180, 'kilograms'),
        WEIGHT_UNIT_POUNDS_SLUG: (60, 399, 'pounds'),
        WEIGHT_UNIT_STONES_SLUG: (4, 30, 'stones'),
        TEMPERATURE_UNIT_CELSIUS_SLUG: (95, 105, 'farenheit'),
        TEMPERATURE_UNIT_FAHRENHEIT_SLUG: (35, 40, 'celsius'),
        PERCENTAGE_UNIT_SLUG: (70, 100),
        MMHG_UNIT_SLUG: (40, 250),
        MG_PER_DL_UNIT_SLUG: (40, 999),
        BPM_UNIT_SLUG: (30, 150),
        PPM_UNIT_SLUG: (0, 100),
        STEPS_UNIT_SLUG: (1, UNLIMITED_POSITIVE),
        ML_CUBED_PER_SECOND_UNIT_SLUG: (0, UNLIMITED_POSITIVE)
    },
    SCALE_SLUG : {
        WEIGHT_UNIT_KILOGRAMS_SLUG: (27, 180, 'kilograms'),
        WEIGHT_UNIT_POUNDS_SLUG: (60, 399, 'pounds'),
        WEIGHT_UNIT_STONES_SLUG: (4, 30, 'stones')
    },
    BODY_TEMP_SLUG: {
        TEMPERATURE_UNIT_CELSIUS_SLUG: (95, 105, 'farenheit'),
        TEMPERATURE_UNIT_FAHRENHEIT_SLUG: (35, 40, 'celsius')
    },
    ROOM_TEMP_SLUG: {
        TEMPERATURE_UNIT_CELSIUS_SLUG: (-76, 176, 'farenheit'),
        TEMPERATURE_UNIT_FAHRENHEIT_SLUG: (-60, 80, 'celsius')
    },
    GLUCOSE_SLUG: {
        MG_PER_DL_UNIT_SLUG: (40, 999)
    },
    DIASTOLIC_SLUG: {
        MMHG_UNIT_SLUG: (40, 140)
    },
    SYSTOLIC_SLUG: {
        MMHG_UNIT_SLUG: (60, 250)
    },
    OXYGEN_SLUG: {
        PERCENTAGE_UNIT_SLUG: (70, 100)
    },
    AIRFLOW_SLUG: {
        ML_CUBED_PER_SECOND_UNIT_SLUG: (0, UNLIMITED_POSITIVE)
    },
    STEPS_SLUG: {
        STEPS_UNIT_SLUG: (1, UNLIMITED_POSITIVE)
    },
    HEART_RATE_SLUG: {
        BPM_UNIT_SLUG: (30, 150)
    },
    PULSE_SLUG: {
        BPM_UNIT_SLUG: (30, 150)
    },
    CARBON_MONOXIDE_SLUG: {
        PPM_UNIT_SLUG: (0, 100)
    },
    PANIC_SLUG: {
       
    },
    PRESSURE_SLUG: {
        
    },
    TOILET_SLUG: {
        
    },
    DOOR_SENSOR_SLUG: {
        
    },
    MOTION_SENSOR_SLUG: {
        
    },
    BED_SLUG: {
        
    },
    SLEEP_SLUG: {
        
    },
    FIRE_SLUG: {
        
    },
    BODY_WEIGHT_SLUG : {
        WEIGHT_UNIT_KILOGRAMS_SLUG: (27, 180, 'kilograms'),
        WEIGHT_UNIT_POUNDS_SLUG: (60, 399, 'pounds'),
        WEIGHT_UNIT_STONES_SLUG: (4, 30, 'stones')
    }
}

#body wei
WEIGHT_SPEC = {WEIGHT_UNIT_KILOGRAMS_SLUG: RANGE_SPEC_BY_UNIT[SCALE_SLUG][WEIGHT_UNIT_KILOGRAMS_SLUG],
               WEIGHT_UNIT_POUNDS_SLUG: RANGE_SPEC_BY_UNIT[SCALE_SLUG][WEIGHT_UNIT_POUNDS_SLUG],
               WEIGHT_UNIT_STONES_SLUG: RANGE_SPEC_BY_UNIT[SCALE_SLUG][WEIGHT_UNIT_STONES_SLUG]}

TEMP_SPEC = {TEMPERATURE_UNIT_CELSIUS_SLUG: RANGE_SPEC_BY_UNIT[BODY_TEMP_SLUG][TEMPERATURE_UNIT_CELSIUS_SLUG],
             TEMPERATURE_UNIT_FAHRENHEIT_SLUG: RANGE_SPEC_BY_UNIT[BODY_TEMP_SLUG][TEMPERATURE_UNIT_FAHRENHEIT_SLUG]}


ACCEPTED_UNITS_BY_READING_TYPE = {
    SCALE_SLUG: {WEIGHT_UNIT_POUNDS_SLUG, WEIGHT_UNIT_KILOGRAMS_SLUG, WEIGHT_UNIT_STONES_SLUG},
    BODY_TEMP_SLUG: {TEMPERATURE_UNIT_CELSIUS_SLUG, TEMPERATURE_UNIT_FAHRENHEIT_SLUG},
    ROOM_TEMP_SLUG: {TEMPERATURE_UNIT_CELSIUS_SLUG, TEMPERATURE_UNIT_FAHRENHEIT_SLUG},
    GLUCOSE_SLUG: {MG_PER_DL_UNIT_SLUG},
    DIASTOLIC_SLUG: {MMHG_UNIT_SLUG},
    SYSTOLIC_SLUG: {MMHG_UNIT_SLUG},
    OXYGEN_SLUG: {PERCENTAGE_UNIT_SLUG},
    AIRFLOW_SLUG: {ML_CUBED_PER_SECOND_UNIT_SLUG},
    STEPS_SLUG: {STEPS_UNIT_SLUG},
    HEART_RATE_SLUG: {BPM_UNIT_SLUG},
    PULSE_SLUG: {BPM_UNIT_SLUG},
    CARBON_MONOXIDE_SLUG: {PPM_UNIT_SLUG},
    PANIC_SLUG: {BOOLEAN_UNIT_SLUG},
    PRESSURE_SLUG: {BOOLEAN_UNIT_SLUG},
    TOILET_SLUG: {BOOLEAN_UNIT_SLUG},
    DOOR_SENSOR_SLUG: {BOOLEAN_UNIT_SLUG},
    MOTION_SENSOR_SLUG: {BOOLEAN_UNIT_SLUG},
    BED_SLUG: {BOOLEAN_UNIT_SLUG},
    SLEEP_SLUG: {BOOLEAN_UNIT_SLUG},
    FIRE_SLUG: {BOOLEAN_UNIT_SLUG},
    BODY_WEIGHT_SLUG: {WEIGHT_UNIT_POUNDS_SLUG, WEIGHT_UNIT_KILOGRAMS_SLUG, WEIGHT_UNIT_STONES_SLUG}
}

DEFAULT_UNITS_BY_READING_TYPE = {
    SCALE_SLUG: WEIGHT_UNIT_POUNDS_SLUG,
    BODY_TEMP_SLUG: TEMPERATURE_UNIT_FAHRENHEIT_SLUG,
    ROOM_TEMP_SLUG: TEMPERATURE_UNIT_FAHRENHEIT_SLUG,
    GLUCOSE_SLUG: MG_PER_DL_UNIT_SLUG,
    DIASTOLIC_SLUG: MMHG_UNIT_SLUG,
    SYSTOLIC_SLUG: MMHG_UNIT_SLUG,
    OXYGEN_SLUG: PERCENTAGE_UNIT_SLUG,
    AIRFLOW_SLUG: ML_CUBED_PER_SECOND_UNIT_SLUG,
    STEPS_SLUG: STEPS_UNIT_SLUG,
    HEART_RATE_SLUG: BPM_UNIT_SLUG,
    PULSE_SLUG: BPM_UNIT_SLUG,
    CARBON_MONOXIDE_SLUG: PPM_UNIT_SLUG,
    PANIC_SLUG: BOOLEAN_UNIT_SLUG,
    PRESSURE_SLUG: BOOLEAN_UNIT_SLUG,
    TOILET_SLUG: BOOLEAN_UNIT_SLUG,
    DOOR_SENSOR_SLUG: BOOLEAN_UNIT_SLUG,
    MOTION_SENSOR_SLUG: BOOLEAN_UNIT_SLUG,
    BED_SLUG: BOOLEAN_UNIT_SLUG,
    SLEEP_SLUG: BOOLEAN_UNIT_SLUG,
    FIRE_SLUG: BOOLEAN_UNIT_SLUG,
    BODY_WEIGHT_SLUG: WEIGHT_UNIT_POUNDS_SLUG
}

READING_TYPE_SLUG_LIST = [BODY_WEIGHT_SLUG, GLUCOSE_SLUG, DIASTOLIC_SLUG,
                          SYSTOLIC_SLUG, OXYGEN_SLUG, AIRFLOW_SLUG, STEPS_SLUG, BODY_TEMP_SLUG,
                          PULSE_SLUG, ROOM_TEMP_SLUG, CARBON_MONOXIDE_SLUG,
                          SCALE_SLUG, PANIC_SLUG, PRESSURE_SLUG,
                          TOILET_SLUG, DOOR_SENSOR_SLUG, MOTION_SENSOR_SLUG,
                          BED_SLUG, SLEEP_SLUG, FIRE_SLUG]

ACKNOWLEDGE_KEY = 'acknowledgement'
SOURCE_TYPE_KEY = 'source_type'
DEVICE_ID_KEY = 'device_id'
API_KEY_KEY = "api_key"
ORIGINAL_VALUE_KEY = 'value'
READING_TYPE_ID_KEY = 'reading_type_id'
ORIGINAL_UNIT_KEY = 'unit'
PREFERRED_VALUE_KEY = 'pref_value'
PREFERRED_UNIT_KEY = 'pref_unit'
USER_EVENT_KEY = 'user_event'
TAG_KEY = 'tag'
LATITUDE_KEY = 'latitude'
LONGITUDE_KEY = 'longitude'
DURATION_KEY = 'duration'
CREATED_READING_KEY = 'created_reading'
CREATED_TRANSMISSION_KEY = 'created_transmission'
DATA_KEY = 'data'
READINGS_JSON_KEY = 'readings'
EXTRA_FIELDS_KEY = 'extra_fields'
SOURCE_DEVELOPER_KEY = 'source_developer'
CARE_RECEIVER_KEY = 'care_receiver'
SOURCE_MANUFACTURER_KEY = 'source_manufacturer'
ASSOCIATED_READINGS_KEY = 'associated_readings'
PHONE_SOURCE_KEY = 'phone'
DEVICE_SOURCE_KEY = 'device'
CONFIRM_KEY = 'confirm'
PENDING_KEY = 'pending'
REMOVE_KEY = 'remove'


#name of the task
API_PROCESS_TASK = 'independa.api.reading.process'