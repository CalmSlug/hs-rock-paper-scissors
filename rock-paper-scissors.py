import random

user_name = ""
user_rating = ""
user_options = ""
valid_input_dynamic = ""
valid_input_full = ""


def introduction():
    global user_name
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")

def rating():
    global user_rating
    rating_dict = {}
    rating_file = open("rating.txt", "r")
    
    for line in rating_file:
        temp_list = line.split()
        rating_dict[temp_list[0]] = int(temp_list[1])

    rating_file.close()

    if user_name in rating_dict.keys():
        user_rating = rating_dict[user_name]

    else:
        user_rating = 0

def options():
    global user_options
    user_options = input()
    print("Okay, let's start")

def valid_input():
    global valid_input_dynamic
    global valid_input_full

    if user_options:
        valid_input_dynamic = user_options.split(",")

    else:
        valid_input_dynamic = ["rock", "paper", "scissors"]

    valid_input_static = ["!rating", "!exit"]
    valid_input_full = valid_input_dynamic + valid_input_static

def main_loop():
    global user_rating

    while True:
        user_input = input()
        pc_input = random.choice(valid_input_dynamic)

        if user_input not in valid_input_full:
            print("Invalid input")

        elif user_input == "!rating":
            print(f"Your rating: {user_rating}")

        elif user_input == "!exit":
            print("Bye!")
            break

        elif user_input == pc_input:
            user_rating += 50
            print(f"There is a draw ({pc_input})")

        else:
            middle = len(valid_input_dynamic)//2 + 1 # нашли середину списка
            position = valid_input_dynamic.index(user_input) + 1 # нашли, где этот элемент в списке

            if middle > position:  # нужно подвинуть вправо
                n = middle - position
#                print(type(n))
#                print(n)
                list_1 = (valid_input_dynamic[-n:] + valid_input_dynamic[:-n])

                if list_1.index(user_input) > list_1.index(pc_input):
                    user_rating += 100
                    print(f"Well done. The computer chose {pc_input} and failed")

                else:
                    print(f"Sorry, but the computer chose {pc_input}")

            elif middle < position:  # нужно подвинуть влево
                n = position - middle
#                print(type(n))
#                print(n)
                list_1 = (valid_input_dynamic[n:] + valid_input_dynamic[:n])

                if list_1.index(user_input) > list_1.index(pc_input):
                    user_rating += 100
                    print(f"Well done. The computer chose {pc_input} and failed")

                else:
                    print(f"Sorry, but the computer chose {pc_input}")

            else:  # не трогаем позицию

                if valid_input_dynamic.index(user_input) > valid_input_dynamic.index(pc_input):
                    user_rating += 100
                    print(f"Well done. The computer chose {pc_input} and failed")

                else:
                    print(f"Sorry, but the computer chose {pc_input}")


introduction()
rating()
options()
valid_input()
main_loop()
