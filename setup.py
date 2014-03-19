from distutils.core import setup

setup(
    name='UDS Module',
    version='0.1.1',
    author='Wen Zou',
    author_email='wen@independa.com',
    packages=['validate'],
    url='',
    license='LICENSE.txt',
    description='This is UDS module for data validation and queue sender',
    long_description=open('README.txt').read(),
    zip_safe=False,
)