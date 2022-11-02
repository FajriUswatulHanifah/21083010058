#!/bin/bash

#Mendeklarasikan Fungsi nama
function nama {
	echo "Siapa namamu?"
	read nama
}

#Mendeklarasikan Funsi NPM
function npm {
	echo "Sebutkan npm mu!"
	read npm
	echo -e "Hai $nama dengan npm $npm, selamat datang \n di praktikum sistem operasi yang seru ini ya!"
}

#Memanggil Fungsi
nama
npm
