import uuid
from database import Database
import datetime


class Post(object):

    # Creating an object
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.create_date = date
        #self.id = uuid.uuid4().hex if id in None else id  # if there is no predefined id it will generate a random one.
        # uuid4() generates a random number, .hex gives us 32 charecter
        if id == None:
            self.id = uuid.uuid4().hex
        else: self.id = id

    # Writing into mongoDB
    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())  # puting json data into 'posts' collection

    # defining content to write in mongoDB
    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'create_date': self.create_date
        }

    # Finding post content based on id
    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts',
                                 query={'id': id})  # Post.from_mongo('123') will give us the content with 'id' 123
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['create_date'],
                   id=post_data['id'])

    # Finding all blog posts in specific blog
    @staticmethod
    def from_blog(id):
        return Database.find(collection='posts', query={'blog_id': id})
        # [post from post in Database.find(collection='post', query={'blog_id': id})] # we find all of the posts in specific id and returns a list of the posts
