# Paper 1
## 1. Types of software licences
#public-domain #foss #proprietary #freeware #shareware
- ***Public domain software*** are software where legal protections have expired, either being **surrendered** or are **inapplicable**
- ***Free & Open Source Software (FOSS)*** are software where users are given authority to change, copy, study and share the software & its source code. *Copyrights* are still retained by owner.
	- There are a multitude of FOSS licences. Some of them include - BSD, MIT, GPL
- ***Creative Commons (CC) Licences*** are similar to FOSS, except they are for media like music, books, etc.
- ***Open Courseware*** are higher-education course materials such as videos and notes created by universities and distributed for free on the internet.
	- Typically licensed by *CC Licences*
- ***Proprietary Software*** are commercial software for which most of the legal protections under copyright are retained.
- ***Freeware*** is proprietary software that is available for use at no cost. (e.g. Adobe Reader)
- ***Shareware*** is demonstration software that is distributed for free but for a specific evaluation period only. (e.g. Adobe Photoshop 7-day trial)
## 2. **Intellectual property** and plagiarism
#intellectual-property  #plagiarism
-  ***Intellectual property*** are **creations of the mind** that have value and can exist purely as **data** with **no physical form**
- ***Copyright*** is the **legal right** of owners to control the **use and distribution** of their *intellectual property*
- ***Software piracy*** is the crime of **copying, distributing or using** proprietary software in a manner that is **prohibited by its licence**. Sometimes involves use of *cracks* (i.e. playing games from Steam Unlocked)
- ***Cracks*** are programs that **modify proprietary software** so that the software cannot detect that it is being **used illegally**
- ***Copyright infringement*** is the use of copyrighted work without permission of copyright owner
	- To avoid copyright infringement, 
		1. Check and follow website's terms and conditions
		2. Limit reproduction of copyrighted work up to 10%
		3. Consider using public domain material instead (not binded by copyright)
- ***Plagiarism*** is the act of passing someone else's work down as yours
- ***Citation*** is a statement to acknowledge and **provide credits** to the authors of **reproduced material** in books/articles
## 3. Conversion between number systems, as well as file size
#bytes #denary #binary #hexadecimal #number-systems
### File size
---

| Name of unit | Symbol | Size in bytes |                   |
| ------------ | ------ | ------------- | ----------------- |
| kilobyte     | KB     | 1,000         | 1,000             |
| kibibyte     | KiB    | 1,024         | 1,024             |
| megabyte     | MB     | 1,000^2       | 1,000,000         |
| mebibyte     | MiB    | 1,024^2       | 1,048,576         |
| gigabyte     | GB     | 1,000^3       | 1,000,000,000     |
| gibibyte     | GiB    | 1,024^3       | 1,073,741,824     |
| terabyte     | TB     | 1,000^4       | 1,000,000,000,000 |
| tebibyte     | TiB    | 1,024^4       | 1,099,511,627,776 |
- **Examples**
	1. 20 kilobyte to gigabyte$$(20×1000)÷(1000^3)=0.00002$$
	2. 50 gigabyte to mebibyte $$(50×1000^3)÷(1024^2)=47683.7$$
### Number systems
---
1. ***Denary*** is a base 10 number system. Is used in daily life.
2. ***Binary*** is a base 2 number system, made up of 0s and 1s. Used in computers.
3. ***Hexidecimal*** is a base 16 number system (each digit ranges from 0-9, and A-F). Used to represent **MAC addresses**, **IPv6 addresses**, **memory addresses**, and **colour codes**
	- Advantages of using Hexadecimals
		1. represent large numbers with fewer digits in a **compact form**.
		2. uses **less memory** to represent numbers
		3. is still **easily convertible** back and forth between binary and other number systems.
		4. easier for **identification** to specific memory locations when debugging etc.
### Conversion 
---


- **Binary to Denary:**
	\[*Start from right to left*]
	1. Each digit = value (0 or 1) * 2^(index ⟶ index starts at 0)
		- E.g. 0001 in denary is $(1×2^0)+(0×2^1)=1$
	2. Add the values of each digit.

