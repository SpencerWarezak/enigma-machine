## Enigma Machine Project
### By Spencer Warezak -- September 2023

### Inspiration
This project is inspired by the work of Alan Turing, who developed the Turing Machine to decode encrypted messages from Nazi forces during World War II sent via a device known as the Enigma Machine. The Enigma Machine was an incredibly complex encryption device for its time, consisting of an intricate web of wiring and rotor components to create a circuit system that employed caesar cyphers with states changes each time an input was received. The impetus for this small project was borne from my love of the movie <i>The Imitation Game</i>, as well as my interest in cryptography. 

### Overview
The barebones of this implementation will include number of classes simulating the individual components of the Enigma Machine. Let us think of an Enigma Machine class as being a wrapper from all of the internal components of the Enigma Machine, with attribute fields representing the wiring between components. We must account for global states in order to keep track of states between rotors, as well as output from the plugboard.

The rotor will maintain a few different states, most important being the ring setting, which is initially set by the user but them self-modifies as inputs are received, and are highly dependent on the ring settings of the peer rotors.

### Resources
In order to better understand the internals of the Enigma Machine, I refereced a number of resources that I will update as the project increases in complexity. For now, here is what I have referenced:
- https://www.youtube.com/watch?v=ybkkiGtJmkM
- https://www.codesandciphers.org.uk/enigma/rotorspec.htm