from sys import argv

script = raw_input("Script? ")
first = raw_input("First? ")
second = raw_input("Second? ")
third = raw_input("Third? ")

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
