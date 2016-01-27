text = open("text.txt").read().split()
'''
num_1 = 1
num_2 = 1
num_3 = 1
num_4 = 1
num_5 = 1
num_6 = 1
num_7 = 1
num_8 = 1
num_9 = 1
num_10 = 1

for i in range(len(text)):
    if text[i] == 'the':
        num_the += 1
        
for i in range (len(text.sort)):
    if text.sort[i] == text.sort[i + 1]:
        num_1 += 1
        continue
    elif text.sort[i] != text.sort[i + 1]:
        if text.sort[i + 1] == text.sort[i + 2]:
            num_2 += 1
    
    

'''
'''
text1 = sorted(text)

     
d = {}
for word in text1:
    if word in d:
        d[word] += 1
        continue
    else:
        d[word] = 1
sorted_d = sorted(d, key=d.get, reverse=True)
print(sorted_d)
#d_inv = {v: k for k, v in d.items()}

#d_sort = sorted(d_inv.items())

print(d_sort)

print(sorted_d[:10])

'''
'''
a = {}
a['hi'] = 1
a
{'hi': 1}
a['hi'] += 1
a
{'hi': 2}




inv_freq = {6: "the", 12: "a", 1:"hi"}
print(sorted(inv_freq.items()))
'''


#Q3

def my_count(s1, s2):
    num_s2 = 0
    while s1.find(s2) != -1:
    #for c in s1:
        i = s1.find(s2)
        s1 = s1[(i+len(s2)):]
        num_s2 += 1
        
    return num_s2 
'''def my_count(s1, s2):
    num_s2 = 0
    for i in range(s1):
        if s1.find(s2) != -1:
    #for c in s1:
            i = s1.find(s2)
            s1 = s1[(i):]
            num_s2 += 1
            continue
    return num_s2 

print(my_count('heateateateat', 'eat'))
        
   
 

def my_count(s1, s2):
    for c in s1:
        if c.isalpha():
            if s1(c) == s2.find(c):
            





'''

#Q2

names = []
words = text

for i in (len(words)):
    excluded_names_list = ['Mr','Mrs','Miss','I']
    if words[i] not in names and words[i] == words[i].capitalize and words[i] not in excluded_names_list:
        if  ((i > 0 and words[i+1] == 'said') or (i < len(words) and words[i] == 'walked')):
            names.append(words[i])

'''new_list = []
for j in names:
    if j != 'Mr' or 'Mrs' or 'Miss':
        new_list.appned(j)
    return new_list'''

    
print(new_list)