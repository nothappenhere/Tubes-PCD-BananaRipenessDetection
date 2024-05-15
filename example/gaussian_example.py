import cv2
import numpy as np

# Load gambar
image = cv2.imread('img/cavendish/1373px-Cavendish_banana1.jpg')

# Tentukan ukuran kernel dan sigma
kernel_size = (5, 5)
sigma = 1.5

# Terapkan Gaussian blur
blurred_image = cv2.GaussianBlur(image, kernel_size, sigma)

# Definisikan kernel
kernel = (1.0 / 345) * np.array([
    [1, 5,  7,  5,  1],
    [5, 20, 33, 20, 5],
    [7, 33, 55, 33, 7],
    [5, 20, 33, 20, 5],
    [1, 5,  7,  5,  1]
])

# Terapkan filter
filtered_image = cv2.filter2D(image, -1, kernel)

# Tampilkan gambar asli dan gambar yang telah di-blur
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
