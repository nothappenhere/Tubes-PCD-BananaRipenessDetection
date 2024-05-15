import cv2
import numpy as np

# Load gambar
image = cv2.imread('img/cavendish/1373px-Cavendish_banana1.jpg')

# Tentukan ukuran kernel box filter
kernel_size = (3, 3)  # Ukuran kernel 3x3

# Terapkan box filter
smoothed_image = cv2.filter2D(image, -1, kernel_size)

# Tentukan kernel box filter
kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]) / 9

# Terapkan filter
filtered_image = cv2.filter2D(image, -1, kernel)


# Tampilkan gambar asli dan yang telah dihaluskan
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
