print("#Question 1")

def find_lol(file):
    text = open(file).read().split("\n")
    print(text)
    lis = []
    lis2 = []
    for i in range(len(text)):
        lis2.append(text[i].lower())
    
        if "lol" in lis2[i]:
            lis.append(text[i])

    return lis
    
    
print(find_lol("data2.txt"))

print("#Question 2")

d = { 1:2, 5:"fgd", 7:34}

def dict_to_str(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a space. Each key-value pair is separated
    by a comma.
    For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".
    """
    
    temp = ""
    for c in d:
        temp += str(c) + "," + str(d[c]) + "\n"
        
    return temp


print(dict_to_str(d))

print("#Question 3")

d = {5:"fgd", 7:34, 1:2, 3:"dfhgdf"}

def dict_to_str_sorted(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a space. Each key-value pair is separated
    by a comma, and the pairs are sorted in ascending order by key.
    For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
    return "0, 3\n1, 2\n, 10:5"""
    lis1 = []
    lis2 = []
    
    for c in d:
        lis1.append(c)
        lis2.append(d[c])
        
    lis1.sort()#sorted list of keys
    
    d1 = {}
    
    for i in range(len(lis1)):
        d1[lis1[i]] = lis2[i]
    
    temp = ""
 
    for c in d1:
        temp += str(c) + "," + str(d1[c]) + "\n"
        
    return temp    
  

print(dict_to_str_sorted(d))