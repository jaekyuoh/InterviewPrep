import time
# Implement your function below.
def common_elements(list1, list2):
    result = []
    dic = dict.fromkeys(list1)
    for element in list2:
        if element in dic:
            result.append(element)
    return result

def common_elements2(list1, list2):
    result = []
    l1_set = set(list1)
    for element in list2:
        if element in l1_set:
            result.append(element)
    return result

def common_elements_dojo(list1, list2):
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1
            p2 += 1
        elif list1[p1] > list2[p2]:
            p2 += 1
        else:
            p1 += 1
    return result
if __name__ == '__main__':
    # NOTE: The following input values will be used for testing your solution.
    list_a1 = [1, 3, 4, 6, 7, 9]
    list_a2 = [1, 2, 4, 5, 9, 10]
    # print(common_elements(list_a1, list_a2)) # should return [1, 4, 9] (a list).

    list_b1 = [1, 2, 9, 10, 11, 12]
    list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
    # print(common_elements(list_b1, list_b2)) # should return [1, 2, 9, 10, 12] (a list).

    list_c1 = [0, 1, 2, 3, 4, 5]
    list_c2 = [6, 7, 8, 9, 10, 11]
    # print(common_elements(list_c1, list_c2)) # should return [] (an empty list).

    list_long1 = []
    list_long2 = []

    import random
    for x in range(100):
        list_long1.append(random.randint(1,1001))
    for x in range(100):
        list_long2.append(random.randint(1,1001))

    s = time.time()
    print(common_elements(list_long1, list_long2))
    e = time.time()
    print(e-s)


    s = time.time()
    print(common_elements_dojo(list_long1, list_long2))
    e = time.time()
    print(e-s)
 
    from IPython import embed
    embed()