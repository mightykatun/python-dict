from tqdm import tqdm
print("indexing dictionary...")
wordlist = {}
for x in tqdm(range(36664)):
    definition = []
    file = open("sourcedict.txt", "r", encoding = "utf8")
    content = file.readlines()
    word = content[x]
    definition = word.split(" ", 1)
    definition[0] = definition[0].lower()
    if word == "\n":
        continue
    else:
        wordlist.update({definition[0] : definition[1]})
file.close()
print("dictionary dumped")
print("number of elements", len(wordlist))
print("writing in dict.txt...")
file = open("dict.txt", "w", encoding = "utf8")
newcontent = str(wordlist)
file.writelines(newcontent)
file.close()
print("dictionary dumped")
input("enter to exit")
