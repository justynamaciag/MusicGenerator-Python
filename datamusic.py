from datetime import datetime
import csv
from miditime.miditime import MIDITime

class music_from_data(object):

    epoch = datetime(1990, 1, 1)
    mymidi = None

    tempo = 150
    seconds_per_year = 100
    base_octave = 4
    octave_range = 3

    velocity = 110

    def __init__(self, file, key):
        self.current_key = key
        self.convert_to_miditime(file)


    def generate_pitch(self, key):
        scale_pct = self.mymidi.linear_scale_pct(0, self.maksimum, key)
        mode = self.current_key
        note = self.mymidi.scale_to_note_classic(scale_pct, mode)
        return self.mymidi.note_to_midi_pitch(note)


    def convert_to_miditime(self, filename):
        self.mymidi = MIDITime(self.tempo, filename, self.seconds_per_year, self.base_octave, self.octave_range)
        fp = open('data.csv')
        data = csv.DictReader(fp)

        data_list = list(data)

        self.minimum = self.mymidi.get_data_range(data_list, 'Key')[0]
        self.maksimum = self.mymidi.get_data_range(data_list, 'Key')[1]

        first_day = self.mymidi.map_week_to_day(data_list[0]['Year'],data_list[0]['Week'])

        notes = []

        i=0;

        for f in data_list:
            week_start_date = self.mymidi.map_week_to_day(f['Year'], f['Week'], first_day.weekday())
            data_to_int = self.mymidi.days_since_epoch(week_start_date)
            beat = self.mymidi.beat(data_to_int)

            notes.append([
                i,
                self.generate_pitch(float(f['Key'])),
                self.velocity,
                4
            ])
            i += 1

        self.mymidi.add_track(notes)
        self.mymidi.save_midi()

