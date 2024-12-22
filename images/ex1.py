from pathlib import Path
from PIL import Image, ImageFilter

# Open an image
parent = Path(__file__).parent
path = parent.joinpath("example.jpg")
image = Image.open(path)

# Apply a blur filter
blurred_image = image.filter(ImageFilter.FIND_EDGES)
blurred_image.save(parent.joinpath("blurred_example.jpg"))

# Convert image to grayscale
grayscale_image = image.convert("L")
grayscale_image.save(parent.joinpath("grayscale_example.jpg"))

# Resize image]
resized_image = image.resize((200, 200))
resized_image.save(parent.joinpath("resized_example.jpg"))

# crop
cropped_image = image.crop((50, 50, 300, 300))
cropped_image.save(parent.joinpath("cropped_example.jpg"))

print("Image processing with Pillow completed.")
