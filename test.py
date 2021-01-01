from src import nosdb


"""
methods supported:
    create(key, data)
    read(key)
    delete(key)
"""

obj = nosdb.Database()

# creates an entry
data = '{"test": "data"}'
key = "abcd"
obj.create(key, data)

# reads the created entry
print(obj.read(key))
print("\n")
#
# generates read error
print(obj.read("45"))
print("\n")
#
# generates delete error
obj.delete("2")
print("\n")
#
# generates create error
obj.create(key, data)
print("\n")

