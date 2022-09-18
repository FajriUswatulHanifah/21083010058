#!/bin/bash

printf "Hai aku hani\n"
printf "Boleh aku tau siapa namamu?\n"
read nama

case "$nama" in
	"gak")
		echo "kamu cuek sekali!, tapi tak apa, aku suka hehe"
		;;
	"tidak")
		echo "privacy jigeum sekali orang ini"
		;;
	"gk")
		echo "cuek, pelit, and privacy jigeum sekali dah manusia ini"
		;;
	"ndak")
		echo "iyee iyee tak memaksa, pelit!"
		;;
	"gak boleh")
		echo "orang pelit kuburannya sempit!"
		;;
	"tidak boleh")
		echo "saran aja uy, jan pelit pelit!"
		;;
	"bayar")
		echo "sudah tak bisa berkata kata aku manusia! AIGOOO!!"
		;;
	*)
		echo "Hai $nama! Terimakasih sudah berbagi namamu wkwk"
		;;
esac
