start = input("Do want to convert from minutes to hours or hours to minutes? Type m to convert into minutes or h to convert into hours.")

if start == "h":
    min = int(input("How many minutes are you converting into hours?"))
    print(str(min//60)+" hours")
elif start =="m":
    hours = int(input("How many hours are you converting into minutes?"))
    print(str(hours*60)+" minutes")
