import cv2
import numpy as np

# Membaca citra dari file
image = cv2.imread('img/banana/banana.jpg', cv2.IMREAD_COLOR)

# Perbaikan Kontras menggunakan Histogram Equalization
def enhance_contrast(image):
    # Konversi ke ruang warna YCrCb
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    # Pisahkan kanal
    y, cr, cb = cv2.split(ycrcb)
    # Equalisasi histogram pada kanal Y
    y_eq = cv2.equalizeHist(y)
    # Gabungkan kembali kanal
    ycrcb_eq = cv2.merge((y_eq, cr, cb))
    # Konversi kembali ke ruang warna BGR
    enhanced_image = cv2.cvtColor(ycrcb_eq, cv2.COLOR_YCrCb2BGR)
    return enhanced_image

# Penajaman Citra menggunakan Laplacian Filter
def sharpen_image(image):
    # Aplikasikan filter laplacian
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    sharpened_image = cv2.convertScaleAbs(laplacian)
    return sharpened_image

# Penghalusan Citra menggunakan Gaussian Blur
def smooth_image(image):
    # Aplikasikan Gaussian Blur
    smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)
    return smoothed_image

# Terapkan peningkatan kualitas citra
enhanced_image = enhance_contrast(image)
sharpened_image = sharpen_image(image)
# smoothed_image = smooth_image(image)

# Tampilkan hasil
cv2.imshow('Original Image', image)
cv2.imshow('Enhanced Contrast', enhanced_image)
cv2.imshow('Sharpened Image', sharpened_image)
# cv2.imshow('Smoothed Image', smoothed_image)

# Tunggu hingga tombol sembarang ditekan untuk keluar
cv2.waitKey(0)
cv2.destroyAllWindows()

# Simpan hasil ke file
# cv2.imwrite('enhanced_contrast.jpg', enhanced_image)
# cv2.imwrite('sharpened_image.jpg', sharpened_image)
# cv2.imwrite('smoothed_image.jpg', smoothed_image)
