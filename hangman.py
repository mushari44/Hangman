
import random
from words import words
from hangman_visual import lives_visual_dict
import string

while True:

    def get_valid_word(words):
        word = random.choice(words)  # randomly chooses something from the list
        while '-' in word or ' ' in word:
            word = random.choice(words)

        return word.upper()


    def hangman():
        global letter
        word = get_valid_word(words)
        word_letters = set(word)  # letters in the word
        alphabet = set(string.ascii_uppercase)
        used_letters = set()  # what the user has guessed

        lives = 7

        # getting user input
        while len(word_letters) > 0 and lives > 0:
            # letters used
            # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
            print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

            # what current word is (ie W - R D)

            word_list=[letter if letter in used_letters else '-'for letter in word]

            print(lives_visual_dict[lives])
            print('Current word: ', ' '.join(word_list))




            user_letter = input('Guess a letter: ').upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print('')

                else:
                    lives = lives - 1  # takes away a life if wrong
                    print('\nYour letter,', user_letter, 'is not in the word.')
                    for letter in word:
                        pass
                    while letter!=user_letter:
                        if lives<4:
                                print("you have",lives,"lives left do you want a hint ?")
                                help = input("(y/n)")
                                if help == 'y':
                                    print("for each hint you will lose 1 life : ")
                                    print("this word has ",len(word),"letters")
                                    wich_letter=input("what letter do you want to display ?")
                                    if wich_letter=="1":
                                        print("first litter is : ", word[0])
                                        break
                                    elif wich_letter=='2':
                                        print('\nSecond letter is : ',word[1] )
                                        break
                                    elif wich_letter == '3':
                                        print('\nthird letter is : ', word[2])
                                        break
                                    elif wich_letter == '4':
                                        print('\nfourth letter is : ', word[3])
                                        break
                                    elif wich_letter == '5':
                                        print('\nfifth letter is : ', word[4])
                                        break
                                    elif wich_letter == '6':
                                        print('\nsixth letter is : ', word[5])
                                        break
                                    elif wich_letter == '7':
                                        print('\nSeventh letter is : ', word[6])
                                        break
                                    elif wich_letter == '8':
                                        print('\neighth letter is : ', word[7])
                                        break
                                    elif wich_letter == '9':
                                        print('\nninth letter is : ', word[8])
                                        break

                                    for letter in word:
                                        if letter!=word:
                                            print("this word has ",len(word),"letter")
                                            break
                                elif help == 'n':
                                    break
                        else: break


            elif user_letter in used_letters:
                print('\nYou have already used that letter. Guess another letter.')

            else:
                print('\nThat is not a valid letter.')



        # gets here when len(word_letters) == 0 OR when lives == 0
        if lives == 0:
            print(lives_visual_dict[lives])
            print('You died, sorry. The word was', word)

        else:
            print('YAY! You guessed the word', word, '!!')
        while True:
            Q=input("do you want to play again ? (y/n)")
            if Q.lower()=='y':
                break
            elif Q.lower()=='n':
                exit()


    if __name__ == '__main__':
        hangman()
