import random
import pygame

#clean the text and split it into words
from reference import text

#make a map of the words and the next words that follow them
wordMap = {}

for i in range(len(text) - 2):
    key = (text[i], text[i + 1])
    nextWord = text[i + 2]

    if key not in wordMap:
        wordMap[key] = [nextWord]
    else:
        wordMap[key].append(nextWord)



#Now we actually generate the text
sentence = []
seed1 = random.randint(0,len(text) - 2) 
seed2 = seed1 + 1 

sentence.append(text[seed1])
sentence.append(text[seed2])

currentWord = tuple(sentence)

while len(sentence) < 500:
    x = wordMap.get(currentWord)
    
    if x is not None: 
        newWord = random.choice(x)
        sentence.append(newWord)
        currentWord = tuple(sentence[-2:])
    
    else:
        sentence.append(".")
        break

print(" ".join(sentence))