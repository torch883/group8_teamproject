import json

def load_data(filename):
    file=open(filename, "r")
    data=json.load(file)
    file.close()
    return data