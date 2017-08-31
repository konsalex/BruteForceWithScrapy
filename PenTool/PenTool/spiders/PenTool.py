import string 
import scrapy
from itertools import combinations
from scrapy.exceptions import CloseSpider

class Myspider(scrapy.Spider):
    
    name = "WebSummit"

    custom_settings = {
        'CONCURRENT_REQUESTS': 30,
        'CONCURRENT_REQUESTS_PER_DOMAIN':15,
        
    }

    def start_requests(self):

            for x in combinations(string.ascii_uppercase,3) :

                up=(''.join(x))


                for y in combinations(string.digits,5) :

                    dig=(''.join(y))


                    for z in string.ascii_lowercase :


                        low=(''.join(z))


                        url= "http://yourURLhere.com"  ### Put here the URL of your prefer and the code format here is code=up+dig+low


                        yield scrapy.Request(url=url, callback=self.parse)

                    
        
    def parse(self, response):



        if "unavailable" in response.text :

            return

        else :

            raise CloseSpider('Code Found : {}' .format(response.url))