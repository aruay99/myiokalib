from setuptools import setup, find_packages

setup(
    name='myiokalib',
    version='0.1.0',
    description='A library for interacting with the ioka API',
    author='Aruay Berdikulova',
    author_email='aruaiberdk@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)

