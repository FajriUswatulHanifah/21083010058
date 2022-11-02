#!/bin/bash

#Mendeklarasikan fungsi nama
nama() {
	echo "Siapa namamu?"
	read nama
}

#Mendeklarasikan fungsi npm
npm() {
	echo "Sebutkan npm mu!"
	read npm
	echo -e "Hai $nama dengan npm $npm, Selamat datang \n di praktikum sistem operasi yang seru ini ya!"
}

#Memanggil fungsi 
nama
npm
