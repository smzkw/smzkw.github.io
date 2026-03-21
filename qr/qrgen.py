# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "qrcode[pil]>=8.2",
# ]
# ///
import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://smzkw.github.io/")

img = qr.make_image(image_factory=StyledPilImage, embedded_image_path="qrface.png")
img.save("qr.png")
