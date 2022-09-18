#!/bin/bash

# deklarasi integer
a=1224
b=2412

# built-in memakai let untuk operasi perhitungan
let jumlah=$a+$b
let kurang=$b-$a
let kali=$a*$b

#memakai expr
bagi='expr $a / $b'

# memakai subtitusi $ ((eksperesi))
mod=$(($a%$b))

echo "a + b = $jumlah"
echo "a - b = $kurang"
echo "a * b = $kali"
echo "a / b = $bagi"
echo "a % b = $mod"

b=$a

echo "a = $a"
echo "b = $b"
