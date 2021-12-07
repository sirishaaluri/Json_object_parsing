def deep_get(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)

from functools import reduce
def deep_get(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)

data1 = {'a':{'b':{'c':'d'}}}
data2 = {'one':'1', 'a':{'b':{'c':'d'}}}
print (deep_get(data1, "a"))
print (deep_get(data1, "a.b"))
print (deep_get(data1, "a.b.c"))
print (deep_get(data2, "one"))
print (deep_get(data1, "a.c.a", default="No Value found"))
