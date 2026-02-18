#Customer Action(Click,Scroll,Exit)

import itertools
import random

print("Customer Action Analysis")

actions=["Click","Scroll","Exit"]

sample_space=list(itertools.product(actions,repeat=2))

print("sample Space : ")
print(sample_space)
print("\nTotal outcomes in sample space :",len(sample_space))

event_E=[outcome for outcome in sample_space if "Click" in outcome]

print("\nEvent E (At least one click) :")
print(event_E)

probability_E=len(event_E)/len(sample_space)

print("\nProbability of at least one Click :")
print("P(E) =",probability_E)
print("Fraction form : {}/{}".format(len(event_E),len(sample_space)))


#Dice Simulation

print("\nDice Simulation")

trials=1000
count_sum_7=0

for _ in range(trials):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    
    if dice1+dice2==7:
        count_sum_7+=1
        
experimental_probability=count_sum_7/trials
theoretical_probability=6/36

print("Number of Trials : ",trials)
print("Number of times sum=7 : ",count_sum_7)
print("Experimental Probability : ",experimental_probability)
print("Theoretical Probability : ",theoretical_probability)
        