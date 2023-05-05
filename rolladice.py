import random
response= input("press y to roll your dice and anything to exit")
while response == "y":
    num = random.randint(1,6)
    print(num)
    response= input("press y to roll again and anything to exit")
    

print("\n")