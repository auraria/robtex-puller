# robtex-puller
This script is to pull data from robtex about an IP address or Domain to help analysts in getting information.
This supports multiple IPs.

This is actively being dev-ed. please let me know if you run into any issues and provide the IP or URL.


# REQUIREMENTS:
Python3

# IMPORTS:
bs4, json, requests, re, sys, urlib3

# Example usage:

python robtex.py 92.118.37.26

92.118.37.26 | International Hosting Company | AS35606 | ON Telecoms NETBLOCK | Greece

python robtex.py google.com

2404:6800:4003:c02::8b | google.com | AS15169 | 48 | Google Google, Inc | Google


robtex.py 103.133.108.72 81.22.45.62 192.168.2.56 141.98.81.52 61.177.172.32 218.92.0.31 185.143.221.29 92.118.37.26 104.206.128.23 185.200.118.18 112.85.42.16 185.176.27.16 68.183.83.16 139.220.192.14 178.62.42.14 185.137.233.14 103.114.107.12 103.89.91.12 187.115.165.12 178.128.214.11

103.133.108.72 | Vcloud service limited company K1, Villiage 2, Thach Da, Me Linh, Hanoi | 22

81.22.45.62 | To determine the registration information for a more specific range, please try a more specific query. If you see this object as a result of a single IP query, it means the IP address is currently in the free pool of address space managed by the RIPE NCC. | AS49505 | Mirror Image Internet -European IP Space | United Kingdom

192.168.2.56 | Internet Assigned Numbers Authority (IANA) | EMBRATEL

141.98.81.52 | Cloud VDS Network | 24

61.177.172.32 | CHINANET jiangsu province network China Telecom A12,Xin-Jie-Kou-Wai Street Beijing 100088 | AS4134 | CHINANET-BACKBONE No.31,Jin-rong Street | China Telecom | location

218.92.0.31 | CHINANET jiangsu province network China Telecom A12,Xin-Jie-Kou-Wai Street Beijing 100088 | AS4134 | CHINANET-BACKBONE No.31,Jin-rong Street | China Telecom | location

185.143.221.29 | To determine the registration information for a more specific range, please try a more specific query. If you see this object as a result of a single IP query, it means the IP address is currently in the free pool of address space managed by the RIPE NCC. | AS49505 | INFORMATION TECHNOLOGIES LLC | United Kingdom

92.118.37.26 | International Hosting Company | AS35606 | ON Telecoms NETBLOCK | Greece

104.206.128.23 | AAA Enterprises (AE-1218) | AS62904 | SH-2 | Henderson, United States

185.200.118.18 | M247 LTD London Infrastructure | 24

112.85.42.16 | China Unicom Jiangsu province network China Unicom | AS4837 | CHINA169-Backbone CNCGROUP China169 Back | CMI IP Transit | location

185.176.27.16 | To determine the registration information for a more specific range, please try a more specific query. If you see this object as a result of a single IP query, it means the IP address is currently in the free pool of address space managed by the RIPE NCC. | 24

68.183.83.16 | DigitalOcean, LLC (DO-13) | AS14061 | DSLExtreme Network 16 | Reseda, United States

139.220.192.14 | Pacnet Business Solutions LTD Block B Zondy Digital Building Keyuan Road South Nanshan District, Shenzhen, Guangdong, China | AS17638 | CHINATELECOM-TJ-AS-AP ASN for TIANJIN Pr | PBSL&amp;apos;s IP | location

178.62.42.14 | DigitalOcean London | AS14061 | DOSFO DigitalOcean SF Region | Sirius route | location

185.137.233.14 | To determine the registration information for a more specific range, please try a more specific query. If you see this object as a result of a single IP query, it means the IP address is currently in the free pool of address space managed by the RIPE NCC. | Alliance enterprise network

103.114.107.12 | Son Thuy Investment Trading and Service Company Limited Village 1, Thanh Ha, Nam Son, Soc Son, Hanoi | 22

103.89.91.12 | ETC Viet Nam development technology company limited Xa Khuc, Chu Phan, Me Linh, HaNoi | AS135905 | ETC-VN | Hanoi, Vietnam

187.115.165.12 | xd4NICA BRASIL S.A | AS18881 |   | GVT - Global Village Telecom | location

178.128.214.11 | To determine the registration information for a more specific range, please try a more specific query. If you see this object as a result of a single IP query, it means the IP address is currently in the free pool of address space managed by the RIPE NCC. | AS14061 | FORTHnet SA address block | Athens, Greece
