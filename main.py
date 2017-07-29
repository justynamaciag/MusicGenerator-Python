from datamusic import music_from_data
import argparse
from _datetime import datetime
from miditime.miditime import MIDITime

class fac_music(object):

    tempo = 100
    epoch = datetime(1920, 1, 1)
    sec_per_year = 10
    base_octave = 2
    octave_range = 3

    def __init__(self, filename, arg_len):
        len = int(arg_len)
        self.create(filename, len)

    def create(self, filename, len):
        mymidi = MIDITime(127, filename, self.sec_per_year, self.base_octave, self.octave_range, self.epoch)

        midinotes = [
            [0, 60, 127, 3],
        ]

        for i in range(1, len):
            fac = self.fac(i)
            if(fac >= 255):
                fac %= 255
            midinotes.append([i, fac, 100, 1])


        mymidi.add_track(midinotes)
        mymidi.save_midi()

    def fac(self, n):
        tmp=1
        if n in (0,1):
            return 1
        else:
            for i in range(2,n):
                tmp = tmp*i
        return tmp


class basic_sounds(object):
    tempo = 100
    epoch = datetime(1920, 1, 1)
    sec_per_year = 10
    base_octave = 4
    octave_range = 5

    mymidi = None

    def __init__(self, filename, arg_len):
        list_len = int(arg_len)
        self.make_music(filename, list_len)


    def make_music(self, filename, list_len):
        mymidi = MIDITime(127, filename, self.sec_per_year, self.base_octave, self.octave_range, self.epoch)
        midinotes = [
                  [0, 60, 127, 3],
              ]

        for i in range(1, int(list_len/2)):
            midinotes.append([i, i+60, 127, 3])

        for i in range (int(list_len/2) + 1, list_len):
            midinotes.append([i, list_len+1+60-i, 127, 3])

        mymidi.add_track(midinotes)
        mymidi.save_midi()

class fib_music(object):

    tempo = 100
    epoch = datetime(1920, 1, 1)
    sec_per_year = 10
    base_octave = 4
    octave_range = 5

    def __init__(self, filename, arg_len):
        len = int(arg_len)
        self.create(filename, len)

    def create(self, filename, len):
        mymidi = MIDITime(127, filename, self.sec_per_year, self.base_octave, self.octave_range, self.epoch)

        midinotes = [
            [0, 60, 127, 3],

        ]

        for i in range(1, len):
            fib = self.fibb(i)
            if(fib >= 255):
                fib %= 255
            midinotes.append([i, fib, 100, 1])


        mymidi.add_track(midinotes)
        mymidi.save_midi()

    def fibb(self, n):
        a1 = 0
        a2 =  1
        for i in range(1, n):
            a1 = a2
            a2 = a1 + a2
        return a2


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--dat", action="store_true", help="Music from data")
    parser.add_argument("--basic", action="store_true", help="Just basic sounds")
    parser.add_argument("--minor", action="store_true", help="Minor sounds for melodies form data")
    parser.add_argument("--major", action="store_true", help="Major sounds for melodies from data")
    parser.add_argument("--fac", action="store_true", help="Music from factorial")
    parser.add_argument("--fib", action="store_true", help="Music from fibbonaci")
    parser.add_argument("destination", type=str, help="File destination")
    #parser.add_argument("len", type = int, help = "length of the generated melody")

    c_minor = ['C', 'D', 'E', 'F', 'G', 'Ab', 'Bb']
    c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

    args = parser.parse_args()

    if args.dat and args.minor:
        mymidi = music_from_data(args.destination, c_minor)
    elif args.dat and args.major:
        mymidi = music_from_data(args.destination, c_major)
    elif args.basic:
        mymidi = basic_sounds(args.destination, 20)
    elif args.fac:
        mymidi = fac_music(args.destination, 20)
    elif args.fib:
        mymidi = fib_music(args.destination, 20)



main()
