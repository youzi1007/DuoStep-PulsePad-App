# note_playback.py
import os
from pyo import SfPlayer, SigTo

class NotePlayback:
    def __init__(self, samples_dir):
        self.samples_dir = samples_dir
        self.active_players = {}
        self.instrument_mapping = {}
        self.setup_samples()

    def calculate_speed(self, semitone_shift):
        return 2 ** (semitone_shift / 12)

    def generate_velocity_ranges(self, start=0, end=127, slices=16):
        step = (end - start + 1) // slices
        return [(i, i + step - 1) for i in range(start, end + 1, step)]

    def setup_samples(self):
        velocity_ranges = self.generate_velocity_ranges()
        # mapping for notes with 16 velocity layers each
        self.instrument_mapping = {
        # A0 (using A sample, no pitch shift)
        21: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"A0v{i + 1}.wav")
            for i in range(16)
        },

        # A#0 (using A sample, pitch-shifted up)
        22: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"A0v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # B0 (using C sample, pitch-shifted down)
        23: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C1v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # C1 (using C sample, no pitch shift)
        24: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"C1v{i + 1}.wav")
            for i in range(16)
        },

        # C#1 (using C sample, pitch-shifted up)
        25: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C1v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # D1 (using D# sample, pitch-shifted down)
        26: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#1v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # D#1 (using D# sample, no pitch shift)
        27: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"D#1v{i + 1}.wav")
            for i in range(16)
        },

        # E1 (using D# sample, pitch-shifted up)
        28: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#1v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # F1 (using F# sample, pitch-shifted down)
        29: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#1v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # F#1 (using F# sample, no pitch shift)
        30: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"F#1v{i + 1}.wav")
            for i in range(16)
        },

        # G1 (using F# sample, pitch-shifted up)
        31: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#1v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # G#1 (using A sample, pitch-shifted down)
        32: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"A1v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # A1 (using A sample, no pitch shift)
        33: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"A1v{i + 1}.wav")
            for i in range(16)
        },

        # A#1 (using A sample, pitch-shifted up)
        34: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"A1v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # B1 (using C sample, pitch-shifted down from next octave)
        35: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C2v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # C2 (using C sample from next octave, no pitch shift)
        36: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"C2v{i + 1}.wav")
            for i in range(16)
        },

        # C#2 (using C sample, pitch-shifted up)
        37: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C2v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # D2 (using D# sample, pitch-shifted down)
        38: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#2v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # D#2 (using D# sample, no pitch shift)
        39: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"D#2v{i + 1}.wav")
            for i in range(16)
        },

        # E2 (using D# sample, pitch-shifted up)
        40: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#2v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # F2 (using F# sample, pitch-shifted down)
        41: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#2v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # F#2 (using F# sample, no pitch shift)
        42: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"F#2v{i + 1}.wav")
            for i in range(16)
        },

        # G2 (using F# sample, pitch-shifted up)
        43: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#2v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # G#2 (using F# sample, pitch-shifted up)
        44: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#2v{i + 1}.wav"),
                                 "speed": self.calculate_speed(2)}
            for i in range(16)
        },

        # A2 (using A sample, no pitch shift)
        45: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"A2v{i + 1}.wav")
            for i in range(16)
        },

        # A#2 (using A sample, pitch-shifted up)
        46: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"A2v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # B2 (using C sample, pitch-shifted down)
        47: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C3v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # C3 (using C sample, no pitch shift)
        48: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"C3v{i + 1}.wav")
            for i in range(16)
        },

        # C#3 (using C sample, pitch-shifted up)
        49: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C3v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # D3 (using D# sample, pitch-shifted down)
        50: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#3v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # D#3 (using D# sample, no pitch shift)
        51: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"D#3v{i + 1}.wav")
            for i in range(16)
        },

        # E3 (using D# sample, pitch-shifted up)
        52: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#3v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # F3 (using F# sample, pitch-shifted down)
        53: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#3v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # F#3 (using F# sample, no pitch shift)
        54: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"F#3v{i + 1}.wav")
            for i in range(16)
        },

        # G3 (using F# sample, pitch-shifted up)
        55: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#3v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # G#3 (using F# sample, pitch-shifted up)
        56: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#3v{i + 1}.wav"),
                                 "speed": self.calculate_speed(2)}
            for i in range(16)
        },

        # A3 (using A sample, no pitch shift)
        57: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"A3v{i + 1}.wav")
            for i in range(16)
        },

        # A#3 (using A sample, pitch-shifted up)
        58: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"A3v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # B3 (using C sample, pitch-shifted down)
        59: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C4v{i + 1}.wav"), "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # C4 (using C sample, no pitch shift)
        60: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"C4v{i + 1}.wav")
            for i in range(16)
        },

        # C#4 (using C sample, pitch-shifted up)
        61: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C4v{i + 1}.wav"), "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # D4 (using D# sample, pitch-shifted down)
         62: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#4v{i + 1}.wav"), "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

            # D#4 (using D# sample, no pitch shift)
        63: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"D#4v{i + 1}.wav")
            for i in range(16)
        }
    }

    def get_sample_info(self, note, velocity):
        if note in self.instrument_mapping:
            for vel_range, sample_info in self.instrument_mapping[note].items():
                if vel_range[0] <= velocity <= vel_range[1]:
                    if isinstance(sample_info, dict):
                        return sample_info["sample"], sample_info["speed"]
                    else:
                        return sample_info, 1.0
        return None, None

    def start_note_playback(self, note, velocity):
        sample_path, speed = self.get_sample_info(note, velocity)
        if sample_path and os.path.exists(sample_path):
            print(f"Playing note {note} with velocity {velocity}: {sample_path} at speed {speed}")
            player = SfPlayer(sample_path, speed=speed, loop=False, mul=0.5).out()
            self.active_players[note] = player
        else:
            print(f"No sample found for note {note} and velocity {velocity}")

    def stop_note_playback(self, note):
        if note in self.active_players:
            print(f"Stopping sample for MIDI note {note} with smoother fade-out")
            player = self.active_players[note]
            volume_fade = SigTo(value=0, time=1, init=0.5)
            player.setMul(volume_fade)
            player.stop(1)
            del self.active_players[note]
