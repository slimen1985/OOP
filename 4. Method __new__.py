# class Point:
#
#     def __new__(cls, *args, **kwargs):
#         print("Вызов __new__ для " + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print("Вызов __init__ для" + str(self))
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# print(pt)


#Реализация при помощи паттерна SingleTon
class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД:  {self.user}, {self.psw}, {self.port}")

    def close(self0):
        print("Зкрытие соединения с БД")

    def read(self):
        return "Данные из БД"

    def write(self, data):
        print(f"Запись в БД {data}")


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)

print(id(db), id(db2))




