letter1 = input()
letter2 = input()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

if alphabet.index(letter1) <= alphabet.index(letter2):
    print(letter1 + letter2)
else: 
    print(letter2 + letter1)
