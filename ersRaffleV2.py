import random

string_input = raw_input("Enter contestant names separated by comma: ")

winner = string_input.split(",")
print winner
print "And the winner is ......" 
print random.choice(winner)