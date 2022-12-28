

print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
print("+                              OPERASI PERHITUNGAN DERET MATEMATIKA                               +")
print("*                                     SISTEM OPERASI LINUX                                        *")
print("+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+")
print("\n  Program ini terdiri dari perhitungan beberapa deret bilangan matematika mulai dari aritmatika,")
print("                      geometri, bilangan ganjil genap, hingga bilangan prima")
print("\n|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|")
print("\n     Sebelum memulai operasi deret matematika, izinkan saya untuk mengetahui nama anda :v")
nama = input("Siapa Nama Kamu : ")
name = print("            Selamat Menikmati Sistem Operasi Perhitungan deret Matematikanya kak {}" .format(nama))
print("\n|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|\n")


def Main():
    print("Silahkan Pilih Perhitungan Deret Matematika yang Kak {} Inginkan\n" .format(nama))
    print("1. Deret Aritmatika")
    print("2. Deret Geometri")
    print("3. Deret Bilangan Ganjil")
    print("4. Deret Bilangan Genap")
    print("5. Deret Bilangan Prima")
    print("_"*100)
    select = int(input("\nMohon masukkan pilihanmu, dalam bentuk angka ya kak {} : " .format(nama)))      
    if select == 1 :
        aritmatika()
    elif select == 2 :
        geometri()
    elif select == 3 :
        ganjil()
    elif select == 4 :
        genap()
    elif select == 5 :
        prima()
    else :
        print("Mohon maaf kak {} tidak ada perhitungan deret yang dimaksud" .format(nama))

def end():
    print("\n|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|" ) 
    print("●                              TERIMAKASIH BANYAK KAK {} TELAH DATANG                               ●".format(nama))
    print("●                               JIKA BUTUH BANTUAN AKU ADA DISINI :)                                ●")
    print("|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|●|" ) 


