import json
# .json is commonly used for APIs, so I figured the format worked well here.

# Defining the Blogpost class for other scripts
class Blogpost:
    def __init__(self, title, date, content):
        self.title = title
        self.date = date
        self.content = content

class BlogContainer:
    def __init__(self, list_path):

        # Establishing path of file containing stored logs and method for loading posts
        self.list_path = list_path

        # 'posts' is when you load posts.
        self.posts = self.load_posts()

    def load_posts(self):

        # Opens file, 'r' for reading in json
        try:
            with open(self.list_path, 'r') as file:
                bloglist_data = json.load(file)

                # returns every post in the file
                return [Blogpost(**post) for post in bloglist_data]

        # It became necessary.
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_posts(self):

        # Defining a post, with title, date, and text content in json format
        bloglist_data = [{'title': post.title, 'date': post.date, 'content': post.content} for post in self.posts]

        # Writing to file
        with open(self.list_path, 'w') as file:
            json.dump(bloglist_data, file)

        # Originally did append(post), which puts the latest post at the end.
        # Then I discovered insert(0, post) puts it at the beginning.
    def add_post(self, post):
        self.posts.insert(0, post)
        self.save_posts()
