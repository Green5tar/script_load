import uuid
import ast
import json
#open .txt files with list of dict [{},{}] json
d = {}
def first (first):
    with open(str(first)) as file_in:
        text1 = file_in.read()

    text2=text1.replace("'", '|')

    with open(str(first), "w") as w:
        w.write(text2)

def change(file_name, second):
    with open(str(file_name), 'r') as f, open(str(second), "w") as second:
        data=json.loads(f.read())
        #print(data)
        #file=ast.literal_eval(f.read())
        for json_object in data:
            for json_object1 in json_object.items():
                #for json_object2 in json_object1[1]:
                    #json_object1["order_id"]=uuid.uuid4()
                q=json_object1[1]
                if str(type(q))=="<class 'dict'>":
                    moc=q
                    for key, value in moc.items():
                        if key=="order_id":
                            moc[key]=uuid.uuid4()

                    #print(q)

            if "pk" in json_object:
                json_object["id"]=json_object.pop("pk")
                json_object["id"]=uuid.uuid4()
                #print(json_object)
            data = ''.join(str(json_object))
            print("data", data)
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
    text9 = text8.replace('|', "'")
    text10="["+text9+"]"
    with open(str(second), "w") as w:
        w.write(text10)

def ff(first):
    with open(first, "r+") as json_file:
        data = json.load(json_file)

        for obj in data:
            fields = obj['fields']

            #if obj["id"]:
            #    obj["pk"]=obj.pop("id")

            #print(fields)
            if ('name' in fields):
                fields['name_custom'] = fields.pop('name')
            if ('codename' in fields):
                fields['codename_custom'] = fields.pop('codename')
            if "content_type" in fields:
                fields["content_type_custom"] = fields.pop("content_type")

            print(fields)

        json_object = json.dumps(data)
        json_file.write(json_object)

ff("auth.json")
#first(first='order_n_billing.new.json')
#change(file_name="order_n_billing.new.json", second="order_n_billing1.new.json")
#first(first='order_n_billing.new.json')
#change(file_name="order_n_billing.new.json", second="order_n_billing1.new.json")

#ww(second="order_n_billing1.new.json")