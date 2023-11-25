# NAMA  : ACHMAD AZMI ALDI NUGRAHA
# NIM   : 14012300138
# KELAS : 1B.KOM

# KUIS MENGHITUNG TOTAL ANGKA

print('='*65)
print("||                    [ Program Hitung Total ]                 ||")
print("|| catatan: 1.Masukkan 2 untuk mengahiri dan menampilkan total ||")
print("||          2.jika angka < 10 maka tidak dihitung              ||")
print('='*65)

total = 0
angka = None

while True:
    try:
        angka = int(input("Masukkan angka: "))
        if angka == 2: # jika diinput angka 2 maka berakhir
            angka = False
            break
        elif angka < 10: # Jika input angka < 10 maka tidak dihitung
            print("Tolong masukkan angka minimal 10.")
            angka = True
            continue
        total += angka
    except ValueError: # Jika input selain integer maka tidak dihitung
        print("Tolong Masukkan angka yang valid.")

if angka == False:
    print(f"Total dari angka-angka yang anda masukkan adalah: {total}")