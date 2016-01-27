lst = [1,2,3,4]
#lst[len(lst)]
len(lst)
"""for i in range(lst):
    if lst[i] == 1:
        for j in range(lst2):
            if lst[i+j] == lst2[j]"""
for i in range(len(lst)):
    if lst[i] == 2:
        print("I continued")
        continue
    elif lst[i] == 3:
        print("I broke")
        break
    print(lst[i])
            