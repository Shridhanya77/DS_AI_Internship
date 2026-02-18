import random

#Independent Event (Heads AND 6)

print("Independent Events (Heads AND 6)")

p_heads=1/2
p_six=1/6
p_independent=p_heads*p_six

print("Theoretical Proabability (Heads AND 6) : ",p_independent)

trials=1000
count_success=0
for _ in range(trials):
    coin=random.choice(["Heads","Tails"])
    die=random.randint(1,6)
    
    if coin=="Heads" and die==6:
        count_success +=1
        
experimental_independent=count_success/trials

print("Experimental Probability : ",experimental_independent)


#Dependent Event (Marbles without Replacement)
print("Dependent Event (Marbles without Replacement")
p_first_red=5/10
p_second_red=4/9
p_dependent=p_first_red*p_second_red

print("Theoretical Probability (Both Red) :",p_dependent)

trials=1000
count_both_red=0

for _ in range(trials):
    bag=["Red"]*5+["Blue"]*5
    
    first_pick=random.choice(bag)
    bag.remove(first_pick) #without replacement
    second_pick=random.choice(bag)
    
    if first_pick=="Red" and second_pick=="Red":
        count_both_red+=1
        
experimental_dependent=count_both_red/trials
print("Experimental Probability : ",experimental_dependent)
