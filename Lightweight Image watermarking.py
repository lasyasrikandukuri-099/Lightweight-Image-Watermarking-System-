import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# -----------------------------------
# Select Image Using File Picker
# -----------------------------------
Tk().withdraw()

image_path = askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp *.tif"),
        ("All Files", "*.*")
    ]
)

if not image_path:
    print("No image selected.")
    exit()

# -----------------------------------
# Load Image
# -----------------------------------
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to load image!")
    exit()

print(f"Selected Image: {image_path}")

# -----------------------------------
# Watermark Text
# -----------------------------------
watermark = "LASYA2026"

# Convert watermark text to binary
watermark_bits = ''.join(format(ord(char), '08b') for char in watermark)

# -----------------------------------
# DCT Watermark Embedding
# -----------------------------------
watermarked = image.copy()

h, w = image.shape
bit_index = 0

for row in range(0, h - 7, 8):
    for col in range(0, w - 7, 8):

        if bit_index >= len(watermark_bits):
            break

        # Extract 8x8 block
        block = np.float32(
            watermarked[row:row+8, col:col+8]
        )

        # Apply DCT
        dct_block = cv2.dct(block)

        # Current watermark bit
        bit = int(watermark_bits[bit_index])

        # Mid-frequency coefficient
        coeff = int(round(dct_block[3, 4]))

        if bit == 1:
            coeff |= 1
        else:
            coeff &= ~1

        dct_block[3, 4] = float(coeff)

        # Inverse DCT
        idct_block = cv2.idct(dct_block)

        watermarked[row:row+8, col:col+8] = np.clip(
            idct_block,
            0,
            255
        )

        bit_index += 1

    if bit_index >= len(watermark_bits):
        break

# -----------------------------------
# Convert Back to uint8
# -----------------------------------
watermarked = np.uint8(watermarked)

# -----------------------------------
# Save Output Image
# -----------------------------------
input_folder = os.path.dirname(image_path)

output_path = os.path.join(
    input_folder,
    "watermarked_image.png"
)

cv2.imwrite(output_path, watermarked)

# -----------------------------------
# Calculate MSE
# -----------------------------------
mse = np.mean(
    (
        image.astype(np.float64)
        - watermarked.astype(np.float64)
    ) ** 2
)

# -----------------------------------
# Calculate PSNR
# -----------------------------------
if mse == 0:
    psnr = float("inf")
else:
    psnr = 20 * np.log10(
        255.0 / np.sqrt(mse)
    )

# -----------------------------------
# Results
# -----------------------------------
print("\n===== RESULTS =====")
print("Watermark Embedded Successfully!")
print(f"Watermark Text : {watermark}")
print(f"Watermark Length : {len(watermark)} characters")
print(f"MSE  : {mse:.6f}")
print(f"PSNR : {psnr:.2f} dB")
print(f"Output Saved : {output_path}")

# -----------------------------------
# Display Images
# -----------------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Watermarked Image", watermarked)

cv2.waitKey(0)
cv2.destroyAllWindows()