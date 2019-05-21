# -*- coding: utf-8 -*-
from nltk.corpus import stopwords
import nltk
import re
import string
import pattern
nltk.download('stopwords')
from pattern.en import singularize
class docs:
    def __init__(self,doc_name,n):
        self.freq={}
        path = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/"+doc_name
        line = ""
        with open(path) as f:
            line = f.readline()
            line=line.split(" ")
            line = [word.lower() for word in line if word not in [""," "]]
        stop_words = set(stopwords.words('english'))
        new_stopwords = ['also','may','must','since','could','whether']
        new_stopwords_list = stop_words.union(new_stopwords)
        filtered_words = [word for word in line if word not in new_stopwords_list]
        writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/words" + str(n) + ".txt"
        with open(writepath, 'w') as f:
            for i in filtered_words:
                #print(i)
                i = re.sub(r'[^\w]', '', i)
                count = self.freq.get(singularize(i),0)
                self.freq[singularize(i)] = count + 1
                #f("%s\n" % i)
                f.write(singularize(i)+"\n")
        f.close()
obj_array = []
temp = "document"
for i in range(15):
    doc_name = temp + str(i+1) + ".txt"
    obj_array.append(docs(doc_name,i+1))
#Applying KNN on 1st Word:


list_of_final_words = []

                            #-----KNN BASED SCORING-----#
words_list = []
new_score = {}
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/Score1.txt"
with open(writepath, 'r') as f:
    for w in f:
        st1,st2 = w.split()
        st =  st1
        words_list.append(st)

                            #-----1 Round of KNN-----#
path = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/Score1.txt"
f_word=""
f_score=0
i=0
with open(path) as f:
    for w in f:
        #print(w)
        i=i+1
        if i==1:
            break
f_word,f_score = w.split()
#new_score[f_word]=float(f_score)
list_of_final_words.append(f_word)
# f_word is top word of Score1 file
# f_score is score of top most word
import math
def fun(word,j):
    if not word in obj_array[j].freq.keys():
        return 0
    a=obj_array[j].freq[word]
    if a==0:
        return 0
    c=a
    b=len(obj_array[j].freq.keys())
    tot_words=0
    for key, value in obj_array[j].freq.items() :
        tot_words = tot_words +value
    a = (a)/(tot_words+0.0)
    b=math.log((b+0.0)/(c))
    return (a*b)
i=1
while i<len(words_list):
    word1 = words_list[0]
    word2 = words_list[i]
    j=0
    num=0
    den1=0
    den2=0
    while j<15:
        num = num + fun(word1,j)*fun(word2,j)
        den1 = den1 + fun(word1,j)*fun(word1,j)
        den2 = den2 + fun(word2,j)*fun(word2,j)
        j = j + 1
    den = math.sqrt(den1*den2)
    if den==0:
            new_score[word2]=0
    else:
        new_score[word2]=(num + 0.0)/(den + 0.0)
    #print(new_score[word2])
    i = i + 1
knn1_list = []
new_score = [(k, new_score[k]) for k in sorted(new_score, key=new_score.get, reverse=True)]
for key in new_score:
    knn1_list.append(key)
knn1_list = knn1_list[:-350]
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN1.txt"
with open(writepath, 'w') as f:
    for words in knn1_list:
        a,b = words
        f.write("%s %f\n" % (a,  b))
        #print(words)
f.close()


                                #-----2 Round of KNN-----#
words_list = []
new_score = {}
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN1.txt"
with open(writepath, 'r') as f:
    for w in f:
        st1,st2 = w.split()
        st =  st1
        words_list.append(st)
        
        

path = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN1.txt"
f_word=""
f_score=0
i=0
with open(path) as f:
    for w in f:
        i=i+1
        if i==1:
            break

f_word,f_score = w.split()
#new_score[f_word]=float(f_score)
list_of_final_words.append(f_word)
# f_word is top word of Score1 file
# f_score is score of top most word
i=1
while i<len(words_list):
    word1 = words_list[0]
    word2 = words_list[i]
    j=0
    num=0
    den1=0
    den2=0
    while j<15:
        num = num + fun(word1,j)*fun(word2,j)
        den1 = den1 + fun(word1,j)*fun(word1,j)
        den2 = den2 + fun(word2,j)*fun(word2,j)
        j = j + 1
    den = math.sqrt(den1*den2)
    if den==0:
            new_score[word2]=0
    else:
        new_score[word2]=(num + 0.0)/(den + 0.0)
    #print(new_score[word2])
    i = i + 1
