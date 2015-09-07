import os
from setuptools import setup

setup(
    name="birdpy",
    version="0.7.0",
    author="Anthony Casagrande",
    author_email="birdapi@gmail.com",
    description=("Helper functions for python, cherrypy, jinja2, and more!"),
    license="MIT",
    keywords="birdapi",
    url="https://pypi.python.org/pypi/birdpy",
    packages=['birdpy'],
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
    ],
)