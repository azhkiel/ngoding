import cv2

# Membuka akses ke webcam (kamera default di 0)
cap = cv2.VideoCapture(0)

# Mengecek apakah webcam terbuka
if not cap.isOpened():
    print("Tidak dapat mengakses webcam")
else:
    print("Webcam berhasil diakses")

# Loop untuk menangkap setiap frame secara berulang
while True:
    # Membaca frame
    ret, frame = cap.read()
    
    # Memastikan frame berhasil ditangkap
    if not ret:
        print("Gagal mendapatkan frame")
        break
    
    # Menampilkan frame
    cv2.imshow('Webcam', frame)
    
    # Menunggu 1 ms untuk tombol 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Menutup jendela dan melepaskan webcam
cap.release()
cv2.destroyAllWindows()
