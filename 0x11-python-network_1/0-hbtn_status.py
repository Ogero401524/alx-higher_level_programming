#!/usr/bin/python3
import urllib.request
#fuunction
def fetch(url):
    #get url with urlopen
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            readData = data.decode('utf-8')
            print("\t- type:", type(readData))
            print("\t- content:",readData)
            print("\t- utf8 content:", readData)
    except urllib.error.URLError as Er:
        print(f"Error Fetching url:  {Er}")
#program execution aka throw the ARROW.
if __name__ == "__main__":
    urlArrowT = "https://alx-intranet.hbtn.io/status"
    fetch(urlArrowT)
