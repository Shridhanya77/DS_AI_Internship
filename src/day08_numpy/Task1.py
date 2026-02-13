import numpy as np

scores = np.random.randint(50, 101, size=(5, 3))

mean_scores = scores.mean(axis=0)
centered_scores = scores - mean_scores

print("Original Scores (5 Students, 3Subjects) :\n")
print(scores)

print("\nMean of each subject : ")
print(mean_scores)

print("\nCentered Scores  : ")
print(centered_scores)
