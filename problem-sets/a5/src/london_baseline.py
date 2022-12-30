# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

from utils import evaluate_places

total, correct = evaluate_places('birth_dev.tsv', ['London' for _ in range(500)])
print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))