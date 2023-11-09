from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/Web_scraping'
html = requests.get(url)

# print if connection is successful or not
#print(html)

response = requests.get(url)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
 
 #create a new html file to insert the content
    with open('scrapper.html', 'w', encoding='utf-8') as html_file:
        html_file.write(soup.prettify())
    #finding the container wrapping the content we want
    #container = soup.find('div', class_='mw-page-container-inner')
    article_titles = soup.find('div', class_='mw-parser-output')
    #all tags under the mw-parser-output div tag to be stored in a list
    all_tags = article_titles.find_all()
    with open('scrapper.txt', 'w', encoding='utf-8') as titles:
        for tag in all_tags: #loop through the list
            if tag.name == 'table': #check if the tag is a table tag
                tag.decompose() #remove the table tag from the list
            if tag.name:
                print(tag.name)
                texts = tag.text
                titles.write(f"{texts} \n")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")