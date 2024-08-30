
class BaseTable:
    data: list = []

    @classmethod
    def insert(cls, data):
        cls.data.append(data)

    @classmethod
    def update(cls, pk, data):
        cls.data[pk] = data

    @classmethod
    def delete(cls, pk):
        del cls.data[pk]

    @classmethod
    def latest(cls):
        if len(cls.data) == 0:
            raise Exception("No data in the table")
        
        return cls.data[-1]