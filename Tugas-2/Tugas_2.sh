#!/bin/bash

# deklarasi harga per item
face_wash=50000
toner=40000
serum=150000
lotion=20000
micellar_water=15000

# memakai let untuk operasi perhitungan pembelian paket
let bersih1=$micellar_water+$face_wash
let bersih2=$micellar_water+$face_wash+$toner
let bersih3=$toner+$face_wash
let whitening1=$face_wash+$serum
let whitening2=$face_wash+$toner+$serum
let whitening3=$face_wash+$toner+$serum+$lotion

# eksekusi sistem
echo "Selamat Datang di Toko Body Care!"
echo "Boleh kami tau siapa nama anda?"
read nama
echo -e "\nHai kak $nama :)\n Saya akan membantu anda untuk membeli paket Body Care yang ada di toko kami!\n Berikut Daftar Harganya!"
printf "Daftar Harga Per Item\n face_wash=50.000\n toner=40.000\n serum=150.000\n lotion=20.000\n micellar_water=15.000\n"
printf "Dan Berikut Nama Paket yang Tersedia!"
printf " \nPaket bersih1 (micellar_water, face_wash)\n Paket bersih2 (micellar_water, face_wash, toner)\n Paket bersih3 (toner, face_wash)\n Paket whitening1 (face_wash, serum)\n Paket whitening2 (face_wash, toner, serum)\n Paket whitening3 (face_wash, toner, serum, lotion)\n"
printf "Manakah paket yang ingin kak $nama beli? (Tulis nama paketnya saja)\n"
read paket

# pengondisian case menggunakan percabangan
case $paket in
	"bersih1")
		echo "Total yang harus kak $nama bayar adalah $bersih1"
		;;
	"bersih2")
		echo "Total yang harus kak $nama bayar adalah $bersih2"
		;;
	"bersih3")
		echo "Total yang harus kak $nama bayar adalah $bersih3"
		;;
	"whitening1")
		echo "Total yang harus kak $nama bayar adalah $whitening1"
		;;
	"whitening2")
		echo "Total yang harus kak $nama bayar adalah $whitening2"
		;;
	"whitening3")
		echo "Total yang harus kak $nama bayar adalah $whitening3"
		;;
	*)
		echo "Mohon maaf kak $nama, paket tersebut belum tersedia :("
		;;
esac


