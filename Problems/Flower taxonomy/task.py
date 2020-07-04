iris = {}
keys = ['species', 'petal_length', 'petal_width']


def add_iris(id_n: int, species: str, petal_length: float, petal_width: float, **kwargs):
    values = [species, petal_length, petal_width]
    iris_data = new_dictionary(keys, values)
    for key, value in kwargs.items():
        iris_data[key] = value
    iris[id_n] = iris_data


def new_dictionary(keys, values):
    length = len(keys)
    if length != len(values):
        raise Exception("Keys and values do have equal size")
    dictionary = {}
    for i in range(0, length):
        key = keys[i]
        value = values[i]
        dictionary[key] = value
    return dictionary
