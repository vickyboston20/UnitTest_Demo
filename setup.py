from setuptools import setup, find_packages


setup(
    name='src',     # Project class Folder
    version='1.0.0',
    install_requires=[
        'pytest'
    ],
    packages=find_packages()
)