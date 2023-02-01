import requests
from bs4 import BeautifulSoup


# Function to search the song name at bing.com
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
            return result.h2.a.get('href')
    return None


# Function to access the found url and download the tab
def download(songName, url):
    if ' cifra' in songName:
        songName = songName.replace(' cifra', '')
        
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    musicTab = soup.find('pre').text

    with open('cifras/'+songName+".txt", 'w', encoding = 'utf-8') as f:
        f.write(musicTab)


def main():
    while True:
        a = input('Type the song name + the word "cifra" (x to exit): ')
        if a == "" or a == None:
            print("Invalid song name!")
            pass
        elif a == "x":
            print("\nEnding program")
            break
        else:
            url = search(a)
            download(a, url) if url != None else print('\nSong not found! \n')
            

if __name__ == "__main__":
    main()


