from setuptools import setup


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="pymodore",
    version="2020.2.2",
    description="",
    long_description=readfile('README.md'),
    author="Natan 'Albrigs' Fernandes dos Santos",
    author_email="natanfernandessantos@protonmail.com",
    url="",
    py_modules=['pymodore'],
    license=readfile('LICENSE'),
    entry_points={
        'console_scripts': [
            'pymodore = pymodore:pomodoro'
        ]
    },
)
