from setuptools import setup, find_packages
import sys, os

version = '.1'

setup(
    name='ckanext-opendatabc',
    version=version,
    description="Theme extension for OpenDataBC portal",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Hayden Waring',
    author_email='hayden@opengovgear.com',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.opendatabc'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        opendatabc=ckanext.opendatabc.plugin:OpenDataBCTheme

    ''',
)
