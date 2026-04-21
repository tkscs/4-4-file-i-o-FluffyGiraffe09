# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

with open("romeo_and_juliet.txt", "r") as file:
    string = file.read()

# Count how many times the word "Juliet" appears
count = 0
for word in string.split(" "):
    if "juliet" in word.lower():
        count = count + 1
print(count)