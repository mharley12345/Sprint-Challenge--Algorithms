'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if word.find("th") == -1: #base case -> stop when there are no "th" left in the string
        return 0

    else:
        check = word.find("th") #looking for 1st index of "th"
        new_word = word[check+2:] #once index is found slice the string at that position and add 2
        return 1 + count_th(new_word) # If "th" is found return 1 and continue to call the function to complete the traversing of the string

    

