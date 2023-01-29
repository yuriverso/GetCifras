
import requests
from bs4 import BeautifulSoup

radical = "https://www.cifraclub.com.br/?q="

songName = "AnnaJulia"

url = 'https://www.cifraclub.com.br/los-hermanos/anna-julia/'



print("done")

#pesquisar
#escolher
#baixar


def search(songName):
    radical = "https://www.cifraclub.com.br/?q="
    searchName = ""
    for word in songName.split(" "):
        searchName += word+"+"
    searchUrl = radical+searchName
    print("***********************************************************")
    print("Search URL: "+searchUrl)
    print("***********************************************************")
    r = requests.get(searchUrl)
    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup.prettify())
    aS = soup.findAll('a')
    for a in aS:
        print(a)
    #resultBox = soup.find('div', {'class': 'gsc-expansionArea'})
    #print(soup.prettify())'''
    



def downloadSong(songName, url):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    musicTab = soup.find('pre').text

    with open(songName+".txt", 'w') as f:
        f.write(musicTab)

def main():
    while True:
        a = input("Digite o nome da música que quer procurar: ")
        if a == "" or a == None:
            print("Nome de música inválido")
            pass
        else:
            break

if __name__ == "__main__":
    a = "anna julia"
    search(a)
    


