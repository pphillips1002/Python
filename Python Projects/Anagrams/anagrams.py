from Anagrams import load_dictionary

word_list = load_dictionary.load('2of12.txt')
anagram_list = []

name = input("Enter a word to find an anagram: ")
name = name.lower()
print(f"Using {name}.")

input_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == input_sorted:
            anagram_list.append(word)
            print()
if len(anagram_list) == 0:
        print("You need a larger dictionary or a new name!")
else:
        print("Anagrams =",*anagram_list,sep='\n')
