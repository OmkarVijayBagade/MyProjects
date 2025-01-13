#string reversal 
# example     hello  -->  olleh 

def reverse(): 
    word = input("Enter a word: ")
    reversed_word = word[::-1]
    print("Reversed word :- ")
    return reversed_word

print(reverse())