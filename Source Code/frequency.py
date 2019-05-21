import re
frequency = {}
document_text = open('C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/new_word_file.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = []
for w in sorted(frequency, key=frequency.get, reverse=True):
    frequency_list.append(w)
#frequency_list = frequency.keys()
 
#for words in frequency_list:
    #print(words, frequency[words])
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/FreqW.txt"
total_words=0
with open(writepath, 'w') as f:
    for words in frequency_list:
        total_words = total_words + frequency[words]
        f.write("%s %d\n" % (words,  frequency[words]))
f.close()
#-----SCORING OF CANDIDATE EXPANSION TERMS-----#
total_distinct_words = len(frequency)
words_score_step_1={}
document_text = open('C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/FreqW.txt', 'r')
text_string = document_text.read().lower()
text_string = re.findall(r'\b[a-z]{3,15}\b', text_string)
import math 
for word in text_string:
    curr_score =0.0+(frequency[word])*(math.log((total_distinct_words+0.0)/(frequency[word])))
    words_score_step_1[word] =0.0 + (curr_score+0.0)/(total_words+0.0)
    print(curr_score/total_words)
    
    
score_list = []
for w in sorted(words_score_step_1, key=words_score_step_1.get, reverse=True):
    score_list.append(w)
    
writepath = "C:/Users/ARKAZA KUMARI/Desktop/Mini Project/Mini Project/Source Code/Score1.txt"
with open(writepath, 'w') as f:
    for words in words_score_step_1:
        f.write("%s %f\n" % (words,  words_score_step_1[words]))
f.close()
