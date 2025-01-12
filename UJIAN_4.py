def rerata_nilai_mhs(nama = None, data_dict = 0):
    nama = input("Masukkan nama mahasiswa: ")
    data_dict = int(input("Berapa banyak nilai yang ingin Anda masukkan? "))
    nilai = []  # Daftar kosong untuk menyimpan nilai
    total = 0  # total nilai
    
    for i in range(data_dict):
        nilai_input = int(input("Masukkan nilai ke-" + str(i+1) + ":"))
        nilai = nilai + [nilai_input]
        total += nilai_input  # Menambahkan nilai ke total
    
    print("Nilai-nilai:", *nilai)
    print("Rerata =", total / data_dict)

rerata_nilai_mhs()
