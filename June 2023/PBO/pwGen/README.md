# pwGen

Password Generator

Program ini adalah penerapan sederhana untuk menghasilkan dan menyalin password acak menggunakan library Tkinter di Python. Berikut adalah penjelasan dari setiap bagian pada program:

- Program dimulai dengan mengimpor beberapa library yang diperlukan, yaitu `random`, `string`, dan `tkinter`. Library `random` digunakan untuk menghasilkan elemen acak, library `string` digunakan untuk mendefinisikan karakter yang mungkin ada dalam password, dan library `tkinter` digunakan untuk membuat antarmuka grafis.

- Fungsi `generate_password(length)`: Ini adalah fungsi yang digunakan untuk menghasilkan password acak. Fungsi ini menerima parameter `length` yang menentukan panjang password yang diinginkan. Password dihasilkan dengan memilih karakter-karakter acak dari kombinasi `string.ascii_letters` (huruf besar dan kecil), `string.digits` (angka), dan `string.punctuation` (tanda baca). Fungsi ini menggunakan pernyataan `while True` untuk terus menghasilkan password baru hingga memenuhi kriteria tertentu, yaitu setidaknya memiliki satu huruf kecil, satu huruf besar, satu angka, dan satu tanda baca. Setelah password yang memenuhi kriteria ditemukan, password dikembalikan sebagai string.

- Fungsi `generate_button_clicked()`: Ini adalah fungsi yang akan dijalankan ketika tombol "Generate Password" ditekan. Fungsi ini mencoba mengambil panjang password yang dimasukkan oleh pengguna dari `length_entry` (entry widget). Jika panjang password valid, fungsi memanggil fungsi `generate_password()` untuk menghasilkan password acak dengan panjang yang ditentukan. Password yang dihasilkan ditampilkan pada `password_label` (label widget) dan tombol "Copy" diaktifkan. Jika panjang password tidak valid (misalnya bukan angka), pesan kesalahan akan ditampilkan menggunakan `messagebox.showerror()`.

- Fungsi `copy_button_clicked()`: Ini adalah fungsi yang akan dijalankan ketika tombol "Copy" ditekan. Fungsi ini mengambil password dari `password_label` dengan menggunakan metode `.cget("text")`. Password tersebut kemudian disalin ke clipboard menggunakan `window.clipboard_clear()` untuk membersihkan clipboard dan `window.clipboard_append()` untuk menambahkan password ke clipboard. Akhirnya, `messagebox.showinfo()` digunakan untuk menampilkan pesan informasi bahwa password telah berhasil disalin.

- Membuat tampilan utama: Program membuat tampilan utama menggunakan `tk.Tk()`. Nama tampilan diatur menjadi "Password Generator" dengan metode `.title()`, dan ukuran yang diatur menjadi 300x175 piksel dengan metode `.geometry()`. Warna latar belakang tampilan diatur menggunakan `.configure(bg="#f0f0f0")`.

- Mengatur gaya ttk: Program menggunakan gaya ttk untuk mengatur tampilan widget. Gaya untuk `TLabel`, `TButton`, dan `TEntry` diatur menggunakan `style.configure()`. `TLabel` dan `TButton` menggunakan font Arial dengan ukuran 10, sedangkan `TEntry` menggunakan font Arial dengan ukuran 10.

- Membuat frame utama: Program membuat frame utama menggunakan `ttk.Frame()`. Frame ini akan berisi elemen-elemen antarmuka pengguna.

- Membuat label dan entry untuk panjang password: Program membuat `length_label` (label widget) dengan teks "Panjang Password:" dan `length_entry` (entry widget) dengan lebar 10 untuk memasukkan panjang password yang diinginkan. Widget-widget ini ditempatkan menggunakan metode `.grid()`.

- Membuat tombol "Generate Password": Program membuat tombol `generate_button` (button widget) dengan teks "Generate Password" dan memasangnya di grid dengan metode `.grid()`. Ketika tombol ini ditekan, fungsi `generate_button_clicked()` akan dijalankan.

- Membuat label untuk menampilkan password baru: Program membuat `password_label` (label widget) yang awalnya kosong. Password baru yang dihasilkan akan ditampilkan di label ini. `wraplength` diatur menjadi 300 piksel untuk membatasi lebar teks yang ditampilkan agar tidak terlalu panjang. Widget ini ditempatkan menggunakan metode `.grid()`.

- Membuat tombol "Copy": Program membuat tombol `copy_button` (button widget) dengan teks "Copy" dan mengatur statusnya menjadi "disabled" agar tidak dapat ditekan sebelum ada password yang dihasilkan. Ketika tombol ini ditekan, fungsi `copy_button_clicked()` akan dijalankan. Tombol ini juga ditempatkan menggunakan metode `.grid()`.

- Menjalankan loop utama: Terakhir, program memanggil metode `.mainloop()` untuk menjalankan loop utama. Ini memastikan tampilan tetap terbuka dan menanggapi interaksi pengguna hingga jendela ditutup.

Dengan menjalankan program ini, Anda akan mendapatkan antarmuka grafis sederhana yang memungkinkan Anda menghasilkan password acak dengan panjang yang ditentukan dan menyalinnya ke clipboard.