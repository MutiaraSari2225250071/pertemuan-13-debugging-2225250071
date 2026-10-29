def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None
    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi


# T1: Menguji rata-rata empat nilai
print("T1 - Rata-rata:", hitung_rata_rata([80, 60, 90, 70]))

# T2: Menguji rata-rata dua nilai
print("T2 - Rata-rata:", hitung_rata_rata([100, 80]))

# T3: Menguji batas kelulusan nilai 60
print("T3 - Status nilai 60:", status(60))

# T4: Menguji nilai di bawah batas kelulusan
print("T4 - Status nilai 59:", status(59))

# T5: Menguji pencarian nilai tertinggi
print("T5 - Nilai tertinggi:", nilai_tertinggi([80, 60, 90, 70]))

# T6: Menguji rata-rata dengan input kosong
print("T6 - Rata-rata input kosong:", hitung_rata_rata([]))

# T7: Menguji nilai tertinggi dengan input kosong
print("T7 - Nilai tertinggi input kosong:", nilai_tertinggi([]))