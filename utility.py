#json file reader with templating 
import json
import os

def jsonReader(filepath,*args):
    # Replacing dynamic names
    with open (filepath, 'r' ) as f:
        content = f.read()
        for k in args[0].keys():
            content = content.replace(k, args[0][k])
    # Loading as a json object
    data = json.loads(content)
    return data


def existanceCheck(path: str, err : int):
    ERROR_MSG = [
        "Templace File not found",
        "Template Directory not found",
        "Config File not found",
        "Directory not found"
    ]

    if not os.path.exists(path):
        print(ERROR_MSG[err])
        exit(1)
    return

if __name__ == '__main__':
    replace = {
        "{{PROJECT_NAME}}" : "PXP",
    }
    jsonReader('test.json', replace)