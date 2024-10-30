import cv2
from deepface import DeepFace

# Fungsi utama untuk mendeteksi wajah dan memprediksi umur
def face_and_age_detection():
    # Buka webcam (0 adalah id default untuk webcam utama)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Tidak dapat membuka webcam.")
        return

    while True:
        # Baca frame dari webcam
        ret, frame = cap.read()
        
        if not ret:
            print("Gagal menangkap frame.")
            break

        # Konversi frame ke RGB karena DeepFace membutuhkan format RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        try:
            # Deteksi wajah dan prediksi umur
            predictions = DeepFace.analyze(image_rgb, actions=['age'], enforce_detection=False)
            age = predictions['age']

            # Deteksi wajah dengan OpenCV untuk menampilkan kotak di sekitar wajah
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Gambar kotak di sekitar wajah
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # Tampilkan prediksi umur di atas kotak wajah
                cv2.putText(frame, f'Age: {int(age)}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        except Exception as e:
            print(f"Error in face detection: {e}")

        # Tampilkan frame dengan deteksi wajah dan prediksi umur
        cv2.imshow('Face and Age Detection', frame)

        # Tekan 'q' untuk keluar dari loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Lepas resource webcam dan tutup semua window
    cap.release()
    cv2.destroyAllWindows()

# Jalankan fungsi untuk mendeteksi wajah dan umur melalui webcam
face_and_age_detection()
