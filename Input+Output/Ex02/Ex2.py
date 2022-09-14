# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
# Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.

# Expected Output:

# For example: print('Name', 'Is', 'James') will display Name**Is**James

string1 = input("\nInsira a primeira palavra:")
string2 = input("\nInsira a segunda palavra:")
string3 = input("\nInsira a terceira palavra:")

print('Reformatei as três palavras para "%s**%s**%s", missão cumprida' % (string1, string2, string3))