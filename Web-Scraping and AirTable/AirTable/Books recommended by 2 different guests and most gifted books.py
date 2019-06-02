from bs4 import BeautifulSoup as bs
import requests, requests.auth, json
import re
api_key =  "keyGP5NypsZdD6Jkf"
url_airtable = "https://api.airtable.com/v0/appZZ6noUeAtak1BR/Books"
#The URL and key have been mentioned
headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}
a =set()
r1 = requests.get(url_airtable, headers=headers)
d1 = r1.json()
#The data is loaded
url_airtable1 = "https://api.airtable.com/v0/appZZ6noUeAtak1BR/Books?offset="+d1['offset']
r2 = requests.get(url_airtable1, headers=headers)
d2 = r2.json()
#The data of the offset is also loaded
s = 0
k = 0
print("Here are the titles of all the books that have been recommended by more than one guest")
print("\n")
for book in d1['records']:
        if(len((book['fields']['Guest']))) >= 2:
                s = s+1
                print(str(s)+". "+str(book['fields']['Name']))
for book in d2['records']:
        if(len((book['fields']['Guest']))) >= 2:
                s = s+1
                print(str(s)+". "+str(book['fields']['Name']))
print("\n")
#The titles of the books recommended by two different guests has been printed by checking the the length of the "Guests" field
i = 0
m = "Most-gifted book" 
print("Here is the list of most gifted books","\n")
for book in d1['records']:
        a=set()
        for j in book['fields']:
                a.add(j)
        if m in a:
                k = k+1
                print(str(k)+". "+str(book['fields']['Name']))
for book in d2['records']:
        a=set()
        for j in book['fields']:
                a.add(j)
        if m in a:
                k = k+1
                print(str(k)+". "+str(book['fields']['Name']))
#The list of most gifted books is printed by iterating through the data