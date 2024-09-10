
from collections import defaultdict
import uuid


class BaseTable:
    data = {}

    @classmethod
    def insert(cls, data):
        cls.data[data.stream_id] = data

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
        
        key = list(cls.data.keys())[-1]
        
        return cls.data[key]
    
    @classmethod
    def get(cls, stream_id: uuid.UUID):
        if len(cls.data) == 0:
            raise Exception("No data in the table")
        
        return cls.data.get(stream_id)
