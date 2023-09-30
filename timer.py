import keyboard
from time import sleep
import simpleaudio
import wave
import json

json_file = open("settings.json", "r")
json_data = json.load(json_file)

wave_read = wave.open(json_data["wave"], "rb")
audio_data = wave_read.readframes(wave_read.getnframes())
num_channels = wave_read.getnchannels()
bytes_per_sample = wave_read.getsampwidth()
sample_rate = wave_read.getframerate()
target_time = json_data["time"]

def up_timer(secs):
    for i in range(secs, 0, -1):
        print(i)
        sleep(1)
    play_obj = simpleaudio.play_buffer(audio_data, num_channels, bytes_per_sample, sample_rate)
    play_obj.wait_done()

keyboard.add_hotkey(json_data["hotkey"], lambda: up_timer(target_time))
keyboard.wait()
