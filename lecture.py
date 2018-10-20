#read web content
import urllib.request
from bs4 import BeautifulSoup as BS    #lib needed for traversing HTML files
import requests
url = 'https://vision.in.tum.de/teaching/ws2016/mlcv16'

##downloading the page and then dumping it
response = urllib.request.urlopen(url)
webpage = response.read()      # a `bytes` object and dump it in rawdata
#text = webpage.decode('utf-8') # a `str`; this step can't be used if data is binary
response.close()

#Let HTML file be workable
page_souped=BS(webpage,"html.parser")  #page_souped.h1 (show header)  .p (show p tag)
#Grab sth I want. I want the 5th and 6th class level5
files=page_souped.findAll("a",{"class":"media mediafile mf_pdf test"})  #len(slides) check if the "list" is of correct length

# Download the file from `url` and save it locally under `file_name`:
#if a tag has only one child node, and that child node is a string, the child node is made available as tag.string, as well as tag.contents[0]
prefix='https://vision.in.tum.de/'                     
i=0
for entry in files:
    print(entry)
    download_file_url=prefix + entry["href"]
    response2 = requests.get(download_file_url)
    i+=1
    if i<=15:
        with open(entry.string+".pdf", 'wb') as out_file:
            out_file.write(response2.content)
    else :
        with open("Exercise"+entry.string+".pdf", 'wb') as out_file:
            out_file.write(response2.content)
