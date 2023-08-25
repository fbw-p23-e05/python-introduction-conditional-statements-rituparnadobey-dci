play = True

while play == True:
    name = input('Please enter your name: ')
    print('Hey', name)
    quest = input("It's Saturday, wanna go outside!(yes/no): ")

    while quest.lower() != 'yes' or 'no':
         print('Please make a correct input')
         break

    if quest.lower() == 'no':
            print('HAVE A GREAT DAY, BYE!')
            break
            
    elif quest.lower() == 'yes':
        print('You have some options: \n1. Go to a Restaurant \n2. Go for a Movie \n3. or Play Video Game')
        place = int(input('What did you decide, please make an input: '))

        if place == 1:
            print('What would you like to eat: \n1. Italian \n2. Chinese \n3. Lebanese \n4. Turkish')
            cuisine = int(input('Please make a choice: '))
            print('Great Choice!', name)
            print('Check the nearby restaurants & reviews.')

        elif place == 2:
            print('Wanna go alone or go with friends: \n1. Go alone \n2. Go with friends')
            
            mind = int(input('Please make a choice (pick a num:1/2): '))
            if mind == 1:
                print('Great!', name)
                print('Check for the new released movies & nearby treaters.')
            elif mind == 2:
                print('Call your friend!')
                print('Check whether he/she is free or not.')

        elif place == 3:
            print('Turn on your PC and play your favorite game!')
    
        
    print('HAVE A GREAT DAY, BYE!')
 
    