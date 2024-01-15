from PIL import Image
import numpy as np

def encode_data_in_region(image_path, data, region):
    img = Image.open(image_path)
    binary_data = ''.join(format(ord(char), '08b') for char in data)
    if len(binary_data) > region[2] * region[3] * 3:
        raise ValueError("Data too large to be encoded in the specified region")
    img_array = np.array(img)
    y_start, x_start, height, width = region
    binary_data_iter = iter(binary_data)
    for y in range(y_start, y_start + height):
        for x in range(x_start, x_start + width):
            if len(binary_data) == 0:
                break
            pixel = img_array[y, x]
            for i in range(3):
                try:
                    bit = int(next(binary_data_iter))
                except StopIteration:
                    bit = 0  # If we run out of data, pad with zeros
                pixel[i] = (pixel[i] & 0xFE) | bit
    encoded_img = Image.fromarray(img_array)
    return encoded_img

def decode_data_in_region(image_path, region):
    img = Image.open(image_path)
    img_array = np.array(img)
    y_start, x_start, height, width = region
    binary_data = ''
    for y in range(y_start, y_start + height):
        for x in range(x_start, x_start + width):
            pixel = img_array[y, x]
            for channel in pixel:
                binary_data += str(channel & 1)

    padded_binary_data = binary_data.ljust((len(binary_data) + 7) & ~7, '0')
    # Group the binary data into bytes and convert to characters
    data = ''.join(chr(int(padded_binary_data[i:i + 8], 2)) for i in range(0, len(padded_binary_data), 8))
    return data

# specify file path to image
image_path = 'example_image.jpeg'
# secret message
secret_data = "whoami"
# can encode data in more than one region 👀
region_to_encode = (100, 100, 50, 50)  # Define the region as (y_start, x_start, height, width)
encoded_image = encode_data_in_region(image_path, secret_data, region_to_encode)
encoded_image.save('encoded_image.png')

decoded_data = decode_data_in_region('encoded_image.png', region_to_encode)
print(decoded_data)