- **Denary to Binary:**
	1. Repeatedly divide denary number by 2.
	2. Remainder (0 or 1) is the binary digit.
	3. Stop when quotient is 0.
	4. Reverse the order of remainders - that's your binary number!

- **Hex to Denary:**
	\[*Start from right to left*]
	1. Each digit = value (1-15) * 16^(index ⟶ index starts at 0)
	2. Sum the products for the denary answer.

- **Denary to Hex:**
	1. Repeatedly divide denary number by 16
	2. Record remainders as hex digits (0-F)
	3. Stop when quotient is 0.
	4. Reverse the order of remainders - that's your hex number!
## 4. Types of error cases
#syntax-error #logic-error #runtime-error
- ***Syntax errors*** occurs when source code does not follow syntax rules of language, causing translation process from source code to machine code to fail.
	- Common causes:
		- Spelling mistakes (includes case sensitivity)
		- Incorrect indentation
		- Invalid variable names
		- Incorrect sequencing of symbols (e.g. non-matching parentheses)
- ***Run-time errors*** occurs while program runs, causing program to crash/hang 
	- Common causes:
		- Trying to access a list item that does not exist (i.e. index out of range)
		- Mathematical errors (e.g. division by zero)
		- Incorrect use of functions or method
		- Input data that is not properly validated and handled
		- Conditions outside of the program’s control (e.g. running out of memory)
- ***Logic errors*** occurs while program runs, but doesn't cause program to crash/hang. Instead, it causes output to be different from expected one.
	- Common causes:
		- Implementation of flawed algorithms (e.g. checking incorrect conditions, overlooking requirements, inappropriate sequencing of code)
## 5. Phishing & Pharming
#scam #phishing #pharming
1. ***Phishing*** is the use of emails and fake websites that appear to be from reputable companies in order to steal personal information such as passwords and credit card numbers from users.
2. ***Pharming*** is the interception of request sent from a computer to a legitimate website and redirection to a fake website to steal personal data or credit card details.
	- It is more difficult to detect than phishing as the fake websites uses the same address as the real website
## 6. Impacts of Technology on Everyday Life
#education #finance #healthcare #transport #entertainment #ethical-issues
1. Education
	**\[Social impacts]**
	*(Pros)*
	- Better videos, simulations, collaboration, to make lessons more engaging
	- Use AR and VR to explore virtual spaces, makes field trips obsolete, cutting cost
	- Open sharing of information on platforms like Youtube (e.g. Yap Bee Leng Video)
	- Easy to research beyond the textbook
	- Help make more informed career decisions
	 *(Cons)*
	 - Harder to teach because student's attention span low due to social media
	 - Health problems like myopia, insomnia
	 - Discipline issues

	**\[Economic impacts]**
	*(Pros)*
	- Rise of open courseware leads to more for or non profit orgs to provide lessons
	*(Cons)*
	- Teachers need to up-skill to better use the technology
	- Learning institutions find it hard to maintain salaries of teachers as practically anything can be learnt online

	**\[Ethical issues]**
	- Should students be allowed to use phones in schools?
	- Can education technology be more effective than teachers?

2. Finance
	**\[Social impacts]**
	*(Pros)*
	- Can spend, borrow, invest on low cost & easy to use applications
	- No need for physical transactions (i.e. cash)
	- People more informed on smart financial decisions
	*(Cons)*
	- Cyberattacks and false information has lead to vulnerability to financial scams and get rich quick scams

	**\[Economic impacts]**
	 *(Pros)*
	 - Reduce time, cost and effort needed for payments, investments, fundraising, trading and/or data analytics
	 - Algorithmic trading with artificial intelligence, trade decisions are made in split seconds

	**\[Ethical issues]**
	- Should financial technology be limited to protect more vulnerable users?
	- Is it safe or acceptable to have financial markets controlled by secret algorithms instead of humans?

