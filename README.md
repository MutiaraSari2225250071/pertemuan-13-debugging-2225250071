# Pertemuan 13 - Debugging dan Testing

**Nama:** Mutiara Sari  
**NIM:** 2225250071  
**Kelas:** 3A

## 1. Kasus

Praktik ini bertujuan untuk menginvestigasi dan memperbaiki bug pada program Python yang menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi.

Proses debugging dilakukan dengan menjalankan program, mengamati hasil aktual, menelusuri kode menggunakan debugger di Visual Studio Code, mengidentifikasi akar penyebab kesalahan, memperbaiki kode, serta menjalankan kembali test case untuk memastikan hasilnya sesuai dengan hasil yang diharapkan.

File program yang diuji adalah `praktik/praktik_4_debugging.py`.

## 2. Pengujian Awal

Program dijalankan sebelum perbaikan untuk mengetahui perilaku awalnya. Hasil yang diperoleh adalah:

```text
Rata-rata: 60.0
Status 60: Tidak lulus
Tertinggi: 0
```

Hasil tersebut menunjukkan adanya tiga masalah:
1. Perhitungan rata-rata menghasilkan nilai yang tidak sesuai.
2. Nilai 60 dinyatakan tidak lulus, padahal batas kelulusan adalah 60.
3. Fungsi pencarian nilai tertinggi menghasilkan 0 meskipun terdapat nilai yang lebih tinggi.

## 3. Test Case

| ID | Input | Expected | Actual Awal | Status Awal |
|---|---|---|---|---|
| T1 | Rata-rata `[80, 60, 90, 70]` | `75.0` | `60.0` | FAIL |
| T2 | Rata-rata `[100, 80]` | `90.0` | `36.0` | FAIL |
| T3 | Status nilai `60` | `Lulus` | `Tidak lulus` | FAIL |
| T4 | Status nilai `59` | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | Nilai tertinggi `[80, 60, 90, 70]` | `90` | `0` | FAIL |
| T6 | Rata-rata `[]` | `0` | `0.0` | PASS |
| T7 | Nilai tertinggi `[]` | `None` | `0` | FAIL |

**Catatan:** Hasil aktual awal pada tabel ditentukan dari perilaku kode sebelum diperbaiki. Hasil pengujian awal yang benar-benar dicatat saat program dijalankan adalah rata-rata `60.0`, status nilai 60 `Tidak lulus`, dan nilai tertinggi `0`.

## 4. Bug Report

### Bug B01 — Kesalahan Perhitungan Rata-rata

- **Lokasi:** Fungsi `hitung_rata_rata()` pada `praktik/praktik_4_debugging.py`.
- **Gejala:** Hasil rata-rata tidak sesuai dengan jumlah data yang dimasukkan.
- **Akar penyebab:** Program membagi jumlah nilai dengan angka tetap 5, bukan dengan jumlah data yang sebenarnya.
- **Perbaikan:** Menggunakan `len(nilai)` sebagai pembagi dan menangani input kosong.

Kode setelah perbaikan:

```python
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)
```

### Bug B02 — Kesalahan Batas Kelulusan

- **Lokasi:** Fungsi `status()`.
- **Gejala:** Nilai 60 dinyatakan tidak lulus.
- **Akar penyebab:** Kondisi menggunakan operator `>` sehingga nilai yang sama dengan batas kelulusan tidak memenuhi kondisi.
- **Perbaikan:** Mengganti operator `>` menjadi `>=`.

Kode setelah perbaikan:

```python
def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"
```

### Bug B03 — Kesalahan Pencarian Nilai Tertinggi

- **Lokasi:** Fungsi `nilai_tertinggi()`.
- **Gejala:** Fungsi menghasilkan 0 untuk data `[80, 60, 90, 70]`.
- **Akar penyebab:** Nilai awal ditetapkan 0 dan kondisi perbandingan menggunakan operator `<`, sehingga pencarian nilai tertinggi tidak berjalan sebagaimana mestinya.
- **Perbaikan:** Menggunakan elemen pertama sebagai nilai tertinggi awal, membandingkan elemen berikutnya dengan operator `>`, dan menangani input kosong.

Kode setelah perbaikan:

```python
def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None
    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi
```

## 5. Retest

Setelah perbaikan dilakukan, seluruh test case dijalankan kembali. Hasil aktualnya adalah:

| ID | Input | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|---|
| T1 | Rata-rata `[80, 60, 90, 70]` | `75.0` | `75.0` | PASS |
| T2 | Rata-rata `[100, 80]` | `90.0` | `90.0` | PASS |
| T3 | Status nilai `60` | `Lulus` | `Lulus` | PASS |
| T4 | Status nilai `59` | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | Nilai tertinggi `[80, 60, 90, 70]` | `90` | `90` | PASS |
| T6 | Rata-rata `[]` | `0` | `0` | PASS |
| T7 | Nilai tertinggi `[]` | `None` | `None` | PASS |

Berdasarkan hasil retest, ketujuh test case menghasilkan keluaran yang sesuai dengan hasil yang diharapkan. Dengan demikian, seluruh test case dinyatakan **PASS**.

## 6. Cara Menjalankan

Jalankan perintah berikut dari folder utama proyek:

```bash
python3 praktik/praktik_4_debugging.py
```

Pada Windows, program juga dapat dijalankan melalui terminal Visual Studio Code menggunakan interpreter Python yang telah dikonfigurasi.

## 7. Refleksi

Proses debugging membantu saya memahami bahwa kesalahan program tidak selalu berasal dari sintaks, tetapi dapat terjadi pada logika perhitungan dan kondisi. Penggunaan debugger di Visual Studio Code membantu menelusuri alur eksekusi program serta memeriksa nilai variabel. Selain itu, pengujian dengan beberapa variasi input, termasuk nilai batas dan input kosong, membantu menemukan kesalahan yang mungkin tidak terlihat pada satu pengujian saja. Setelah perbaikan, seluruh test case kembali diuji untuk memastikan fungsi program berjalan sesuai dengan hasil yang diharapkan.