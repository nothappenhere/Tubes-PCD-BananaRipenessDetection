import cv2
import numpy as np

# Membaca citra dari file
image_path = 'pre-processing\img\captured_image.jpg'
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Periksa apakah citra berhasil dibaca
if image is None:
    print(f"Tidak dapat membaca file citra dari path: {image_path}")
    exit()

# Daftar kernel yang akan digunakan
kernels = [
    np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ]),
    np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]),
    np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]),
    np.array([
        [1, -2, 1],
        [-2, 5, -2],
        [1, -2, 1]
    ]),
    np.array([
        [1, -2, 1],
        [-2, 4, -2],
        [1, -2, 1]
    ]),
    np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ])
]

# Proses sharpening menggunakan setiap kernel dan tampilkan hasil
for i, kernel in enumerate(kernels, start=1):
    # Proses sharpening menggunakan kernel tertentu
    sharpened_image = cv2.filter2D(image, -1, kernel)
    # Tampilkan hasil dengan menambahkan nomor kernel pada judul jendela
    cv2.imshow(f'Sharpened Image (Kernel {i})', sharpened_image)

# Tunggu hingga tombol sembarang ditekan untuk keluar
cv2.waitKey(0)
cv2.destroyAllWindows()
