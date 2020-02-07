word = input("Message: ")

def split(word):
    return [char for char in word]


def countX(lst, idx): 
    count = 1
    i = idx
    while i < len(lst): 
        if (lst[idx + 1] == lst[idx]): 
            count = count + 1
            i+=1
        else:
            break
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

def encode(msg):

    # initialize a null list
    encodedArray = []
    j = 0

    # traverse for all unique elements
    while j < len(msg):

        # add unique and count to new array
        encodedArray.append(msg[j])
        encodedArray.append(countX(msg , j))
        j = j + countX(msg,j)
        print(j)
    return encodedArray

def toString(array):

    # initialize a empty string
    string = ""

    # go through array and add it to string
    for ele in array:
        string = string + str(ele)
    return string


wordArray = split(word)
# uniqueArray = unique(split(word))
encodedArray = encode(wordArray)
encodedMsg = toString(encodedArray)
print(encodedMsg)