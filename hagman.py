import random
from words import words
import string

def get_valid_word(words):
    word=random.choice(words)
    while'-' in word or ' ' in word:
        word=random.choice(words)
    return word    

def hangman():
    word= get_valid_word(words).upper()
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    letters_left=alphabet-used_letters
    lives=6

    while len(word_letters)>0 and lives>0:
        print(f"\nYou have {lives} lives left and you have used these letters:"," ".join(used_letters))
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print('\tCurrent Word',' '.join(word_list))
        user_letter=input("\nGuess a letter in the word:  ").upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
                print("\nThis letter is not in the word.")
        elif user_letter in used_letters:
            print("\nYou have used this character before. Try Again.")
        else:
            print("\nInvalid Character. Try Again")  
    if lives == 0:
        print("\nYou Died. The word was",word)
    else:
        print("\nYOU WON!! You have guessed the word",word)     

hangman()




    
