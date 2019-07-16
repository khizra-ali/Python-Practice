# import json
# with open("students.json", "w") as fdes:
#     lst = ["inam", "AI", 5364]
#     di = {"name": "inam", "class": "AI"}
#     json.dump(lst, fdes)
#     json.dump(di, fdes)

import json
language = {
    'aaa':'hey',
    'aaa':'hey',
    'aaa':'hey',
    'aaa':'hey',
    'aaa':'hey'
}

with open("lang.json", "w") as f:
    json.dump(language, f) #to write in json file use dump
    
with open("lang.json", "r") as f:
    print(json.load(f)) #to read a json file