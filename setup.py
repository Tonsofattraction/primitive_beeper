from setuptools import setup

setup(
    name='beep',
    version='0.7',
    py_modules=['beeper.beeper', 'beeper.melodies'],
    install_requires=[
        'pyaudio',
    ],
    python_requires='>=3.6',
    maintainer='Tonsofattraction (kuznetsov.d.p@gmail.com)',
    maintainer_email='kuznetsov.d.p@gmail.com',
    url='https://github.com/Tonsofattraction/primitive_beeper',
    entry_points={
        'console_scripts': [
            'beep = beeper.beeper:main',
        ],
    },
)