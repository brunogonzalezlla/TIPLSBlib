import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'TIPLSB'
AUTHOR = 'Bruno González Llaga'
AUTHOR_EMAIL = 'brugonlla@alum.us.es'
URL = 'https://github.com/afernandez119'

LICENSE = 'MIT'
DESCRIPTION = 'Library to trace the path of an image based on LSB.'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
                      'numpy',
                      'Pillow',
                      'datetime',
                      'pytest'
                   ]
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)