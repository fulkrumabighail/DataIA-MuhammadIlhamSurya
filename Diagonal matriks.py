def hitung_hasil_pengurangan_diagonal(matriks):
    n = len(matriks)
    
    diagonal_utama = 0
    diagonal_sekunder = 0
    
    for i in range(n):
        diagonal_utama += matriks[i][i]
        diagonal_sekunder += matriks[i][n - 1 - i]
    
    hasil_pengurangan = diagonal_utama - diagonal_sekunder
    return hasil_pengurangan

# Contoh penggunaan:
matriks = [
    [1, 2, 2],
    [4, 5, 6],
    [9, 8, 3]
]

hasil = hitung_hasil_pengurangan_diagonal(matriks)
print("Hasil pengurangan diagonal adalah:", hasil)