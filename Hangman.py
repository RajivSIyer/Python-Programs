import random

def loadwords(filename, min_wordlen):
    f = open(filename, 'rb')
    rawdata = f.read().decode('utf-8')
    listofwords = rawdata.split('\n')
    f.close()
    filtered_list = []
    for w in listofwords:
        if len(w) >= min_wordlen:
            filtered_list.append(w)
    return filtered_list

def give_word(word_list):
    #word_list = ['Mississippi','Entreupreneur', 'Abacus', 'Kangaroo', 'Flabergasted', 'abandon', 'abbreviation', 'badminton', 'becomingly', 'Behemoth', 'Capillaries']
    word = random.choice(word_list)
    word_list.remove(word)
    return word

def word_split(word):
    vowels = ['a','e','i','o','u']
    reduced_cons = []
    reduced_vowel = []
    for c in word:
        if c in vowels:
            reduced_vowel.append(c)
        else:
            reduced_cons.append(c)

    return (list(set(reduced_vowel)), list(set(reduced_cons)))

def Hint(vowels, consonants):
    if len(vowels):
        letter = random.choice(vowels)
        vowels.remove(letter)
    else:
        letter = random.choice(consonants)
        consonants.remove(letter)
    return letter

def Hangman(word):
    word = word.lower()
    empty_word = list(len(word)*'_')
    showword(empty_word)
    attempts = 6
    hint_cnt = 1
    vow_list, cons_list = word_split(word) 
    while attempts > 0:

        ch = input('Guess a letter: ').lower()
        if ch == 'hint':
            if hint_cnt <= 5:
                hint_cnt += 1
                attempts -= 1
                ch = Hint(vow_list, cons_list)
                print('The hint letter is: ',ch)
            else:
                print('Maximum two hints allowed!')
                continue

        elif len(ch) > 1:
            print('Guess with only a letter!')
            continue
        correct_guess = False

        for i in range(len(word)):
            if ch == word[i]:
                empty_word[i] = ch
                correct_guess = True

        if not correct_guess:
            print("Your guess is incorrect. Try Again!")
            attempts -= 1
        
        else:
            print('Your guess is correct!')
        
        print('Remaining attempts: ', attempts)
        showword(empty_word)

        if '_' not in empty_word:
            print("Congratulations! You won with ", attempts, ' attempt(s) remaining.')
            break
        
    else:
        print('You are Hung!')
        print('The word was: ', word)

def showword(word):
    s = ''
    for c in word:
        s += c + ' '
    print(s)

answer = 'y'
while answer.lower() != 'n':
    l = loadwords('engmix.txt', 5)
    Hangman(give_word(l))
    answer = input("Do you wish to play again? ")