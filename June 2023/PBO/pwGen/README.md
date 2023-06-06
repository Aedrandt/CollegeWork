# pwGen

Password Generator

Program ini menggunakan library Tkinter untuk membuat antarmuka grafis yang memungkinkan pengguna untuk menghasilkan password acak dengan panjang yang ditentukan. Dalam program ini, kita menggunakan beberapa library:
- `random` untuk menghasilkan pilihan acak dalam pembuatan password.
-	`string` berisi kumpulan karakter yang digunakan untuk membangun password.
-	`tkinter` sebagai library utama untuk membuat antarmuka grafis.
-	`messagebox` untuk menampilkan pesan kepada pengguna.
-	`ttk` sebagai modul tambahan untuk Tkinter yang menyediakan tampilan yang lebih baik.

Program ini terdiri dari beberapa fungsi dan langkah-langkah:
1.	Fungsi `generate_password(length)` digunakan untuk menghasilkan password acak dengan panjang yang ditentukan. Fungsi ini memilih karakter acak dari kumpulan karakter yang telah ditentukan, dan memastikan bahwa password memenuhi persyaratan seperti memiliki huruf kecil, huruf besar, digit, dan tanda baca.
2.	Fungsi `generate_button_clicked()` dipanggil ketika tombol "Generate Password" diklik. Fungsi ini mengambil panjang password dari input pengguna, memanggil fungsi `generate_password()` untuk menghasilkan password baru, dan menampilkan password tersebut di antarmuka pengguna. Tombol "Copy" juga diaktifkan agar pengguna dapat menyalin password ke clipboard.
3.	Fungsi `copy_button_clicked()` dipanggil ketika tombol "Copy" diklik. Fungsi ini mengambil password dari antarmuka pengguna, menghapus teks yang tidak perlu, menyalin password ke clipboard, dan memberikan pesan kepada pengguna bahwa password telah berhasil disalin.
4.	Program membuat jendela utama dengan menggunakan Tkinter, mengatur tampilan antarmuka dengan menggunakan elemen-elemen seperti label, entry, dan tombol. Juga mengatur gaya dan warna latar belakang jendela.
5.	Program dijalankan dalam loop utama menggunakan `window.mainloop()` untuk menjaga jendela tetap terbuka dan menangani interaksi pengguna.

Dengan demikian, program ini memberikan antarmuka yang mudah digunakan untuk menghasilkan password acak dengan panjang yang diinginkan.
