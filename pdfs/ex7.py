from pdf2image import convert_from_path

# Convert PDF pages to images
images = convert_from_path("example.pdf", dpi=300)
import pdb; pdb.set_trace()
for i, image in enumerate(images):
    image.save(f"page_{i+1}.jpg", "JPEG")
print("PDF converted to images.")
