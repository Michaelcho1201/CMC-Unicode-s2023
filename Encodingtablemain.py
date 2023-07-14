import codecs
import string

from typing import Tuple
# prepare map from numbers to letters from location that attached encoding file is in.
dicte = { " " : b''}
# left blank due to different possible paths between different computers.

f = open("C://Users//micha//OneDrive//Desktop//encodings.txt" , 'r')

for line in f:
    keystr = r"\u"
    cvalue = r"\u"
    value = " "
    if not(line[4].isalnum()):
        keystr = keystr + line[2] + line[3]
    else:
        keystr = keystr +line[2] + line[3] + line[4] + line [5]

    bytekey = bytes(keystr, 'ascii')


    if line.find("#") >-1:
        i = line.find("#")
        for element in range(7, 11):
            if line[element] != " ":
                cvalue = cvalue + line[element]
    if cvalue != " ":
        bytevalue = bytes(cvalue, 'ascii')
        value = bytevalue.decode('unicode-escape').encode('latin1').decode('utf8')
        dicte[value] = bytekey

_encode_table = dicte

print(_encode_table)


# prepare inverse map
_decode_table = {v: k for k, v in _encode_table.items()}


def custom_encode(text: str) -> Tuple[bytes, int]:
    # example encoder that converts ints to letters
    # see https://docs.python.org/3/library/codecs.html#codecs.Codec.encode
    return b''.join(_encode_table[x] for x in text), len(text)


def custom_decode(binary: bytes) -> Tuple[str, int]:
    # example decoder that converts letters to ints
    # see https://docs.python.org/3/library/codecs.html#codecs.Codec.decode

    encoding =  []

    for i in range (0, len(binary), 2):
        chunk = binary[i : i +2]

        encoding.append(chunk)
    result = b''.join(encoding)
    return _decode_table[result] , len(binary)


def custom_search_function(encoding_name):
    return codecs.CodecInfo(custom_encode, custom_decode, name='KPS9566')


def main():

    # register your custom codec
    # note that CodecInfo.name is used later
    codecs.register(custom_search_function)

    binary = b'\\uA4A1'
    # decode letters to numbers
    text = codecs.decode(binary, encoding='KPS9566')
    print(text)
    # encode numbers to letters
    binary2 = codecs.encode(text, encoding='KPS9566')
    print(binary2)
    # encode(decode(...)) should be an identity function
    assert binary == binary2

if __name__ == '__main__':
    main()
