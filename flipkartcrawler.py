import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import types


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_1_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_1_na_na_pr&as-pos=0&as-type=RECENT&suggestionId=laptop%7Cin+Laptops&requestId=36786db6-c8cd-4cb4-9741-611883a832f2&as-backfill=on&page=1"

html = urllib.request.urlopen(url,context=ctx).read()

soup = BeautifulSoup(html,'html.parser')

#https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_1_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_1_na_na_pr&as-pos=0&as-type=RECENT&suggestionId=laptop%7Cin+Laptops&requestId=36786db6-c8cd-4cb4-9741-611883a832f2&as-backfill=on&page=2

  
elements = soup.find_all("div",{"class":"bhgxx2 col-12-12"})
#soup.find_all('div', attrs={'class': 'bhgxx2 col-12-12'})
#price = row.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})

#foo_descendants = row.descendants
    
# for row in elements:
# 	x = row.descendants
#     print(x)
#bar = row.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
for row in elements:   
    name = row.find('div', attrs={'class': '_3wU53n'})
    rating = row.find('div', attrs={'class': 'hGSR34'})
    price = row.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    if ((price is not None) and (name is not None) and (rating is not None)):
        print("Name : {}\nPrice : {}\nRating : {}\n\n".format(name.text,price.text,rating.text))
    #x=row.descendants
    #for d in x:
     #   if d.name == 'div' and d.get('class', '') == ['_1vC4OE _2rQ-NK']:
      #      print(d.text)