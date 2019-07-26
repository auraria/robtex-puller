# robtex-puller
This script is to pull data from robtex about an IP address or Domain to help analysts in getting information.

This is actively being dev-ed. please let me know if you run into any issues and provide the IP or URL.


REQUIREMENTS:
Python3

#IMPORTS:
bs4, json, requests, re, sys, urlib3

Example usage:

python robtex.py 92.118.37.26
92.118.37.26 | International Hosting Company | AS35606 | ON Telecoms NETBLOCK | Greece

python robtex.py google.com
2404:6800:4003:c02::8b | google.com | AS15169 | 48 | Google Google, Inc | Google
