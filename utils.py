# TIPS
# Sort --> operate
# Use dictionary or set 
# Use % 

list1 = [1,2,34]

dic_none = dict.fromkeys(list1)
dic_zero = dict.fromkeys(list1, 0)

set1 = set(list1)

list1.sort(reverse=True)

print(dic_none)
print(dic_zero)
print(set1)
print(list1)