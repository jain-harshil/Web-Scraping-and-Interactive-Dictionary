from bs4 import BeautifulSoup as bs
import requests, requests.auth, json
import re
import random
#The random library and other appropriate libraries have been loaded
api_key =  "keyGP5NypsZdD6Jkf"
url_airtable = " https://api.airtable.com/v0/appT8pFYcy0olYfPQ/Questions"
headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}
#The URL and key is mentioned
r1 = requests.get(url_airtable, headers=headers)
d1 = r1.json()
#The data is loaded
c = []
d = []
e = []
f = []
g = []
l = []
m = []
n = []
o = []
t = []
p = 0
q = 0
r = 0
s = 0
#Variables defined for future use
for b in d1['records']:
    if b['fields']['Topic'] == 'Basics':
        s = s+1
    if b['fields']['Topic'] == 'Functions':
        p = p+1
    if b['fields']['Topic'] == 'File Handling':
        q = q+1
    if b['fields']['Topic'] == 'Regular Expressions':
        r = r+1
#The list containing the various topics is created
for b in d1['records']:
    if b['fields']['Difficulty Level'] == 'Easy':
        c.append(b['fields']['Questions'])
    if b['fields']['Difficulty Level'] == 'Cakewalk':
        d.append(b['fields']['Questions'])
    if b['fields']['Difficulty Level'] == 'Medium':
        e.append(b['fields']['Questions'])
    if b['fields']['Difficulty Level'] == 'Hard':
        f.append(b['fields']['Questions'])
    if b['fields']['Difficulty Level'] == 'Challenging':
        g.append(b['fields']['Questions'])
    if b['fields']['Topic'] == 'Basics':
        l.append(b['fields']['Questions'])
    if b['fields']['Topic'] == 'Functions':
        m.append(b['fields']['Questions'])
    if b['fields']['Topic'] == 'File Handling':
        n.append(b['fields']['Questions'])
    if b['fields']['Topic'] == 'Regular Expressions':
        o.append(b['fields']['Questions'])
b1 = [val for val in c if val in l]
b2 = [val for val in c if val in m]
b3 = [val for val in c if val in n]
b4 = [val for val in c if val in o]
b5 = [val for val in d if val in l]
b6 = [val for val in d if val in m]
b7 = [val for val in d if val in n]
b8 = [val for val in d if val in o]
b9 = [val for val in e if val in l]
b10 = [val for val in e if val in m]
b11 = [val for val in e if val in n]
b12 = [val for val in e if val in o]
b13 = [val for val in f if val in l]
b14 = [val for val in f if val in m]
b15 = [val for val in f if val in n]
b16 = [val for val in f if val in o]
b17 = [val for val in g if val in l]
b18 = [val for val in g if val in m]
b19 = [val for val in g if val in n]
b20 = [val for val in g if val in o]
print("Here are the type and the number of questions available")
print("Easy and Basics: ",len(b1))
print("Easy and Functions: ",len(b2))
print("Easy and File Handling: ",len(b3))
print("Easy and Regular Expressions: ",len(b4))
print("Cakewalk and Basics: ",len(b5))
print("CakeWalk and Functions: ",len(b6))
print("CakeWalk and File Handling: ",len(b7))
print("CakeWalk and Regular Expressions: ",len(b8))
print("Medium and Basics: ",len(b9))
print("Medium and Functions: ",len(b10))
print("Medium and File Handling: ",len(b11))
print("Medium and Regular Expressions: ",len(b12))
print("Hard and Basics: ",len(b13))
print("Hard and Functions: ",len(b14))
print("Hard and File Handling: ",len(b15))
print("Hard and Regular Expressions: ",len(b16))
print("Challenging and Basics: ",len(b17))
print("Challenging and Functions: ",len(b18))
print("Challenging and File Handling: ",len(b19))
print("Challenging and Regular Expressions: ",len(b20))
print("Please enter the number of Easy questions of 'Basics' you want")
h1 = int(input())
print("Please enter the number of Easy questions of 'Functions' you want")
h2 = int(input())
print("Please enter the number of Easy questions of 'File Handling' you want")
h3 = int(input())
print("Please enter the number of Easy questions of 'Regular Expressions' you want")
h4 = int(input())
print("Please enter the number of Cakewalk questions of 'Basics' you want")
h5 = int(input())
print("Please enter the number of Cakewalk questions of 'Functions' you want")
h6 = int(input())
print("Please enter the number of Cakewalk questions of 'File Handling' you want")
h7 = int(input())
print("Please enter the number of Cakewalk questions of 'Regular Expressions' you want")
h8 = int(input())
print("Please enter the number of Medium questions of 'Basics' you want")
h9 = int(input())
print("Please enter the number of Medium questions of 'Functions' you want")
h10 = int(input())
print("Please enter the number of Medium questions of 'File Handling' you want")
h11 = int(input())
print("Please enter the number of Medium questions of 'Regular Expressions' you want")
h12 = int(input())
print("Please enter the number of Hard questions of 'Basics' you want")
h13 = int(input())
print("Please enter the number of Hard questions of 'Functions' you want")
h14 = int(input())
print("Please enter the number of Hard questions of 'File Handling' you want")
h15 = int(input())
print("Please enter the number of Hard questions of 'Regular Expressions' you want")
h16 = int(input())
print("Please enter the number of Challenging questions of 'Basics' you want")
h17 = int(input())
print("Please enter the number of Challenging questions of 'Functions' you want")
h18 = int(input())
print("Please enter the number of Challenging questions of 'File Handling' you want")
h19 = int(input())
print("Please enter the number of Challenging questions of 'Regular Expressions' you want")
h20 = int(input())
#Appropriate input is taken

