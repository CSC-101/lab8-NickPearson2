def groups_of_3(list:list[int])->list[list[int]]:
    new_list = []
    r = len(list) % 3
    for i in range(0,len(list)-1,3):
        the_list = list[i:i+3]
        new_list.append(the_list)
    if r == 1:
        new_list.append([list[len(list)-1]])
    return new_list
