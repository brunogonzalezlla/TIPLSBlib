from setuptools import find_packages, setup

setup(
    name='TIPLSB',
    packages=find_packages(include=['TIPLSB']),
    version='0.1.0',
    description='Library to trace the path of an image based on LSB and RSA.',
    author='Bruno González',
    license='MIT',
)