3. Healthcare
	**\[Social impacts]**
	*(Pros)*
	- Patients can be diagnosed online through video conference
		- Transfer of medical information is more secure
		- Allow people in remote areas or have limited mobility to get healthcare
	- 3D printing allows for more complex prosthetic body parts
	*(Cons)*
	- People don't trust machinery in providing healthcare
	- Patients might use misinformation from the internet to incorrectly diagnose themselves

	**\[Economic impacts]**
	 *(Pros)*
	- New market where the focus is automating healthcare
	*(Cons)*
	- Job displacement where robots take over
	
	**\[Ethical issues]**
	- Is it acceptable for robots to replace humans in providing certain kinds of healthcare?
	- Is it acceptable to transfer private medical information over the Internet?

4. Transportation
	**\[Social impacts]**
	*(Pros)*
	- Travelling is less stressful and more predictable due to detailed maps and real-time traffic analytics and public transport timings
	*(Cons)*
	- Some people are uncomfortable that their houses are used in mapping software without their permission
	
	**\[Economic impacts]**
	 *(Pros)*
	 - Rise of markets like self-driving vehicles
	 - Companies that offer on-demand taxi services through mobile apps
	 - Mapping software makes geographical information more accessible and useful for travellers and locals alike

	**\[Ethical issues]**
	- Is it acceptable for mapping companies to drive through neighbourhoods and take pictures to put them online?
	- What about the privacies of the people who were shown in the video footages or the pictures?
	
5. Entertainment
	**\[Social impacts]**
	*(Pros)*
	- More exciting and engaging forms of entertainment
	- Games have brought people together
	- Mobile games incentivises people to meet up IRL through in-game rewards (i.e. Pokemon Go)
	*(Cons)*
	- Addiction may arise
		- People will neglect what is important and lose social skills
	- Gambling habits may develop (i.e. Gatcha games)
	
	**\[Economic impacts]**
	 *(Pros)*
	 - Entertainment industry is growing with new opportunities opened by improvements in VR, AR and motion tracking
	 - Businesses are using strategies from game design to increase incentives for work

	**\[Ethical issues]**
	- Is it right for game companies to make money off addicted players? Through purchasing of special add ons and features to power up their characters.
	- Is it right for businesses to use technology to monitor employees more extensively

# Paper 2
#python
## Hangman variation
```python
import random

class Game:
    def __init__(self, word):
        """
        Initialise variables needed
        """
        self.mistakes = 0 # Counts number of mistakes
        self.turns = 1 # Counts number of tunrs
        self.won = False # Bool to store whether player has won
        self.word = word # Word to be guessed
        # Initialises a list of all unguessed letters represented by '-'
        self.state =["_" for i in range(len(self.word))]
    
    def turn(self):
        """
        Function to handle guessing and checking if player found letter
        """
        # If the list of guessed letters joined is equal to word to be guessed, call win 
        if "".join(self.state) == self.word:
            self.win()
            return
        # Print out information of current turn --> no. of mistakes etc.
        print(f"Turn {self.turns}, {5-self.mistakes} chance(s) left")
        print(f"{self.mistakes} mistake(s) have been made 😈")
        print(f"Progress: {' '.join(self.state)}")
        guess = input("Now, you guess: ")
        self.turns += 1
        found_in_turn = False
        # Replace each underscore with letter if it is found in the word to be guessed
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
        print("You have been defeated by immense vocabulary...")
        print(f"Suck it! The word was {self.word} 😂")
    
    def win(self):
        """
        Function called when player wins
        """
        print(f"""Damn! The word {self.word} wasn't enough to defeat you!
        How could you have guessed it in {self.turns} turns with only 
        {self.mistakes} mistakes?! NOOOOOOOOOOOOOOOOO 😭!""")
        self.won = True
    
    def start(self):
        print("Welcome to Hangman v1269 Alpha Pre-Release ️🤯️")
        # Main loop that runs forever until a) 5 times made or b) Player has won
        while self.mistakes != 5 and self.won == False:
            self.turn()
        if not self.won:
            self.over()
        
# Make new variable with class of Game
game = Game(random.choice(['babies', 'eagles', 'labels']))

# Call main function of game
game.start()
```