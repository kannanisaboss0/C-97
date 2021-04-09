import random 


print("Welcome to Number Game! In this game you will compete against the computer! The computer produces a randomly generated number. Your job is to guess the number correctly. You will get 10 chances. Do it before the chances run out!")
print("Before we begin....Set the range of numbers between which the computer chooses. It is completely upto your discretion!")

range1=int(input("Minimum:"))
range2=int(input("Maximum:"))
randomNumber=str(random.randint(range1,range2))
guess=input("Great now the game has been set up! Enter a number to play the game")
chances=10

while(guess!=randomNumber):
    if(chances>0):  
        chances=chances-1
        guess=input("Enter your guess:")
        if(guess>randomNumber):
            print("The number is lower than your guess")
        elif(guess<randomNumber):
            print("The number is higher than your guess")   
        print(randomNumber)
        print(str(chances)+"  chances left")
        if(chances<=3):
            print("Hurry! Only "+str(chances)+" chances left!")
    else:
        print("You lost the game")
        print("The number was "+randomNumber)
        print("Here are the statistics:")
        print("Chances:10")
        print("Number:"+randomNumber)
        print("Minimum Range:"+str(range1))
        print("Maximum Range:"+str(range2))
        probability=(10/((range2-range1)+1))*100
        print("Probability of winning:"+str(probability)+"%")
        break      
        
else:
    print("Congratulations you have guessed the nubmer!") 
    print("The number was "+randomNumber)   
    print("Here are the statistics:")
    print("Chances:10")
    print("Number:"+randomNumber)
    print("Minimum Range:"+str(range1))
    print("Maximum Range:"+str(range2))
    probability=(10/((range2-range1)+1))*100
    print("Probability of winning:"+str(probability)+"%")
            
    
        
          
        