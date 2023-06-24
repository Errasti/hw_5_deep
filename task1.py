import os


def parse_path(file_path):
    path, file = os.path.split(file_path)
    name, ext = os.path.splitext(file)
    return path, name, ext


tuple_test = parse_path("/test/test/test/test.test")
print(tuple_test)
