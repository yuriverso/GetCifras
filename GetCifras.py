import requests
from bs4 import BeautifulSoup
from os import listdir


"""
make functions to download from cifras and ultimate tabs
"""


def makeRequest(songName, google=False, bing=False):
    if google:
        radical = "https://www.google.com/search?q="
    elif bing:
        radical = "https://www.bing.com/search?q="
    searchUrl = radical + songName.replace(' ', '+')
    print("Searching for tab at: "+searchUrl)
            
    r = requests.get(searchUrl)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


# Function to search the song name at google.com
def googleSearch(songName):
    attempt = 1
    while attempt <= 2:
        if attempt == 1:
            songName += ' cifra'
    
            soup = makeRequest(songName, google=True)
            for a in soup.findAll('a'):
                if "cifraclub.com.br" in a.get("href") or "cifras.com.br" in a.get("href"):
                    return "https://"+'/'.join(a.get("href").split("//")[1].split('/')[:-1])
                
        elif attempt == 2:
            songName += " tab"

            soup = makeRequest(songName, google=True)
            for a in soup.findAll('a'):
                if "ultimate-guitar.com" in a.get("href"):
                    return "https://"+'/'.join(a.get("href").split("//")[1].split('/')[:-1])
                
        attempt += 1
    print("No song found. ")
    return None


# Function to search the song name at bing.com
def bingSearch(songName):
    attempt = 1
    while attempt <= 2:
        if attempt == 1:
            songName += ' cifra'
    
            soup = makeRequest(songName, bing=True)
            for li in soup.find("ol").findAll("li"):
                if "cifraclub" in li.find('a').get("href") or "cifras" in li.find('a').get("href"):
                    return li.find('a').get("href")
                
        elif attempt == 2:
            songName += " tab"

            soup = makeRequest(songName, bing=True)
            for li in soup.find("ol").findAll("li"):
                if "ultimate-guitar.com" in li.find('a').get("href"):
                    return li.find('a').get("href")
                
        attempt += 1
    print("No song found. ")
    return None

    """radical = "https://www.bing.com/search?q="
    searchUrl = radical + songName.replace(' ', '+')
    print("")
    r = requests.get(searchUrl)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.findAll("li", {"class": "b_algo"})
    for result in results:
        if "cifraclub" in result.h2.a.get("href"):
            return result.h2.a.get("href")
    return None"""


# Function to access the found url and download the tab
def cifraclubDownload(songName, url):
    if " cifra" in songName:
        songName = songName.replace(" cifra", "")
        
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    musicTab = soup.find("pre").text
    
    if songName+".txt" in listdir("cifras"):
        songName+="_2"
        
    with open("cifras/"+songName+".txt", 'w', encoding = "utf-8") as f:
        f.write(musicTab)
    print("\nTab downloaded!\n")


def main():
    while True:
        songName = input("Type the song name (x to exit): ")
        if songName == "" or songName == None:
            print("Invalid song name!")
            pass
        elif songName == "x":
            print("\nEnding program")
            break
        else:
            # google search
            search = None
            #search = googleSearch(songName)
            if search == None:
                print("Not found at google.com, trying another approach...")
                # bing search
                search = bingSearch(songName)
            if "cifraclub" in search:
                cifraclubDownload(songName, search)
            elif "cifras" in search:
                pass
            elif "ultimate" in search:
                pass
            
            
            
            #url = search(a)
            #download(a, url) if url != None else print("\nSong not found! \n")
            

if __name__ == "__main__":
    main()


