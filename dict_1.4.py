from difflib import get_close_matches
import ast
print("Python Dictionary")
print("loading...")
file = open("dict.txt", "r", encoding = "utf8")
content = file.readlines()
strcontent = "".join(map(str, content))
dictionary = ast.literal_eval(strcontent)
keylist = list(dict.keys(dictionary))
print("done")
while True:
    wrequest = input("definition of ")
    if wrequest == "":
        print("type a word")
    else:
        try:
            print("")
            print(dictionary[wrequest])
        except KeyError:
            print("word not in dictionary")
            close = get_close_matches(wrequest, keylist, 4)
            length = len(close)
            if length > 0:
                print("did you mean any of these")
                for i in range(int(length)):
                    print(close[i])
            else:
                print("no similar words")
            print("")
            continue
