import cv2

# Inisialisasi kamera
camera = cv2.VideoCapture(0)  # '0' biasanya mengacu pada kamera default

if not camera.isOpened():
    print("Tidak dapat membuka kamera")
    exit()

while True:
    # Membaca frame dari kamera
    ret, frame = camera.read()

    if not ret:
        print("Tidak dapat membaca frame")
        break

    # Tampilkan frame dalam jendela
    cv2.imshow('Frame', frame)

    # Tunggu tombol 'q' ditekan untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Ambil satu frame terakhir untuk disimpan sebagai gambar
ret, frame = camera.read()
if ret:
    cv2.imwrite('captured_image.jpg', frame)
    print("Gambar disimpan sebagai captured_image.jpg")

# Rilis kamera dan tutup semua jendela
camera.release()
cv2.destroyAllWindows()
