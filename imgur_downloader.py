from imgurpython import ImgurClient
import urllib.request
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--dest", dest="path", default='~/Scaricati/')
parser.add_option("-a", "--album", dest="album_id")
parser.add_option("-r", "--reddit", dest="subreddit")
parser.add_option("-p", "--page", dest="page", default=0)
(options, args) = parser.parse_args()
path = options.path

client_id = ''
client_secret = ''

if(options.album_id != None):
    album_id = options.album_id
    print("Download dell'album con id = " + album_id)
    print("Destinazione = " + path)
    
    cl = ImgurClient(client_id, client_secret)
    
    items = cl.get_album_images(album_id)
    image_n = str(len(items))
    i = 1
    for item in items:
        image_url = item.link
        print("Immagine " + str(i) + " su " + image_n + " " + image_url)
        i+=1
        urllib.request.urlretrieve(image_url, path + item.id + image_url[image_url.rfind('/')+1:])

if(options.subreddit != None):
    subreddit = options.subreddit
    print("Download della reddit = " + subreddit)
    print("Destinazione = " + path)
    
    cl = ImgurClient(client_id, client_secret)
    
    j=0
    while(j<=options.page):
        print("Pagina : " + str(j))
        items = cl.subreddit_gallery(subreddit,page=j)
        image_n = str(len(items))
        i = 1
        for item in items:
            image_url = item.link
            print("Immagine " + str(i) + " su " + image_n + " " + image_url)
            urllib.request.urlretrieve(image_url, path + image_url[image_url.rfind('/')+1:])
            i+=1
        j+=1
