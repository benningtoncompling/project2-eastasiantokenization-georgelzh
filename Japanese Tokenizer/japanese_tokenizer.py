import re
import sys

# inFile = sys.argv[1]
# outFile = sys.argv[2]

with open("./in.txt", "r", encoding='UTF-8') as f:
    inputTxt = f.read().splitlines()

with open("./japanese_wordlist.txt", "r", encoding='UTF-8') as dic:
    japaneseDic = dic.read().splitlines()  #Sadip told me splitlines() function. It will also remove the \n

outPut = open("./output.txt", "a", encoding='UTF-8')

for word in inputTxt:
    outPut.write("。\n")
    strLength = len(word)
    limit = 0

    for left in range(limit, strLength):
        for right in range(strLength, limit, -1):

            currentWord = word[left:right]

            if currentWord in japaneseDic:
                outPut.write(currentWord + " ")
                limit = right + 1
                break

            # elif currentWord not in japaneseDic:
            #     outPut.write(currentWord + " ")
            #     limit = right
            #     break

            #
            # else:
            #     currentWord


# Zak helped me with understanding of the algorithm, also he introduced me the function of readline()
# make a function of maxmatch where you pass sentence and dictionary to compare, returning sentence with a space if it matches.
# I didn't get a list at first, also I needed to remove the \n
# Sadip also told me to do with open as xx: to deal with file. because it will open and close the file automatically.