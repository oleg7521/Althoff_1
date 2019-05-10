class Person:
    def __init__(self):
        pass

def compare(obj1, obj2):
    return obj1 is obj2

a = Person()
a1 = a
b = Person()

print(compare(a, a1))
print(compare("a", "b"))


