from bs4 import BeautifulSoup
import requests
import json
import re
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


iplookup = [] #list of robtex urls used to search ips
urllookup = []
lookup = [] #list of lookup responses

class robtex:
    def __init__(self, argv): ##init which assigned the output from req to ip
        self.ip = argv #take value of ip which is input from req and assigns it to self.ip
        for i in self.ip: #loop to pull ip arguments
            if re.match(r"[\d\.]+",i) is not None: #This regex searches for IP address format and will return the ip, if not it will go to the else statement on 21
                self.url = 'https://www.robtex.com/ip-lookup/{}'.format(i) #robtex url to search with the ip from self.ip in the url to search
                iplookup.append(self.url) #appends robtex url with ips to search to the urls list
            else:
                self.url = 'https://www.robtex.com/ip-lookup/{}'.format(i) #robtex url to search with the ip from self.ip in the url to search
                urllookup.append(self.url) #appends robtex url with ips to search to the urls list



    def get(self):
        for i in iplookup: #loop to go through urls in the urls list
            response = requests.get(i, verify=False) #get request to completed robtex url from above
            soup = BeautifulSoup(response.text, 'html.parser')  #use Beautifulsoup's html parser for the output and assign that to soup
            results = soup.find_all('div', class_='dns')    #take html output from soup, find all div sets, under the class dns(this is all found from the html output itself)
            results2 = re.findall(r"(?<=\>)[\w\.\-\,\(\)\s\/]+(?!\<\/b)", str(results), re.M|re.I) #regex find all non-html data we want to view
            if len(results2) >= 13:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[4]+' | '+results2[8]+' | '+results2[12])
            elif len(results2) == 12:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8]+' | '+results2[10]) 
            elif len(results2) == 11:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8]+' | '+results2[10]) 
            elif len(results2) == 10:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8])
            elif len(results2) == 9:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8])
            elif len(results2) == 8:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[4]+' | '+results2[6])
            elif len(results2) == 7:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[4]+' | '+results2[6])
            elif len(results2) == 6:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[4])
            elif len(results2) == 5:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[4])
            elif len(results2) == 4:
                lookup.append(results2[0]+' | '+results2[2]+' | '+results2[3])
            elif len(results2) == 3:
                lookup.append(results2[0]+' | '+results2[2])
            elif len(results2) == 2:
                lookup.append(results2[0]+' | '+results2[1])
            elif len(results2) == 1:
                lookup.append(results2[0])
            elif len(results2) == 0:
                lookup.append(i+' Nothing Found! Trying pinging the host and looking up that IP')

        for u in urllookup: #loop to go through urls in the urls list
            response = requests.get(u, verify=False) #get request to completed robtex url from above
            soup = BeautifulSoup(response.text, 'html.parser')  #use Beautifulsoup's html parser for the output and assign that to soup
            results = soup.find_all('div', class_='dns')    #take html output from soup, find all div sets, under the class dns(this is all found from the html output itself)
            results22 = re.findall(r"(?<=\>)[\w\.\-\,\(\)\d\s\/]+", str(results), re.M|re.I) #regex find all non-html data we want to view
            results2 = re.findall(r"[\w\.\-\,\s\.]{3,}",str(results22), re.I|re.M)
            if len(results2) > 14:
                lookup.append(results2[0]+results2[1]+' | '+results2[2]+' | '+results2[4]+' | '+results2[8]+' | '+results2[12]+' | '+results2[14]+' | '+results2[15])
            elif len(results2) == 14:
                lookup.append(results2[0]+results2[1]+' | '+results2[2]+' | '+results2[4]+' | '+results2[8]+' | '+results2[12])
            elif len(results2) == 13:
                lookup.append(results2[0]+results2[1]+' | '+results2[2]+' | '+results2[4]+' | '+results2[8]+' | '+results2[12])
            elif len(results2) == 12:
                lookup.append(results2[0]+results2[1]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8]+' | '+results2[10]) 
            elif len(results2) == 11:
                lookup.append(results2[0]+results2[1]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8]+' | '+results2[10]) 
            elif len(results2) == 10:
                lookup.append(results2[0]+results2[1]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8])
            elif len(results2) == 9:
                lookup.append(results2[0]+results2[1]+' | '+results2[2]+' | '+results2[6]+' | '+results2[8])
            elif len(results2) == 8:
                lookup.append(results2[0]+results2[1]+' | '+results2[2]+' | '+results2[4]+' | '+results2[6])
            elif len(results2) == 7:
                lookup.append(results2[0]+results2[1]+' | '+results2[2]+' | '+results2[4]+' | '+results2[6])
            elif len(results2) == 6:
                lookup.append(results2[0]+results2[1]+' | '+results2[2]+' | '+results2[4])
            elif len(results2) == 5:
                lookup.append(results2[0]+results2[1]+' | '+results2[2]+' | '+results2[4])
            elif len(results2) == 4:
                lookup.append(results2[0]+results2[1]+' | '+results2[2]+' | '+results2[3])
            elif len(results2) == 3:
                lookup.append(results2[0]+results2[1]+' | '+results2[2])
            elif len(results2) == 2:
                lookup.append(results2[0]+results2[1])
            elif len(results2) == 1:
                lookup.append(results2[0])
            elif len(results2) == 0:
                lookup.append(u+' Nothing Found! Trying pinging the host and looking up that IP')
  
            

            
req = robtex(sys.argv[1:]) #allows the use of arguments in robtex script
#req = robtex(input('Place your ip address here: ')) #take user input and assign it to robtex class which is passed to arg ip
req.get() #runs get function with req assigned arg

for l in lookup: #looping through the lookup array
    print(l) #print individual lookups
