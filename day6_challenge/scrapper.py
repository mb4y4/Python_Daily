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
    # with open('scrapper.txt', 'w', encoding='utf-8') as titles:
    #     for title in article_titles:
    #         texts = title.text
    #         titles.write(f"{texts} \n")
    print (article_titles)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")