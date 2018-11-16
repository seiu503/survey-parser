from bs4 import BeautifulSoup
with open("html/AtEaseSurvey_mod4OCR.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# cities = soup.find_all('tr', {'class' : 'city-sh'})
paragraphs = soup.find_all('p')

for paragraph in paragraphs:
    print(paragraph.string)