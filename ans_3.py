from re import split
from collections import Counter
import itertools

sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen"]

word_tree =[]
k =0

for i in sentences:
    word_tree.append(split('\W+',sentences[k]))
    k += 1

sentence_list = list(itertools.chain.from_iterable(word_tree))
word_count = Counter(sentence_list)
print("Word trees = ",word_tree)
print("\nNumber of time each word appears: ",dict(word_count))
