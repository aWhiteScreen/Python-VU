from setuptools import setup, Extension

pangram_module = Extension('perfect_pangram', sources=['perfect_pangram.c'])
rational_module = Extension('rational', sources=['rational_number.c'])

setup(
    name='pangram_and_rational',
    version='1.0',
    description='Modules for checking perfect pangrams and a rational number with an add method',
    ext_modules=[pangram_module, rational_module]
)
