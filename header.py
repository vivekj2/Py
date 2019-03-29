import urllib2
import sys

def main():
    url=raw_input("Enter URL to scan:")
    header=urllib2.urlopen(url).info()
    print'\n'
    print(str(header))

if __name__ == '__main__':
    main()
