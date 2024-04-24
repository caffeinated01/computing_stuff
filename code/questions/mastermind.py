"""
Mastermind
Red, Yellow, Green, Blue, White, Black
random sequence of color generated
player guesses
using White and Black pegs, game tells player which are correct
black --> correct color, and position
white --> correct color only
"""
import random

class Game:
    def __init__(self, attempts, combis):
        """
        Initialise variables
        """
        # Dictionary for colour name to corresponding emoji
        self.colors = {
            'r': '🟥',
            'y': '🟨',
            'g': '🟩',
            'b': '🟦',
            'w': '⬜',
            'd': '⬛',
        }
        # Dictionary for accuracy to corresponding emoji
        self.pegs = {            
            'w': '⬜',
            'b': '⬛',
            '?': '❔',
        }
        self.attempts = attempts
        self.combis = combis
        self.turns = 1
        # Generate a the answer
        self.sequence = [random.choice([i for i in self.colors.keys()]) for i in range(combis)]
        # Current accuracy of guess
        self.state = [self.pegs['?'] for i in range(combis)]
        # Generate empty boxes. This list is to save all player's gueses for displaying
        self.steps = [['☐' for i in range(combis)] for i in range(attempts)]
        # Bool for if player won or not
        self.won = False

    def draw_board(self):
        """
        Draw mastermind board
        """
        # Initialise empty docstring
        steps = """"""
        # Loop through all of the guesses player has made, add to the docstring
        for i in self.steps:
            steps = steps + "\n" + " " + "  ".join(i)
        
        # Print board with accuracy of guess as well as player's guesses
        board = f"""-============-\n {" ".join(self.state)}\n{steps}\n-============-
        """
        print(board)
    
    def turn(self):
        """
        Called each time for player to make guess, main game logic
        """
        guess = input(f'Turn {self.turns}, Guess, ')
        # Input validation
        if len(guess) != self.combis:
            print(f"Guess must have {self.combis} colours, try again.")
            return
        for i in guess:
            if i not in self.colors.keys():
                print(f"Invalid colour, {i}, try again.")
                return
        
        # Split guess into each individual color
        g = [i.lower() for i in guess]
        
        # Empty lists to store the guess of player and generate accuracy of guess respectively
        this = []
        state = []

        # Check accuracy of guess
        for i in range(len(g)):
            if g[i] == self.sequence[i]:
                state.append(self.pegs['b'])
            elif g[i] in self.sequence:
                state.append(self.pegs['w'])
            else:
                state.append(self.pegs['?'])
            
            this.append(self.colors[g[i]])
        
        # Save guess and accuracy
        self.steps[self.turns-1] = this
        self.state = state
        
        # Check if won, if yes set bool to True so program will terminate in main loop
        if self.state == [self.pegs['b'] for i in range(self.combis)]:
            self.won = True
            return

        # Increment turn
        self.turns += 1
    
    def win(self):
        """
        Function for winning
        """
        self.draw_board()
        print(f" I'm impressed...You beat the MASTERMIND in {self.turns} turn(s)!")
    
    def over(self):
        """
        Function for losing
        """
        self.draw_board()
        print("You suck at mastermind")
        print(f"The actual sequence, {' '.join([self.colors[i] for i in self.sequence])}")
    def start(self):
        """
        Main loop of game
        """
        print("""
  __  __                 _                   __  __   _               _ 
 |  \/  |   __ _   ___  | |_    ___   _ __  |  \/  | (_)  _ __     __| |
 | |\/| |  / _` | / __| | __|  / _ \ | '__| | |\/| | | | | '_ \   / _` |
 | |  | | | (_| | \__ \ | |_  |  __/ | |    | |  | | | | | | | | | (_| |
 |_|  |_|  \__,_| |___/  \__|  \___| |_|    |_|  |_| |_| |_| |_|  \__,_|
                                                                        
        """)
        print("1. Learn how to play?\n2. Play now")
        choice = input()
        # Print instructions
        if choice == '1':
            print("""
A random sequence of colours is generated.
Your goal is to guess the colours; For example, if 🟥🟩🟦⬛ is generated, your input to guess would be RGBD
All colours available are,
R: 🟥,
Y: 🟨,
G: 🟩,
B: 🟦,
W: ⬜'
D: ⬛,
    
After each guess, the top of the board will indicate your accuracy
⬛ signifies correct colour and correct position
⬜ signifies correct colour, but incorrect position
❔ signifies wrong colour / no guesses yet
GLHF!
""")
        # Loop until number of attempts maxed out
        while self.turns != self.attempts + 1:
            # If bool evaluates to be true, call win function and terminate
            if self.won:
                self.win()
                return
            self.draw_board()
            self.turn()
        
        # If the loop is over, means number of attempts maxed out without winning, so call lose function
        self.over()
        
# Generate new game with 10 max attempts, and 4 colours per guess
game = Game(10, 4)
# Call main loop of game
game.start()
