from setuptools import setup, find_packages

setup(
    name='cryptoAPI',
    version='1.0.0',
    author='SrDiegoH',
    description='API to encrypt and decrypt texts',
    url='https://github.com/SrDiegoH/cryptoAPI',
    packages=find_packages(where='.', exclude=(), include=('*',)),
    classifiers=[ 'Python' ],
    install_requires=['flask', 'pycryptodome'],
    python_requires='<3.9.7',
    include_package_data=True,
    install_package_data=True,
)