knn1_list= []
new_score = [(k, new_score[k]) for k in sorted(new_score, key=new_score.get, reverse=True)]
for key in new_score:
    knn1_list.append(key)
knn1_list = knn1_list[:-350]
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN2.txt"
with open(writepath, 'w') as f:
    for words in knn1_list:
        a,b = words
        f.write("%s %f\n" % (a,  b))
        #print(words)
f.close()



                                 #-----3 Round of KNN-----#


words_list = []
new_score = {}
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN2.txt"
with open(writepath, 'r') as f:
    for w in f:
        st1,st2 = w.split()
        st =  st1
        words_list.append(st)
        
        

path = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN2.txt"
f_word=""
f_score=0
i=0
with open(path) as f:
    for w in f:
        i=i+1
        if i==1:
            break

f_word,f_score = w.split()
#new_score[f_word]=float(f_score)
list_of_final_words.append(f_word)
# f_word is top word of Score1 file
# f_score is score of top most word
i=1
while i<len(words_list):
    word1 = words_list[0]
    word2 = words_list[i]
    j=0
    num=0
    den1=0
    den2=0
    while j<15:
        num = num + fun(word1,j)*fun(word2,j)
        den1 = den1 + fun(word1,j)*fun(word1,j)
        den2 = den2 + fun(word2,j)*fun(word2,j)
        j = j + 1
    den = math.sqrt(den1*den2)
    if den==0:
            new_score[word2]=0
    else:
        new_score[word2]=(num + 0.0)/(den + 0.0)
    #print(new_score[word2])
    i = i + 1
knn1_list= []
new_score = [(k, new_score[k]) for k in sorted(new_score, key=new_score.get, reverse=True)]
for key in new_score:
    knn1_list.append(key)
knn1_list = knn1_list[:-350]
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN3.txt"
with open(writepath, 'w') as f:
    for words in knn1_list:
        a,b = words
        f.write("%s %f\n" % (a,  b))
        #print(words)
f.close()


                                 #-----4 Round of KNN-----#


words_list = []
new_score = {}
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN3.txt"
with open(writepath, 'r') as f:
    for w in f:
        st1,st2 = w.split()
        st =  st1
        words_list.append(st)
        
        

path = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN3.txt"
f_word=""
f_score=0
i=0
with open(path) as f:
    for w in f:
        i=i+1
        if i==1:
            break

f_word,f_score = w.split()
#new_score[f_word]=float(f_score)
list_of_final_words.append(f_word)
# f_word is top word of Score1 file
# f_score is score of top most word
i=1
while i<len(words_list):
    word1 = words_list[0]
    word2 = words_list[i]
    j=0
    num=0
    den1=0
    den2=0
    while j<15:
        num = num + fun(word1,j)*fun(word2,j)
        den1 = den1 + fun(word1,j)*fun(word1,j)
        den2 = den2 + fun(word2,j)*fun(word2,j)
        j = j + 1
    den = math.sqrt(den1*den2)
    if den==0:
            new_score[word2]=0
    else:
        new_score[word2]=(num + 0.0)/(den + 0.0)
    #print(new_score[word2])
    i = i + 1
knn1_list= []
new_score = [(k, new_score[k]) for k in sorted(new_score, key=new_score.get, reverse=True)]
for key in new_score:
    knn1_list.append(key)
knn1_list = knn1_list[:-350]
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN4.txt"
with open(writepath, 'w') as f:
    for words in knn1_list:
        a,b = words
        f.write("%s %f\n" % (a,  b))
        #print(words)
f.close()


                                 #-----5 Round of KNN-----#


words_list = []
new_score = {}
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN4.txt"
with open(writepath, 'r') as f:
    for w in f:
        st1,st2 = w.split()
        st =  st1
        words_list.append(st)
        
        

path = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN4.txt"
f_word=""
f_score=0
i=0
with open(path) as f:
    for w in f:
        i=i+1
        if i==1:
            break

f_word,f_score = w.split()
#new_score[f_word]=float(f_score)
list_of_final_words.append(f_word)
# f_word is top word of Score1 file
# f_score is score of top most word
i=1
while i<len(words_list):
    word1 = words_list[0]
    word2 = words_list[i]
    j=0
    num=0
    den1=0
    den2=0
    while j<15:
        num = num + fun(word1,j)*fun(word2,j)
        den1 = den1 + fun(word1,j)*fun(word1,j)
        den2 = den2 + fun(word2,j)*fun(word2,j)
        j = j + 1
    den = math.sqrt(den1*den2)
    if den==0:
            new_score[word2]=0
    else:
        new_score[word2]=(num + 0.0)/(den + 0.0)
    #print(new_score[word2])
    i = i + 1
