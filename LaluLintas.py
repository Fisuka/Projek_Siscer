# Fungsi Keanggotaan
def pendek(x):
    if x <= 20:
        return 1
    elif x > 20 and x < 70:
        return (70 - x) / 50
    else:
        return 0

def panjang(x):
    if x <= 20:
        return 0
    elif x > 20 and x < 70:
        return (x - 20) / 50
    else:
        return 1

# Inferensi Mamdani
def inferensi_mamdani(kepadatan_jalur1, kepadatan_jalur2):
    hasil_inferensi = []

    # Aturan Fuzzy
    hasil_inferensi.append(min(pendek(kepadatan_jalur1), pendek(kepadatan_jalur2))) 
    hasil_inferensi.append(min(pendek(kepadatan_jalur1), panjang(kepadatan_jalur2)))
    hasil_inferensi.append(min(panjang(kepadatan_jalur1), pendek(kepadatan_jalur2)))
    hasil_inferensi.append(min(panjang(kepadatan_jalur1), panjang(kepadatan_jalur2)))

    return hasil_inferensi

# Defuzzifikasi
def defuzzifikasi_mamdani(hasil_inferensi):
    durasi_lampu_hijau = (((hasil_inferensi[0] * 10) + (hasil_inferensi[1] * 10) + (hasil_inferensi[2] * 50) + (hasil_inferensi[3] * 20) ) / 
                    (hasil_inferensi[0] + hasil_inferensi[1] + hasil_inferensi[2] + hasil_inferensi[3]))

    return durasi_lampu_hijau

# Input variabel dari pengguna
kepadatan_jalur1_input = float(input("Masukkan nilai kepadatan jalur1 (0-10): "))
kepadatan_jalur2_input = float(input("Masukkan nilai kepadatan jalur2 (0-10): "))

# Inferensi Mamdani
hasil_inferensi = inferensi_mamdani(kepadatan_jalur1_input, kepadatan_jalur2_input)

# Defuzzifikasi Mamdani
durasi_lampu_hijau = defuzzifikasi_mamdani(hasil_inferensi)

print("Durasi Lampu Hijau Jalur 1:")
print(durasi_lampu_hijau)