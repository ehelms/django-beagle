import httplib
import urllib
import urllib2
import re

from BeautifulSoup import BeautifulSoup


class GoogleScholar:
    title = "Google Scholar"
    
    def __init__(self):
        self.SEARCH_BASE_URL = "http://scholar.google.com/scholar"

    def search(self, terms, count):
        resp = self._get_response(terms, count)
        titles = self._scrape(resp)
        return titles
    
    
    def _get_response(self, terms, start):
        start = start - 20
        params = urllib.urlencode({'q': "+".join(terms), 'start': start, 
                                    'hl' : 'en',
                                    'btnG' : 'Search', 'as_sdt' : '40000000000',
                                    'as_vis' : '1' })
        url = self.SEARCH_BASE_URL + "?" + params
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12' }
        request = urllib2.Request(url, None, headers)
        resp = urllib2.urlopen(request)
        return resp


    def _scrape(self, response):
        titles = []
        try:
            html = response.read()
            results = []
            html = html.decode('ascii', 'ignore')
                        
            # Screen-scrape the result to obtain the publication information
            soup = BeautifulSoup(html)
        
            entries = soup.findAll("div", { "class" : "gs_ri"})

            for entry in entries:
                title       = ""
                link        = ""
                citation    = ""

                attrs = BeautifulSoup(str(entry)).findAll("h3", { "class" : "gs_rt"})
                for attr in attrs:
                    temp = BeautifulSoup(str(attr))
                    
                    link = temp.a.get('href')

                    for item in temp.a.contents:
                        item = str(item).replace("<b>", "")
                        item = str(item).replace("</b>", "")
                        title = title + str(item)

                line = BeautifulSoup(str(entry)).findAll("div", { "class" : "gs_a"})
                for item in line[0].contents:
                    item = str(item).replace("<b>", "")
                    item = str(item).replace("</b>", "")
                    citation = citation + str(item)
    
                citation = citation.split(' - ')
                year = re.search('(19|20)\d\d', citation[1]).group()
                authors = re.sub("<[^>]+>", '', citation[0])
                authors = authors.lstrip('&hellip;').rstrip('&hellip; ').strip(';').strip(',').strip()

                titles.append({'title' : title, 'link' : link, 
                                'year' : year, 'authors' : authors})

        except urllib2.HTTPError:
            print "ERROR: ",
            print resp.status, resp.reason
            return []
        
        return titles
