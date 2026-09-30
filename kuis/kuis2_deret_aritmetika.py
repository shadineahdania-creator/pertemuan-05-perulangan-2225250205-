print("Deret Aritmetika")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi n dengan while (banyak suku harus bilangan positif)
while n <= 0:
    print("Banyak suku (n) tidak valid. Harus lebih dari 0.")
    n = int(input("Banyak suku n: "))

total = 0

print("\n--- Hasil Deret ---")
# Menampilkan suku dan menghitung total menggunakan for
for i in range(1, n + 1):
    # Rumus suku ke-n deret aritmetika: Un = a + (n-1)b
    suku = a + (i - 1) * d
    print(f"Suku ke-{i} = {suku}")
    total += suku

print(f"\nTotal deret aritmetika = {total}")