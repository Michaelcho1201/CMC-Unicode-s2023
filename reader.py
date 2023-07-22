"""function to allow  decoding of any files in KPS9566 encoding, and encoding of any files not in KPS9566 encoding."""
import os, os.path, Encodingtablemain, codecs
""" Program requests full file path to operate on as input from user in run terminal. """
path = input("Please input full file path to operate on:" )
""" creates custom encoding using the encoding table (Encodingtablemain) file. NOTE both files must be in same project directory."""
encodings =Encodingtablemain.custom_search_function('KPS9566')
""" Program requests input of True for deocding, or False for encoding """
choice = input("Please input True to decode, or False to encode:" )
""" Decoding and Encoding portion."""
if choice == "True":
    f = open(path, 'rb')
    bytes = f.read()
    words = bytes.split()
    for i in range(0, len(words)):
        byte = words[i]
        text = encodings.decode(byte)
        print(list(zip(text))[0])
    f.close()

else:
    f = open(path, 'r')
    strings = f.read()
    words = strings.split()
    for i in range(0, len(words)):
        word = words[i]
        text = encodings.encode(byte)
        print(list(zip(text))[0])
    f.close()
