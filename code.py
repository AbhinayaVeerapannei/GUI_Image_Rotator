# import the Python Image processing Library
from PIL import Image
import matplotlib.pyplot as plt

# Giving The Original image Directory Specified
Original_Image = Image.open("/Users/abhi/Documents/GitHub/GUI_Image_Rotator/image.webp")

# Rotate Image By 180 Degree
rotated_image1 = Original_Image.rotate(180)

# This is Alternative Syntax To Rotate The Image
rotated_image2 = Original_Image.transpose(Image.ROTATE_90)

# This Will Rotate Image By 60 Degree
rotated_image3 = Original_Image.rotate(60)

# Display the images using matplotlib
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(Original_Image)
plt.title("Original Image")

plt.subplot(2, 2, 2)
plt.imshow(rotated_image1)
plt.title("Rotated by 180 degrees")

plt.subplot(2, 2, 3)
plt.imshow(rotated_image2)
plt.title("Rotated by 90 degrees")

plt.subplot(2, 2, 4)
plt.imshow(rotated_image3)
plt.title("Rotated by 60 degrees")

plt.show()