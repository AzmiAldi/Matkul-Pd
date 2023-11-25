# NAMA  : ACHMAD AZMI ALDI NUGRAHA
# NIM   : 14012300138
# KELAS : 1B.KOM

# 1. menampilkan bilangan genap
print("\nMenampilkan Bilangan Genap\n")

N = int(input("Masukkan angka N :"))
i = 2
while i <= N:
    if i % 2 == 0:
        print(i)
    i += 2