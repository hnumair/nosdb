from src import nosdb

obj = nosdb.Database()

# creates an entry
data = "Test Data"
key = "aaaa"
obj.create(key, data)

# reads the created entry
print(obj.read(key))
print("\n")
#
# reads already created entry
#print(obj.read("name"))
#print("\n")
#
# reads already created json object
#print(obj.read("obj"))
#print("\n")
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

