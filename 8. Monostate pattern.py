class ThreadData:
    __shared_attrs = {
        'name': 'thread1_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs
