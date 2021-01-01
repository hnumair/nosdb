import json
import os
import sys

class Database:

    # Database initialization
    def __init__(self, *args):

        self.alive = True

        if len(args) == 0:

            # if filepath is not specified
            self.filepath = os.path.join(os.getcwd(), "database")
            if not os.path.isdir(self.filepath):
                os.mkdir(self.filepath)
            self.filepath = os.path.join(self.filepath, 'database.json')
            if os.path.getsize(self.filepath) < 10**9:
                open(self.filepath, "a+")
            else:
                print("Database full (max 1GB)")
                self.alive = False
                return
        else:

            # if filepath is specified
            self.filepath = args[0]
            self.filepath = os.path.join(self.filepath, 'database.json')
            if not os.path.isfile(self.filepath):
                if os.path.getsize(self.filepath) < 10**9:
                    open(self.filepath, "a+")
                else:
                    print("Database full (max 1GB)")
                    self.alive = False
                    return


    # Input validation
    def validInput(self, key, data):

        self.key = key
        self.data = data

        # Key size restriction
        if type(self.key) is str:
            self.key = self.key[0:32]
        else:
            print("Create Error: Only strings are allowed for the key (max: 32)")
            return False

        # JSON Value restriction
        try:
            json.loads(self.data)
        except ValueError as e:
            print("Create Error: Enter valid JSON value")
            return False

        if(sys.getsizeof(self.data) > 16000):
            print("Create Error: JSON Object too large (max: 16KB)")
            return False

        return True

    # creates a new entry in the database
    def create(self, key, data):

        if not self.alive:
            return

        dict = {}
        self.key = key
        self.data = data
        if not self.validInput(self.key, self.data):
            return


        indata = {"%s" % self.key: "%s" % self.data}
        with open(self.filepath, "r+") as infile:
            try:
                dict = json.load(infile)
            except ValueError:
                print("Database empty")

            if self.key in dict:
                print("Create Error: The key entered already exists.")
                return

            dict.update(indata)
            infile.seek(0)
            json.dump(dict, infile, indent = 4)
            print("True")
            return


    # retrieves the value corresponding to the key passed 
    def read(self, key):

        if not self.alive:
            return

        self.key = key
        with open(self.filepath, "r") as infile:
            json_obj = json.load(infile)
        if self.key in json_obj:
            return [self.key, json_obj[self.key]]
        else:
            return("Read Error: Specified key does not exists.")


    # deletes the value corresponding to the key passed
    def delete(self, key):

        if not self.alive:
            return

        self.key = key;
        with open(self.filepath, "r+") as infile:
            json_obj = json.load(infile)

        if self.key in json_obj:
            del json_obj[self.key]
        else:
            print("Delete Error: Specified key does not exists.")
            return

        with open(self.filepath, "w") as outfile:
            json.dump(json_obj, outfile, indent = 4)
            print("True")
