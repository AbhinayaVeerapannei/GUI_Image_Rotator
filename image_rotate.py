# Import the Python Image processing Library
from PIL import Image
import matplotlib.pyplot as plt

def main():
    # Get the image path and angle from the user
    image_path = input("Enter the path to the image: ")
    angle = float(input("Enter the angle to rotate the image: "))

    try:
        # Open the image
        Original_Image = Image.open(image_path)
        
        # Rotate the image by the user-specified angle
        rotated_image = Original_Image.rotate(angle, expand=True)
        
        # Display the images using matplotlib
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.imshow(Original_Image)
        plt.title("Original Image")
        plt.axis('off')  # Hide the axis for better visualization

        plt.subplot(1, 2, 2)
        plt.imshow(rotated_image)
        plt.title(f"Rotated by {angle} degrees")
        plt.axis('off')  # Hide the axis for better visualization

        plt.show()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
