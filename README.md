# Lightweight Image Watermarking System

## Overview

The Lightweight Image Watermarking System is a digital image security solution developed using **Python**, **OpenCV**, and **Digital Signal Processing (DSP)** techniques. The project enables secure embedding of ownership information into digital images while preserving visual quality. By incorporating watermark data directly into the image's frequency components, the system provides a practical mechanism for copyright protection, ownership verification, and content authentication.

Unlike visible watermarks that can be cropped or removed, this project uses an invisible watermarking approach based on the **Discrete Cosine Transform (DCT)**, a widely used DSP technique in image compression and multimedia processing.

---

## Technologies Used

* Python
* OpenCV
* NumPy
* Digital Signal Processing (DSP)
* Discrete Cosine Transform (DCT)

---

## Project Objectives

* Protect intellectual property rights of digital images.
* Embed ownership information without affecting image quality.
* Verify image authenticity and ownership.
* Provide a lightweight and computationally efficient watermarking solution.
* Demonstrate practical applications of DSP in image security.

---

## Key Features

* Invisible watermark embedding.
* DCT-based frequency domain watermarking.
* High image quality preservation.
* Ownership verification support.
* Low computational complexity.
* Real-time processing capability.
* Automatic image quality evaluation using PSNR and MSE.

---

# System Architecture

Input Image
↓
Image Preprocessing
↓
8×8 Block Division
↓
DCT Transformation
↓
Watermark Bit Embedding
↓
Inverse DCT (IDCT)
↓
Watermarked Image
↓
PSNR & MSE Evaluation

---

# Step-by-Step Working

## Step 1: Image Selection

The user selects an image using a file picker dialog. The selected image is loaded into the system using OpenCV.

```python
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
```

The image is converted to grayscale for efficient processing and reduced computational overhead.

---

## Step 2: Watermark Generation

The ownership information is stored as text.

Example:

```text
LASYA2026
```

Each character is converted into its binary representation.

```python
watermark_bits = ''.join(format(ord(char), '08b') for char in watermark)
```

Example:

```text
L = 01001100
A = 01000001
```

The resulting binary sequence becomes the watermark data.

---

## Step 3: Image Block Division

The image is divided into multiple 8×8 pixel blocks.

Example:

```text
8×8 Block
┌─────────┐
│         │
│ Pixels  │
│         │
└─────────┘
```

DCT is applied independently to each block.

---

## Step 4: Applying DCT (DSP Technique)

The Discrete Cosine Transform converts image information from the spatial domain to the frequency domain.

```python
dct_block = cv2.dct(block)
```

The DCT separates image information into:

* Low-frequency components
* Mid-frequency components
* High-frequency components

This frequency representation allows watermark information to be hidden more effectively.

---

## Step 5: Watermark Embedding

A mid-frequency coefficient is selected:

```python
dct_block[3,4]
```

The watermark bit is embedded by modifying the Least Significant Bit (LSB) of the selected coefficient.

```python
coeff |= 1
```

or

```python
coeff &= ~1
```

Why mid-frequency coefficients?

* Less visible to human eyes.
* More resistant to compression.
* Better balance between robustness and image quality.

---

## Step 6: Inverse DCT

After embedding the watermark bit, the image block is reconstructed using the Inverse Discrete Cosine Transform.

```python
idct_block = cv2.idct(dct_block)
```

The reconstructed blocks form the final watermarked image.

---

## Step 7: Save Watermarked Image

The modified image is saved.

```python
cv2.imwrite("watermarked_image.png", watermarked)
```

The image appears visually identical to the original image while secretly containing ownership information.

---

# Role of DSP in the Project

Digital Signal Processing plays a critical role in watermark embedding.

Instead of modifying visible pixels directly, DSP techniques modify image frequency coefficients.

Benefits include:

* Better imperceptibility.
* Improved robustness.
* Reduced visual distortion.
* Resistance to image compression.
* Enhanced ownership verification.

The Discrete Cosine Transform (DCT) is one of the most widely used DSP techniques and is also employed in JPEG image compression.

---

# Image Quality Evaluation

To ensure that watermarking does not noticeably degrade image quality, two metrics are calculated:

## Mean Squared Error (MSE)

MSE measures the average pixel difference between the original and watermarked image.

Formula:

MSE = (1 / MN) Σ [Original - Watermarked]²

Python Implementation:

```python
mse = np.mean(
    (image.astype(np.float64) -
     watermarked.astype(np.float64)) ** 2
)
```

Lower MSE values indicate better image quality.

---

## Peak Signal-to-Noise Ratio (PSNR)

PSNR measures the quality of the watermarked image compared to the original image.

Formula:

PSNR = 20 × log10(MAX / √MSE)

Where:

* MAX = 255 for an 8-bit image
* MSE = Mean Squared Error

Python Implementation:

```python
if mse == 0:
    psnr = float('inf')
else:
    psnr = 20 * np.log10(
        255.0 / np.sqrt(mse)
    )
```

---

## PSNR Interpretation

| PSNR Value | Image Quality |
| ---------- | ------------- |
| > 40 dB    | Excellent     |
| 30 - 40 dB | Good          |
| 20 - 30 dB | Moderate      |
| < 20 dB    | Poor          |

Typical output:

```text
MSE  : 0.018542
PSNR : 65.45 dB
```

A PSNR above 40 dB indicates that the watermark is virtually invisible to the human eye.

---

# Intellectual Property Protection

## Ownership Verification

The watermark stores ownership information such as:

* Author Name
* Copyright ID
* Organization Name
* Unique Digital Identifier

The embedded information can be extracted later to prove ownership.

---

## Copyright Protection

The watermark remains associated with the image even when distributed online, helping deter unauthorized usage and redistribution.

---

## Content Authentication

Watermarks can help verify that images have not been altered or tampered with after publication.

---

## Brand Protection

Organizations can embed brand identifiers into marketing materials, product catalogs, and promotional content.

---

# Real-World Applications

* Copyright protection for photographers.
* Digital artwork ownership verification.
* Secure image distribution.
* Brand protection and logo security.
* Publishing and media authentication.
* Intellectual property rights management.
* Educational and research image protection.

---

# Future Enhancements

* Watermark extraction module.
* Logo-based watermarking.
* Color image watermarking.
* Robustness testing against noise and compression.
* SSIM (Structural Similarity Index) evaluation.
* GUI using Tkinter.
* QR-code-based watermark embedding.
* Cloud-based image ownership verification.

---

# Conclusion

This project demonstrates how Python, OpenCV, and DSP techniques can be combined to build an efficient and lightweight image watermarking system. By embedding ownership information into DCT frequency coefficients and evaluating image quality using MSE and PSNR, the system provides a practical solution for copyright protection, content authentication, and intellectual property rights management while maintaining excellent visual quality.

