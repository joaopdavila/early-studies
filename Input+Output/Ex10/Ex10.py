# Exercise 10: Read line number 4 from the following file

# Create a test.txt file and add the below content to it.

# test.txt file:

# line1
# line2
# line3
# line4
# line5
# line6
# line7

with open(r'C:/Users/davil/Documents/Python Scripts/Input+Output/Ex10/test.txt','r') as fp:
    line = fp.readlines()
    print(line[3])