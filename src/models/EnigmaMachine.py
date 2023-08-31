## Imports
from RotorWrapper import RotorWrapper
from Rotor import Rotor

## Enigma Machine Class
## 
## This class represents our Enigma Machine internally
## We have our Rotor and Rotor Wrapper, we now need to accept inputs to our enigma
## machine and translate their messages to encoded/decoded text
## 
## One feature of the enigma machine was that communication came in via morse code
## In this module, we will not be accepting morse code, but rather just the encoded
## message if we are decoded, or the message to encode if we are encoding
##
## The object is to have multiple enigma machines communicating with eachother,
## such that we can set their settings accordingly and talk to one another across
## terminals. If sending a message across sockets, we will be adding a layer of
## morse code encoding to it after the multi-layer caesar cipher. If receiving a
## message, we will be decoding the morse code and then inputting that character
## encoding into the enigma machine to successfully read the message

class EnigmaMachine:
    def __init__(self, starting_pos: [int], reflector: str, plugboard: [tuple]):
        ## Error handling
        if len(starting_pos) != 3:
            raise Exception("Invalid number of starting positions. Must be exactly equal to 3.")
        
        ## Create our rotor wrapper -- we want this to be inaccessible outside 
        ## of the object, so prefix with __
        rotors = [Rotor(pos, index+1) for index, pos in enumerate(starting_pos)]
        self.__wrapper = RotorWrapper(rotors, reflector)
        
        ## Set our plugboard
        self.__plugboard = {}
        self.__init_plugboard(plugboard)


    ## Init plugboard -- internal function
    def __init_plugboard(self, plugboard: [tuple]):
        for tup in plugboard:
            a = tup[0]
            b = tup[1]

            ## Type checking inputs
            if ord(a) > 122 or ord(a) < 97 or ord(b) > 122 or ord(b) < 97:
                raise Exception(f"Please ensure that {a} and {b} are both lowercase alphabetic characters!")
            
            ## Duplicate checking
            if a in self.__plugboard or b in self.__plugboard:
                raise Exception(f"{a} or {b} is already in the plugboard. Please ensure to keep the \
                                pairings unique!")
            
            self.__plugboard[a] = b
            self.__plugboard[b] = a

    ## Method to handle text inputs
    ## We are parsing the text, ensuring that all characters are alphabetic between a-z
    ## The input for this method is the text to encode/decode
    ## The output for this method is the encoded/decoded text
    def encode_message(self, text: str) -> str:
        rStr = []
        words = text.split(' ')
        for word in words:
            word_arr = []
            for char in word:
                lower_c = char.lower()

                ## Error handling
                if ord(lower_c) > 122 or ord(lower_c) < 97:
                    raise Exception(f"{char} is not an alphabetic character!")
                
                ## Encode in plugboard
                encoded_char = lower_c
                if encoded_char in self.__plugboard:
                    encoded_char = self.__plugboard[encoded_char]

                ## Complete encoding in rotors
                encoded_char = self.__wrapper._handle_input(lower_c)

                ## Re-encode through the plugboard
                if encoded_char in self.__plugboard:
                    encoded_char = self.__plugboard[encoded_char]

                word_arr.append(encoded_char)

            rStr.append(''.join(word_arr))
        
        ## return encoded/decoded string
        return ' '.join(rStr)