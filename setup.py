from setuptools import setup
from sys import version_info

if version_info.major < 3:
    raise Exception("Please install this with: pip3 install pymodore")

setup(
    name="pymodore",
    version="1.1.1",
    author="Natan 'Albrigs' Fernandes dos Santos",
    author_email="natanfs013@gmail.com",
    py_modules=['pymodore'],
    description='A simple terminal pomodore timer.',
    url='https://github.com/NatanFernandesSantos/pymodore',
    license='GNU 3.0',
    keywords=['pomodoro','console','profit', 'command', 'line', 'timer'],
    python_requires='>=3',
    install_requires=[
        'Click',
        'termcolor',
        'python-vlc',
        'gtts'
    ],
    entry_points='''
        [console_scripts]
        pymodore=pymodore:pomodoro
    ''',
     classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],

)
