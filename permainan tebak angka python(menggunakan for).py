#Number Guessing Program
import random
randoms = random.randint(0,100)


print (50 * "=")
print ("\tSELAMAT DATANG DI PERMAINAN TEBAK ANGKA 1")
print (50 * "=")


for percobaan in range (10) :
    jawaban = int(input(f"\nPercobaan ke:{percobaan +1}\t Masukan Angka Yang anda tebak: "))

    if randoms > jawaban :
        print("angka yang anda masukan terlalu kecil")
    elif randoms < jawaban :
        print("angka yang anda masukan terlalu besar")
    elif jawaban == randoms :
        print(50* "=")
        print ("\tSelamat anda berhasil Menebak!!!")
        print(50* "=")
        break

a = input("APAKAH ANDA INGIN MELIHAT JAWABANNYA 1 [Y] or [N]: ")
if a == "y" :
    print(50* "=")
    print("\t\t\t",randoms)
    print(50* "=")
elif a == "n" :
    print (50 * "=")
    print ("YOWES ANJOYY")
    print (50 * "=\n\n\n")

    




