
import random
import string
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def S_to_L (str) :
    lst=list(str)
    return lst 



def L_to_S (lst) :
   str =''
   for ele in lst:
    str += ele 
   return str     



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''    

    s = L_to_S(letters_guessed) 
    if s == secret_word:
      return True
    else:
      return False
       



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    s=''
    for ele in secret_word:
     if ele in letters_guessed:
       s += ele
     else :
        s += '_ '
    return (s)
   



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letter=S_to_L(string.ascii_lowercase)
    if letters_guessed== []:
      return string.ascii_lowercase
    for e in letters_guessed: 
     if e in all_letter:
      all_letter.remove(e)
    rest=L_to_S(all_letter)  
    return  rest
    
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' ,len(secret_word) ,' letters long.')
    print('-------------')
    global letters_guessed 
    letters_guessed =[]
    guessed_before=[]
    tries =6
    warns =3
    while(tries and warns ):
      print('You have ',warns,' warnings left.')
      print('You have ' ,tries, ' guesses left.')
      print('Available letters: ',get_available_letters(guessed_before))
      s= input('Please guess a letter:')
      if s =='*':
        show_possible_matches(get_guessed_word(secret_word,guessed_before),guessed_before)
        continue
      if(s.isalpha() and s not in guessed_before ):
        guessed_before.append(s)
        s=s.lower()
        guessed_before.append(s)
        if s in secret_word:
         print('Good guess: ',get_guessed_word(secret_word,guessed_before))
         print('-------------')
         letters_guessed.append(s)
        else:
         print('Oops! That letter is not in my word: ',get_guessed_word(secret_word,guessed_before))
         print('-------------')
         tries -=1
         if s in 'aieou' :
           tries -=1
      else:
        warns -=1
        guessed_before.append(s)
        if (s.isalpha()):
          print("Oops! You've already guessed that letter. You  have ",warns," warnings:",get_guessed_word(secret_word,guessed_before)) 
        else:
           print('You can only input an alphabet.')
        print('-------------')
      if (is_word_guessed(secret_word,get_guessed_word(secret_word,guessed_before))):
        print('Congratulations, you won!')
        total_score=tries*len(letters_guessed)
        print('Your total score for this game is: ',total_score)
        break
      if tries==0 :
        print('Sorry, you ran out of guesses. The word was ',secret_word,'.')   
        break
      if  warns==0 :
        print('Sorry, you ran out of warnings. The word was ',secret_word,'.')  
        break

# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    Lst=[]
    my=my_word.replace(' ','')
    if len(my)==len(other_word):
      for ele in range (len(other_word)):
        if my[ele]==other_word[ele] or my[ele]=='_':
          Lst.append('1')
        if my.count(my[ele]) < other_word.count(other_word[ele]) and my.count(my[ele]) > 0 :
          return False
      if len(other_word)==len(Lst):
        return True 
      else:
        return False  
    else: 
      return False
    


def show_possible_matches(my_word,gussed_before):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    i=0
    j=0
    for ele in wordlist:
      if (match_with_gaps(get_guessed_word(secret_word,gussed_before),ele)):
        i+=1
        if i==1 and j==0 :
          print('Possible word matches are: ')
          j+=1
        print(ele)
        if i ==55899 and j ==0:
          print('No matches found')
        
      


    



def hangman_with_hints(secret_word):   #------------------>*** i merged it with the original game ***
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass






if __name__ == "__main__":
    
    
    secret_word =  choose_word(wordlist)
    hangman(secret_word)

    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
