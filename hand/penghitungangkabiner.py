def decimal_to_binary(n):
    return bin(n).replace("0b", "")  # Menghapus prefix '0b'

while True:
    user_input = input("Masukkan angka desimal (atau ketik 'metu' untuk keluar): ")
    
    if user_input.lower() == 'metu':
        print("Keluar dari program.")
        break
    
    try:
        number = int(user_input)  # Mengonversi input ke integer
        binary_representation = decimal_to_binary(number)
        print(f"Representasi biner dari {number} adalah: {binary_representation}")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka desimal yang valid.")
