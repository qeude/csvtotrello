from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='csvtotrello',
    version='0.3.2',
    description='A package to bulk import csv backlog into Trello',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/qeude/csvtotrello',
    author='Quentin Eude',
    author_email='quentineude@gmail.com',
    license='MIT',
    packages=['csvtotrello'],
    install_requires=[
        'py-trello',
    ],
    entry_points={
        'console_scripts': [
            'csvtotrello = csvtotrello.bulk_import:main'
        ]
    },
    zip_safe=False
)
