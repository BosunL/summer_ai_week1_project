import math as mathmatics
import random

result_1 = mathmatics.pow(2,4)
print("result_1 is", result_1)

result_2 = mathmatics.pow(16,1 )
print("result_2 is", result_2)

result_3= random.randint(0,100)
print("result_3 is", result_3)

names = ("Aaryllis" ,"Godson", "Emily" ,"Reina","Derin","Elena","Inacio")
print("Names after shuffling:", names)

result_4= random.choice(names)
print("Chosen name is: ", result_4)