import httplib
import urllib
import urllib2
import re

from BeautifulSoup import BeautifulSoup


class ACMPortal:
    title = "ACM Portal"

    def __init__(self):
        self.SEARCH_BASE_URL = "http://dl.acm.org/results.cfm"

    def search(self, terms, count):
        if count < 10:
            resp = self._get_response(terms, count)
        else: 
            resp = self._get_response(terms, count - 20)
        titles = self._scrape(resp)
        return titles


    def _get_response(self, terms, start):
        params = urllib.urlencode({'query': "+".join(terms), 'start' : start + 1 })
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
            
            entries = soup.findAll('table', style="padding: 5px; 5px; 5px; 5px;")
            for entry in entries:
        
                rows = BeautifulSoup(str(entry)).findAll("tr")

                title = re.sub("<[^>]+>", '', str(BeautifulSoup(str(rows[0].contents[1])).findAll('a', { 'class' : 'medium-text' })[0])).strip()
                link = 'http://dl.acm.org/' + BeautifulSoup(str(rows[0].contents[1])).findAll('a', { 'class' : 'medium-text' })[0].attrs[0][1]
                year = BeautifulSoup(str(rows[1])).findAll('td')[0].contents[0].strip().split(' ')[1]
                publication = re.sub("<[^>]+>", '', str(BeautifulSoup(str(rows[1])).findAll('td')[2].contents[1])).strip()
                authors = re.sub("<[^>]+>", '', str(BeautifulSoup(str(rows[0].contents[1])).findAll('div', { 'class' : 'authors' })[0])).strip()

                titles.append({'title' : title, 'link' : link, 
                                'year' : year, 'authors' : authors})

        except urllib2.HTTPError:
            print "ERROR: ",
            print resp.status, resp.reason
            return []

        return titles
