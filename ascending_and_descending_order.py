#Podajemy liczbe i ma ja ulozyc od najwiekszej cyfry do najmniejszej i na odwrot
#concatenated tlumaczyc an powiazac (link together)
#iterable is an object that can be looped over. e.g. list , string , tuple etc.
#The join() method returns a string concatenated with the elements of an iterable.
#If the iterable contains any non-string values, it raises a TypeError exception.

def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))


print(descending_order(1247621))


def ascending_order(num):
    return int("".join(sorted(str(num), reverse=True)))


print(ascending_order(1247621))
