# Create your views here.
import urllib
import urllib2
import re
import lxml.html

from django.http import HttpResponse


def parse_jabong(request):
    url = 'http://www.jabong.com/men/shoes/men-sports-shoes/?special_price=1&page=3'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {}
    headers = {
        'User-Agent':user_agent,
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    html = response.read()
    tree = lxml.html.fromstring(html)
    for el in tree.cssselect("li.itm a.itm-link"):
        print "Title:", "'"+el.cssselect(".itm-title")[0].text.strip()+"'"
        old_price_text = el.cssselect(".itm-price.old")[0].text
        print "Old Price:", old_price_text
        re_float = re.compile(r'.*?(?P<number>\d+\.?\d*).*?')
        old_price = re_float.match(old_price_text).group("number")
        print "#######################################"
    return HttpResponse(html)
