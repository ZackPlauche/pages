from setuptools import setup, find_packages

setup(
    name='selenium-pages',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pydantic==2.0.3',
        'selenium==4.10.0',
        'PySocks==1.7.1',
    ]

)