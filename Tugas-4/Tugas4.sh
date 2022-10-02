echo "Harap Masukkan Angka Positif :"
read bilangan

until [ ! $bilangan -gt 0 ]
do
   echo $bilangan
   bilangan=$((bilangan-2))
done

