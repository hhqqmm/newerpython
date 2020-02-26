import requests
URL = 'http://172.17.50.43/varsity/'
r = requests.get(URL)
print(r.text)
print("Status code:")
print("\t*", r.status_code)
#headers
h = requests.head(URL)
print("Header:")
print("********")
#print line by line
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("********")

#This Will modify header user-agent
headers = {
    'User-Agent' : 'Iphone 8'
}
#Test it on an external site
URL2 = 'http://httpbin.org/headers'
rh = requests.get(URL2, headers=headers)
print(rh.text)
