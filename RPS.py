import time
import random


class Game:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        while True:
            print("Choose:[2P|BOT]")
            self.game_mode = input("MODE:\n").upper()
            if self.game_mode == "BOT":
                for i in range(5 + 1):
                    print(f"[STARTING IN {i}s.]")
                    time.sleep(1)
                self.ai_mode()
                break
            elif self.game_mode == "2P":
                for i in range(5 + 1):
                    print(f"[STARTING IN {i}s.]")
                    time.sleep(1)
                self.pvp()
                break

    def ai_mode(self):
        while True:
            pick2 = None
            time.sleep(1)
            for i in range(random.randint(5, 20)):
                pick2 = random.choice(["R", "P", "S"])
                print(f"{"\n" * 100}BOT IS PICKING{"." * i}")
                time.sleep(1)
            print("\n" * 100)
            print("PLEASE ONLY INPUT THE [R, P, S]")
            print(f"[R:ROCK|P:PAPER|S:SCISSORS]")
            pick1 = input("PLAYER1:\n").upper()
            self.system(pick1=pick1, pick2=pick2, name1="PLAYER1", name2="BOT")

    def pvp(self):
        time.sleep(1)
        print("\n" * 100)
        print("PLEASE ONLY INPUT THE [R, P, S]")
        print(f"[R:ROCK|P:PAPER|S:SCISSORS]")
        pick1 = input(f"PLAYER1:").upper()
        print("\n" * 100)
        print("PLEASE ONLY INPUT THE [R, P, S]")
        print(f"[R:ROCK|P:PAPER|S:SCISSORS]")
        pick2 = input(f"PLAYER2:").upper()
        self.system(pick1=pick1, pick2=pick2, name1="PLAYER1", name2="PLAYER2")

    def system(self, pick1, pick2, name1, name2):
        if pick1 == pick2:
            print(f"\n[{name1}:{pick1}|{name2}:{pick2}]\nTIE")
            self.score1 += .5
            self.score2 += .5

        elif ((pick1 == 'P' and pick2 == 'R') or
              (pick1 == 'S' and pick2 == 'P') or
              (pick1 == 'R' and pick2 == 'S')):
            print(f"\n[{name1}:{pick1}|{name2}:{pick2}]")
            self.score1 += 1

        elif ((pick2 == 'P' and pick1 == 'R') or
              (pick2 == 'S' and pick1 == 'P') or
              (pick2 == 'R' and pick1 == 'S')):
            print(f"\n[{name1}:{pick1}|{name2}:{pick2}]")
            self.score2 += 1

        else:
            if self.game_mode == "2P":
                print(f"CHECK IF THE {pick1}|{pick2}, IS IN THE CHOICES. PLEASE TRY AGAIN.\n")
                time.sleep(5)
                self.pvp()
            elif self.game_mode == "BOT":
                print(f"CHECK IF THE {pick1}, IS IN THE CHOICES. PLEASE TRY AGAIN.\n")
                time.sleep(5)
                self.ai_mode()

        self.display_scores(name1=name1, name2=name2)

    def display_scores(self, name1, name2):
        print(f"SCORE:[{name1}:{self.score1}|{name2}:{self.score2}]\n")
        print("PLEASE WAIT 10s")
        time.sleep(5)
        if self.game_mode == "2P":
            time.sleep(5)
            self.pvp()
        elif self.game_mode == "BOT":
            time.sleep(5)
            self.ai_mode()


if __name__ == "__main__":
    Game()

print("Change name [Y:YES|N:NO]")