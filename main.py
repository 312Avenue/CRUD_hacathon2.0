from crud import crud
import time


choice = {
    'Listining': crud.listining,
    'Retrieve': crud.retrieve,
    'Update': crud.update,
    'Delete': crud.delete,
    'Create': crud.create
    }


while True:
    print('Actions: Create \n\t Listining \n\t Retrieve \n\t Update \n\t Delete')
    guess_choice = input('Choice action: ').capitalize()
    
    if guess_choice != 'Exit':
        if guess_choice == 'Create' or guess_choice == 'Listining':
            print(choice[guess_choice]())
        else:
            print(choice[guess_choice](input('Enter ID: ')))
    elif guess_choice == 'Exit':
        print('Bye')
        break
    else:
        print('Wrong input, try again')
        continue

    time.sleep(5)