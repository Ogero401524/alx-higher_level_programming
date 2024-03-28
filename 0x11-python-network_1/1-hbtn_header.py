#!/usr/bin/python3
import urllib.request
import sys
if __name__ == "__main__":
    urlArgs = sys.argv[1]

    try:
        with urllib.request.urlopen(urlArgs) as response:
            READdata = response.headers.get('X-Request-Id')
            if READdata:
                print(READdata)
            else:
                print("X-Request-Id header not found in the response.")

    except urllib.error.URLError as e:
        print("Error fetching URL:", e)
