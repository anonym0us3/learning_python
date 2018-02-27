#def how_parrot():
#    print("he's pining for the fjords!")
#    
#how_parrot()
#
#def lumber(name):
#    if name.lower() == 'billy':
#        print(name + " likes pie! Pie Pie Pie Pie Pie Pie Pie!")
#    else:
#        print("{} sleeps all night and {} works all day!".format(name, name))
#              
#lumber("BiLly")
#
#even = bool(5 % 2 == 0)
#print(even)

try:
    count = int(input("random # goes here: "))
except ValueError:
    print("that's not a #")
else:
    print("hi " * count)