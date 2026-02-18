#Bayes' Theorem

print("Bayes' Theorem - Spam Filter Example")

p_spam=0.1
p_ham=0.9

p_free_given_spam=0.9
p_free_given_ham=0.05

p_free=(p_free_given_spam*p_spam)+(p_free_given_ham*p_ham)

print("Total Probability of 'Free' appearing : ",p_free)

p_spam_given_free=(p_free_given_spam*p_spam)/p_free
print("Probability email is Spam given it contains 'Free' :",p_spam_given_free)
