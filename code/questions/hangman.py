import random
from time import sleep

class Game:
    def __init__(self, word):
        self.mistakes = 0
        self.turns = 1
        self.won = False
        self.word = word
        self.guessed = []
        self.state =["_" for i in range(len(self.word))]
        self.states = [
        """
        -------
        |     |
        |
        |
        |
        |
        |
        -------
        """, 
        """
        -------
        |     |
        |     O
        |
        |
        |
        |
        |-------
        """,
        """
        -------
        |     |
        |     O
        |    -|-
        |     
        |
        |
        |-------
        """,
        """
        -------
        |     |
        |     O
        |    -|-
        |     |
        |
        |
        |-------
        """,
        """
        -------
        |     |
        |     O
        |    -|-
        |     |
        |     
        |
        |-------
        """,
        """
        -------
        |     |
        |     O
        |    -|-
        |     |
        |    - -
        |
        |-------
        """,
        """
        -------
        |     
        |
        |     O  'You won!'
        |    -|-
        |     |
        |    | |
        |-------
        """
        ]
    
    def turn(self):
        if "".join(self.state) == self.word:
            self.win()
            return
        print(f"Turn {self.turns}, {5-self.mistakes} chance(s) left")
        print(f"To demoralise you, {self.mistakes} mistake(s) have been made 😈")
        print("Current state of the game:"," ".join(self.state))
        print(self.states[self.mistakes])
        guess = input("Now, you guess: ")
        self.turns += 1
        found_in_turn = False
        for i in range(len(self.word)):
            if self.word[i] == guess:
                self.state[i] = guess
                found_in_turn = True
        
        if found_in_turn == True:
            print(f"I'm impressed, you found the letter {guess}\n")
            return
        
        print("Another step closer to defeat, good job!\n")
        self.mistakes += 1
    
    def over(self):
        print("You have been defeated by immense vocabulary...")
        print(f"Suck it! The word was {self.word} 😂")
    
    def win(self):
        print(self.states[-1])
        print(f"Damn! The word {self.word} wasn't enough to defeat you! How could you have guessed it in {self.turns} turns with only {self.mistakes} mistakes?! NOOOOOOOOOOOOOOOOO 😭!")
        self.won = True
    
    def start(self):
        print("Welcome to Hangman v1269 Alpha Pre-Release ️🤯️")
        while self.mistakes != 5 and self.won == False:
            self.turn()
        if not self.won:
            self.over()
        

game = Game(random.choice(['babies', 'eagles', 'labels', 'pacify', 'packed', 'oafish', 'iambus']))


game.start()
