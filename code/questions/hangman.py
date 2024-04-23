import random
from time import sleep

class Game:
    def __init__(self, word):
        """
        Initialise variables needed
        """
        self.mistakes = 0 # Counts number of mistakes
        self.turns = 1 # Counts number of tunrs
        self.won = False # Bool to store whether player has won
        self.word = word # Word to be guessed
        self.state =["_" for i in range(len(self.word))] # Initialises a list of all unguessed letters represented by underscores "_"
        self.states = [ # Ascii art for each time the game progresses
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
        |     |
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
        """
        Function to handle guessing and checking if player found letter
        """
        if "".join(self.state) == self.word: # If the list of guessed letters joined is equal to word to be guessed, call win 
            self.win()
            return
        # Print out information of current turn --> no. of mistakes etc.
        print(f"Turn {self.turns}, {5-self.mistakes} chance(s) left")
        print(f"To demoralise you, {self.mistakes} mistake(s) have been made 😈")
        print("Current state of the game:"," ".join(self.state))
        print(self.states[self.mistakes])
        guess = input("Now, you guess: ")
        self.turns += 1
        found_in_turn = False
        # Replace each underscore with the letter if it is found in the word to be guessed
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
        """
        Function called when player loses (i.e. runs out of tries)
        """
        print(self.states[self.mistakes])
        print("You have been defeated by immense vocabulary...")
        print(f"Suck it! The word was {self.word} 😂")
    
    def win(self):
        """
        Function called when player wins
        """
        print(self.states[-1])
        print(f"Damn! The word {self.word} wasn't enough to defeat you! How could you have guessed it in {self.turns} turns with only {self.mistakes} mistakes?! NOOOOOOOOOOOOOOOOO 😭!")
        self.won = True
    
    def start(self):
        print("Welcome to Hangman v1269 Alpha Pre-Release ️🤯️")
        # Main loop that runs forever until a) Player guesses wrongly 5 times or b) Player has won
        while self.mistakes != 5 and self.won == False:
            self.turn()
        if not self.won:
            self.over()
        
# Make new variable with class of Game
game = Game(random.choice(['babies', 'eagles', 'labels', 'pacify', 'packed', 'oafish', 'iambus']))

# Call main function of game
game.start()
