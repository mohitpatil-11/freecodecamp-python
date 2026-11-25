from hash_table import HashTable

table = HashTable()

# Add
table.add("apple", 10)
table.add("banana", 20)
table.add("cherry", 30)

# Collision: "ab" and "ba" have the same character sum, so they share a bucket
table.add("ab", 1)
table.add("ba", 2)

print("Collection:", table.collection)

# Lookup
print("apple:", table.lookup("apple"))
print("ab:", table.lookup("ab"))
print("ba:", table.lookup("ba"))
print("grape (missing):", table.lookup("grape"))

# Remove
table.remove("banana")
print("banana after remove:", table.lookup("banana"))

table.remove("ab")
print("ba still there:", table.lookup("ba"))

print("Collection:", table.collection)