random.shuffle(b1)
random.shuffle(b2)
random.shuffle(b3)
random.shuffle(b4)
random.shuffle(b5)
random.shuffle(b6)
random.shuffle(b7)
random.shuffle(b8)
random.shuffle(b9)
random.shuffle(b10)
random.shuffle(b11)
random.shuffle(b12)
random.shuffle(b13)
random.shuffle(b14)
random.shuffle(b15)
random.shuffle(b16)
random.shuffle(b17)
random.shuffle(b18)
random.shuffle(b19)
random.shuffle(b20)
#The list is shuffled randomly

ma = []
for i in range (h1):
    if h1<=len(b1):
        ma.append([b1[i]])
    else:
        print("Wrong input")
for i in range (h2):
    if h2<=len(b2):
            ma.append([b2[i]])
    else:
        print("Wrong input")
for i in range (h3):
    if h3<=len(b3):
            ma.append([b3[i]])
    else:
        print("Wrong input")
for i in range (h4):
    if h4<=len(b4):
            ma.append([b1[4]])
    else:
        print("Wrong input")
for i in range (h5):
    if h5<=len(b5):
            ma.append([b5[i]])
    else:
        print("Wrong input")
for i in range (h6):
    if h6<=len(b6):
            ma.append([b6[i]])
    else:
        print("Wrong input")
for i in range (h7):
    if h7<=len(b7):
            ma.append([b7[i]])
    else:
        print("Wrong input")
for i in range (h8):
    if h8<=len(b8):
            ma.append([b8[i]])
    else:
        print("Wrong input")
for i in range (h9):
    if h9<=len(b9):
            ma.append([b9[i]])
    else:
        print("Wrong input")
for i in range (h10):
    if h10<=len(b10):
            ma.append([b10[i]])
    else:
        print("Wrong input")
for i in range (h11):
    if h11<=len(b11):
            ma.append([b11[i]])
    else:
        print("Wrong input")
for i in range (h12):
    if h12<=len(b12):
            ma.append([b12[i]])
    else:
        print("Wrong input")
for i in range (h13):
    if h13<=len(b13):
            ma.append([b13[i]])
    else:
        print("Wrong input")
for i in range (h14):
    if h14<=len(b14):
            ma.append([b14[i]])
    else:
        print("Wrong input")
for i in range (h15):
    if h15<=len(b15):
            ma.append([b15[i]])
    else:
        print("Wrong input")
for i in range (h16):
    if h16<=len(b16):
            ma.append([b16[i]])
    else:
        print("Wrong input")
for i in range (h17):
    if h17<=len(b17):
            ma.append([b17[i]])
    else:
        print("Wrong input")
for i in range (h18):
    if h18<=len(b18):
            ma.append([b18[i]])
    else:
        print("Wrong input")
for i in range (h19):
    if h19<=len(b19):
            ma.append([b19[i]])
    else:
        print("Wrong input")
for i in range (h20):
    if h20<=len(b20):
            ma.append([b20[i]])
    else:
        print("Wrong input")
print(ma)
#The questions are printed

