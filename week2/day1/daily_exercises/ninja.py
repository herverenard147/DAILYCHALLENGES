# # Exercise 1

3 <= 3 < 9 # True 

3 == 3 == 3 # True

bool(0) # False

bool(5 == "5") # False

bool(4 == 4) == bool("4" == "4") # True

bool(bool(None))    # False

x = (1 == True) 
y = (1 == False)
a = True + 4 
b = False + 10

print("x is", x) # True
print("y is", y) # False
print("a:", a) # 5
print("b:", b) # 10

# # Exercise 2

# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

longest_sentence = ""
while True:
    sentence = input("Enter the longest sentence you can without the character 'A': ")
    if 'A' in sentence or 'a' in sentence:
        print("The sentence contains the character 'A'. Try again.")
    elif len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! You have set a new longest sentence.")
    else:
        print("The sentence is not longer than the current longest sentence. Try again.")


# # Exercise 3

# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

paragraph = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

print("The paragraph contains", len(paragraph), "characters.")
print("The paragraph contains", len(paragraph.split(".")), "sentences.")
print("The paragraph contains", len(paragraph.split()), "words.")
print("The paragraph contains", len(set(paragraph.split())), "unique words.")
print("The paragraph contains", len(paragraph.strip()), "non-whitespace characters.")

if len(paragraph.split(".")) > 0:
    print("The average amount of words per sentence is", len(paragraph.split()) / len(paragraph.split(".")))
else:
    print("The paragraph contains no sentences.")

print("The paragraph contains", len(paragraph.split()) - len(set(paragraph.split())), "non-unique words.")      