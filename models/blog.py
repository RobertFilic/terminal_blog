import uuid
import datetime

from database import Database
from models.post import Post


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        if id is None:
            self.id = uuid.uuid4().hex
        else:
            self.id = id

    # ask user to write a new post
    def new_post(self):
        title = raw_input("Enter post title: ")  # type: str
        content = raw_input("Enter post content: ")
        date = raw_input("Enter post date, or leave blank for today (in format DDMMYYYY): ")  # type: object
        if date =="":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y") # converts string to date

        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date)

        post.save_to_mongo()  # save the post to mongoDB

    def get_post(self):
        #return Database.find(collection='posts', query={'blog_id': id})
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'id': id})
        # we return an OBJECT with relevant data
        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id'])