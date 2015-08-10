import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase
import urllib2, urllib
from BeautifulSoup import BeautifulSoup
import string

lists = []
visited = []
        
class simple(FunkLoadTestCase):
    def setUp(self):
        self.server_url = lists[i]
        
    def test_simple(self):
        
        server_url = self.server_url
       
        nb_time = self.conf_getInt('test_simple', 'nb_time')
        for i in range(nb_time):
            self.get(server_url, description='Get url')
               

if __name__ == '__main__' :
    
    def treestructure(url) :
        try :
            html = urllib2.urlopen(url)
        except urllib2.HTTPError:
            return None
        visited.append(url)
        soup = BeautifulSoup(html.read())
        htmlfile = soup.findAll('a')
        for link in htmlfile :
            link2 = link['href']
            if len(link2) > 0 :
                link3 = str(link2)
                if link3[0] == '/' :
                    link3 = url + link3
                    for site in visited :
                        if site == link3 :
                            return None
                        else :
                            print link3
                            lists.append(link3)
                            treestructure(link3)
    
    url = "http://www.sumhr.in"
    print url
    lists.append(url)
    treestructure(url)        
                
    for i in range(len(lists)) :
        unittest.main()
        
