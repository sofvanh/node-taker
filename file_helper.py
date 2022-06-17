import json


def get_raw_string_from_file(file):
    f = open(file, "r")
    d = f.read()
    f.close()
    return d


def get_data_from_file(file):
    return json.loads(get_raw_string_from_file(file))


def write_data_to_file(data):
    f = open("data.json", "w")
    s = json.dumps(data, indent=2, sort_keys=True)
    f.write(s)
    f.close()
