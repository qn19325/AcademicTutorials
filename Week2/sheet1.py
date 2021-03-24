import random

def ListToString(list_of_strings):
    concatenated_string = str()
    for x in list_of_strings:
        concatenated_string = concatenated_string + x
    return concatenated_string


def GetEmptyCells(list_of_strings):
    list_of_ints = list()
    for idx, val in enumerate(list_of_strings):
        if val == ' ':
            list_of_ints.append(idx)
    return list_of_ints


def GetRandomElement(list):
    rand_num = random.randrange(0, len(list))  
    return list[rand_num]


def MaxIndices(list_of_ints):
    indexes = list()
    for idx, val in enumerate(list_of_ints):
        if val == max(list_of_ints):
            indexes.append(idx)
    return indexes

# TESTING
#print( ListToString(['A','B','C']) == 'ABC' )
#print( GetEmptyCells([' ','B','C',' ']) == [0,3] ) 
#print( GetRandomElement([1,2,3,4,5]) )
#print( MaxIndices([0,8,20,5]) == [2] )
#print( MaxIndices([7,2,5,7,5]) == [0,3] )