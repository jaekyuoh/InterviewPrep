# Implement your function below.
def is_one_away(s1, s2):
    used_operation = False
    if len(s1) - len(s2) >= 2 or len(s2) - len(s1) >= 2:
        return False
    elif len(s1) == len(s2):
        operation = 'change'
        str_long = s1
        str_short = s2
    elif len(s1) > len(s2):
        operation = 'add'
        str_long = s1
        str_short = s2 + ' '
    else:
        operation = 'add'
        str_long = s2
        str_short = s1 + ' '

    for i in range(len(str_long)):
        if i < len(str_short):
            if str_long[i] != str_short[i]:
                if not used_operation:
                    if operation == 'change':
                        str_short = str_short[:i] + str_long[i] + str_short[i+1:]
                    else:
                        str_short = str_short[0:i] + str_long[i] + str_short[i:]
                    used_operation = True
                else:
                    return False
            else:
                continue
        else:
            return False

    return True

# Implement your function below.
def is_one_away_dojo(s1, s2):
    if len(s1) - len(s2) >= 2 or len(s2) - len(s1) >= 2:
        return False
    elif len(s1) == len(s2):
        return is_one_away_same_length(s1, s2)
    elif len(s1) > len(s2):
        return is_one_away_diff_lengths(s1, s2)
    else:
        return is_one_away_diff_lengths(s2, s1)


def is_one_away_same_length_dojo(s1, s2):
    count_diff = 0
    for i in range(len(s1)):
        if not s1[i] == s2[i]:
            count_diff += 1
            if count_diff > 1:
                return False
    return True


# Assumption: len(s1) == len(s2) + 1
def is_one_away_diff_lengths_dojo(s1, s2):
    i = 0
    count_diff = 0
    while i < len(s2):
        if s1[i + count_diff] == s2[i]:
            i += 1
        else:
            count_diff += 1
            if count_diff > 1:
                return False
    return True

if __name__ == '__main__':
    # NOTE: The following input values will be used for testing your solution.
    print(is_one_away("abcde", "abcd"))  # should return True
    print(is_one_away("abde", "abcde"))  # should return True
    print(is_one_away("a", "a"))  # should return True
    print(is_one_away("abcdef", "abqdef"))  # should return True
    print(is_one_away("abcdef", "abccef"))  # should return True
    print(is_one_away("abcdef", "abcde"))  # should return True
    print(is_one_away("aaa", "abc"))  # should return False
    print(is_one_away("abcde", "abc"))  # should return False
    print(is_one_away("abc", "abcde"))  # should return False
    print(is_one_away("abc", "bcc"))  # should return False