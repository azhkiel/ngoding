import cv2
import mediapipe as mp

# Inisialisasi MediaPipe untuk deteksi tangan
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Fungsi untuk menghitung jumlah jari yang terangkat
def count_fingers(hand_landmarks):
    # Indeks landmark tangan berdasarkan dokumentasi MediaPipe
    finger_tips = [4, 8, 12, 16, 20]  # Ujung jari ibu jari, telunjuk, tengah, manis, kelingking
    finger_mcp = [2, 5, 9, 13, 17]    # Titik referensi di pangkal jari (metacarpal)

    # Menyimpan hasil jari terangkat
    fingers_up = []

    # Ibu jari (berbeda dengan jari lain karena bergerak ke samping)
    if hand_landmarks.landmark[finger_tips[0]].x < hand_landmarks.landmark[finger_mcp[0]].x:
        fingers_up.append(1)  # Ibu jari terangkat
    else:
        fingers_up.append(0)  # Ibu jari tidak terangkat

    # Jari telunjuk sampai kelingking
    for i in range(1, 5):
        if hand_landmarks.landmark[finger_tips[i]].y < hand_landmarks.landmark[finger_mcp[i]].y:
            fingers_up.append(1)  # Jari terangkat
        else:
            fingers_up.append(0)  # Jari tidak terangkat

    return sum(fingers_up)  # Menghitung jumlah jari yang terangkat

# Fungsi utama untuk hand tracking dan finger counting
def hand_tracking_and_finger_counting():
    cap = cv2.VideoCapture(0)  # Menggunakan webcam
    
    with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Tidak dapat membuka kamera!")
                break

            # Konversi frame ke RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.flip(image, 1)  # Membalikkan gambar secara horizontal untuk tampilan cermin

            # Proses deteksi tangan
            results = hands.process(image)

            # Kembali ke format BGR untuk ditampilkan oleh OpenCV
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Jika tangan terdeteksi
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Gambar landmark tangan
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # Hitung jumlah jari yang terangkat
                    fingers_count = count_fingers(hand_landmarks)
                    
                    # Tampilkan hasil di layar
                    cv2.putText(image, f'jari yang terangkat: {fingers_count}', (10, 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

            # Tampilkan hasil
            cv2.imshow('Hand Tracking & Finger Counting', image)

            # Keluar jika tombol 'q' ditekan
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

# Menjalankan fungsi hand tracking dan finger counting
hand_tracking_and_finger_counting()
