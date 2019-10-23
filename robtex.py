
if __name__ == "__main__":
    import requests
    import os
    import re
    import sys
    import threading
    import json
    import urllib3
    import time
    from bs4 import BeautifulSoup
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    
    starttime = time.time()
    robtexip = []
    robtexurl = []
    lookup = []
    jobs = []


    def fun1(blah):
        #blah = argv
        for i in blah:
            if re.match(r"[\d\.]+", i) is not None:
                url = 'https://www.robtex.com/ip-lookup/{}'.format(i)
                robtexip.append(url)
            else:
                url = 'https://www.robtex.com/ip-lookup/{}'.format(i)
                robtexurl.append(url)
    run = threading.Thread(target=fun1, args=(sys.argv[1:],))
    run.start()
    run.join()

    def getrobip(robip):
            response = requests.get(robip, verify=False) #get request to completed robtex url from above
            soup = BeautifulSoup(response.text, 'html.parser')  #use Beautifulsoup's html parser for the output and assign that to soup
            results = soup.find_all('div', class_='dns')    #take html output from soup, find all div sets, under the class dns(this is all found from the html output itself)
            results2 = re.findall(r"(?<=\>)[\w\.\-\,\(\)\:\s\/]+(?!\<\/b)", str(results), re.M|re.I) #regex find all non-html data we want to view
            try:
                results2.remove('asname')
            except:
                pass
            try:
                results2.remove('a')
            except:
                pass
            try:
                results2.remove('ptr')
            except:
                pass
            try:
                results2.remove('bgp')
            except:
                pass
            try:
                results2.remove('descr')
            except:
                pass
            try:
                results2.remove('location')
            except:
                pass
            try:
                results2.remove('whois')
            except:
                pass
            try:
                results2.remove('route')
            except:
                pass
            try:
                results2.remove('rout')
            except:
                pass
            try:
                results2.remove('whoi')
            except:
                pass
            try:
                results2.remove('pt')
            except:
                pass
            try:
                results2.remove('asnam')
            except:
                pass
            try:
                results2.remove('desc')
            except:
                pass
            try:
                results2.remove('bg')
            except:
                pass
            try:
                results2.remove('locatio')
            except:
                pass
            if len(results2) >= 13:
                lookup.append(results2[0]+' | '+results2[1]+' | '+results2[2]+' | '+results2[4]+' | '+results2[8]+' | '+results2[12])
            elif len(results2) == 12:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8]+' | '+results2[10]) 
            elif len(results2) == 11:
                lookup.append(results2[0]+' | '+results2[1]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8]+' | '+results2[10]) 
            elif len(results2) == 10:
                lookup.append(results2[0]+' | '+results2[1]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8])
            elif len(results2) == 9:
                lookup.append(results2[0]+' | '+results2[1]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8])
            elif len(results2) == 8:
                lookup.append(results2[0]+' | '+results2[1]+' | '+results2[2]+' | '+results2[4]+' | '+results2[6])
            elif len(results2) == 7:
                lookup.append(results2[0]+' | '+results2[1]+' | '+results2[2]+' | '+results2[4]+' | '+results2[6])
            elif len(results2) == 6:
                lookup.append(results2[0]+' | '+results2[1]+' | '+results2[2]+' | '+results2[4])
            elif len(results2) == 5:
                lookup.append(results2[0]+' | '+results2[1]+' | '+results2[2]+' | '+results2[4])
            elif len(results2) == 4:
                lookup.append(results2[0]+' | '+results2[1]+' | '+results2[2]+' | '+results2[3])
            elif len(results2) == 3:
                lookup.append(results2[0]+' | '+results2[1]+' | '+results2[2])
            elif len(results2) == 2:
                lookup.append(results2[0]+' | '+results2[1])
            elif len(results2) == 1:
                lookup.append(results2[0])
            elif len(results2) == 0:
                lookup.append(robip+' Nothing Found! Trying pinging the host and looking up that IP')

    def getroburl(roburl):
            response = requests.get(roburl, verify=False) #get request to completed robtex url from above
            soup = BeautifulSoup(response.text, 'html.parser')  #use Beautifulsoup's html parser for the output and assign that to soup
            results = soup.find_all('div', class_='dns')    #take html output from soup, find all div sets, under the class dns(this is all found from the html output itself)
            results22 = re.findall(r"(?<=\>)[\w\.\-\,\(\)\:\d\s\/]+", str(results), re.M|re.I) #regex find all non-html data we want to view
            results2 = re.findall(r"[\w\.\-\,\:\s\.]{3,}",str(results22), re.I|re.M)
            try:
                results2.remove('asname')
            except:
                pass
            try:
                results2.remove('a')
            except:
                pass
            try:
                results2.remove('ptr')
            except:
                pass
            try:
                results2.remove('bgp')
            except:
                pass
            try:
                results2.remove('descr')
            except:
                pass
            try:
                results2.remove('location')
            except:
                pass
            try:
                results2.remove('whois')
            except:
                pass
            try:
                results2.remove('route')
            except:
                pass            
            if len(results2) == 0:
                lookup.append(roburl+' Nothing Found! Trying pinging the host and looking up that IP')
            elif len(results2) > 8:
                lookup.append(results2[2]+' | '+results2[0]+results2[1]+' | '+results2[5]+' | '+results2[7]+' | '+results2[8]+' '+results2[9])
            else:
                lookup.append(results2[0]+results2[1])

    if robtexip != None:
        for robip in robtexip:
            ri = threading.Thread(target=getrobip, args=(robip,))
            jobs.append(ri)
            ri.start()

    if robtexurl != None:
        for roburl in robtexurl:
            ru = threading.Thread(target=getroburl, args=(roburl,))
            jobs.append(ru)
            ru.start()

    for j in jobs:
        j.join()
        
    f = time.time() - starttime

    for l in lookup:
        print(l)
    print("this took this many seconds: " + str(f))
