# Implement your function below.
def non_repeating(given_string):
    dic = {}
    for i in given_string:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] = -1
    for key, val in dic.items():
        if val == 1:
            return key
    return None

if __name__ == '__main__':
    # NOTE: The following input values will be used for testing your solution.
    non_repeating("abcab") # should return 'c'
    non_repeating("abab") # should return None
    non_repeating("aabbbc") # should return 'c'
    non_repeating("aabbdbc") # should return 'd'

    print(non_repeating("abcab"))
