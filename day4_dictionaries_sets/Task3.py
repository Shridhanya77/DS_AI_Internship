friend_a={"Python","Cooking","Hiking","Movies"}
friend_b={"Hiking","Gaming","Photography","Python"}
common_interests=friend_a & friend_b
all_interests=friend_a | friend_b
unique_to_a=friend_a-friend_b
print("Common interests :",common_interests)
print("All interests : " ,all_interests)
print("Interests only friend A has :" ,unique_to_a)
