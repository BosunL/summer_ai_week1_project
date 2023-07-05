import math
import random as chance

result_1 = math.pow(2,4)
print("result_1 is", result_1)

result_2 = math.pow(16,1)
print("result_2 is", result_2)

result_3= chance.randint(0,100)
print("result_3 is", result_3)

names = ("Aaryllis" ,"Godson", "Emily" ,"Reina","Derin","Elena","Inacio")
print("Names after shuffling:", names)

result_4= chance.choice(names)
print("Chosen name is: ", result_4)