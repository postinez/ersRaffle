import random

file = open(r"C:\Users\jonathan.postans\Desktop\Python\referrers.txt","r")
lines = file.readlines()

for word in lines:
	winner = word.split()

file.close()

print "And the winner is ......" 
print random.choice(winner)