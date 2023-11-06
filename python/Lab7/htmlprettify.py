from bs4 import BeautifulSoup

# Reads HTML file content
with open('samplepage.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Replace text in <p> with class "targetedClass"
for p in soup.find_all('p', class_='targetClass'):
    p.string = "This text has been replaced."

# Remove the div with id "unwantedDiv"
unwantedDiv = soup.find('div', id='unwantedDiv')
if unwantedDiv:
    unwantedDiv.decompose()

# Adds the edited html content to a separate page.
with open('modifiedsamplepage.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

print(soup.prettify())