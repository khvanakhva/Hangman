def tallest_people(**kwargs):
    maximum = max(kwargs.values())
    res_names = []
    for key, value in kwargs.items():
        if value == maximum:
            res_names.append(key)

    res_names.sort()

    for name in res_names:
        print(name, ':', maximum)

