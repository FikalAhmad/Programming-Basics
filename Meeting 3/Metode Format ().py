# Metode Format ()

# Menggunakan Posisi Default
default_order = "{}, {}, dan {}".format("Budi", "Galih", "Ratna")
print('\n--- Urutan default ---')
print(default_order)

# Menggunakan Argument Posisi
positional_order = "{1}, {0}, dan {2}".format("Budi", "Galih", "Ratna")
print('\n--- Urutan default ---')
print(positional_order)


# Format Integer
print("{0} bila diubah jadi biner menjadi {0:b}".format(12))

# Pembulatan
print("Sepertiga sama dengan: {0:.3f}".format(1/3))

# Meratakan String
print("|{:<10}|{:^10}|{:>10}|".format('beras', 'gula', 'garam'))