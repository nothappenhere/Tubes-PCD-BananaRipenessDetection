import cv2

# Buka kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Terapkan threshold
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Temukan kontur
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Dapatkan bounding box dari setiap kontur
        x, y, w, h = cv2.boundingRect(contour)
        
        # Filter berdasarkan ukuran bounding box
        if w * h > 5000:  # Anda bisa menyesuaikan threshold ini sesuai kebutuhan
            # Gambar kotak di sekitar kontur
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Tambahkan teks "objek"
            cv2.putText(frame, 'objek', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
    
    # Tampilkan hasil
    cv2.imshow('Contours with Bounding Box', frame)
    
    # Keluar dengan menekan 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
