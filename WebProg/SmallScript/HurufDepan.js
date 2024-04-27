let nama = ["Masagus","Muhammad","Ahdan","Aedra","Hanif","Masayu","Ariani","Asya","Salsabila"];
let groups = {};
let i=0;
while (i < nama.length, i++){
    let name = prompt("Enter a name:");
    if (name) {
        nama.push(name);
    }
}
for (let name of nama) {
    let firstLetter = name.charAt(0).toUpperCase();
    if (!groups[firstLetter]) {
        groups[firstLetter] = [];
    }
    groups[firstLetter].push(name);
}
for (let group in groups) {
    console.log(
    "Nama yang diawali huruf " + group + ": " + groups[group].join(", ")
    );
}