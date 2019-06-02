from bs4 import BeautifulSoup as bs
import requests, requests.auth, json
import re
import datetime
import time
#All libraries required have been imported
print("Please enter the start_date in YYYY-MM-DD format")
a = str(input())
print("Please enter the end_date in YYYY-MM-DD format")
b = str(input())
#An input is taken in the appropriate format

url_airtable = " https://api.airtable.com/v0/appN4MSVPspT61ZEc/Talks"
api_key = "keyGP5NypsZdD6Jkf"
#The URL and key have been mentioned
c = []
e = []
f = []
g = []
#Empty list defined for future purpose
m = 0
headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}

r = requests.get(url_airtable, headers=headers)
data = r.json()
#The data corresponding to the URL has been loaded
url_airtable1 = " https://api.airtable.com/v0/appN4MSVPspT61ZEc/Talks?offset="+data['offset']
r1 = requests.get(url_airtable1, headers=headers)
data1 = r1.json()
#The data corresponding to the offset data has been loaded

for book in data['records']:
	c.append(book['fields']['Date'][0:10])
for book in data1['records']:
	c.append(book['fields']['Date'][0:10])
#A list is created containing all dates
d1 = datetime.date(int(a[0:4]),int(a[5:7]),int(a[8:10]))
d2 = datetime.date(int(b[0:4]),int(b[5:7]),int(b[8:10]))
#The dates are converted into datetime format
i = str(d1<=d2)
n=0
if i == "True":
        for i in range (len(c)):
                d3 = datetime.date(int(c[i][0:4]),int(c[i][5:7]),int(c[i][8:10]))
                e.append(d3)
        s = 0
        for book in data['records']:
                d4 = datetime.date(int(book['fields']['Date'][0:4]),int(book['fields']['Date'][5:7]),int(book['fields']['Date'][8:10]))
                d7 = book['fields']['Date'][0:10]
                d5 = d4>=d1
                d6 = d4<=d2
                d5 = str(d5)
                d6 = str(d6)
                #The two dates given as the input are compared
                if d5 == "True" and d6 == "True" and d7 in book['fields']['Date'][0:10]:
                        n=n+1
                        if n==1:
                                 print("Here is the list of the titles of all the talks that happened between the two dates")
                        s = s+1
                        print(str(s)+". "+str(book['fields']['FullTitle']))
                #The titles of all talks are printed by making use of date time object
        for book in data1['records']:
                d4 = datetime.date(int(book['fields']['Date'][0:4]),int(book['fields']['Date'][5:7]),int(book['fields']['Date'][8:10]))
                d7 = book['fields']['Date'][0:10]
                d5 = d4>=d1
                d6 = d4<=d2
                d5 = str(d5)
                d6 = str(d6)
                #The two dates given as input are compared
                if d5 == "True" and d6 == "True" and d7 in book['fields']['Date'][0:10]:
                        n=n+1
                        if n==1:
                                 print("Here is the list of the titles of all the talks that happened between the two dates")
                        s = s+1
                        print(str(s)+". "+str(book['fields']['FullTitle']))
                #The titles of all books are printed by making use of date time object
        if s == 0:
                print("No talk took place between these dates")
                #An appropriate message is thrown if no talk took place between the mentioned dates
else:
        print("Start_date cannot be after end_date")
        #An appropriate error is thrown if start date is before the end date
