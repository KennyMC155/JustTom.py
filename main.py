from funk import searchingGame, mathematicOper
import time


print("Hello, my name is Tom, let's play")
time.sleep(1)
print("Enter number of game you want:")
print("1)  Guess number")
print("2)  Calculate something(+,-,/,*)")
print("3)  STOP the game  ")
gamenumber = int(input())
while gamenumber != 3:
    if gamenumber == 1:
        searchingGame()
        time.sleep(3)
        print("Enter number of game you want:")
        print("1)  Guess number")
        print("2)  Calculate something(+,-,/,*)")
        print("3)  STOP the game  ")
        gamenumber = int(input())
    elif gamenumber == 2:
        print("So,we are going to calculate something, I just need to knowe x,y and mathematic operation")
        z = mathematicOper()
        print(f"So the result will be {z}")
        time.sleep(3)
        print("Enter number of game you want:")
        print("1)  Guess number")
        print("2)  Calculate something(+,-,/,*)")
        print("3)  STOP the game  ")
        gamenumber = int(input())
else:
    print("Ok, bye")
    


