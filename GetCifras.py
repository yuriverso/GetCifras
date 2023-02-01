import requests
from bs4 import BeautifulSoup


def search(songName):
    radical = "https://www.bing.com/search?q="
    searchUrl = radical + songName.replace(' ', '+')
    print("***********************************************************")
    print("Search URL: "+searchUrl)
    print("***********************************************************")
    
    r = requests.get(searchUrl)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.findAll('li', {'class': 'b_algo'})
    for result in results:
        if 'cifraclub' in result.h2.a.get('href'):
            print(result.h2.a.get('href'))
            return result.h2.a.get('href')
    return None



def download(songName, url):
    if ' cifra' in songName:
        songName = songName.replace(' cifra', '')
        
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    musicTab = soup.find('pre').text

    with open('cifras/'+songName+".txt", 'w') as f:
        f.write(musicTab)

def main():
    while True:
        a = input("Digite o nome da música que quer procurar: ")
        if a == "" or a == None:
            print("Nome de música inválido")
            pass
        elif a == "sair":
            print("Finalizando o programa...")
            break
        else:
            url = search(a)
            download(a, url) if url != None else print('\n A música procurada nao foi encontrada \n')
            

if __name__ == "__main__":
    main()


