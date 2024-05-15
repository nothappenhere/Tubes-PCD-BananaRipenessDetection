import cv2
import numpy as np

# Load gambar
image = cv2.imread("img/cavendish/1373px-Cavendish_banana1.jpg", cv2.IMREAD_GRAYSCALE)

# Membuat strel berbentuk persegi dengan ukuran 5x5
square_strel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Membuat strel berbentuk elips dengan ukuran 5x5
ellipse_strel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Membuat strel berbentuk cross dengan ukuran 5x5
cross_strel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

# Operasi erosi dengan strel persegi
erosion_square = cv2.erode(image, square_strel, iterations=1)

# Operasi dilasi dengan strel elips
dilation_ellipse = cv2.dilate(image, ellipse_strel, iterations=1)

# Operasi opening dengan strel cross
opening_cross = cv2.morphologyEx(image, cv2.MORPH_OPEN, cross_strel)

# Operasi closing dengan strel persegi
closing_square = cv2.morphologyEx(image, cv2.MORPH_CLOSE, square_strel)

# Tampilkan gambar dan hasil morfologi
cv2.imshow('Original Image', image)
cv2.imshow('Erosion (Square)', erosion_square)
cv2.imshow('Dilation (Ellipse)', dilation_ellipse)
cv2.imshow('Opening (Cross)', opening_cross)
cv2.imshow('Closing (Square)', closing_square)
cv2.waitKey(0)
cv2.destroyAllWindows()
