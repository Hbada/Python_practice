# variables for trying out iPython; after %run, variables remain accessible
a = 25
b = 2

# something that can be timed with %timeit in iPython
c = [45, 33, 66, 25]

for item in c:
    d = item / 3
    print(d)

# now want to make new list ouf of the results in the for loop
count = 0
e = [] # empty list
for item in c:
    count = count + 1
    f = item / 3
    e.append(f)
print (e)
