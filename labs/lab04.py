
str(42)

list0 = [1, 2, 3]
list1 = [1, 2, 3]

#question 1

def list_to_string(lis):
    output = ""
    for i in range(len(lis[i])):
        output += str(lis[i])
    return output

#question 2

list1 = [1, 4, 2, 3, 5, 6, 7]
list2 = [1, 2, 3]

def lists_are_the_same(list1, list2):
    if len(list1) == len(list2):
        for i in range (len(list1)):
            if list1[i] != list2[i]:
                return False
        return True
    return False

print(lists_are_the_same(list1, list2))

list1 = [1, 4, 2, 3, 5, 6, 7]
list2 = [1, 2, 3]

#question 3

def list1_start_with_list2(list1, list2):
    if len(list1) >= len(list2):
        for i in range (len(list2)):
            if list1[i] != list2[i]:
                return False
        return True
    return False

lis2 = [1, 2, 3, 4]
lis1 = [1, 2, 3, 4, 5]

print(list1_start_with_list2(lis2, lis1))

#question 4
#2 in 1

def match_pattern(list1, list2):
    if len(list1) >= len(list2):
        for j in range (len(list1) - len(list2)):
            check = True
            for i in range (len(list2)):
                if list1[i + j] != list2[i]:
                    check = False
            if check:
                return True    
    return False
    
lis4 = [1, 2, 3]
lis5 = [1, 2, 3]    

print(match_pattern(lis4, lis5))

#question 5

def duplicates(list0):
    for i in range (len(list0)-1):
        if list0[i] == list0[i + 1]:
            return True
    return False

list0 = [1, 2, 2, 3, 4]

print(duplicates(list0))
  
        
    
    
    
        
        
