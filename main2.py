import codecs
import string

from typing import Tuple


# prepare map from numbers to letters
_encode_table =  {"ㄱ" : b'u3131'}

# prepare inverse map
_decode_table = {v: k for k, v in _encode_table.items()}
print (_encode_table.items())
print (_decode_table.items())


def custom_encode(text: str) -> Tuple[bytes, int]:
    # example encoder that converts ints to letters
    # see https://docs.python.org/3/library/codecs.html#codecs.Codec.encode
    return b''.join(_encode_table[x] for x in text), len(text)


def custom_decode(binary: bytes) -> Tuple[str, int]:
    # example decoder that converts letters to ints
    # see https://docs.python.org/3/library/codecs.html#codecs.Codec.decode
    return ''.join(_decode_table[x] for x in binary), len(binary)


def custom_search_function(encoding_name):
    return codecs.CodecInfo(custom_encode, custom_decode, name='KPS9566')


def main():

    # register your custom codec
    # note that CodecInfo.name is used later
    codecs.register(custom_search_function)

    binary = b'\u3131'
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
