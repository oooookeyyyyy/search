from os import path, walk

def search(filename, search_path):
    result = []
    for root, dirs , files in walk(search_path):
        if filename in dirs :
            result.append(path.join(root, filename))
        elif filename in files :
            result.append(path.join(root, filename))
    return result
