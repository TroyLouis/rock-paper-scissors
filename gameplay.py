import random

print("*** Welcome to Rock, Paper, Scissors! ***")

values = ['rock','paper','scissors']

gamePlay = {('rock','paper'):{'computer': 1, 'challenger': 0},
          ('rock','rock'):{'computer': 0, 'challenger': 0},
          ('rock','scissors'):{'computer': 0, 'challenger': 1},
          ('paper','rock'):{'computer': 0, 'challenger': 1},
          ('paper','paper'):{'computer':0,'challenger':0},
          ('paper','scissors'):{'computer':1,'challenger':0},
          ('scissors','rock'):{'computer':1, 'challenger':0},
          ('scissors','paper'):{'computer':0, 'challenger':1},
          ('scissors','scissors'):{'computer':0, 'challenger':0}
          }

class Choices():

    userScore = 0
    computerScore = 0

    def __init__(self):
        pass

    def computerChoice(self):
        self.computerValue = random.choice(values)
        return "The computer chooses " + self.computerValue + "!"

    def challengerChoice(self):
        while True:
            try:
                self.challengerValue = input("Choose rock, paper, or scissors: ")
            except ValueError:
                continue
            if self.challengerValue.lower() not in (values):
                continue
            else:
                return "You chose " + self.challengerValue + "!"
                break

def scoreboard():
    return "The score is {} to {}".format(Choices.userScore, Choices.computerScore)

def whoWon(challengerValue,computerValue):
    Choices.userScore += gamePlay[challengerValue,computerValue]['challenger']
    Choices.computerScore += gamePlay[challengerValue,computerValue]['computer']

while True:

    choice = Choices()
    challenger = choice.challengerChoice()
    print(challenger)
    computer = choice.computerChoice()
    print(computer)
    whoWon(choice.challengerValue, choice.computerValue)
    score = scoreboard()
    print(score)

    if Choices.userScore == 5:
        print("You win!")
        break
    elif Choices.computerScore == 5:
        print("You lose!")
        break
