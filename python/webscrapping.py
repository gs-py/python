from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Maria_Trubnikova"

res = requests.get(url)
tex = res.text
soup = BeautifulSoup(tex, 'html.parser')

# Find the element with the specified ID and class attributes
heading_element = soup.find('a')
print(heading_element)
# Extract the text content from the element
for hm in heading_element:
    print(hm.text)