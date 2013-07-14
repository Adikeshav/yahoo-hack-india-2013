# Create your views here.
import urllib
import urllib2
import re
import lxml.html

from django.http import HttpResponse
from django.template.defaultfilters import slugify
from history.models import History

from products.models import Item, Website, Brand, Category


def parse_jabong(request):
    website = Website.objects.get(name="Jabong")
    brand = Brand.objects.get(name="Adidas")
    category = Category.objects.get(name="Shoes")
    url = 'http://www.jabong.com/men/shoes/men-sports-shoes/Adidas/?special_price=1&page=4'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {}
    headers = {
        'User-Agent': user_agent,
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    html = response.read()
    tree = lxml.html.fromstring(html)
    for el in tree.cssselect("li.itm a.itm-link"):
        print el.cssselect(".itm-title")[0].text.strip()
        try:
            search_item = Item.objects.get(name=el.cssselect(".itm-title")[0].text.strip())
        except:
            search_item = None
        print search_item
        if search_item is None:
            print "Item does not exist. Creating new"
            item = Item()
            item.name = el.cssselect(".itm-title")[0].text.strip()
            print item.name
            item.gender_type = "MALE"
            product_url = el.attrib["href"]
            item.url = product_url
            item.category = category
            item.brand = brand
            item.website = website
            item.slug = slugify(item.name + "=" + item.website.slug)
            old_price_text = el.cssselect(".itm-price.old")[0].text
            new_price_text = el.cssselect(".itm-price.special-b")[0].text
            discount_rate_text = el.cssselect(".itm-price.discount")[0].text
            re_float = re.compile(r'.*?(?P<number>\d+\.?\d*).*?')
            old_price = re_float.match(old_price_text).group("number")
            new_price = re_float.match(new_price_text).group("number")
            discount_rate = re_float.match(discount_rate_text).group("number")

            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            values = {}
            headers = {
                'User-Agent': user_agent,
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(product_url, data, headers)
            product_response = urllib2.urlopen(req)
            product_html = product_response.read()
            product_tree = lxml.html.fromstring(product_html)
            print product_tree
            print product_tree.cssselect(".prd-image")
            print product_tree.cssselect(".prd-image")[0].attrib["src"]
            item.image_url1 = product_tree.cssselect("#prdImage")[0].attrib["src"]
            item.details = product_tree.cssselect(".prd-description")[0].text
            item.save()
            history = History()
            history.item = item
            history.offer_text = item.brand.name + " " + item.name + " " + old_price_text + " " + new_price_text + " " + discount_rate_text
            history.selling_price = float(new_price)
            history.actual_price = float(old_price)
            history.discount_rate = float(discount_rate)
            history.is_on_sale = True
            history.save()

            print item
        print "#######################################"
    return HttpResponse(html)
