import cv2
import numpy as np

def min_max_normalization(image):
    min_val = np.min(image)
    max_val = np.max(image)
    normalized_image = (image - min_val) / (max_val - min_val) * 255
    return normalized_image.astype(np.uint8)

# Baca citra
image = cv2.imread("img/cavendish/1373px-Cavendish_banana1.jpg", cv2.IMREAD_GRAYSCALE)

# Lakukan normalisasi
normalized_image = min_max_normalization(image)

# Tampilkan citra asli dan citra yang telah dinormalisasi
cv2.imshow("Original Image", image)
cv2.imshow("Normalized Image", normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
