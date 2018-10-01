from setuptools import setup, find_packages


setup(
    name='nhs-number-validator',
    version='1.0.0',
    license="MIT",
    packages=find_packages(),
    install_requires=['nose2==0.8.0',
                      'pycodestyle==2.4.0'],
    description='Checks the validity of an NHS number using the modulus 11 algorithm',
    long_description="\n" + open('README.md').read()
)
