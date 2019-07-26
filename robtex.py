from bs4 import BeautifulSoup
import requests
import json
import re
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


urls = [] #list of robtex urls used to search ips
lookup = [] #list of lookup responses

class robtex:
    def __init__(self, argv): ##init which assigned the output from req to ip
        self.ip = argv #take value of ip which is input from req and assigns it to self.ip
        for i in self.ip: #loop to pull ip arguments
            self.url = 'https://www.robtex.com/ip-lookup/{}'.format(i) #robtex url to search with the ip from self.ip in the url to search
            urls.append(self.url) #appends robtex url with ips to search to the urls list
       

    def get(self):
        for u in urls: #loop to go through urls in the urls list
            response = requests.get(u, verify=False) #get request to completed robtex url from above
            soup = BeautifulSoup(response.text, 'html.parser')  #use Beautifulsoup's html parser for the output and assign that to soup
            results = soup.find_all('div', class_='dns')    #take html output from soup, find all div sets, under the class dns(this is all found from the html output itself)
            results2 = re.findall(r"[\w\s\-\_\.\,\(\)\!\#\$\%\^\&\*\@\;\:]+(?=\<\/)", str(results), re.M|re.I) #regex find all non-html data we want to view
            #print(str(results2)) #Use this for troubleshooting if information is not being displayed
            if len(results2) > 40:
                lookup.append(results2[3]+' | '+results2[0]+results2[1]+' | '+results2[7]+' | '+results2[5]+' | '+results2[9]+' | '+results2[11])#print html selection from the array, results/results2 is an array
            
            elif len(results2) >= 30:
                lookup.append(results2[3]+' | '+results2[0]+''+results2[1]+' | '+results2[5]+' | '+results2[9]+' | '+results2[13]+' | '+results2[15]) 

            #elif len(results2) <= 40:
            #    lookup.append(results2[0]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8]+' | '+results2[10]+' | '+results2[12]) 
            
            elif len(results2) > 11:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8]+' | '+results2[10]+' | '+results2[11])
            
            elif len(results2) > 10:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8]+' | '+results2[10])

            elif len(results2) > 4:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[4])

            elif len(results2) == 4:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[3])
            
            elif len(results2) == 0:
                lookup.append(u+' Nothing Found! Trying pinging the host and looking up that IP')
            

            
req = robtex(sys.argv[1:]) #allows the use of arguments in robtex script
#req = robtex(input('Place your ip address here: ')) #take user input and assign it to robtex class which is passed to arg ip
req.get() #runs get function with req assigned arg

for l in lookup: #looping through the lookup array
    print(l) #print individual lookups