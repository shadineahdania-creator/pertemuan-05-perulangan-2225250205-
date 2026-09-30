# Pertemuan 05 Perulangan Python
Nama: Shadine Ahdania Sofyan
NIM: [Isi NIM Anda]
Kelas: Pendidikan Matematika [Isi Kelas/Grup Anda]

## Tujuan
Menggunakan for dan while untuk menyelesaikan masalah iteratif.

## Cara Menjalankan
python3 kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2
1. Program meminta pengguna memasukkan nilai suku pertama (a), beda (d), dan banyak suku (n).
2. Lakukan validasi menggunakan perulangan `while` untuk memastikan nilai `n` lebih besar dari 0 (bilangan positif). Jika `n` <= 0, program akan terus meminta input `n` yang valid.
3. Siapkan variabel penyimpan `total` dengan nilai awal 0.
4. Lakukan perulangan `for` dari 1 sampai dengan `n`.
5. Pada setiap perulangan iterasi, hitung nilai suku ke-i menggunakan rumus: `suku = a + (i - 1) * d`.
6. Cetak nilai suku tersebut ke layar, lalu tambahkan nilainya ke dalam variabel `total`.
7. Setelah perulangan selesai, cetak hasil akhir `total` (jumlah seluruh suku) ke layar.

## Hasil Pengujian

| Input (a, d, n) | Keluaran yang Diharapkan (Suku & Jumlah) | Keluaran Aktual (Suku & Jumlah) | Status |
| :--- | :--- | :--- | :---: |
| a = 2<br>d = 3<br>n = 5 | Suku: 2, 5, 8, 11, 14<br>Jumlah: 40 | Suku: 2, 5, 8, 11, 14<br>Jumlah: 40 | Sukses |
| a = 10<br>d = -2<br>n = 4 | Suku: 10, 8, 6, 4<br>Jumlah: 28 | Suku: 10, 8, 6, 4<br>Jumlah: 28 | Sukses |
| a = 1.5<br>d = 0.5<br>n = 3 | Suku: 1.5, 2.0, 2.5<br>Jumlah: 6.0 | Suku: 1.5, 2.0, 2.5<br>Jumlah: 6.0 | Sukses |

## Refleksi
Satu kesalahan perulangan yang rentan terjadi adalah *infinite loop* (perulangan tanpa batas) pada penggunaan `while` untuk validasi `n`. Hal ini terjadi jika kita lupa menambahkan perintah untuk meminta input ulang di dalam blok `while`. Cara memperbaikinya adalah dengan memastikan ada perintah pembaruan nilai variabel (contoh: meminta input `n` kembali) di dalam blok `while` sehingga kondisinya suatu saat bisa bernilai `False` dan perulangan berhenti. Kesalahan umum lainnya adalah lupa memberikan indentasi (tab/spasi) pada kode di dalam blok `for` atau `while`, yang dapat diperbaiki dengan menggeser baris kode yang berada di dalam perulangan tersebut ke kanan.