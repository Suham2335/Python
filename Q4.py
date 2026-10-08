sentence = input("Enter a sentence: ")

sentence = "_".join(sentence.split())
sentence = sentence.lower()

words = sentence.split()

print("Number of words:", len(words))
print("Python appears:", words.count("python"), "times")

longest = max(words, key=len)

print("Longest word:", longest)