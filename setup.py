from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return [line for line in lines if not line.startswith("-")]

required = parse_requirements('requirements.txt')

setup(
    name='pages',
    version='0.1',
    url='https://github.com/ZackPlauche/pages',
    author='Zack Plauche',
    author_email='zackknowspython@gmail.com',
    description='A simple library for creating page objects in Python',
    packages=find_packages(),
    install_requires=required,
)