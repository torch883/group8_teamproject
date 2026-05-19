import json

def load_data(filename):
    try:
        file=open(filename, "r")
        data=json.load(file)
        file.close()
        return data
    except FileNotFoundError:
        print("File not found")
        return[]
    except json.JSONDecodeError:
        print("File is not valid json")
        return[]