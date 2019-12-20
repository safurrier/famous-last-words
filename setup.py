import pathlib
from setuptools import find_packages, setup
import configparser

# Load Config file
config = configparser.ConfigParser()
config.read('tox.ini')
project_info = config['project']


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='src',
    packages=find_packages(),
    version='0.0.1',
    description=project_info['description'],
    long_description=README,
    long_description_content_type="text/markdown",    
    author=project_info['author'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],    
    license=project_info['license'],
)
