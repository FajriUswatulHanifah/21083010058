#!swads/bin/bash

# pertama melakukan pendeklarasian array
distroLinux=("Mint" "Ubuntu" "Kali" "Arch" "Debian")

# melakukan random distro
let pilih=$RANDOM%5

# eksekusi
echo "Saya Memilih Distro $pilih, ${distroLinux[$pilih]} !"
