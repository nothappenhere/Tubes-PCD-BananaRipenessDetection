import cv2
import numpy as np

# Load gambar
image = cv2.imread('img/cavendish/1373px-Cavendish_banana1.jpg')

# Definisikan kernel Laplacian
laplacian_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Terapkan filter Laplacian
sharpened_image = cv2.filter2D(image, -1, laplacian_kernel)


# Load gambar
image = cv2.imread('img/cavendish/1373px-Cavendish_banana1.jpg', cv2.IMREAD_GRAYSCALE)

# Definisikan kernel Sobel untuk deteksi tepi horizontal
sobel_kernel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

sobel_kernel_y = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

# Terapkan filter Sobel
sharpened_image_sobel_x = cv2.filter2D(image, -1, sobel_kernel_x)
sharpened_image_sobel_Y = cv2.filter2D(image, -1, sobel_kernel_y)


# Definisikan kernel Scharr untuk deteksi tepi horizontal
scharr_kernel_x = np.array([
    [-3, 0, 3],
    [-10, 0, 10],
    [-3, 0, 3]
])

scharr_kernel_y = np.array([
    [-3, -10, -3],
    [0, 0, 0],
    [3, 10, 3]
])

# Terapkan filter Scharr
sharpened_image_scharr_x = cv2.filter2D(image, -1, scharr_kernel_x)
sharpened_image_scharr_y = cv2.filter2D(image, -1, scharr_kernel_y)

# Tampilkan gambar asli dan yang telah di-sharpen
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.imshow('Sharpened Image (Sobel-X)', sharpened_image_sobel_x)
cv2.imshow('Sharpened Image (Sobel-Y)', sharpened_image_sobel_Y)
cv2.imshow('Sharpened Image (Scharr-X)', sharpened_image_scharr_x)
cv2.imshow('Sharpened Image (Scharr-Y)', sharpened_image_scharr_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
