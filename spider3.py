import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

# Set the starting point for the spider and initialize
url = "http://www.nytimes.com"
br = mechanize.Browser()

# lists for upcoming que'd urls, and ones already visited
urls = [url]
visited = [url]

# Since the amount of urls in the list is dynamic
#   we just let the spider go until some last url didn't
#   have new ones on the webpage
while len(urls) > 0: #so long as there is a url remaining that hasnt been visited it will keep running
    try:
        br.open(urls[0])
        urls.pop(0)
        for link in br.links():
            newurl = urlparse.urljoin(link.base_url, link.url)
             #print newurl
            if newurl not in visited and url in newurl:
                visited.append(newurl)
                urls.append(newurl)
                print newurl
    except:
        print "error"
        urls.pop(0)

print visited

