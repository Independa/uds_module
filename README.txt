This is the module for the UDS

To Install:

pip install git+https://independamodule:L0AiGxrQ@github.com/Independa/uds_module.git

To Use in requirements.txt, add:
-e git+https://independamodule:L0AiGxrQ@github.com/Independa/uds_module.git@release#egg=UDS_Readings_Module

GitHub Account
Username: independamodule
Email: wen@independa.com
Password: L0AiGxrQ

References:
https://devcenter.heroku.com/articles/python-pip
http://guide.python-distribute.org/creation.html
http://www.pip-installer.org/en/1.1/usage.html


To use validation
from validate.validation import *
Call validate(value, reading_type, unit)
Returns: {'success': False, 'message': 'value range invalid for unit'}


To use readings parameters dictionary
from validate.readings import *
call get_readings_parameter_dictionary
returns the dictionary of reading parameters.
