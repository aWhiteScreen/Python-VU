from setuptools import setup, Extension

module = Extension('perfect_pangram', sources=['perfect_pangram.c'])

setup(
    name='perfect_pangram',
    version='1.0',
    description='Module for checking for perfect pangrams',
    ext_modules=[module]
)
