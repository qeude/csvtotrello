from setuptools import setup

setup(
    name='csvtotrello',
    version='0.1',
    description='A package to bulk import csv backlog into Trello',
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