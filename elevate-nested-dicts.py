# Raise nested dictionary to top level
# dictionaries and lists are mutable
# Copy of the dict determines the starting keys and values, alter original dict
def elevate_nested_dicts(dictionary, parent=None):
    finished = False
    while not finished:
        finished = True
        dcopy = dictionary.copy()
        for key, val in dcopy.items():
            if isinstance(val, dict):
                finished = False
                elevate_nested_dicts(val.copy(), parent=dictionary)
                del dictionary[key]
            elif parent is not None:
                if key not in parent.keys():
                    parent[key] = val
                # del dictionary[key]
    return dictionary