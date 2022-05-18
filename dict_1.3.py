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
    try:
        print("")
        print(dictionary[wrequest])
    except KeyError:
        print("word not in dictionary")
        close = get_close_matches(wrequest, keylist)
        print("did you mean")
        print("")
        print(close[0])
        print(close[1])
        print(close[2])
        print("")
        continue
