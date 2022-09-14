# Exercise 6: Write all content of a given file into a new file by skipping line number 5

# Create a test.txt file and add the below content to it.

# Given test.txt file:

# line1
# line2
# line3
# line4
# line5
# line6
# line7

# Expected Output: new_file.txt

# line1
# line2
# line3
# line4
# line6
# line7

with open('C:/Users/User/Dropbox/João Pedro/Estudos/Python/Input+Output/Ex06/test.txt','r') as fp:
    lines = fp.readlines()

with open('C:/Users/User/Dropbox/João Pedro/Estudos/Python/Input+Output/Ex06/new_file.txt','w') as fp:
    count = 0
    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            fp.write(line)
        count += 1