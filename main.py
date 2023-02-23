import random

logo ="""
___________.__         ___________               ___________                                           
\__    ___/|__| ____   \__    ___/____    ____   \__    ___/___   ____      _________    _____   ____  
  |    |   |  |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \    / ___\__  \  /     \_/ __ \ 
  |    |   |  \  \___    |    |   / __ \\  \___    |    |(  <_> )  ___/   / /_/  > __ \|  Y Y  \  ___/ 
  |____|   |__|\___  >   |____|  (____  /\___  >   |____| \____/ \___  >  \___  (____  /__|_|  /\___  >
                   \/                 \/     \/                      \/  /_____/     \/      \/     \/ 
"""

num=[0,1,2,3,4,5,6,7,8]
print(f""" {num[0]} | {num[1]} | {num[2]}\n===========\n {num[3]} | {num[4]} | {num[5]}\n===========\n {num[6]} | {num[7]} | {num[8]}""")

def choose_number(num_list1, num_list2):
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    number_choose = random.choice(number)
    while number_choose in num_list1 or number_choose in num_list2:
        number_choose = random.choice(number)
        continue
    return number_choose


def check_numbers(number_list):
    check=False
    win_numbers = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
    for win_element in win_numbers:
        check = all(item in number_list for item in win_element)
        if check:
            return check
    return check


def play_game():
    print(logo)
    user_nums = []
    computer_nums = []
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(f""" {num[0]} | {num[1]} | {num[2]}\n===========\n {num[3]} | {num[4]} | {num[5]}\n===========\n {num[6]} | {num[7]} | {num[8]}""")
    user_choose = input("Please choose the player O or X ?")
    if user_choose == "O":
        computer_choose ="X"
    else:
        computer_choose = "O"

    is_game_over = False
    while not is_game_over:
        user_choose_loc = int(input("Please choose the number ?"))
        if user_choose_loc in user_nums or user_choose_loc in computer_nums:
            print("Number has been chose, please select another number.")
        else:
            user_nums.append(user_choose_loc)
            computer_choose_loc = choose_number(user_nums, computer_nums)
            computer_nums.append(computer_choose_loc)
            num[user_choose_loc] = user_choose
            num[computer_choose_loc] = computer_choose
            print(
                f""" {num[0]} | {num[1]} | {num[2]}\n===========\n {num[3]} | {num[4]} | {num[5]}\n===========\n {num[6]} | {num[7]} | {num[8]}""")

            if check_numbers(user_nums):
                print("Congratulates!!!You win")
                is_game_over = True
            elif check_numbers(computer_nums):
                print("Lose,oppenent win")
                is_game_over = True
            else:
                if (len(user_nums)+len(computer_nums))==9:
                    print("It's a drawer")
                    is_game_over = True

while input("Do you want to play a Tic Tac Toe Game? Type 'y' or 'n':").lower()=='y':
    play_game()