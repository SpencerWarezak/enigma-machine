##
## Reflector Map found at https://www.codesandciphers.org.uk/enigma/rotorspec.htm
## These are all reflector maps used in enigma machines. In order for devices to communicate
## effectively, they must both be set to the same reflector value

class Reflector:
    reflectorB = {
        'a': 'y',
        'y': 'a',
        'b': 'r',
        'r': 'b',
        'c': 'u',
        'u': 'c',
        'd': 'h',
        'h': 'd',
        'e': 'q',
        'q': 'e',
        'f': 's',
        's': 'f',
        'g': 'l',
        'l': 'g',
        'i': 'p',
        'p': 'i',
        'j': 'x',
        'x': 'j',
        'k': 'n',
        'n': 'k',
        'm': 'o',
        'o': 'm',
        't': 'z',
        'z': 't',
        'v': 'w',
        'w': 'v'
    }

    reflectorC = {
        'a': 'f',
        'f': 'a',
        'b': 'v',
        'v': 'b',
        'c': 'p',
        'p': 'c',
        'd': 'j',
        'j': 'd',
        'e': 'i',
        'i': 'e',
        'g': 'o',
        'o': 'g',
        'h': 'y',
        'y': 'h',
        'k': 'r',
        'r': 'k',
        'l': 'z',
        'z': 'l',
        'm': 'x',
        'x': 'm',
        'n': 'w',
        'w': 'n',
        't': 'q',
        'q': 't',
        's': 'u',
        'u': 's'
    }

    reflectorB_Dunn = {
        'a': 'e',
        'e': 'a',
        'b': 'n',
        'n': 'b',
        'c': 'k',
        'k': 'c',
        'd': 'q',
        'q': 'd',
        'f': 'u',
        'u': 'f',
        'g': 'y',
        'y': 'g',
        'h': 'w',
        'w': 'h',
        'i': 'j',
        'j': 'i',
        'l': 'o',
        'o': 'l',
        'm': 'p',
        'p': 'm',
        'r': 'x',
        'x': 'r',
        's': 'z',
        'z': 's',
        't': 'v',
        'v': 't'
    }

    reflectorC_Dunn = {
        'a': 'r',
        'r': 'a',
        'b': 'd',
        'd': 'b',
        'c': 'o',
        'o': 'c',
        'e': 'j',
        'j': 'e',
        'f': 'n',
        'n': 'f',
        'g': 't',
        't': 'g',
        'h': 'k',
        'k': 'h',
        'i': 'v',
        'v': 'i',
        'l': 'm',
        'm': 'l',
        'p': 'w',
        'w': 'p',
        'q': 'z',
        'z': 'q',
        's': 'x',
        'x': 's',
        'u': 'y',
        'y': 'u'
    }