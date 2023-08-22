import json

def extract_route(request):
    split1 = request.split("\n")[0]
    split2 = split1.split(" ")[1]
    route = split2[1:]
    return route

def read_file(path):
    file = open(path, mode='r+b')
    lines = file.read()
    return lines

def load_data(path):
    filepath = 'data/' + path
    file = read_file(filepath)
    return json.loads(file)

def load_template(path):
    filepath = 'templates/' + path
    file = open(filepath, mode="r")
    return file.read()

def add_anotacao(params):
    notes = load_data("notes.json")
    notes.append(params)
    print(notes)
    with open("data/notes.json",'w',encoding="utf-8") as myjson:
        myjson.write(str(notes).replace("'",'"'))

def build_response(body='', code=200, reason='OK', headers=''):
    if len(headers) > 0:
        return ("HTTP/1.1 " + str(code) + " " + reason + "\n" + headers + "\n\n" + body).encode()
    else:
        return ("HTTP/1.1 " + str(code) + " " + reason + "\n\n" + body).encode()
    