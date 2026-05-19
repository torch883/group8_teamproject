import json

def load_data(filename):
    try:
        file=open(filename, "r")
        content=file.read()
        file.close()
    
        if content.strip() == "":
            print("File is empty")
            return []
    
        data=json.loads(content)   
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
        print("Data saved successfully")
    except Exception as e:
        print("Error saving data:", e)