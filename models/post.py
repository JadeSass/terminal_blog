import uuid
import datetime
from database import Database


class Post(object):
    
    def __init__(self, title, content, author, blog_id, date=datetime.datetime.now(), id=None):
        self.title = title
        self.content = content
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id
        self.blog_id = blog_id
        self.created_date = date

    def save_to_mongo(self):
        Database.insert(collection = 'posts', data = self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'created_date': self.created_date,
            'title': self.title,
            'content': self.content,
            'author': self.author
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'id':id})

        return cls(title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   blog_id=post_data['blog_id'],
                   date=post_data['created_date'],
                   id=post_data['id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id':id})]














