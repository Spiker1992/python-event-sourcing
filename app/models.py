
import uuid
from commons.base_table import BaseTable


class PostTable(BaseTable):
    ...

class Post:
    stream_id: uuid.UUID
    title: str  
    content: str

    objects = PostTable

    def __init__(self, stream_id, title = None, content = None):
        self.stream_id = stream_id
        self.title = title
        self.content = content

    def save(self):
        PostTable.insert(self)
    
