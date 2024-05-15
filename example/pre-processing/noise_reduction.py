import cv2
import numpy as np

# Membaca citra dari file
image_path = 'pre-processing\img\captured_image.jpg'
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Periksa apakah citra berhasil dibaca
if image is None:
    print(f"Tidak dapat membaca file citra dari path: {image_path}")
    exit()

# Penghalusan Citra menggunakan Mean Filter (Box Filter)
def smooth_image_with_mean_filter(image, kernel_size):
    smoothed_image = cv2.blur(image, kernel_size)
    return smoothed_image

# Terapkan mean filter dengan kernel 3x3
kernel_size_3x3 = (3, 3)
smoothed_image_3x3 = smooth_image_with_mean_filter(image, kernel_size_3x3)

# Terapkan mean filter dengan kernel 2x2
kernel_size_2x2 = (2, 2)
smoothed_image_2x2 = smooth_image_with_mean_filter(image, kernel_size_2x2)

# Mendefinisikan kernel kustom
custom_kernel = np.array([[1, 1, 1],
                          [1, 1, 1],
                          [1, 1, 1]]) / 9  # Normalisasi agar total kernel menjadi 1

# Menerapkan konvolusi dengan kernel kustom
smoothed_image_custom_kernel = cv2.filter2D(image, -1, custom_kernel)

# Tampilkan hasil
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image 3x3', smoothed_image_3x3)
cv2.imshow('Smoothed Image 2x2', smoothed_image_2x2)
cv2.imshow('Smoothed Image custom', smoothed_image_custom_kernel)

# Tunggu hingga tombol sembarang ditekan untuk keluar
cv2.waitKey(0)
cv2.destroyAllWindows()

# Simpan hasil ke file
# cv2.imwrite('smoothed_image_3x3.jpg', smoothed_image_3x3)
# cv2.imwrite('smoothed_image_2x2.jpg', smoothed_image_2x2)
