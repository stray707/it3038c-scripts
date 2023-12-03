import requests

url = 'http://127.0.0.1:5000/create_post'

title = input("Enter the title: ")
text_content = input("Enter the text content: ")

payload = {'title': title, 'text_content': text_content}
response = requests.post(url, data=payload)
# Utilizes the POST method for posting


if response.status_code == 200:
    print("post created successfully!")
else:
    print("Error creating post.")