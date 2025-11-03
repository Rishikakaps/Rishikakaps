# what will happen if i used list with a sentence 

words = list("This is a sample sentence.")
print(words)
sorted_words = sorted(words, key=str.lower)
print(sorted_words)
sort_words = words.sort()
print(sort_words)
id(sort_words)
id(sorted_words)

