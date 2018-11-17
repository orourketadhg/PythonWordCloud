try:
    import re
except ImportError:
    import re
    print("re Importing Error")

fo = open("output.html", "w")
fo.write('<!DOCTYPE html>\
    <html>\
    <head lang="en">\
    <meta charset="UTF-8">\
    <title>Tag Cloud Generator</title>\
    </head>\
    <body>\
    <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black;\
    border:1px solid black">')


# your code goes here!

# generate the dictionary and a temp list
wordCount = {}
words = []
blacklistWords = ['and', 'or', 'this', 'the', 'a', 'that', '--', '.', '']

# checking to see if file exists in project dir
try:
    # open the .txt file
    txt = open("gettisburg.txt", "r")

    # split .txt file into single word strings
    for line in txt:
        words.append(line.split())

    # removing the periods from words that have them
    for line in words:
        for word in line:
            # if comma separate and append
            if ',' in word:
                words.append(re.split('[,]', word))

            # if period separate and append
            if '.' in line:
                words.append(re.split('[.]', word))

            # remove words with period or comma in them
            if ',' in word or '.' in word:
                line.remove(word)

    # loop through each sublist
    for line in words:
        # loop though each sublist element
        for word in line:
            # if word already exists increment keys value
            if word in wordCount:
                wordCount[word] += 1

            # else create new dictionary element and set value to 1
            elif word not in blacklistWords:
                wordCount[word] = 1

    # checking the dictionary and list are populated
    # print(wordCount)
    print(words)

    # close txt file to prevent data corruption
    txt.close()

# no file found in dir
except FileNotFoundError:
    print("No File Found")


# fo.write('<span style="font-size: 10px"> HELLO </span>')

# write dictionary to webpage
for key in wordCount:
    fo.write('<span style="font-size: {}px"> {} </span>'.format(wordCount[key]*10, key))

fo.write('</div>\
    </body>\
    </html>')
