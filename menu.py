from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        # Ask user for author name
        self.user = raw_input("Enter your author name: ")
        self.user_blog = None # set a default value for "user_blog". We will need to find the right blog in the database

        # Check if they already have an account
        if self._user_has_account():
            print("Welcome back {}".format(self.user))

        # if not, prompt them to create one
        else:
            self._prompt_user_for_account()

    # check in the database if there is an author with defined name.
    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id']) # search for a blog based on id
            return True
        else:
            return False

    # if they dont have an account they have to "start a new blog"
    def _prompt_user_for_account(self):
        title = raw_input("Enter blog title: ")
        description = raw_input("Enter blog description: ")
        blog = Blog(author = self.user,
                    title = title,
                    description = description)

        blog.save_to_mongo()
        self.user_blog = blog



    """ users are able to select what to do. 
    Read blogs, write a blog, register"""
    def run_menu(self):
        # User read or write blog?
        read_or_write = raw_input("Do you want to read (R) or write (W) a blog? ")

        # if read:
            # list blogs in database
            # allow user to pick one
            # display post
        if read_or_write == 'R':
            print("Which blog would you like to read? {}".format(self.user))
            self._list_blogs()
            self._view_blog()
            pass

        #if write
            # if not, prompt to create new blog
        if read_or_write == 'W':
            blog = Database.find_one('blogs', {'author': self.user}) # finding author's blog
            print("Here is your new blog post {} for your blog {}".format(self.user, blog['title']))
            self.user_blog.new_post()

        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection="blogs",
                                  query={})
        # Print all blogs
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = raw_input("Enter the ID of the blog you'd like to read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_post()
        for post in posts:
            print("Date: {}, title: {}\n\n{}\n\n".format(post['create_date'], post['title'], post['content']))

