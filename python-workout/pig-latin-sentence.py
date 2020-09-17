sentence = input("Enter a sentence: ")

output = [ ]
for word in sentence.split():
    if word[0] in 'aeiou':
        output.append(f"{word}way")
    else:
        output.append(f"{word[1:]}{word[0]}ay")

print(' '.join(output))

#*****or*****

sentence = input("Enter a sentence: ")

for word in sentence.split():
    if word[0] in 'aeiou':
        print(f"{word}way", end=' ')
    else:
        print(f"{word[1:]}{word[0]}ay", end=' ')