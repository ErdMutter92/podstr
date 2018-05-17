#!/usr/bin/python3.6

from setuptools import setup

setup(name='podstr',
    version='0.0.4',
    description='command line tool for managing podcasts',
    author='Brandon Bleau',
    author_email='brandon@bleauweb.net',
    url='http://gitlab.bleauweb.net/',
    packages=['podstr'],
    install_requires=[
        'podcastparser',
        'requests',
        'PyYaml',
    ],
    entry_points={
        'console_scripts': [
            'podstr=podstr.cli:main'
        ],
    },
)
