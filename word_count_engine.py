# open file 
f = open("sample_text/Lorem.txt", "r")

# take data stream and store as variable 'data'
data = f.read()

# close file
f.close()


print(data)

# split stream into strings at each white space
words = data.split(" ")
print("The words in the text are:")
print(words)

# count the number of words
num_words = len(words)
print("The number of words is ", num_words)

# if any line breaks occur, split them
lines = data.split("\n")
print("The lines in the text are:")
print(lines)
print("The number of lines is", len(lines))


def word_count(str):
  counts = dict()
  words = str.split()

  for word in words:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1
  
  
  return counts

print(word_count(data))