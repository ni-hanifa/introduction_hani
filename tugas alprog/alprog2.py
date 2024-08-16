tinggi_ayam = []

user_input = input("Masukkan tinggi-tinggi ayam: ")
split_user_input = user_input.split()
for num in split_user_input:
    tinggi_ayam.append(int(num))
    
ayam_tertinggi = tinggi_ayam[0]
indeks = 0
for tinggi in range(1, len(tinggi_ayam)):
    if tinggi_ayam[tinggi] > ayam_tertinggi:
        ayam_tertinggi = tinggi_ayam[tinggi]
        indeks = tinggi
        
print(f"{indeks + 1}\n")