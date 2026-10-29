def hitung_rata_rata(nilai):
    total = sum(nilai)
    return total / len(nilai)


print("Rata-rata 3 nilai:", hitung_rata_rata([80, 90, 70]))
print("Rata-rata 2 nilai:", hitung_rata_rata([100, 80]))