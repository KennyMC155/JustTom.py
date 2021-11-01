from funk import searchingGame, mathematicOper,  main_menu
import time


print("Hello, my name is Tom, let's play")
time.sleep(2)
main_menu()
gamenumber = int(input())
while gamenumber != 3:
    if gamenumber == 1:
        searchingGame()
        time.sleep(3)
        main_menu()
        gamenumber = int(input())
    elif gamenumber == 2:
        time.sleep(3)
        mathematicOper()
        main_menu()
        gamenumber = int(input())
else:
    print("Ok, bye")
