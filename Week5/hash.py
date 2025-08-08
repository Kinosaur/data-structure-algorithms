from sys import stdin


# Read the sequence of operations to be operated on the hash table
operations = []
for line in stdin:
    line = line.split()
    if len(line) > 2:
        line[2] = int(line[2])
    operations.append(line)

table_size = 12     # Set table size here
hash_table = [[] for _ in range(table_size)]


def show_hash_table():
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')


def hash_func(s):
    # Return the hash value (index) based on the key
    return sum(ord(char) for char in s) % table_size


def insert(s, v):
    index = hash_func(s)
    # Check if the key already exists in the hash table
    for pair in hash_table[index]:
        if pair[0] == s:
            return -1  # Key already exists
    # If not, append the key-value pair
    hash_table[index].append([s, v])
    return 0


def search(s):
    index = hash_func(s)
    # Search for the key in the hash table
    for pair in hash_table[index]:
        if pair[0] == s:
            return pair[1]
    return -1  # Key does not exist


def delete(s):
    index = hash_func(s)
    # Search for the key in the hash table
    for i, pair in enumerate(hash_table[index]):
        if pair[0] == s:
            del hash_table[index][i]  # Delete the key-value pair
            return 0
    return -1


# The main program to execute the sequence of operations
for op in operations:
    if op[0] == "insert":
        result = insert(op[1], op[2])
        show_hash_table()
        print(f"Insert result: {result}")
    elif op[0] == "search":
        result = search(op[1])
        print(f"Search result for {op[1]}: {result}")
    elif op[0] == "delete":
        result = delete(op[1])
        show_hash_table()
        print(f"Delete result for {op[1]}: {result}")