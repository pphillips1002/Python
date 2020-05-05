def main():
    """Takes in word and adds 'way' if letter begins with vowel otherwise moves first letter to the end and adds 'ay'"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    print('Welcome to the Pig Latin Generator')
    word = input('Enter a word: ')

    # adds 'way' if letter at index 0 is a vowel, prints new word
    if word[0].lower() in vowels:
        pig_word = word + 'way'
        print(pig_word)
    # switches letter at index 0 to index -1 and adds 'ay', prints new word
    else:
        pig_word = word[1:] + word[0] + 'ay'
        print(pig_word)


if __name__ == '__main__':
    main()
