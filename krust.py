import random
 
options = ("akmens","papīrs","šķēres")
player = None
computer = random.choice(options)

while player not in options:
    player = input("enter:")


print(f"Player; {player}")
print(f"Comuter; {computer}")