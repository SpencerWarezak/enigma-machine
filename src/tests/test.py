import sys
sys.path.append('src/models')
from EnigmaMachine import EnigmaMachine

def main() -> int:
    plugboard = []
    seen = []
    plugboard_input = input("What would you like your plugboard settings to be? Please input pairings directly adjacent as such: ab cd ef ...: ")

    for pairing in plugboard_input.split(" "):
        if len(pairing) != 2:
            raise Exception("Please enter pairings of 2!")
        
        if pairing[0] not in seen and pairing[1] not in seen:
            seen.append(pairing[0])
            seen.append(pairing[1])
        else:
            raise Exception("Please do not enter duplicate values!")
        
        plugboard.append((pairing[0], pairing[1]))

    if len(plugboard) > 13:
        raise Exception("Please do not enter duplicates and leave pairings to 13 max!")
    
    reflector = input("Please selected a reflector. Your options are: [ B, C, B Dunn, C Dunn ]: ")

    starting_pos = []
    for _ in range(3):
        starting_pos.append(int(input("Please input a number 1-26 for the starting position of the rotor: ")))

    em = EnigmaMachine(starting_pos, reflector, plugboard)
    message = input("Please enter a string to encode. Enter 'exit' to exit: ")
    while (message != 'exit'):
        encoded_message = em.encode_message(message)
        decoded_message = em.encode_message(encoded_message)
        print(f"Encoded Message: {encoded_message}\nDecoded Message: {decoded_message}\n")
        message = input("Please enter a string to encode. Enter 'exit' to exit: ")

    return 0

main()