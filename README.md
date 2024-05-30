# Python-Dictionary
Finds the definition of a given word.

Thanks to https://github.com/sujithps for the base of the sourcedict.txt file.
(I just removed the empty lines and the "per letter indexing").

The dictdumper.py transorms the sourcedict.txt in a python dictionary and saves it in
the form of a string in dict.txt.

Then, dict.py loads dict.txt and finds the type (definition) based on an user key input (word).
If the word is not in the dictionary, it will propose similar words to your input.