def aritmatika():
    print("\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
    print("+                             OPERASI PERHITUNGAN DERET ARITMATIKA                                +")
    print("*                                     SISTEM OPERASI LINUX                                        *")
    print("+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+")
    print("\nSilahkan pilih perhitungan aritmatika yang yang kak {} inginkan\n" .format(nama))
    print("1. Suku ke-n")
    print("2. Jumlah suku ke-n")
    print("_"*100)
    deret_1 = int(input("\nTentukan : "))
    if deret_1 == 1 :
        u1 =int(input("\nMasukkan suku pertama : "))
        u2 =int(input("Masukkan suku kedua: "))
        n =int(input("Banyak nya suku : "))
        b = u2 - u1
        Un = (u1+(n-1)*b)
        print("\nDari hasil perhitungan di dapatkan a = ", u1, "sedangkan beda masing-masing suku = ", b )
        print("Un : ", Un)
        i = 1
        a = u1
        hasil = 0
        c = [u1, ]
        print("\n Hasil Deret Aritmatika : ")
        while True :      
            if i < n :   
                i = i +1
                a = a + b
                hasil = a
                c.append(hasil)
            else :
                break
        print(c)
        print("\n")
        print("*"*100)
        lanjut = "" 
        while (lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY") :
            print("               Hai kak {}, anda telah menyelesaikan perhitungan deret aritmatika ini :)" .format(nama))
            lanjut = str(input("               Apakah kak {} ingin lanjut ke perhitungan lainnya?  yay or nay? : " .format(nama)))
            print("*"*100)

            if lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY":
                end()
                break
            else :
                Main()
            
    elif deret_1 == 2 :
        u1 = int(input("\nMasukkan suku pertama : "))
        u2 = int(input("Masukkan suku kedua: "))
        n = int(input("Banyak nya suku : "))
        b = u2 - u1
        Un = (u1+(n-1)*b)
        Sn = (n/2*(u1+Un))
        print("\nDari hasil perhitungan tan di dapatkan a = ", u1, "sedangkan beda masing-masing suku = ", b, "dan nilai Un = ", Un )
        i = 1
        a = u1
        hasil = 0
        c = [u1, ]
        print("\n Hasil Deret Aritmatika: ")
        while True :      
            if i < n :   
                i = i +1
                a = a + b
                hasil = a
                c.append(hasil)
            else :
                break
        print(c)
        print("\nMaka jumlah Sn Deret Aritmatika : ", Sn)
        print("\n")
        print("*"*100)
        lanjut = "" 
        while (lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY") :
            print("               Hai kak {}, anda telah menyelesaikan perhitungan deret aritmatika ini :)" .format(nama))
            lanjut = str(input("               Apakah kak {} ingin lanjut ke perhitungan lainnya?  yay or nay? : " .format(nama)))
            print("*"*100)

            if lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY":
                end()
                break
            else :
                Main()
    else :
        print("Mohon maaf kak {} tidak ada program aritmatika yang dimaksud" .format(nama))
        
def geometri():
    print("\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
    print("+                              OPERASI PERHITUNGAN DERET GEOMETRI                                 +")
    print("*                                     SISTEM OPERASI LINUX                                        *")
    print("+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+")
    print("\nSilahkan pilih perhitungan geometri yang kak {} inginkan\n" .format(nama))
    print("1. Suku ke-n")
    print("2. Jumlah suku ke-n\n")
    print("_"*100)
    deret_2=int(input("\nTentukan : "))
    if deret_2 == 1 :
        u1 = int(input("\nMasukkan suku pertama : "))
        u2 = int(input("Masukkan suku kedua: "))
        n =int(input("Banyak nya suku : "))
        r = u2 / u1
        Un = (u1*r**(n-1))
        print("\nDari hasil perhitungan di dapatkan a = ", u1, "sedangkan rasio masing-masing suku = ", r )
        print("Un : ", Un)
        i = 1
        a = u1
        c = [u1, ]
        print("\n Hasil Deret Geometri : ")
        while True :      
            if i < n :   
                i = i +1
                a = a * r
                hasil = a
                c.append(hasil)
            else :
                break
        print(c)
        print("\n")
        print("*"*100)
        lanjut = "" 
        while (lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY") :
            print("               Hai kak {}, anda telah menyelesaikan perhitungan bilangan geometri ini :)" .format(nama))
            lanjut = str(input("               Apakah kak {} ingin lanjut ke perhitungan lainnya?  yay or nay? : " .format(nama)))
            print("*"*100)

            if lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY":
                end()
                break
            else :
                Main()
        
    elif deret_2 == 2 :
        u1 =int(input("\nMasukkan suku pertama : "))
        u2 =int(input("Masukkan suku kedua: "))
        n =int(input("Banyak nya suku : "))
        r = u2 / u1
        Un = (u1*r**(n-1))
        Sn = (u1*r**n-1)/(r-1)
        print("\nDari hasil perhitungan di dapatkan a = ", u1, "sedangkan rasio masing-masing suku = ", r, "dan nilai Un = ", Un )
        i = 1
        a = u1
        c = [u1, ]
        print("\n Hasil Deret Geometri: ")
        while True :      
            if i < n :   
                i = i +1
                a = a * r
                hasil = a
                c.append(hasil)
            else :
                break
        print(c)
        print("\nMaka jumlah Sn Deret Geometri : ", Sn)
        print("\n")
        print("*"*100)
        lanjut = "" 
        while (lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY") :
            print("               Hai kak {}, anda telah menyelesaikan perhitungan deret geometri ini :)" .format(nama))
            lanjut = str(input("               Apakah kak {} ingin lanjut ke perhitungan lainnya?  yay or nay? : " .format(nama)))
            print("*"*100)

            if lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY":
                end()
                break
            else :
                Main()
    else :
        print("Mohon maaf kak {} tidak ada program geometri yang dimaksud" .format(nama))

def ganjil():
    print("\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
    print("+                               OPERASI PERHITUNGAN DERET GANJIL                                  +")
    print("*                                     SISTEM OPERASI LINUX                                        *")
    print("+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+")
    print("_"*100)
    awal = int(input("\nMasukkan angka awal : "))
    akhir = int(input("Masukkan angka akhir : "))
    bilangan_ganjil = []
    for i in range(awal, akhir+1) :
        if (i % 2 != 0):
          bilangan_ganjil.append(i)
    print("\nHasil Deret Ganjil : ")
    print(bilangan_ganjil)
    print("\n")
    print("*"*100)
    lanjut = "" 
    while (lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY") :
        print("               Hai kak {}, anda telah menyelesaikan perhitungan bilangan ganjil ini :)" .format(nama))
        lanjut = str(input("               Apakah kak {} ingin lanjut ke perhitungan lainnya?  yay or nay? :" .format(nama)))
        print("*"*100)

        if lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY":
            end()
            break
        else :
            Main()
        
def genap():
    print("\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
    print("+                                OPERASI PERHITUNGAN DERET GENAP                                  +")
    print("*                                     SISTEM OPERASI LINUX                                        *")
    print("+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+")
    print("_"*100)
    awal = int(input("\nMasukkan angka awal : "))
    akhir = int(input("Masukkan angka akhir : "))
    bilangan_genap = []
    for i in range(awal, akhir+1):
        if (i % 2 == 0):
          bilangan_genap.append(i)
    print("\n Hasil Deret Genap : ")
    print(bilangan_genap)
    print("\n")
    print("\n")
    print("*"*100)
    lanjut = "" 
    while (lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY") :
        print("               Hai kak {}, anda telah menyelesaikan perhitungan bilangan Genap ini :)" .format(nama))
        lanjut = str(input("               Apakah kak {} ingin lanjut ke perhitungan lainnya?  yay or nay? :" .format(nama)))
        print("*"*100)

        if lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY":
            end()
            break
        else :
            Main()
    
def prima():
    print("\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
    print("+                                OPERASI PERHITUNGAN DERET PRIMA                                  +")
    print("*                                     SISTEM OPERASI LINUX                                        *")
    print("+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+")
    print("_"*100)
    angka_awal = int(input("\nMasukan angka awal: "))
    angka_akhir = int(input("Masukan angka akhir: "))

    list_angka = [i for i in range(angka_awal, angka_akhir +1 )]

    bilangan_prima = []
    for i in list_angka:
        if (i==2 or i==3 or i==5 or i==7) or (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0):
            bilangan_prima.append(i)
    print("\n Hasil Deret Prima : ")
    print(bilangan_prima)
    print("\n")
    print("*"*100)
    lanjut = "" 
    while (lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY") :
        print("               Hai kak {}, anda telah menyelesaikan perhitungan bilangan prima ini :)" .format(nama))
        lanjut = str(input("               Apakah kak {} ingin lanjut ke perhitungan lainnya ?  yay or nay? :" .format(nama)))
        print("*"*100)
        

        if lanjut != "Y" and lanjut != "y" and lanjut !="yay" and lanjut !="Yay" and lanjut !="YAY":
            end()
            break
        else :
            Main()

if __name__ == "__main__":
    Main()
