# note_playback.py
import os
from pyo import SfPlayer, SigTo

class NotePlayback:
    def __init__(self, samples_dir, trumpet_dir):
        self.samples_dir = samples_dir
        self.trumpet_dir = trumpet_dir
        self.active_players = {}
        self.piano_mapping = {}
        self.trumpet_mapping = {}
        self.setup_samples()

    def calculate_speed(self, semitone_shift):
        return 2 ** (semitone_shift / 12)

    def generate_velocity_ranges(self, start=0, end=127, slices=16):
        step = (end - start + 1) // slices
        return [(i, i + step - 1) for i in range(start, end + 1, step)]

    def setup_samples(self):
        velocity_ranges = self.generate_velocity_ranges()
        trumpet_velocity_ranges = self.generate_velocity_ranges(0,127,2)

        # mapping for notes with 2 velocity layers each
        self.trumpet_mapping = {
            # G#3 (using A sample, no pitch shift)
            56: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.G#3-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.G#3-PB-loop.wav")
            },

            # A3 (using A sample, no pitch shift)
            57: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.A3-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.A3-PB-loop.wav")
            },

            # A#3 (using A sample, no pitch shift)
            58: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.A#3-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.A#3-PB-loop.wav")
            },

            # B3 (using A sample, no pitch shift)
            59: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.B3-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.B3-PB-loop.wav")
            },

            # C4 (using A sample, no pitch shift)
            60: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.C4-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.C4-PB-loop.wav")
            },

            # C#4 (using A sample, no pitch shift)
            61: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.C#4-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.C#4-PB-loop.wav")
            },

            # D4 (using A sample, no pitch shift)
            62: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.D4-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.D4-PB-loop.wav")
            },

            # D#4 (using A sample, no pitch shift)
            63: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.D#4-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.D#4-PB-loop.wav")
            },

            # E4 (using A sample, no pitch shift)
            64: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.E4-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.E4-PB-loop.wav")
            },

            # F4 (using A sample, no pitch shift)
            65: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.F4-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.F4-PB-loop.wav")
            },

            # F#4 (using A sample, no pitch shift)
            66: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.F#4-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.F#4-PB-loop.wav")
            },

            # G4 (using A sample, no pitch shift)
            67: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.G4-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.G4-PB-loop.wav")
            },

            # G#4 (using A sample, no pitch shift)
            68: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.G#4-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.G#4-PB-loop.wav")
            },

            # A4 (using A sample, no pitch shift)
            69: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.A4-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.A4-PB-loop.wav")
            },

            # A#4 (using A sample, no pitch shift)
            70: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.A#4-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.A#4-PB-loop.wav")
            },

            # B4 (using A sample, no pitch shift)
            71: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.B4-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.B4-PB-loop.wav")
            },

            # C5 (using A sample, no pitch shift)
            72: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.C5-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.C5-PB-loop.wav")
            },

            # C#5 (using A sample, no pitch shift)
            73: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.C#5-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.C#5-PB-loop.wav")
            },

            # D5 (using A sample, no pitch shift)
            74: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.D5-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.D5-PB-loop.wav")
            },

            # D#5 (using A sample, no pitch shift)
            75: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.D#5-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.D#5-PB-loop.wav")
            },

            # E5 (using A sample, no pitch shift)
            76: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.E5-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.E5-PB-loop.wav")
            },

            # F5 (using A sample, no pitch shift)
            77: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.F5-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.F5-PB-loop.wav")
            },

            # F#5 (using A sample, no pitch shift)
            78: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.F#5-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.F#5-PB-loop.wav")
            },

            # G5 (using A sample, no pitch shift)
            79: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.G5-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.G5-PB-loop.wav")
            },

            # G#5 (using A sample, no pitch shift)
            80: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.G#5-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.G#5-PB-loop.wav")
            },

            # A5 (using A sample, no pitch shift)
            81: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.A5-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.A5-PB-loop.wav")
            },

            # A#5 (using A sample, no pitch shift)
            82: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.A#5-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.A#5-PB-loop.wav")
            },

            # B5 (using A sample, no pitch shift)
            83: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.B5-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.B5-PB-loop.wav")
            },

            # C6 (using A sample, no pitch shift)
            84: {
                trumpet_velocity_ranges[0]: os.path.join(self.trumpet_dir, "Trumpet.novib.mf.C6-PB-loop.wav"),
                trumpet_velocity_ranges[1]: os.path.join(self.trumpet_dir, "Trumpet.novib.ff.C6-PB-loop.wav")
            }
        }

        # mapping for notes with 16 velocity layers each
        self.piano_mapping = {
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
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C4v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # C4 (using C sample, no pitch shift)
        60: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"C4v{i + 1}.wav")
            for i in range(16)
        },

        # C#4 (using C sample, pitch-shifted up)
        61: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C4v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # D4 (using D# sample, pitch-shifted down)
         62: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#4v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

            # D#4 (using D# sample, no pitch shift)
        63: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"D#4v{i + 1}.wav")
            for i in range(16)
        },
















        # E4 (using D# sample, pitch-shifted up)
        64: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#4v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # F4 (using F# sample, pitch-shifted down)
        65: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#4v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # F#4 (using F# sample, no pitch shift)
        66: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"F#4v{i + 1}.wav")
            for i in range(16)
        },

        # G4 (using F# sample, pitch-shifted up)
        67: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#4v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # G#4 (using F# sample, pitch-shifted up)
        68: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#4v{i + 1}.wav"),
                                 "speed": self.calculate_speed(2)}
            for i in range(16)
        },

        # A4 (using A sample, no pitch shift)
        69: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"A4v{i + 1}.wav")
            for i in range(16)
        },

        # A#4 (using A sample, pitch-shifted up)
        70: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"A4v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # B4 (using C sample, pitch-shifted down)
        71: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C5v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # C5 (using C sample, no pitch shift)
        72: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"C5v{i + 1}.wav")
            for i in range(16)
        },

        # C#5 (using C sample, pitch-shifted up)
        73: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C5v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # D5 (using D# sample, pitch-shifted down)
        74: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#5v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # D#5 (using D# sample, no pitch shift)
        75: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"D#5v{i + 1}.wav")
            for i in range(16)
        },

        # E5 (using D# sample, pitch-shifted up)
        76: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#5v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # F5 (using F# sample, pitch-shifted down)
        77: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#5v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # F#5 (using F# sample, no pitch shift)
        78: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"F#5v{i + 1}.wav")
            for i in range(16)
        },

        # G5 (using F# sample, pitch-shifted up)
        79: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#5v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # G#5 (using F# sample, pitch-shifted up)
        80: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#5v{i + 1}.wav"),
                                 "speed": self.calculate_speed(2)}
            for i in range(16)
        },

        # A5 (using A sample, no pitch shift)
        81: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"A5v{i + 1}.wav")
            for i in range(16)
        },

        # A#5 (using A sample, pitch-shifted up)
        82: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"A5v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # B5 (using C sample, pitch-shifted down)
        83: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C6v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # C6 (using C sample, no pitch shift)
        84: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"C6v{i + 1}.wav")
            for i in range(16)
        },

        # C#6 (using C sample, pitch-shifted up)
        85: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C6v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # D6 (using D# sample, pitch-shifted down)
        86: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#6v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # D#6 (using D# sample, no pitch shift)
        87: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"D#6v{i + 1}.wav")
            for i in range(16)
        },

        # E6 (using D# sample, pitch-shifted up)
        88: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#6v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # F6 (using F# sample, pitch-shifted down)
        89: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#6v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # F#6 (using F# sample, no pitch shift)
        90: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"F#6v{i + 1}.wav")
            for i in range(16)
        },

        # G6 (using F# sample, pitch-shifted up)
        91: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#6v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # G#6 (using F# sample, pitch-shifted up)
        92: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#6v{i + 1}.wav"),
                                 "speed": self.calculate_speed(2)}
            for i in range(16)
        },

        # A6 (using A sample, no pitch shift)
        93: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"A6v{i + 1}.wav")
            for i in range(16)
        },

        # A#6 (using A sample, pitch-shifted up)
        94: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"A6v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # B6 (using C sample, pitch-shifted down)
        95: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C7v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # C7 (using C sample, no pitch shift)
        96: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"C7v{i + 1}.wav")
            for i in range(16)
        },

        # C#7 (using C sample, pitch-shifted up)
        97: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C7v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # D7 (using D# sample, pitch-shifted down)
        98: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#7v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # D#7 (using D# sample, no pitch shift)
        99: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"D#7v{i + 1}.wav")
            for i in range(16)
        },

        # E7 (using D# sample, pitch-shifted up)
        100: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"D#7v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # F7 (using F# sample, pitch-shifted down)
        101: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#7v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # F#7 (using F# sample, no pitch shift)
        102: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"F#7v{i + 1}.wav")
            for i in range(16)
        },

        # G7 (using F# sample, pitch-shifted up)
        103: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#7v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # G#7 (using F# sample, pitch-shifted up)
        104: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"F#7v{i + 1}.wav"),
                                 "speed": self.calculate_speed(2)}
            for i in range(16)
        },

        # A7 (using A sample, no pitch shift)
        105: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"A7v{i + 1}.wav")
            for i in range(16)
        },

        # A#7 (using A sample, pitch-shifted up)
        106: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"A7v{i + 1}.wav"),
                                 "speed": self.calculate_speed(1)}
            for i in range(16)
        },

        # B7 (using C sample, pitch-shifted down)
        107: {
            velocity_ranges[i]: {"sample": os.path.join(self.samples_dir, f"C8v{i + 1}.wav"),
                                 "speed": self.calculate_speed(-1)}
            for i in range(16)
        },

        # C8 (using C sample, no pitch shift)
        108: {
            velocity_ranges[i]: os.path.join(self.samples_dir, f"C8v{i + 1}.wav")
            for i in range(16)
        }
    }

    def get_piano_sample_info(self, note, velocity):
        if note in self.piano_mapping:
            for vel_range, sample_info in self.piano_mapping[note].items():
                if vel_range[0] <= velocity <= vel_range[1]:
                    if isinstance(sample_info, dict):
                        return sample_info["sample"], sample_info["speed"]
                    else:
                        return sample_info, 1.0
        return None, None

    def get_trumpet_sample_info(self, note, velocity):
        if note in self.trumpet_mapping:
            for vel_range, sample_info in self.trumpet_mapping[note].items():
                if vel_range[0] <= velocity <= vel_range[1]:
                    if isinstance(sample_info, dict):
                        return sample_info["sample"], sample_info["speed"]
                    else:
                        return sample_info, 1.0
        return None, None

    def start_piano_note_playback(self, note, velocity):
        sample_path, speed = self.get_piano_sample_info(note, velocity)
        if sample_path and os.path.exists(sample_path):
            print(f"Playing piano note {note} with velocity {velocity}: {sample_path} at speed {speed}")
            player = SfPlayer(sample_path, speed=speed, loop=False, mul=0.5).out()
            self.active_players[note] = player
        else:
            print(f"No sample found for piano note {note} and velocity {velocity}")

    def start_trumpet_note_playback(self, note, velocity):
        sample_path, speed = self.get_trumpet_sample_info(note, velocity)
        if sample_path and os.path.exists(sample_path):
            print(f"Playing trumpet note {note} with velocity {velocity}: {sample_path} at speed {speed}")
            player = SfPlayer(sample_path, speed=speed, loop=False, mul=0.5).out()
            self.active_players[note] = player
        else:
            print(f"No sample found for trumpet note {note} and velocity {velocity}")

    def stop_piano_note_playback(self, note):
        if note in self.active_players:
            print(f"Stopping piano note {note} with smoother fade-out")
            player = self.active_players[note]
            volume_fade = SigTo(value=0, time=2, init=0.5)  # Customize fade-out time for piano
            player.setMul(volume_fade)
            player.stop(1)
            del self.active_players[note]

    def stop_trumpet_note_playback(self, note):
        if note in self.active_players:
            print(f"Stopping trumpet note {note} with smoother fade-out")
            player = self.active_players[note]
            volume_fade = SigTo(value=0, time=3, init=0.5)  # Customize fade-out time for trumpet
            player.setMul(volume_fade)
            player.stop(1)
            del self.active_players[note]

    def start_uploaded_note_playback(self, file_path):
        if file_path and os.path.exists(file_path):
            print(f"Playing uploaded file: {file_path}")
            player = SfPlayer(file_path, speed=1.0, loop=False, mul=0.5).out()
            self.active_players[file_path] = player  # Track by file path
        else:
            print(f"File not found: {file_path}")

    def stop_uploaded_note_playback(self, file_path):
        if file_path in self.active_players:
            print(f"Stopping uploaded file playback: {file_path}")
            player = self.active_players[file_path]
            volume_fade = SigTo(value=0, time=2, init=0.5)  # Customize fade-out time
            player.setMul(volume_fade)
            player.stop(1)
            del self.active_players[file_path]



    # def get_sample_info(self, note, velocity):
    #     if note in self.piano_mapping:
    #         for vel_range, sample_info in self.piano_mapping[note].items():
    #             if vel_range[0] <= velocity <= vel_range[1]:
    #                 if isinstance(sample_info, dict):
    #                     return sample_info["sample"], sample_info["speed"]
    #                 else:
    #                     return sample_info, 1.0
    #     return None, None
    #
    # def start_note_playback(self, note, velocity):
    #     sample_path, speed = self.get_sample_info(note, velocity)
    #     if sample_path and os.path.exists(sample_path):
    #         print(f"Playing note {note} with velocity {velocity}: {sample_path} at speed {speed}")
    #         player = SfPlayer(sample_path, speed=speed, loop=False, mul=0.5).out()
    #         self.active_players[note] = player
    #     else:
    #         print(f"No sample found for note {note} and velocity {velocity}")
    #
    # def stop_note_playback(self, note):
    #     if note in self.active_players:
    #         print(f"Stopping sample for MIDI note {note} with smoother fade-out")
    #         player = self.active_players[note]
    #         volume_fade = SigTo(value=0, time=2, init=0.5)
    #         player.setMul(volume_fade)
    #         player.stop(1)
    #         del self.active_players[note]
