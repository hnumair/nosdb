from src import nosdb 

# creates an entry
data = "Test Data"
key = "a"
nosdb.create(key, data)

# reads the created entry
print(nosdb.read(key))
print("\n")

# reads already created entry
print(nosdb.read("name"))
print("\n")

# reads already created json object
print(nosdb.read("obj"))
print("\n")

# generates read error
print(nosdb.read("45"))
print("\n")

# generates delete error
nosdb.delete("2")
print("\n")

# generates create error
nosdb.create(key, data)
print("\n")

