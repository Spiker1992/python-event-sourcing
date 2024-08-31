
from commons.base_table import BaseTable


class PostTable(BaseTable):
    ...

class Post:
    title: str  
    content: str

    objects = PostTable

    def __init__(self, title = None, content = None):
        self.title = title
        self.content = content

    def save(self):
        PostTable.insert(self)
    
