def char_count(str):
  char_dict = {}
  char_list = []

  for char in str:
    if char == ' ':
      continue
    elif char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
 
  for key, value in char_dict.items():
    char_list.append([key, value])

  char_list.sort(key=lambda x: x[1], reverse=True)

  for each_list in range(len(char_list)-1):
    for item in range(len(char_list)-1):
      if char_list[item][1] == char_list[item+1][1]:
        if char_list[item][0] > char_list[item+1][0]:
          temp = char_list[item]
          char_list[item] = char_list[item+1]
          char_list[item+1] = temp

  return char_list