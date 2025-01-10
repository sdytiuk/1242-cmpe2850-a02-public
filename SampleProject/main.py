import random
import string
import math

globalVar = 'CMPE2850'

def generate_random_words(num_words=100, word_length=5):
  """
  Generates a list of random words.

  Args:
    num_words: The number of words to generate.
    word_length: The length of each word.

  Returns:
    A list of randomly generated words.
  """
  #print("What is globalvar?", globalVar)
  globalVarLocal = globalVar + 'B'
  print("What is globalvar?", globalVar)
  letters = string.ascii_lowercase
  words = []
  for _ in range(num_words):
    word = ''.join(random.choice(letters) for _ in range(word_length))
    words.append(word)
  return words

def count_word_occurrences(words):
  """
  Counts the occurrences of each word in the given list.

  Args:
    words: A list of words.

  Returns:
    A dictionary where keys are words and values are their counts.
  """
  word_counts = {}
  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1
  return word_counts


def todo():
    """

    :return:
    """
    pass

def todo2():
    pass

if __name__ == "__main__":
  random_words = generate_random_words()
  word_counts = count_word_occurrences(random_words)
  print(word_counts)

  #how do we find words that occur more than one time?
  #morethan1 = []
  t = ('Tane', 'Aldrich', 'Matt', 'Steven')
  l = ['Tane', 'Aldrich', 'Matt', 'Steven']
  l.append('Jacob')
  print(t[0], l[::-1])


  #let's get the random words that start with a
  print(sorted([x for x in random_words if x[0] in ['a','e','i','o','u']]))

  print(2/1, 5/3, 2//1, 5.2//3)

  h = 1
  ++h
  print(h)
  print(math.sqrt(25))
  print(25**0.5)

  print(random.choices(random_words, k=1)[0])



