from database import Database
from models.post import Post

Database.initialize()

post = Post(blog_id="123",
            title="Another great post",
            content="This is some sample content",
            author= "Robee")

#save new blog post in DB
#post.save_to_mongo()

# Get content from the DB
posts = post.from_blog(id='123')
for post in posts:
    print(post['content'])

#select a blog based on it's id
#post = Post.from_mongo(id= "c78093310c374388a36fb7dd6f049e97")
#print(post)

