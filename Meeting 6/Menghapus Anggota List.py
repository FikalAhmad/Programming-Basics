# Menghapus Anggota List

my_list = ['p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
my_list.remove('p')

# Output ['y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
print(my_list)

my_list.remove('n')
# remove hanya menghapus elemen pertama yang dijumpai
# Output ['p', 'y', 't', 'h', 'o', 'i', 'n', 'd', 'o']

# Output 'y'
print(my_list.pop(1))

del my_list[2]
print(my_list)

my_list.clear()
# Output []
print(my_list)