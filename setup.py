from distutils.core import setup
from setuptools import find_packages

def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except:
        pass

setup(
    name = 'signalz',
    version = '0.1',
    description = 'Data generators in Python',
    long_description = readme(),
    author = 'Matous Cejnek',
    maintainer = "Matous Cejnek",
    author_email = 'matousc@gmail.com',
    license = 'MIT',
    url = 'http://matousc89.github.io/signalz/',
    download_url = 'https://github.com/matousc89/signalz/',
    keywords = ['signals', 'data', 'time-series', 'generators'],
    install_requires=[
        'numpy',
    ],    
    bugtrack_url = "https://github.com/matousc89/signalz/issues", 
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Testing',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Programming Language :: Python',
    ],
)
