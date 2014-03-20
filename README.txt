This is the module for the UDS

To Install: pip install git+https://wenzou:Sn5BmjLY@bitbucket.org/wenzou/python_module.git

GitHub Account
Username: independamodule
Email: wen@independa.com
Password: Dq7&gm9x

Bitbucket Account
Username: wenzou
Email: wen@tailwindweb.com
Password: Sn5BmjLY

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
