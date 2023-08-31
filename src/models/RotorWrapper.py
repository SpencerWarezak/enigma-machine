## Imports
from reflector import Reflector

## RotorWrapper Class
## 
## This class manages our rotor group, acting as a global state manager
## Because we cannot directly manage the interation between two rotors in
## our Rotor class, we need a wrapper class to manage the global state of
## all three rotors in our enigma machine
## 
## The rotor wrapper will be initialized with all three rotors that we create
## when we create an instance of our Enigma Machine
## 
## The enigma machine will accept input and then call methods in the rotor wrapper
## to handle not only the encryption generated by the three rotors, but their
## internal rotations, as well
##
## For example, our initialization might look something like:
##      r1 = Rotor(1, 1)
##      r2 = Rotor(5, 2)
##      r3 = Rotor(12, 3)
##      wrapper = RotorWrapper([r1, r2, r3])
##
## given a char c that has already been gathered, we might have something like this next:
##      wrapper.handle_input(c)
##
## Internally, this will check each rotor position and rotate them accordingly, as noted
## in the rotor class
## Mechanically, each rotor position is rotated as stated above after the letter is encoded
##
## The rotor wrapper also contains a reflector map that shifts the character once more before
## being re-input in to the rotor system for a second translation route. According to the technical
## specifications at https://www.codesandciphers.org.uk/enigma/rotorspec.htm, there are 4 reflector
## types: reflector B, reflector C, reflector B Dünn, and reflector C Dünn

class RotorWrapper():
    reflectors_map = {
        "B": Reflector.reflectorB,
        "C": Reflector.reflectorC,
        "B Dunn": Reflector.reflectorB_Dunn,
        "C Dunn": Reflector.reflectorC_Dunn
    }

    def __init__(self, rotors, reflector):
        self._rotors = rotors if len(rotors) == 3 else []
        if (len(self._rotors) == 0):
            raise Exception("The Enigma Machine requires exaclty 3 rotors!")
        
        self._reflector = self.reflectors_map[reflector] if reflector in self.reflectors_map else {}
        if self._reflector == {}:
            raise Exception("Invalid reflector type input. Please select from [ B, C, B Dunn, C Dunn ].")

    ## Method to handle inputs
    ## We want to achieve a few things with this method
    ## The first of which is 




        
