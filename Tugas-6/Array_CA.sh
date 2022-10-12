#!/bin/bash

# Mendeklarasikan Array Compound Assignment
distroLinuxDesktop=('BlankOn' 'Ubuntu' 'Debian' 'ArchLinux' 'LinuxMint')
distroLinuxServer=('UbuntuServer' 'centOS' 'FedoraServer')

# Cara mengambil atau memanggil  nilai array
echo ${distroLinuxDesktop[*]}
echo ${distroLinuxServer[*]}
