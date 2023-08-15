#prompt user to give school details
#the details will be stored in vaiables

#Person Identifier
print("Kindly help us to fill the following ")
name = print("what is your name: ", input())
stream = print("which class are you in: ", input())

#performance
print("What was your performance on these subjects")
math = int(print(input()))
Eng = int(print(input()))
Phy = int(print(input()))

#Co_curriculum
print("what co curricular do you participate in")
co_curr = input()

#print our information
print("My name is", name)
print("My stream is", stream)
print("I had a score of", Eng,"English")
print("I participate in", co_curr)