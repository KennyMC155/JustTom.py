def numbSearch(minN, maxN):
    return  (minN + maxN)//2

def main_menu():
    print("Enter number of game you want:")
    print("1)  Guess number")
    print("2)  Calculate something(+,-,/,*)")
    print("3)  STOP the game  ")


def searchingGame():
    print("Enter two numbers: the minimum number and maximum nuber")
    print ("First number will be min(Please not less -100)")
    minN = int(input())
    print("Second number will be max(Please  not more 100)")
    maxN = int(input())
    x = numbSearch(minN, maxN)
    print(f"So,is your number {x}???")  
    print("Enter 'y' if my  guess is correct, 'h' if I should search higher or 'l' if lower")
    letter = str(input())
    while letter != 'y':
        if letter == 'h':
            minN = x
            x = numbSearch(minN, maxN)
            print(f"So,is your number {x} (enter 'y','h','l')???")
            letter = str(input())
        elif letter  == 'l':
            maxN = x
            x  = numbSearch(minN, maxN)
            print(f"So,is your number {x} (enter 'y','h','l')???")
            letter = str(input())
        else:
            print("Sorry,I didn't undersand you(enter 'y','h','l')?")
            letter = str(input())
    else:
        print(f"Great, so {x} is your number")   



def mathematicOper():  
    print("So,we are going to calculate something, I just need to knowe x,y and mathematic operation")
    result = 'None'
    print("Enter X")
    x = int(input())
    print("Enter Y")
    y = int(input())
    print("Enter math operation(+,-,*,/,^)")
    mathoper = str(input())
    
    operation_by_operator = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '^': lambda x, y: x ** y,
    }
    
    if mathoper == "/" and y == 0:
        print("Sorry can't divide to 0")   
    elif mathoper not in operation_by_operator:
        print("Sorry can't do that")
    else:
        operation = operation_by_operator[mathoper]
        result = operation(x, y)
        print (f"So the result will be {result}")
          
          
          
          
          
          