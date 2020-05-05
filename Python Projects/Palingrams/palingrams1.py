"""Find all word-pair palingrams in a dictionary file."""
from Palingrams import load_dictionary

word_list = load_dictionary.load('2of12.txt')


# find word-pair plaingrams
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end - i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end - i], word))
    return pali_list


palingrams = find_palingrams()
#sort palingrams on first word
palingrams_sorted = sorted(palingrams)

print(f'\nNumber of plaingrams = {len(palingrams_sorted)}\n')

for first, second in palingrams_sorted:
    print(f'{first}{second}')
