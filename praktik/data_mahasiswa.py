def cari_mahasiswa(data, nim):
    return data.get(nim)

def rata_rata_nilai(data):
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

print("=== PENCARIAN MAHASISWA ===")
nim = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim)
if hasil is not None:
    print(f"{nim}: {hasil}")
else:
    print("Data tidak ditemukan")

nim_tidak_ada = "A999"
hasil_tidak_ada = cari_mahasiswa(data_mahasiswa, nim_tidak_ada)
if hasil_tidak_ada is not None:
    print(f"{nim_tidak_ada}: {hasil_tidak_ada}")
else:
    print("Data tidak ditemukan")

print("\n=== PENAMBAHAN MAHASISWA BARU ===")
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}
print("Data A006 berhasil ditambahkan.")

print("\n=== PEMBARUAN NILAI MAHASISWA ===")
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai A002 berhasil diperbarui menjadi 82.")

print("\n=== REKAP SELURUH DATA MAHASISWA ===")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} | Nama: {info['nama']} | Kelas: {info['kelas']} | Nilai: {info['nilai']}")

print("\n=== RATA-RATA NILAI KELAS ===")
print(f"Rata-rata = {rata_rata_nilai(data_mahasiswa):.2f}")