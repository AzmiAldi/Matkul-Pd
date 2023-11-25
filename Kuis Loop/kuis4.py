# NAMA  : ACHMAD AZMI ALDI NUGRAHA
# NIM   : 14012300138
# KELAS : 1B.KOM

# 4. tebakan angka hanya 1-20 dibatasi 10 kali jika masih salah: waktu selesai

import random

#menuliskan angka acak antara 1 dan 20
angka_rahasia = random.randint(1, 20)
sisa_percobaan = 10

print('='*41)
print("Hai! Ayo main tebak angka antara 1-20.")
print("Kamu punya 10 percobaan. Selamat bermain!")
print('='*41)

while sisa_percobaan > 0:
    try:
        tebakan = int(input("Masukkan tebakan kamu : "))
        if tebakan == angka_rahasia:
            print(f"Selamat! Kamu menang dengan sisa percobaan: {sisa_percobaan} ")
            break
        if tebakan < angka_rahasia:
            print("Tebakan Kamu terlalu rendah.")
        elif tebakan > angka_rahasia:
            print("Tebakan Kamu terlalu tinggi.")
        sisa_percobaan -= 1
        print(f"Sisa percobaan: {sisa_percobaan}")
    except ValueError:
        print("Tolong masukkan angka yang valid.")

if sisa_percobaan == 0:
    print(f"Maaf, percobaan Kamu habis. Angka yang benar adalah: {angka_rahasia}")