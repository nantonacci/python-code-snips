def my_hashing_func(str, list_size):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte
    return sum % list_size

# initialize a list with five empty slots
my_list = [None] * 5

my_list[my_hashing_func("aqua", len(my_list))] = "#00FFFF" #put value in list

print(my_list[my_hashing_func("aqua", len(my_list))]) #get value from list

def hash_djb2(stringo):
    hash = 5381

    for char in stringo:
        hash = (hash * 33) + ord(char)
    return hash

print(hash_djb2('hello world'))