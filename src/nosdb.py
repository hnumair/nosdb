import json

class Database:
    def __init__(self, filename):
        self.filename = filename;

# creates a new entry in the database
    def create(self, key, data):
        dict = {}
        self.key = key
        self.data = data
    #dict[key] = data
        indata = {"%s" % self.key: "%s" % self.data}
        #print(indata)
        with open(self.filename, "r+") as infile:
            dict = json.load(infile)
            if self.key in dict:
                print("Create Error: The key entered already exists.")
                return

            dict.update(indata)
            infile.seek(0)
        #print(dict)
            json.dump(dict, infile, indent = 4)

    #with open("data.json", "w") as outfile:
        #json.dump(dict, outfile)


# retrieves the value corresponding to the key passed 
    def read(self, key):
        self.key = key

        with open(self.filename, "r") as infile:
            json_obj = json.load(infile)
        #return dict[key]
    #return json_obj
        if self.key in json_obj:
            return json_obj[self.key]
        else:
            print("Read Error: Specified key does not exists.")
            return


# deletes the value corresponding to the key passed
    def delete(self, key):
        self.key = key;

        with open(self.filename, "r+") as infile:
            json_obj = json.load(infile)

        if self.key in json_obj:
            del json_obj[self.key]
        else:
            print("Delete Error: Specified key does not exists.")
            return

        with open(self.filename, "w") as outfile:
            json.dump(json_obj, outfile, indent = 4)
