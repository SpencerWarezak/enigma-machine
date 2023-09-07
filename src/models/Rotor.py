## Rotor Class
## 
## This class represents a rotor component in the Enigma Machine, and contains the following properties
##     Order (1, 2, or 3)
##     Ring Setting (1-26 corresponding to a-z)
##     -- this will be subject to change based on the order
## 
## The ring setting is subject to change on each iteration for order == 1
## The ring setting is subject to change on iterations for order == 2 where setting == ring setting of order == 1
## The ring setting is subject to change on iterations for order == 3 where setting == ring setting of order == 2
##
## When the ring setting for a rotor changes, we need to recalculate its caesar cipher mapping
## For example, if the ring setting is 1, then the letter a maps to a, b maps to b, etc.
## If the setting is 2, then a maps to b, b maps to c, c maps to d, etc.
## If the setting is 3, then a maps to c, b maps to d, c maps to e, etc.
## Thus, we need to maintain a cipher map for each rotor that takes into account this change, such that _letter = order(_letter) + (setting - 1) % ord(_letter)

class Rotor:
    def __init__(self, starting_pos: int, order: int):
        self._order = order if order in [1, 2, 3] else -1 ## order of the rotor (can be values 1-3)
        if self._order == -1:
            raise Exception("Invalid order submitted! Must be in the range of 1-3 (inclusive).")
        
        self._ring_setting = starting_pos if starting_pos in range(1, 27) else -1 ## set the ring setting initially to the starting position
        if self._ring_setting == -1:
            raise Exception("Invalid starting position! Must be in the range of 1-26 (inclusive).")

        self._cipher_map = {} ## set the cipher map to empty and then fill it
        self._set_cipher_map(starting_pos)

        ## notch position for the first rotor is q
        ## notch position for the second rotor is e
        ## notch position for the third rotor is v
        self._notch_position = (
            1 + ord('q') - ord('a') if self._order == 1
            else 1 + ord('e') - ord('a') if self._order == 2 
            else 1 + ord('v') - ord('a')
        )

        self._rotation_pending = False

    def _set_cipher_map(self, shift: int):
        offset = ord('a')
        for char in range(ord('a'), ord('z') + 1):
            cipher_char = chr((char - offset + shift - 1) % 26 + offset)
            self._cipher_map[chr(char)] = cipher_char

    def _rotate(self):
        self._ring_setting = self._ring_setting + 1 if self._ring_setting < 26 else 1
        self._set_cipher_map(self._ring_setting)
        self._rotation_pending = False

    def _check_for_rotation(self):
        if self._rotation_pending:
            self._rotate()

    def _trigger_rotation(self):
        self._rotation_pending = True