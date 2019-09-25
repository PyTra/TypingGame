import random

_LEVEL1 = 4
_LEVEL2 = 8
_LEVEL3 = 12
# the length of words per difficulty level

def _get_words(x: int, y: int, z: int) -> dict:
    # returns the dict of words from file of 58k English words
    
    words = {'1':[], '2':[], '3':[], '4':[]}
    
    with open('words.txt') as word_file:
        for line in word_file:
            temp = line.rstrip('\n')
            
            if len(temp) <= x:
                words['1'].append(temp)
                
            elif len(temp) <= y:
                words['2'].append(temp)
            
            elif len(temp) <= z:
                words['3'].append(temp)
                
            else:
                words['4'].append(temp)
                
    return words
    

def get_random_words(difficulty: int, number: int) -> list:
    # input is the difficulty level and the number of words desired (both are int)
    # returns a list of random words that adhere to input specifications
    
    result = []
    words = _get_words(_LEVEL1, _LEVEL2, _LEVEL3)
    
    for i in range(number):
        result.append(random.choice(words[str(difficulty)]))
        
    return result


def test():
    # function to test output of random words
    
    print(get_random_words(1, 5))
    print(get_random_words(2, 5))
    print(get_random_words(3, 5))
    print(get_random_words(4, 5))
    

test()