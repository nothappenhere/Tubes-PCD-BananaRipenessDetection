import cv2
import numpy as np

# Load gambar
image = cv2.imread('img/cavendish/1373px-Cavendish_banana1.jpg', cv2.IMREAD_GRAYSCALE)

# Definisikan kernel struktur
kernel = np.ones((5,5),np.uint8)

# 1. Erosi
erosion = cv2.erode(image, kernel, iterations = 1)

# 2. Dilasi
dilation = cv2.dilate(image, kernel, iterations = 1)

# 3. Opening
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# 4. Closing
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# 5. Morfologi Tepi
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# 6. Hitung Area
_, labels = cv2.connectedComponents(image)
region_count = np.max(labels)

# 7. Transformasi Jarak
dist_transform = cv2.distanceTransform(image, cv2.DIST_L2, 5)

# 8. Skeletonization
_, skeleton = cv2.threshold(dist_transform, 0.1*dist_transform.max(), 255, 0)

# Tampilkan gambar dan hasil morfologi
cv2.imshow('Original Image', image)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.imshow('Gradient', gradient)
cv2.imshow('Skeleton', skeleton.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
