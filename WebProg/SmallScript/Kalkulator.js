let bil1 = prompt("Masukkan bilangan pertama: ");
let bil2 = prompt("Masukkan bilangan kedua: ");
let operasi = prompt("Masukkan operasi yang diinginkan (+, -, *, /):");
let hasil;
switch (operasi) {
    case "+":
        hasil = Number(bil1) + Number(bil2);
        break;
    case "-":
        hasil = Number(bil1) - Number(bil2);
        break;
    case "*":
        hasil = Number(bil1) * Number(bil2);
        break;
    case "/":
        if (Number(bil2) === 0) {
            alert("Bilangan pembagi tidak boleh nol.");
        } else {
            hasil = Number(bil1) / Number(bil2);
        }
        break;
    default:
        alert("Operasi matematika yang diinginkan tidak dapat dijalankan.");
    return;}
console.log("Hasil operasi: " + hasil);