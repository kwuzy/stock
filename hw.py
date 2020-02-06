word = input("Message: ")

def split(word):
    return [char for char in word]


def countX(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count 

def unique(list): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

def encode(unique_list,msg):

    # initialize a null list
    encodedArray = []

    # traverse for all unique elements
    for ele in uniqueArray:
        # add unique and count to new array
        encodedArray.append(ele)
        encodedArray.append(countX(wordArray, ele))
    return encodedArray

def toString(array):

    # initialize a empty string
    string = ""

    # go through array and add it to string
    for ele in array:
        string = string + str(ele)
    return string


wordArray = split(word)
uniqueArray = unique(split(word))
encodedArray = encode(uniqueArray,wordArray)
encodedMsg = toString(encodedArray)
print(encodedMsg)