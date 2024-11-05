"""
I created this program because every time I went to play a game called War,
people fought, saying that the dice had to be played at the same time,
with this program everything was solved
"""
import random
attacker = int(input("How many dice will the Attacker roll? "))
defensor = int(input("How many dice will the Defender roll? "))
dices_Attacker = []
dices_Defensor = []
count = 0
attacker_wins = 0
defensor_wins = 0

if attacker > 3 or defensor > 3:
    print("FAILED")
else:
    while count < attacker:
        dices_Attacker.append(random.randint(1, 6))
        count += 1
    count = 0
    while count < defensor:
        dices_Defensor.append(random.randint(1, 6))
        count += 1
    dices_Attacker.sort(reverse=True)
    dices_Defensor.sort(reverse=True)
    print(f"The Attacker's dices are:: {dices_Attacker}")
    print(f"The Defensor's dices are:: {dices_Defensor}")

for x,y in zip(dices_Attacker, dices_Defensor):
    if x > y:
        attacker_wins += 1
    else:
        defensor_wins += 1
print(f"The attacker won: {attacker_wins}, and Defensor won: {defensor_wins}")