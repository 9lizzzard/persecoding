dance = "<+&>"
input = input()

for char in dance:
    if char == input:
        position = dance.index(char)
        new_dance = dance[position:] 
        new_dance += dance
        new_dance += dance[:position]

print(new_dance)
