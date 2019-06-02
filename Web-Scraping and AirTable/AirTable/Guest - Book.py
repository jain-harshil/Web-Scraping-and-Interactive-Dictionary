from bs4 import BeautifulSoup as bs
import requests, requests.auth, json
import re
from difflib import get_close_matches

f = str(input())
url_airtable1 = "https://api.airtable.com/v0/appZZ6noUeAtak1BR/Guests"
url_airtable2 = "https://api.airtable.com/v0/appZZ6noUeAtak1BR/Books"
api_key = "keyGP5NypsZdD6Jkf"
#The URL and key have been mentioned
a = []
#Empty list defined for further use
headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}

r1 = requests.get(url_airtable1, headers=headers)
r2 = requests.get(url_airtable2, headers=headers)
data1 = r1.json()
data2 = r2.json()
#The data has been loaded from the website
url_airtable3 = "https://api.airtable.com/v0/appZZ6noUeAtak1BR/Books?offset="+data2['offset']
r3 = requests.get(url_airtable3, headers=headers)
data3 = r3.json()
#The offset data is also loaded corresponding to its URL
for guest in data1['records']:
	a.append(guest['fields']['Name'])
#The list of names of guests has been created
b = get_close_matches(f,a)
if f not in a:
        f = b
if f not in a:
    s = 0
    if len(f) == 0:
        print("The guest name entered is incorrect")
#An error is thrown if the guest name entered is incorrect
    else:
        for i in range (len(f)):
            print((str(i+1)+". "),f[i])
#The lists of the guests is printed
        print("Enter the number of the Guest which you expected")
        y = int(input())
        g = f[y-1]
        print("Here is the list of books recommended by the Guest")
        for i in data1["records"]:
            if(i["fields"]["Name"]==g):
                m=i['id']
        for j in data2['records']:
            if(m in j['fields']['Guest']):
                s = s+1
                print(str(s)+". "+str(j["fields"]["Name"]))
        for j in data3['records']:
            if(m in j['fields']['Guest']):
                s = s+1
                print(str(s)+". "+str(j["fields"]["Name"]))
#The list of books recommended by the guest is printed by iterating through the data loaded
elif f in a:
        s = 0
        print("Here is the List of Books recommended by the Guest")
        for i in data1["records"]:
                if(i["fields"]["Name"]==f):
                        m=i['id']
        for j in data2['records']:
                if(m in j['fields']['Guest']):
                        s = s+1
                        print(str(s)+". "+j["fields"]["Name"])
        for j in data3['records']:
                if(m in j['fields']['Guest']):
                        s = s+1
                        print(str(s)+". "+j["fields"]["Name"])
#The list of books recommended by the guest is printed by iterating through the offset data loaded