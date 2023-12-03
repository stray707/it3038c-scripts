import requests
import sys
from blog_utils import create_blog_post

def get_title_from_user():
    return input("Enter a title for the blog post: ")

def main():
    if len(sys.argv) != 2:
        print("Usage: python create_blog_from_file.py <text_file>")
        sys.exit(1)

    text_file = sys.argv[1]

    try:
        with open(text_file, 'r') as file:
            # Read content from the text file
            content = file.read()

            # Get the title from the user
            title = get_title_from_user()

            # Create a blog post using the utility function
            blog_post = create_blog_post(title)

            # Display the created blog post
            print(f"Created Blog Post:\nTitle: {blog_post['title']}\nDate: {blog_post['date']}\nContent:\n{content}")

            # Send the data to the Flask application (replace with the appropriate Flask URL)
            url = 'http://127.0.0.1:5000/create_blog'
            data = {'title': blog_post['title']}
            response = requests.post(url, data=data)

            if response.status_code == 200:
                print("Blog post successfully created in the Flask application.")
            else:
                print("Error creating blog post in the Flask application.")

    except FileNotFoundError:
        print(f"Error: File '{text_file}' not found.")

if __name__ == '__main__':
    main()