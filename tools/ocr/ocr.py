from PIL import Image
from pytesseract import pytesseract
image = Image.open("test.png")
text = pytesseract.image_to_string(image)
print(text)