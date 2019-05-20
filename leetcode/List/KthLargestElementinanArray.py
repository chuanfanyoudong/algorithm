
def solution(target_number):
    if not isinstance(target_number, int):
        return None
    list_target_number = list(str(target_number))
    length = len(list_target_number)
    j = length - 1
    tag = 0
    while j > 0:
        k = j
        while k > 0:
            if int(list_target_number[j]) > int(list_target_number[k]):
                list_target_number[j], list_target_number[k] = \
                list_target_number[k], list_target_number[j]
                tag = 1
                break
            k -= 1
        j -= 1
    if tag == 0:
        return None
    target_number = int("".join(list_target_number))
    return target_number


if __name__ == '__main__':
    target = 35268
    print(solution(target))