# Mengakses Anggota List

my_list = ["I", "love", "python", "programming", 2017]
# Output: I
my_list[0]

# Output
my_list[2]

# List dalam list
your_list = ["hello", [1, 2, 3], "python"]

# Output 1
print(your_list[1][0])

# Output 2
print(your_list[1][2])

# IndexError
my_list[6]