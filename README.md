# Dijkstra dalam Situasi Darurat: Navigasi di Lingkungan Labirin saat Bencana Banjir
Penulis: Angga Theo Kekuatanta Pasaribu, Fiolita Chresia Putri, Gebrina Augustine Padatu, Jennifer Christabelle, Rafelixa Reynard Isak, Teofilus Satria Rada Insani
Institusi: Informatika, Fakultas Teknologi Informasi, Universitas Pelita Harapan

## Deskripsi Proyek
Proyek ini mengeksplorasi penerapan algoritma Dijkstra untuk menentukan jalur evakuasi terpendek di wilayah padat penduduk yang terdampak bencana banjir. Penelitian ini memanfaatkan data citra satelit dari Google Earth untuk membangun graf berbobot yang merepresentasikan medan yang kompleks seperti gang-gang sempit. Simulasi dilakukan untuk mengukur efektivitas algoritma berdasarkan tingkat keberhasilan, waktu eksekusi, dan konsistensi pada berbagai skenario graf.

## Fitur Utama
Data Pemrosesan: Menggunakan citra satelit untuk memetakan wilayah terdampak dan mengonversinya menjadi graf berbobot.
Implementasi Algoritma: Algoritma Dijkstra diterapkan untuk menentukan jalur terpendek dengan pendekatan greedy.
Evaluasi dan Validasi: Menganalisis tingkat keberhasilan algoritma dalam menghasilkan jalur evakuasi optimal pada dataset dengan kompleksitas yang bervariasi.
Visualisasi: Menampilkan rute evakuasi pada peta virtual.
Teknologi yang Digunakan
Python (Library: Pillow, NetworkX)
Google Earth untuk pengumpulan data
Representasi graf berbobot untuk simulasi

## Hasil
Rata-rata tingkat keberhasilan mencapai 79% untuk menemukan jalur terpendek.
Rata-rata waktu eksekusi algoritma adalah 52,39 detik, dengan variasi berdasarkan kompleksitas graf.
Algoritma menunjukkan efisiensi yang baik pada graf dengan struktur sederhana dan tetap konsisten pada berbagai pengujian.
Kontribusi
Proyek ini dapat menjadi referensi dalam pengembangan sistem evakuasi berbasis teknologi untuk situasi darurat, seperti banjir, khususnya di daerah dengan struktur yang kompleks.

## Penjelasan isi file
- Dijkstra for Maze.ipynb : Main file untuk research ini
- Convert.py : Untuk meng-convert file gambar jadi grayscale
- Testing : Hasil testing running time dan rat eof growth
