def calculate_mode(input_list):
    # Dictionary to keep track of frequency
    most_freq_dict = {}
    # Initialize counter to keep track of key with highest value
    most_freq_counter = 0
    # Initiliaze an answer list
    answer_list = []
    # iterate through list and add to dict
    for elem in input_list:
        if elem in most_freq_dict:
            most_freq_dict[elem] += 1
        else:
            most_freq_dict[elem] = 1

    # find the highest value in dict
    for elem in most_freq_dict:
        if most_freq_dict[elem] > most_freq_counter:
            most_freq_counter = most_freq_dict[elem]

    # Add each element with this hight count to the answer list
    for elem in most_freq_dict:
        if most_freq_dict[elem] == most_freq_counter:
            answer_list.append(elem)
    
    return answer_list
