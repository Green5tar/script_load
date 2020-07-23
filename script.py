import uuid
import ast
import json
#open .txt files with list of dict [{},{}] json
d = {}
def change(file_name, second):
    with open(str(file_name), 'r') as f, open(str(second), "w") as second:
        data=json.loads(f.read())
        print(data)
        #file=ast.literal_eval(f.read())
        for json_object in data:
            if "pk" in json_object:
                json_object["id"]=json_object.pop("pk")
                json_object["id"]=uuid.uuid4()
                print(json_object)
            data = ''.join(str(json_object))
            #print("data", data)
            #print(json_object,"11")
            second.write(data)
        #print(second.read().replace("'",'"'))
        #second.write(q)
        #print(q)


def ww(second):
    with open(str(second)) as file_in:
        text1 = file_in.read()

    text2=text1.replace("'", '"')
    text3 = text2.replace('True', 'true')
    text4 = text3.replace("False", 'false')
    text5 = text4.replace("None", 'null')
    text6 = text5.replace('UUID("', '"')
    text7 = text6.replace('")', '"')
    text8 = text7.replace('}{', '},{')
    with open(str(second), "w") as w:
        w.write(text8)

change(file_name="accounts.new2.json", second="accounts.new.json")

ww(second="accounts.new.json")