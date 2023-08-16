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