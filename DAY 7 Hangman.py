print('Welcome to HANGMAN on CLI')
wordbank = input('Please enter in a list of words seperated by commas (word, word, word)\nEntered: ')
wordbank = wordbank.split(', ')
print(wordbank)
def index_finder(word, letter):
    '''finds at which indexes a letter is found in an array version of word'''
    indx = []
    for i, let in enumerate(word):
        if let == letter:
            indx.append(i)
    return indx

def hangman(word):
    word_empty_string =[]
    word_list = list(word)
    for letter in range(len(word)):
        word_empty_string.append('_')
    print(word)
    print(word_empty_string)
    
    while '_' in word_empty_string:
        guessed = input("Guess a letter: ")
        if guessed in word_list:
            let_ind = index_finder(word_list, guessed)
            for indx in let_ind:
                word_empty_string[indx] = guessed
            print(word_empty_string)





for word in wordbank:
    hangman(word)