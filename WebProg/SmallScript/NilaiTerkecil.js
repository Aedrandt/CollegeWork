let numb = [];
let jumlah = prompt("Masukkan jumlah angka:"); 
for (let i = 0; i < jumlah; i++) {
    let num = parseFloat(prompt(`Masukkan angka ke-${i + 1}:`));
    numb.push(num);
    }
let smallNumb = Math.min(...numb);
console.log(`Nilai terkecil dalam array adalah: ${smallNumb}`);