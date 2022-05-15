import ast
print("Python Dictionary")
print("loading...")
file = open("dict.txt", "r", encoding = "utf8")
content = file.readlines()
strcontent = "".join(map(str, content))
dictionary = ast.literal_eval(strcontent)
print("done")
while True:
    wrequest = input("definition of ")
    try:
        print("")
        print(dictionary[wrequest])
    except KeyError:
        print("word is not in dictionary")
        print("")
        continue
    while True:
        follow = input("continue y/n ")
        if follow == "y":
            break
        if follow == "n":
            input("enter to exit")
            exit()
        else:
            print("input exception")
