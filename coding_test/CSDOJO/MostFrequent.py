# Implement your function below.
def most_frequent(given_list):
    # keys = set(given_list)
    # dictionary = dict.fromkeys(keys,0)
    dictionary = {}
    max_val = 0
    max_item = None
    for i in given_list:
        if i not in dictionary:
            dictionary[i] = 1
        else:    
            dictionary[i] += 1

        if max_val < dictionary[i]:
            max_val = dictionary[i]
            max_item = i
    return max_item



if __name__ == '__main__':
    # NOTE: The following input values will be used for testing your solution.
    # most_frequent(list1) should return 1
    list1 = [1, 3, 1, 3, 2, 1]
    # most_frequent(list2) should return 3
    list2 = [3, 3, 1, 3, 2, 1]
    # most_frequent(list3) should return None
    list3 = []
    # most_frequent(list4) should return 0
    list4 = [0]
    # most_frequent(list5) should return -1
    list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
    print(most_frequent(list1))
    print(most_frequent(list2))
    print(most_frequent(list3))
    print(most_frequent(list4))
    print(most_frequent(list5))