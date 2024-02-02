import random


class Mode:
    def __init__(self):
        while True:
            print("\nEasy:1-10 life:5\nMedium:1-50 life:5\nHard:1-100 life:5")
            pick_mode = input("Pick a Operator:\n").upper()

            if pick_mode == "EASY":
                self.play(1, 10, 5, "EASY")
            elif pick_mode == "MEDIUM":
                self.play(1, 50, 5, "MEDIUM")
            elif pick_mode == "HARD":
                self.play(1, 100, 5, "HARD")
            elif pick_mode == "BYPASS":
                self.play(1, 100, 5, "HARD_BYPASS")
            elif pick_mode == "LUCKY":
                self.lucky()
            elif pick_mode == "DEV":
                self.dev()
            elif pick_mode == "EXIT":
                break

    def play(self, start, end, max_lives, game_mode):
        random_num = random.randint(start, end)
        while game_mode != "HARD":
            hint_mode = input("HINT ON|OFF: ").upper()
            if hint_mode == "ON" or hint_mode == "OFF":
                break
            else:
                print("\nINVALID INPUT. PLEASE TRY AGAIN.")
        else:
            hint_mode = "OFF"
            print("NO HINT!! OFF OR HARD MODE.")

        print(f"\nMODE:{game_mode}\n")
        for life in range(max_lives, 0, -1):
            print(f"\nLIFE LEFT:{life}")
            pick = int(input("PICK A NUMBER:"))
            if hint_mode == "ON":
                if pick < random_num:
                    print(f"GREATER THAN:{pick}")
                elif pick > random_num:
                    print(f"LESS THAN:{pick}")

            if pick == random_num:
                print(f"\nYOU:{pick} IS EQUAL TO RANDOM:{random_num}")
                print(f"CONGRATS!! YOU WON THE {game_mode} MODE.")
                break
        else:
            print(f"\nRANDOM NUMBER:{random_num}")
            print("LOST!! YOU RUN OUT OF LIFE.")

    def lucky(self):
        print("WELCOME TO SECRET MODE")
        print("LUCKY:1-10 LIFE:1 HINT:OFF")

        random_num = random.randint(1, 10)
        print(random_num)

        for life in range(1, 0, -1):
            print(f"LIFE LEFT: {life}")
            pick = int(input("TRY YOUR LUCK:"))

            if pick == random_num:
                print(f"{pick} = {random_num}")
                print("YOU'RE SO LUCKY BOY!!!")
                print(f"LIFE LEFT:{life}")
                break
        else:
            print(f"\nRANDOM NUMBER:{random_num}")
            print("YOU'RE LUCK IS SUCK!!!")

    def dev(self):
        print("WELCOME TO DEV MODE")
        while True:
            try:
                num1 = int(input("INPUT STARTER NUMBER: "))
                num2 = int(input("INPUT END NUMBER: "))
                if num1 == num2:
                    print(f"\nERROR: FIRST NUMBER:{num1} AND SECOND NUMBER:{num2} IS SAME. PLEASE TRY AGAIN.")
                else:
                    max_lives = int(input("INPUT LIFE COUNT: "))
                    if max_lives <= 0:
                        max_lives = 1
                        print("\nDEFAULT LIFE MODE\n")
                    break
            except ValueError:
                print("\nINVALID INPUT: PLEASE ENTER A NUMBER. PLEASE TRY AGAIN.")

        while True:
            hint_mode = input("HINT ON|OFF: ").upper()
            if hint_mode == "ON" or hint_mode == "OFF":
                break
            else:
                print("\nINVALID INPUT. PLEASE TRY AGAIN.")

        while True:
            custom_message = input("CUSTOM MESSAGE ON|OFF: ").upper()
            if custom_message == "ON":
                message = input("WIN MESSAGE: ").upper()
                lost = input("LOST MESSAGE: ").upper()
                break
            elif custom_message == "OFF":
                message = "CONGRATS MY BOY!!!"
                lost = "NUH THAT ALL YOU CAN DO!!!"
                break

        print(f"\nDEV:{num1}-{num2} LIFE:{max_lives} HINT:{hint_mode} CUSTOM MESSAGE:{custom_message}\n")
        random_num = random.randint(num1, num2)

        for max_lives in range(max_lives, 0, -1):
            print(f"\nLIFE LEFT:{max_lives}")
            pick = int(input("PICK A NUMBER:"))
            if hint_mode == "ON":
                if pick < random_num:
                    print(f"GREATER THAN:{pick}")
                elif pick > random_num:
                    print(f"LESS THAN:{pick}")
            if pick == random_num:
                print(message)
                print(f"\nYOU:{pick} EQUAL TO RANDOM:{random_num}")
                print(f"LIFE LEFT:{max_lives}")
                break
        else:
            print(f"\nRANDOM NUMBER:{random_num}")
            print(lost)


Mode()
