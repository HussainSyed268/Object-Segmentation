from PIL import Image
import numpy as np

input_image = Image.open("coins.png")
grayscale_image = input_image.convert("L")
threshold_value = 163

# Create a binary image by applying thresholding
binary_data = np.array(grayscale_image) > threshold_value
binary_image = Image.fromarray(np.uint8(binary_data) * 255)  # Convert to 0-255 range

binary_image.show()
