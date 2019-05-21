from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
from pattern.en import singularize
# to search 
#query = input()
query="Swine flu vaccine"
title = []
result = []
link = ""
curr_result = ""
f = open("output2.txt","w")
i=0
total1 = ""
total2 = ""
for j in search(query, tld="com", num=15, start=0, stop=14, pause=2):
    url = j
    print(url)
    page = requests.get(url)
    if not page:
        continue
    soup = BeautifulSoup(page.content)
    para = soup.find_all('p')
    titl = soup.find_all('title')
    text2 = ""
    text=""
    for a in para:
        temp = a.get_text()
        temp = re.sub(r'[^\w]', '', temp)
        text = text + temp
        text = text + " "
    for a in titl:
        temp = a.get_text()
        temp = re.sub(r'[^\w]', '', temp)
        text2 = text2 + temp
        text2 = text2 + " "
    #re.sub(r'[^\w]', ' ', text)
    #re.sub(r'[^\w]', ' ', text2)
    result.append(text)
    title.append(text2)
    total1 = total1 + text
    total2 = total2 + text2
    total1 = total1 + " "
    total2 = total2 + " "
    i=i+1
    if i==1:
        f1 = open("document1.txt","w")
        text = re.sub(r'[^\w]', '', text)
        text2 = re.sub(r'[^\w]', '', text2)
        f1.write(text2)
        f1.write(text)
    
    if i==2:
        f1 = open("document2.txt","w")
        f1.write(text2)
        f1.write(text)
    
    if i==3:
        f1 = open("document3.txt","w")
        f1.write(text2)
        f1.write(text)
    
    if i==4:
        f1 = open("document4.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==5:
        f1 = open("document5.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==6:
        f1 = open("document6.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==7:
        f1 = open("document7.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==8:
        f1 = open("document8.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==9:
        f1 = open("document9.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==10:
        f1 = open("document10.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==11:
        f1 = open("document11.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==12:
        f1 = open("document12.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==13:
        f1 = open("document13.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==14:
        f1 = open("document14.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==15:
        f1 = open("document15.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==16:
        f1 = open("document16.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==17:
        f1 = open("document17.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==18:
        f1 = open("document18.txt","w")
        f1.write(text2)
        f1.write(text)
        
    if i==19:
        f1 = open("document19.txt","w")
        f1.write(text2)
        f1.write(text)
    
    if i==20:
        f1 = open("document20.txt","w")
        f1.write(text2)
        f1.write(text)
#
total1 = re.sub(r'[^\w]', ' ', total1)
total2 = re.sub(r'[^\w]', ' ', total2)

f.write(total1)
f.write(total2)
#Coverting to Seperate Words
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
path = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/output2.txt"
line = ""
with open(path) as f:
    line = f.readline()
    line=line.split(" ")
    line = [word.lower() for word in line if word not in [""," "]]
filtered_words = [word for word in line if word not in stopwords.words('english')]
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/words.txt"

with open(writepath, 'w') as f:
    for i in filtered_words:
	    f.write("%s\n" % singularize(i))
f.close()

writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/query.txt"
with open(writepath, 'w') as f:
    f.write(query)
f.close()
