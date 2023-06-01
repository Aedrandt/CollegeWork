# MDM

Mengelola Data Mahasiswa
Kode pada program ini adalah implementasi dari beberapa kelas yang menghubungkan antar Mahasiswa, Jurusan, dan Universitas.

Kelas Mahasiswa:
- Kelas Mahasiswa memiliki tiga atribut: nama, nim, dan jurusan.
- Metode __init__ digunakan sebagai konstruktor untuk menginisialisasi atribut-atribut tersebut.
- Metode tampilkan_info digunakan untuk menampilkan informasi lengkap tentang seorang mahasiswa, yaitu nama, nim, dan nama jurusan.

Kelas Jurusan:
- Kelas Jurusan memiliki dua atribut: NamaJurusan (nama jurusan) dan DaftarMahasiswa (daftar mahasiswa yang terdaftar di jurusan tersebut).
- Metode __init__ digunakan sebagai konstruktor untuk menginisialisasi atribut-atribut tersebut.
- Metode tambah_mahasiswa digunakan untuk menambahkan objek mahasiswa ke dalam daftar mahasiswa jurusan.
- Metode tampilkan_daftar_mahasiswa digunakan untuk menampilkan daftar mahasiswa yang terdaftar di jurusan tersebut.

Kelas Universitas:
- Kelas Universitas memiliki dua atribut: NamaUniversitas (nama universitas) dan DaftarJurusan (daftar jurusan yang ada di universitas tersebut).
- Metode __init__ digunakan sebagai konstruktor untuk menginisialisasi atribut-atribut tersebut.
- Metode tambah_jurusan digunakan untuk menambahkan objek jurusan ke dalam daftar jurusan universitas.
- Metode tampilkan_daftar_jurusan digunakan untuk menampilkan daftar jurusan yang ada di universitas tersebut.

Dengan menggunakan tiga kelas di atas, kita dapat membuat objek Mahasiswa, Jurusan, dan Universitas, dan menghubungkannya sesuai dengan yang didefinisikan dalam kode. Misalnya, objek Mahasiswa dapat ditambahkan ke dalam objek Jurusan menggunakan metode tambah_mahasiswa, dan objek Jurusan dapat ditambahkan ke dalam objek Universitas menggunakan metode tambah_jurusan.

Dalam tampilan akhir, kita dapat memanggil metode tampilkan_info untuk menampilkan informasi lengkap tentang seorang mahasiswa dan metode tampilkan_daftar_jurusan untuk menampilkan daftar jurusan yang ada di universitas.
