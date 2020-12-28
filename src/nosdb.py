import json

# creates a new entry in the database
def create(key, data):
    dict = {}
    #dict[key] = data
    indata = {"%s" % key: "%s" % data}
    #print(indata)
    with open("data.json", "r+") as infile:
        dict = json.load(infile)
        if key in dict:
            print("Create Error: The key entered already exists.")
            return

        dict.update(indata)
        infile.seek(0)
        #print(dict)
        json.dump(dict, infile, indent = 4)

    #with open("data.json", "w") as outfile:
        #json.dump(dict, outfile)


# retrieves the value corresponding to the key passed 
def read(key):
    with open("data.json", "r") as infile:
        json_obj = json.load(infile)
    #return dict[key]
    #return json_obj
    if key in json_obj:
        return json_obj[key]
    else:
        print("Read Error: Specified key does not exists.")
        return


# deletes the value corresponding to the key passed
def delete(key):
    with open("data.json", "r+") as infile:
        json_obj = json.load(infile)

    if key in json_obj:
        del json_obj[key]
    else:
        print("Delete Error: Specified key does not exists.")
        return

    with open("data.json", "w") as outfile:
        json.dump(json_obj, outfile, indent = 4)
