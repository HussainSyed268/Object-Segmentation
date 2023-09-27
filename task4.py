from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2

# Open the input image
input_image = Image.open("coins.png")
# Convert the RGB image to grayscale
grayscale_image = input_image.convert("L")
# Define a threshold value (adjust as needed)
threshold_value = 163

# Create a binary image by applying thresholding
binary_data = np.array(grayscale_image) > threshold_value
binary_image = Image.fromarray(np.uint8(binary_data) * 255)  # Convert to 0-255 range
# Invert the binary image (coins become white, background becomes black)
inverted_binary_image = Image.fromarray(255 - binary_data.astype(np.uint8) * 255)

# Find contours in the inverted binary image
contours, _ = cv2.findContours(np.array(inverted_binary_image), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create an image to draw the contours and bounding rectangles
contour_image = np.zeros_like(np.array(inverted_binary_image), dtype=np.uint8)

# Filter and draw only the large contours (coins) and bounding rectangles
min_contour_area = 300  # Adjust this threshold as needed

# Convert the contour_image to a Pillow image for drawing
contour_image_pillow = Image.fromarray(255 - contour_image)

draw = ImageDraw.Draw(contour_image_pillow)

for contour in contours:
    if cv2.contourArea(contour) > min_contour_area:
        # Draw the contour
        cv2.drawContours(contour_image, [contour], -1, 255, thickness=cv2.FILLED)



# Invert the contour image back to the original orientation
segmented_image = Image.fromarray(255 - contour_image)

# Create a copy of the segmented image for drawing rectangles
image_with_rectangles = segmented_image.copy()
draw = ImageDraw.Draw(input_image)
font = ImageFont.load_default()  # Use the default font

coin_counter = 0
for contour in contours:
    if cv2.contourArea(contour) > min_contour_area:
        # Get the coordinates of the bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)
        coin_counter += 1
        # Draw a green rectangle around the coin with a width of 20 pixels
        draw.rectangle([x, y, x + w, y + h], outline="red", width=2)

        draw.text((x + 5, y + 5), str(coin_counter), fill="red", font=font)

# Show the image with green rectangles
input_image.show()