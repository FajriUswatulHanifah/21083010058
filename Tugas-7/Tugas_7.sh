#!/bin/bash

#Mendeklarasikan fungsi panjang
panjang() {
	echo "Masukkan Panjang : "
	read panjang
}

#Mendeklarasikan fungsi lebar
lebar() {
	echo "Masukkan Lebar : "
	read lebar
}

#Mendeklarasikan fungsi luas
luas() {
	echo "Program Menghitung Luas Bidang Persegi"
	panjang		#Memanggil fungsi panjang didalam fungsi luas
	lebar		#Memanggil fungsi lebar didalam fungsi luas
	#Menghitung Luas Persegi
	let luas=$panjang*$lebar
	echo -e "Luas Persegi : \n" $luas
}

#Memanggil fungsi luas
luas
