# function to allow  decoding of any files in KPS9566 encoding, and encoding of any files not in KPS9566 encoding.
import os, os.path, main2, codecs
# path variable left undefined for easy modification due to different paths in differnet comuputers.
path = ""
#creates custom encoding using the encoding table (main2) file. NOTE both files must be in same project directory.
encodings =main2.custom_search_function('KPS9566')
# choice is booleon  that can be modified. If user wants to decode, set to true. If user wants to encode, set to false.
choice = True
# decoding and encoding part.
if choice:
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
