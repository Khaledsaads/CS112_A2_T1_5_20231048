#File : CS112_A1_T2_Game 2 _20231048.py.
''' purpuse : it's game between to player , every one from them choose a number form 1 to 9 but if someone choose
a number it can not be choosen a gain. if one of them can reach to 15 by get the sum of three number form the
numbers that have been choosen by him first : he won the game
'''
#Author : khaled saad mahmoud mohammed
#ID :20231048

i=0

#allawed numbers
list_of_number=[1,2,3,4,5,6,7,8,9]

#numbers that the 1st player have been used
list_of_number1=[]
#numbers that the 2nd player have been used
list_of_number2=[]
while True:


    #the input of the first player
    print(" first player, it's your turn to enter the number:  ")
    while True :
     try:
        #input of the 1st player
        fnum=  int(input())
     except:
       print("You have to enter an integer input ")
     else:
         break

    #ensure that 1st player will use number from 1 to 9
    while fnum <0 or fnum>9:
        print ("Enter a valid number,please:  ")
        while True:
         try:

          #new input form the 1st player
          fnum = int(input())
         except:
            print("You have to enter an integer input:  ")
         else :
             break

    #forbidden 1st player to enter used number
    while fnum not in list_of_number:
        print("This number has taken before , please enter a new valid number:  ")
        while True:
         try:

           #new input from 1st player
           fnum = int(input())
         except:
             print("You have to enter an integer input:  ")
         else:
             break

    #remove choosen number from the list of allawed number to forbidden him using the same number agian
    list_of_number.remove(fnum)

    #add the used number from 1st to his list of used numbers
    list_of_number1.append(fnum)

    #check if he won or not
    if i==2 :
        if  list_of_number1[0] + list_of_number1[1] + list_of_number1[2] == 15:
             print("First player won the game ")
             print("numbers that have been taken by the 1st player is ", list_of_number1)
             print("numbers that have been taken by the 2nd player is ", list_of_number2)
             break
    elif i == 3:
        if list_of_number1[0] + list_of_number1[1] + list_of_number1[3] == 15 or list_of_number1[2] + \
                    list_of_number1[1] + list_of_number1[3] == 15 or list_of_number1[0] + list_of_number1[2] + \
                    list_of_number1[3] == 15:
             print("First player won the game")
             print("numbers that have been taken by the 1st player is ", list_of_number1)
             print("numbers that have been taken by the 2nd player is ", list_of_number2)
             break
    elif i == 4:
        if list_of_number1[0] + list_of_number1[1] + list_of_number1[3] == 15 or list_of_number1[2] + \
                list_of_number1[1] + list_of_number1[3] == 15 or list_of_number1[0] + list_of_number1[2] + \
                list_of_number1[3] == 15 or list_of_number1[0] + list_of_number1[1] + \
                list_of_number1[4] == 15 or list_of_number1[0] + list_of_number1[2] + \
                list_of_number1[4] == 15 or list_of_number1[0] + list_of_number1[3] + \
                list_of_number1[4] == 15:
            print("First player won the game")
            print("numbers that have been taken by the 1st player is ", list_of_number1)
            print("numbers that have been taken by the 2nd player is ", list_of_number2)
            break

    print ("numbers that have been taken by the 1st player is ",list_of_number1)
    print ("numbers that have been taken by the 2nd player is ",list_of_number2)
    print

    #if there is no winner and there is no element in the list of allawed number
    if list_of_number == []:
        print ("Draw")
        break
    print("second player , it's your turn to enter the number:  ")
    while True:
     try:
       #input form 2nd player
       lnum = int(input())
     except:
       print ("2nd player: You have enter an integer input:  ")
     else:
         break

    # ensure that 2nd player will use number from 1 to 9
    while lnum < 0 or lnum > 9:
        print("Enter a valid number,please:  ")
        while True:
          try:

          #new input form the 2nd player
            lnum = int(input())
          except:
             print("You have to enter an integer input:  ")
          else :
              break
    #forbidden 2nd player to enter used number
    while lnum not in list_of_number:            
        print("This number has taken before , please enter a new valid number:  ")
        while True:
         try:

           #new input from 2nd player
           lnum = int(input())
         except:
             print("You have to enter an integer input:  ")
         else:
             break 
    # remove choosen number from the list of allawed number to forbidden him using the same number agian
    list_of_number.remove(lnum)

    # add the used number from 1st to his list of used numbers
    list_of_number2.append(lnum)

    # check if he won or not
    if i == 2:
        if list_of_number2[0] + list_of_number2[1] + list_of_number2[2] == 15:
            print("second player won the game")
            print("numbers that have been taken by the 1st player is ", list_of_number1)
            print("numbers that have been taken by the 2nd player is ", list_of_number2)
            break
    elif i == 3:
        if list_of_number2[0] + list_of_number2[1] + list_of_number2[3] == 15 or list_of_number2[2] + \
                list_of_number2[1] + list_of_number2[3] == 15 or list_of_number2[0] + list_of_number2[2] + \
                list_of_number2[3] == 15:
            print("second player won the game")
            print("numbers that have been taken by the 1st player is ", list_of_number1)
            print("numbers that have been taken by the 2nd player is ", list_of_number2)
            break
    elif i == 4:

        if list_of_number2[0] + list_of_number2[1] + list_of_number2[3] == 15 or list_of_number2[2] + \
                list_of_number2[1] + list_of_number2[3] == 15 or list_of_number2[0] + list_of_number1[2] + \
                list_of_number2[3] == 15 or list_of_number2[0] + list_of_number2[1] + \
                list_of_number2[4] == 15 or list_of_number2[0] + list_of_number2[2] + \
                list_of_number2[4] == 15 or list_of_number2[0] + list_of_number2[3] + \
                list_of_number2[4] == 15:
            print("second player won the game")
            print("numbers that have been taken by the 1st player is ", list_of_number1)
            print("numbers that have been taken by the 2nd player is ", list_of_number2)
            break

    #to know The number of numbers entered
    i += 1
    print ("numbers that have been taken by the 1st player is ",list_of_number1)
    print ("numbers that have been taken by the 2nd player is ",list_of_number2)

