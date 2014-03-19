__author__ = 'wenzou'


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

RANGE_SPEC_BY_UNIT = {
    BOOLEAN_UNIT_SLUG: (0, 1),
    WEIGHT_UNIT_KILOGRAMS_SLUG: (27, 180, 'kilograms'),
    WEIGHT_UNIT_POUNDS_SLUG: (60, 399, 'pounds'),
    WEIGHT_UNIT_STONES_SLUG: (4, 30, 'stones'),
    TEMPERATURE_UNIT_CELSIUS_SLUG: (95, 105, 'farenheit'),
    TEMPERATURE_UNIT_FAHRENHEIT_SLUG: (35, 40, 'celsius'),
    OXYGEN_SLUG: (70, 100),
    SYSTOLIC_SLUG: (60, 250),
    DIASTOLIC_SLUG: (40, 140),
    PULSE_SLUG: (30, 150),
    GLUCOSE_SLUG: (40, 999)
}

WEIGHT_SPEC = {WEIGHT_UNIT_KILOGRAMS_SLUG: RANGE_SPEC_BY_UNIT[WEIGHT_UNIT_KILOGRAMS_SLUG],
               WEIGHT_UNIT_POUNDS_SLUG: RANGE_SPEC_BY_UNIT[WEIGHT_UNIT_POUNDS_SLUG],
               WEIGHT_UNIT_STONES_SLUG: RANGE_SPEC_BY_UNIT[WEIGHT_UNIT_STONES_SLUG]}

TEMP_SPEC = {TEMPERATURE_UNIT_CELSIUS_SLUG: RANGE_SPEC_BY_UNIT[TEMPERATURE_UNIT_CELSIUS_SLUG],
             TEMPERATURE_UNIT_FAHRENHEIT_SLUG: RANGE_SPEC_BY_UNIT[TEMPERATURE_UNIT_FAHRENHEIT_SLUG]}


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
    }

READING_TYPE_SLUG_LIST = [BODY_WEIGHT_SLUG, GLUCOSE_SLUG, DIASTOLIC_SLUG,
                          SYSTOLIC_SLUG, OXYGEN_SLUG, AIRFLOW_SLUG, STEPS_SLUG, BODY_TEMP_SLUG,
                          PULSE_SLUG, ROOM_TEMP_SLUG, CARBON_MONOXIDE_SLUG,
                          SCALE_SLUG, PANIC_SLUG, PRESSURE_SLUG,
                          TOILET_SLUG, DOOR_SENSOR_SLUG, MOTION_SENSOR_SLUG,
                          BED_SLUG, SLEEP_SLUG, FIRE_SLUG]