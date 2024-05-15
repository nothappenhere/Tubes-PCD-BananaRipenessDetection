# Import modul-modul yang dibutuhkan
import sys  # Import modul 'sys' untuk mengakses fungsi-fungsi sistem
import cv2  # Import modul 'cv2 (OpenCV)' untuk pemrosesan gambar dan video
from PyQt5 import QtCore, QtWidgets  # Import modul 'QtCore' dan 'QtWidgets' dari PyQt5 untuk pembuatan antarmuka grafis
from PyQt5.QtCore import *  # Import semua kelas dan fungsi dari modul 'QtCore'
from PyQt5.QtGui import *  # Import semua kelas dan fungsi dari modul 'QtGui'
from PyQt5.QtWidgets import *  # Import semua kelas dan fungsi dari modul 'QtWidgets'
from PyQt5.uic import loadUi  # Import fungsi 'loadUi' dari modul 'uic' di PyQt5 untuk memuat file .UI yang telah dibuat menggunakan Qt Designer
from util import *

class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage, self).__init__()
        loadUi('ui/main.ui', self)
        self.Image = None

        # Initialize lower and upper bounds for banana colors
        self.lower = {
            'matang': (8, 70, 60),          # Nilai batas rendah untuk pisang matang (B, G, R)
            'mentah': (30, 50, 50),         # Nilai batas rendah untuk pisang mentah (B, G, R)
            'setengah matang': (10, 140, 120)  # Nilai batas rendah untuk pisang setengah matang (B, G, R)
        }
        self.upper = {
            'matang': (25, 255, 255),       # Nilai batas atas untuk pisang matang (B, G, R)
            'mentah': (100, 255, 255),      # Nilai batas atas untuk pisang mentah (B, G, R)
            'setengah matang': (25, 255, 255)  # Nilai batas atas untuk pisang setengah matang (B, G, R)
        }
        self.colors = {
            'matang': (24, 181, 124), # BGR
            'mentah':  (44, 222, 243), # BGR
            'setengah matang': (0, 140, 255) # BGR
        }
        
        self.btn_input.clicked.connect(self.loadFile)
        self.btn_simpan.clicked.connect(self.saveImage)

    def loadFile(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, 'Memuat Gambar', "", "Images (*.png *.jpg *.jpeg)")
            if file_path:
                self.Image = cv2.imread(file_path)
                self.displayImage(self.Image, 1)

                # Pre-processing
                normalisasi = normalize_image(self.Image)
                resize = cv2.resize(normalisasi, (450, 450))
                gaussian = gaussian_filter(resize)
                noise_reduc = noise_reduction(gaussian)
                sharpening = sharpening_image(noise_reduc)
                self.displayImage(sharpening, 2)

                # Convert to HSV color space
                hsv_image = cv2.cvtColor(sharpening, cv2.COLOR_BGR2HSV)
                contours = {}
                
                # Perform masking and morphological operations for each banana color
                # for color, lower, upper in zip(self.colors.keys(), self.lower.values(), self.upper.values()):
                for key_color, color in self.upper.items():
                    # Initialize structuring element for morphological operations
                    strel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                    # Perform masking
                    masking_image = cv2.inRange(hsv_image, self.lower[key_color], self.upper[key_color])
                    # Perform morphological opening to remove small noise
                    masking_image = opening_image(masking_image, strel)
                    # Perform morphological closing to fill in small gaps
                    masking_image = closing_image(masking_image, strel)

                    # Display the result
                    if key_color == 'matang':
                        self.displayImage(masking_image, 5)
                    elif key_color == 'mentah':
                        self.displayImage(masking_image, 3)
                    elif key_color == 'setengah matang':
                        self.displayImage(masking_image, 4)

                    # mencari conture di setiap warna
                    contour, _ = cv2.findContours(masking_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    # bila conture pada warna tersebut di temukan
                    if(len(contour) > 0):
                        # maka masukan ke dalam array associative dan cari conture terbesarnya
                        contours[key_color] = max(contour, key=cv2.contourArea)

                    # mencari conture terbesar pada array di setiap warna, dapatkan (key nya
                    key = max(contours, key=lambda x: cv2.contourArea(contours[x]))
                    # simpan 
                    largest_contour = contours[key]

                    # perhalus bentuk dari conture 
                    epsilon = 0.01 * cv2.arcLength(largest_contour, True)
                    approx = cv2.approxPolyDP(largest_contour, epsilon, True)

                    # cari titik tengahnya dari conture
                    ((X, Y), radius) = cv2.minEnclosingCircle(approx)

                    # gambarnya conture yang di tangkap
                    cv2.drawContours(resize, [approx], -1, (0, 0, 255), 3)

                    if (len(approx) > 10):
                        # text berdasarkan key yang di dapat
                        if key == "matang" :
                            text = "matang"
                        elif key == "mentah":
                            text = "mentah"
                        elif key == "setengah matang":
                            text = "setengah matang"

                        # Menentukan titik tengah kontur untuk menyimpan text
                        M = cv2.moments(largest_contour)
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])

                        (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 2, 3)
                        text_x = cX - text_width // 2
                        text_y = cY + text_height // 2

                        if radius > 90:
                            # gambar conture berserta dengan text
                            cv2.circle(resize, (int(X), int(Y)), int(radius), self.colors[key], 3)
                            cv2.putText(resize, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3, cv2.LINE_AA)
                            self.Image = resize

                self.displayImage(self.Image, 6)
                palette = dominant_color(file_path)  # Mendapatkan palet warna dominan
                for i, color in enumerate(palette):
                    # Menentukan label yang sesuai untuk menampilkan warna dominan
                    label_warna = getattr(self, f"label_warna{i+1}")
                    # Menghitung kecerahan warna latar belakang
                    brightness = (0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]) / 255
                    # Menentukan warna teks berdasarkan kecerahan latar belakang
                    if brightness < 0.5:  # Jika latar belakang gelap
                        label_warna.setStyleSheet(f"color: white; background-color: #{color[0]:02x}{color[1]:02x}{color[2]:02x}; border: 1px solid #000")
                    else:  # Jika latar belakang terang
                        label_warna.setStyleSheet(f"color: black; background-color: #{color[0]:02x}{color[1]:02x}{color[2]:02x}; border: 1px solid #000")
                    label_warna.setText(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}".upper())
            else:
                QMessageBox.warning(self, "Warning", "Tidak ada gambar yang dipilih.")
        except Exception as e:
            QMessageBox.critical(self, "Error", "Kesalahan saat memuat gambar: {}".format(str(e)))

    def saveImage(self):
        pixmap = self.img_hasil.pixmap()
        if pixmap is not None:
            output_image = pixmap.toImage()
            file_path, _ = QFileDialog.getSaveFileName(self, 'Simpan Gambar', "Output", "Images (*.jpg);;Images (*.png *.jpeg)")
            if file_path:
                output_image.save(file_path)
                QMessageBox.information(self, "Success", "Gambar berhasil disimpan.")
            else:
                QMessageBox.warning(self, "Warning", "Operasi penyimpanan dibatalkan.")
        else:
            QMessageBox.critical(self, "Critical", "Tidak ada gambar untuk disimpan.")

    def displayImage(self, Image, windows=1):
        qformat = QImage.Format_Indexed8  # Mengatur format gambar awal ke Format_Indexed8 (skala abu-abu)
        # Memeriksa apakah gambar memiliki 3 dimensi (gambar berwarna)
        if len(Image.shape) == 3:
            # Jika gambar memiliki 4 channel (RGBA), maka format gambar diatur ke Format_RGBA8888
            if (Image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            # Jika gambar memiliki 3 channel (RGB), maka format gambar diatur ke Format_RGB888
            else:
                qformat = QImage.Format_RGB888
        # Membuat objek 'QImage' dari array gambar
        img = QImage(Image, Image.shape[1], Image.shape[0], Image.strides[0], qformat)
        img = img.rgbSwapped()  # Menukar saluran warna (RGB ke BGR atau sebaliknya)
        
        # Menampilkan gambar dalam label yang sesuai berdasarkan nilai windows
        if windows == 1:
            self.img_input.setPixmap(QPixmap.fromImage(img))  # Menampilkan gambar dalam label untuk gambar asli
            self.img_input.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)  # Mengatur perataan gambar di label
            self.img_input.setScaledContents(True)  # Mengaktifkan konten gambar yang dapat diskalakan
        elif windows == 2:
            self.img_preprocess.setPixmap(QPixmap.fromImage(img))  # Menampilkan gambar dalam label untuk gambar asli
            self.img_preprocess.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)  # Mengatur perataan gambar di label
            self.img_preprocess.setScaledContents(True)  # Mengaktifkan konten gambar yang dapat diskalakan
        elif windows == 3:
            self.img_mentah.setPixmap(QPixmap.fromImage(img))  # Menampilkan gambar dalam label untuk gambar asli
            self.img_mentah.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)  # Mengatur perataan gambar di label
            self.img_mentah.setScaledContents(True)  # Mengaktifkan konten gambar yang dapat diskalakan
        elif windows == 4:
            self.img_setengah.setPixmap(QPixmap.fromImage(img))  # Menampilkan gambar dalam label untuk gambar asli
            self.img_setengah.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)  # Mengatur perataan gambar di label
            self.img_setengah.setScaledContents(True)  # Mengaktifkan konten gambar yang dapat diskalakan
        elif windows == 5:
            self.img_matang.setPixmap(QPixmap.fromImage(img))  # Menampilkan gambar dalam label untuk gambar asli
            self.img_matang.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)  # Mengatur perataan gambar di label
            self.img_matang.setScaledContents(True)  # Mengaktifkan konten gambar yang dapat diskalakan
        elif windows == 6:
            self.img_hasil.setPixmap(QPixmap.fromImage(img))  # Menampilkan gambar dalam label untuk gambar asli
            self.img_hasil.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)  # Mengatur perataan gambar di label
            self.img_hasil.setScaledContents(True)  # Mengaktifkan konten gambar yang dapat diskalakan

app = QtWidgets.QApplication(sys.argv)  # Membuat objek aplikasi QApplication
window = ShowImage()  # Membuat objek window dari class 'ShowImage'
window.setWindowTitle("Banana Ripeness Detection")  # Menetapkan judul jendela aplikasi
window.show()  # Menampilkan jendela aplikasi
sys.exit(app.exec_())  # Mengakhiri aplikasi dan menjalankan event loop untuk menangani event yang terjadi