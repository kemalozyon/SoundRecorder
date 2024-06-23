import sounddevice as sd
import scipy.io.wavfile

print(sd.query_devices())

default_input_device = sd.default.device[0]
input_device_info = sd.query_devices(default_input_device,'input')

print(input_device_info)

duration = 5  # Duration of recording in seconds
freq = 44100  # Sampling frequency

# Set the correct number of channels
channels = input_device_info['max_input_channels']

# Record audio
recording = sd.rec(int(duration * freq), samplerate=freq, channels=channels)

# Wait until the recording is finished
sd.wait()
scipy.io.wavfile.write('output.wav', freq, recording)
