from setuptools import setup

setup(
    name='beep',
    version='0.2',
    py_modules=['beeper', 'melodies'],
    install_requires=[
        'pyaudio',
    ],
    maintainer='Tonsofattraction (kuznetsov.d.p@gmail.com)',
    maintainer_email='kuznetsov.d.p@gmail.com',
    url='https://github.com/Tonsofattraction/primitive_beeper',
    entry_points={
        'console_scripts': [
            'beep = beeper:main',
        ],
    },
)