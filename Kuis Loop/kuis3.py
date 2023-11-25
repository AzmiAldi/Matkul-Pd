# NAMA  : ACHMAD AZMI ALDI NUGRAHA
# NIM   : 14012300138
# KELAS : 1B.KOM

# 3. menghitung total dari angka 10 berhenti dengan nomor 2

print("Program Hitung Total")
print("catatan: Masukkan 2 untuk mengahiri dan menampilkan total")

total = 10
angka = None
while angka != 2:
    try:
        angka = int(input("Masukkan angka: "))
        if angka == 2:
            break
        total += angka
    except ValueError:
        print("Tolong Masukkan angka yang valid.")


print(f"Total dari angka-angka yang anda masukkan adalah: {total}")