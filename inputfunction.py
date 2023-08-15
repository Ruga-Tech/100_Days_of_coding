#We are using raw_input() for this example
#define variable raw_input
#raw_input = input()
#The start of the code
print ("How old are you? ")
age = raw_input()

print ("How tall are you? ")
tall = raw_input()

print ("How much do you weigh? ")
weight = raw_input()

#This is the print statement
print ("So you're %r old, %r tall and %r heavy." % (age, tall, weight))