word = input("Enter a word: ")

if word[0] in 'aeiou':
    print(f'{word}way')
else:
    print(f'{word[1:]}{word[0]}ay')