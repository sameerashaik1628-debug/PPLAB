import random
ran=random.randint(1,100)
guess=int(input("Enter a number"));
print(ran)
if(guess==ran):
    print("your guess is right");
else:
    print("your guess is wrong");
