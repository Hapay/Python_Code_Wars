def array_diff(a, b):
    for item in b:
        for items in a:
            if item in a:
                a.remove(item)
    return a


a = [1, 2, 2, 3, 4]
b = [2, 3]
print(array_diff(a, b))



#def array_diff(a, b):
    #return [x for x in a if x not in b]