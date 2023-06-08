array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

def linear_search(value_to_find, array_to_search_through):
    for idx in range(len(array_to_search_through)):
        if array_to_search_through[idx] == value_to_find:
            return idx
    
    return None 

def linear_search_global(value_to_find, array_to_search_through):
    answerArr = []
    for idx in range(len(array_to_search_through)):
        if array_to_search_through[idx] == value_to_find:
            answerArr.append(idx)

    return answerArr