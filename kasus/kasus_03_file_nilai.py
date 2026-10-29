def baca_nilai(teks):
    """Mengubah teks menjadi daftar nilai numerik yang valid."""
    nilai = []

    if teks.strip() == "":
        return nilai

    for bagian in teks.split(","):
        bagian = bagian.strip()

        try:
            angka = float(bagian)
        except ValueError:
            print(f"Data tidak valid: {bagian}")
            continue

        if 0 <= angka <= 100:
            nilai.append(angka)
        else:
            print(f"Nilai di luar rentang 0-100: {angka}")

    return nilai


def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return None

    return sum(nilai) / len(nilai)


# Pengujian 1: seluruh data valid
data_1 = baca_nilai("80, 90, 70")
print("Data 1:", data_1)
print("Rata-rata 1:", hitung_rata_rata(data_1))

# Pengujian 2: terdapat data yang bukan angka
data_2 = baca_nilai("80, abc, 90")
print("Data 2:", data_2)
print("Rata-rata 2:", hitung_rata_rata(data_2))

# Pengujian 3: terdapat nilai di luar rentang
data_3 = baca_nilai("75, 120, 60")
print("Data 3:", data_3)
print("Rata-rata 3:", hitung_rata_rata(data_3))

# Pengujian 4: input kosong
data_4 = baca_nilai("")
print("Data 4:", data_4)
print("Rata-rata 4:", hitung_rata_rata(data_4))