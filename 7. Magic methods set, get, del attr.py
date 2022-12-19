class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        print("__getattribute__")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя аттрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        print("__delattr__: " + item)
        object.__delattr__(self, item)




pt1 = Point(1, 2)
pt2 = Point(10, 20)
pt1.y = 5
del pt1.x
print(pt1.__dict__)
# a = pt1.x
# print(a)