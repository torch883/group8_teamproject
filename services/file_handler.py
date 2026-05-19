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
    
def save_data(filename, data):
    try:
        file=open(filename, "w")
        json.dump(data, file, indent=4)
        file.close()
    except Exception as e:
        print("Error saving data:", e)