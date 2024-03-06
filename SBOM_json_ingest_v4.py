import json

file_location = r'sucker.json'
with open(file_location) as json_file:
    data = json.load(json_file)

nested_json = data["components"]
nested_data = json.loads(nested_json)

def func1(data):
    for key,value in data.items():
        print (str(key)+'->'+str(value))
        if type(value) == type(dict()):
            func1(value)
        elif type(value) == type(list()):
            for val in value:
                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    func1(val)
func1(nested_data)