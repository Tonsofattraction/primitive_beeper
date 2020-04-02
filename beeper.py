import math
import pyaudio
import threading
import argparse
import re
from melodies import *


def parse_options():
    """ parse command line options """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'timeout',
        nargs=1,
        help='Time after which it will beep. You can use "d","h","m","s" multipliers like this 1d3h2m3s',
        default='',
        action='store',
    )
    parser.add_argument(
        '--melody',
        dest='melody',
        help='melody to beep (available melodies: %s)' % ', '.join(MELODIES.keys()),
        default='beepr',
        action='store',
    )
    return parser.parse_args()


def parse_duration(duration):
    """
    Parse duration string, such as '3h2m3s' into seconds
    """
    _re_token = re.compile("([0-9.]+)([dhms]?)")

    def parse_token(time, multiplier):
        multipliers = {
            'd': 86400,
            'h': 3600,
            'm': 60,
            's': 1,
        }
        if multiplier:
            if multiplier in multipliers:
                return int(float(time) * multipliers[multiplier])
            else:
                raise ValueError()
        else:
            return int(float(time))

    return sum(parse_token(*token) for token in _re_token.findall(duration))


def beep(melody, tempo=MEDIUM):
    """
    inspired by this stackoverflow answer by Liam (https://stackoverflow.com/users/4879665/liam)
    https://stackoverflow.com/a/33880295/2361957
    """
    PyAudio = pyaudio.PyAudio     # initialize pyaudio

    # See https://en.wikipedia.org/wiki/Bit_rate#Audio
    BITRATE = 16000    # number of frames per second/frameset.
    WAVEDATA = ''
    melody = MELODIES.get(melody, MELODIES['beepr'])
    for note in melody:
        frequency = note[1]
        length = note[0] * tempo
        numberofframes = int(BITRATE * length)
        if note[1] == PAUSE:
            WAVEDATA += ''.join([chr(128)] * numberofframes)
        else:
            # generating wawes
            for x in range(numberofframes):
                WAVEDATA += chr(int(math.sin(x/((BITRATE/frequency)/math.pi))*127+128))

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1),
                    channels=1,
                    rate=BITRATE,
                    output=True)

    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()


def main():
    options = parse_options()
    timeout = parse_duration(options.timeout[0])
    timer = threading.Timer(float(timeout), beep, [options.melody])
    timer.start()
    timer.join()


if __name__ == '__main__':
    main()