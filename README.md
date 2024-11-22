# Dijkstra dalam Situasi Darurat: Navigasi di Lingkungan Sulit dan Ekstrem Akibat Bencana Alam

Bencana alam sering kali menyebabkan kerusakan parah pada infrastruktur, yang mengakibatkan komunikasi terhambat dan akses menuju wilayah terdampak menjadi sulit. Dalam situasi darurat ini, kemampuan untuk merespon dengan cepat sangat penting untuk menyelamatkan nyawa. Proses penyelamatan konvensional memiliki berbagai kelemahan dalam implementasinya karena keterbatasan visibilitas pada daerah terdampak bencana. Selain itu, proses penyelamatan konvensional dilakukan dengan meraba jalur yang belum tentu merupakan jalur terpendek menuju korban.  

Teknologi drone atau Unmanned Aerial Vehicles (UAV) memiliki potensi besar dalam operasi Search and Rescue (SAR) karena kemampuan manuvernya di medan yang sulit dijangkau. Dengan menggunakan drone, korban dapat lebih mudah ditemukan karena kemampuan terbangnya sehingga dapat memiliki visibilitas yang lebih daripada manusia. Teknologi drone dapat dengan cepat mencapai area sulit tanpa menghadapi rintangan di tanah yang sering memperlambat tim SAR. 

Namun, navigasi di area dengan banyak hambatan, seperti reruntuhan, menjadi tantangan tersendiri. Penelitian ini menggunakan algoritma Dijkstra untuk membantu menemukan jalur terpendek dalam misi SAR berbasis drone. Algoritma ini dipilih karena memiliki kemampuan dalam menghasilkan rute optimal dengan cepat di lingkungan yang kompleks dan menyerupai labirin atau maze. 

Algoritma dijkstra adalah algoritma greedy yang digunakan untuk menemukan shortest path dalam graph. Algoritma ini bekerja dengan menghitung dari titik awal ke titik terdekat kemudian ke titik kedua, dan seterusnya.

Penelitian ini berfokus pada evaluasi efektivitas algoritma Dijkstra dalam menentukan rute optimal di area bencana. Efektivitas diukur berdasarkan kemampuan algoritma untuk mencapai target melalui rute terpendek dalam beberapa kali percobaan. Penelitian ini akan fokus pada dua hal utama: (1) Konsistensi keberhasilan Dijkstra dalam mencapai target melalui jalur optimal, dan (2) efisiensi algoritma dalam hal running time.

# Penjelasan isi file
- DAA runtime : Menghitung runtime pengujian algoritma
- Graph Maker : membuat graph untuk pengujian
- Research : Main file (Dijkstra for maze solver)