knn1_list= []
new_score = [(k, new_score[k]) for k in sorted(new_score, key=new_score.get, reverse=True)]
for key in new_score:
    knn1_list.append(key)
knn1_list = knn1_list[:-350]
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN5.txt"
with open(writepath, 'w') as f:
    for words in knn1_list:
        a,b = words
        list_of_final_words.append(a)
        f.write("%s %f\n" % (a,  b))
        #print(words)
f.close()




                               #-----Query Scoring-----#

#print(len(list_of_final_words))
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/query.txt"
query_words=[]
with open(writepath, 'r') as f:
    qq=f.read()
f.close()
query_words=qq.split()

#
#
#

query_list = []
new_score = {}
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/KNN5.txt"
with open(writepath, 'r') as f:
    for w in f:
        st1,st2 = w.split()
        st =  st1
        query_list.append(st)
        #print(query_list)
        
        


q_score={}
for word1 in list_of_final_words:
    sum=0.0
    #print(word1)
    for word2 in query_words:
        j=0
        while j<15:
            sum=sum+fun(word1,j)*fun(word2,j)
            j=j+1
    q_score[word1]=(sum+0.0)/(len(query_words)+0.0)
    #print(q_score[word1])
    #print(len(q_score))


query_score= []
q_score = [(k, q_score[k]) for k in sorted(q_score, key=q_score.get, reverse=True)]
for key in q_score:
    query_score.append(key)
    #print(query_score)
    #print(len(query_score))

writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/query1_score.txt"
with open(writepath, 'w') as f:
    for words in query_score:
        a,b = words
        f.write("%s %f\n" % (a,  b))
        #print(words)
f.close()



###---------------------------------------------------------------Scoring Sentences----------------------------

sentences_list = []
new_score = {}
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/query1_score.txt"
with open(writepath, 'r') as f:
    for w in f:
        st1,st2 = w.split()
        st =  st1
        sentences_list.append(st)
        #print(sentences_list)



#
from nltk.tokenize import sent_tokenize,word_tokenize
temp="document"
temp1="Summary_doc"
i=0
string=[[]*10 for x in xrange(15)]
for i in range(15):
    new_line_score={}
    document_name=temp+str(i+1)+".txt"
    summary_document_name=temp1+str(i+1)+".txt"
    writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/"+document_name
    new_line_score={}
    with open(writepath, 'r') as f:
        line=f.read().decode('utf-8')
        m=sent_tokenize(line)
        for line in m:
            #print line
            w=word_tokenize(line)
            sum=0.0
            for word2 in w:
                path = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/query1_score.txt"
                with open(path, 'r') as f1:
                    for ww in f1:
                        word1,score = ww.split()
                        #print(ww)
                        #print(word1)
                        if word2==word1:
                            sum=sum+float(score)
                            #print sum
                f1.close()
            new_line_score[line]=sum+0.0
        #print new_line_score
    f.close()
    #print new_line_score
    #import sys
    #reload(sys)
    #sys.setdefaultencoding('utf-8')
    import io
    summary_score= []
    new_line_score = [(k, new_line_score[k]) for k in sorted(new_line_score, key=new_line_score.get, reverse=True)]
    for key in new_line_score:
        summary_score.append(key)

    j=1
    for key1 in summary_score:
        line1,score1 = key1
        f=1
        k=1
        for key2 in summary_score:
            line2,score2 = key2
            if score1==score2 and j!=k:
                if len(line1)<len(line2):
                    #print line1,len(line1)
                    summary_score.remove(key2)
                    f=0
                    break
                else:
                    #print line2,len(line2)
                    summary_score.remove(key1)
                    f=0
                    break
            k=k+1
        #if f==1:
            #print line1,len(line1)
        j = j+1
    summary_score = summary_score[:10]
    #print summary_score
    writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/"+summary_document_name
    with io.open(writepath, 'w',encoding='utf8') as f2:
        for line in summary_score:
            a,b = line
            f2.write("%s %f\n" % (a,  b))
            string[i].append(a)
            #print(line)
    f2.close()
#print string[2][5]
        
    

    
                    
#-----------------------------------------------------------------------------------------------------


