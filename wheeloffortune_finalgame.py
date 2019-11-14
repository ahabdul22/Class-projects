def getPhrase():
    Phrasebank = open("phrasebank.txt").read().splitlines()
    import random
    phrasenum = random.randint(0,100)
    phrase = Phrasebank[phrasenum]
    return phrasenum,phrase
def getCategory(phrasenum):
    category = 0
    if phrasenum < 20:
        category = "Before and After"
    elif phrasenum < 40:
        category = "Song Lyrics"
    elif phrasenum < 60:
        category = "Around the House"
    elif phrasenum < 80:
        category = "Food and Drink"
    else:
        category = "Same Name"
    return category
def phrasePrint(phrase):
    phraselen = len(phrase)
    blankphrase = ['_' for x in range(phraselen)]
    for x in range(phraselen):
        if phrase[x] == " ":
            blankphrase[x] = " "
        else:
            blankphrase[x] = "_"
        x += 1
    return phraselen,blankphrase
def spinTheWheel(phrase,blankphrase,winnings,consonantsguessed):
    import random
    moneyspin = [50,100,100,100,100,100,100,200,200,200,200,250,250,250,500,500,750,750,1000,2000,5000,10000,'Bankrupt','Bankrupt']
    consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    spinland = random.choice(moneyspin)
    if spinland == 'Bankrupt':
        winnings = 0
        print("Uh oh, you've spun a Bankrupt! Your winnings will go down to $0.")
    else:
        print("You've spun $",spinland,"!   ",end="")
        letter = str(input("Guess a letter: ")).upper()
        while letter not in consonants:
            print("Whoops, that's not a consonant!  ",end="")
            letter = str(input("Guess again: ")).upper()
        consonantsguessed.append(letter)
        lettercount = 0
        for x in range(len(phrase)):
            if phrase[x] == letter:
                lettercount += 1
                blankphrase[x] = letter
                x += 1
        if lettercount > 0:
            roundwinnings = spinland * lettercount
            winnings = winnings + roundwinnings
            print("Congratulations, " + letter + " appears in the phrase",lettercount,"times! You've won $",roundwinnings,"." )
        else:
            if winnings > spinland:
                winnings = winnings - spinland
            else:
                winnings = 0
            print("Sorry, " + letter + " does not appear in the puzzle. You will have $",spinland,"deducted from your winnings")
    return winnings,consonantsguessed
def buyAVowel(phrase,blankphrase,winnings,vowelsguessed):
    vowelcount = 0
    vowels = ['A','E','I','O','U']
    if winnings > 249:
        winnings -= 250
        print("Ok! $250 will be deducted from your winnings.",end="")
        vowelbought = str(input(" Which vowel would you like to buy (A, E, I, O, U)?: ")).upper()
        while vowelbought not in vowels:
            print("Whoops, that's not a vowel!  ",end="")
            vowelbought = str(input(" Which vowel would you like to buy (A, E, I, O, U)?: ")).upper()
        vowelsguessed.append(vowelbought)
        for x in range(len(phrase)):
            if phrase[x] == vowelbought:
                vowelcount += 1
                blankphrase[x] = vowelbought
                x += 1
        if vowelcount > 0:
            print("Congratulations, " + vowelbought + " appears in the phrase",vowelcount,"times!" )
        else:
            print("Sorry, " + vowelbought + " does not appear in the puzzle.")
    else:
        print("Sorry, you don't have enough winnings to buy a vowel!")
    return winnings,vowelsguessed
def solveThePuzzle(phrase,winnings,blankphrase,gameSolved):
    userguess = str(input("What's your best guess (be sure to enter your guess with single spaces!)?")).upper()
    if userguess == phrase:
        gameSolved = True
        print("That's correct - you solved the puzzle!")
        print("Congratulations, you've won the game!  Your winnings are $",winnings,".  Thank you for playing the Wheel of Fortune!")
    else:
        winnings = 0
        print("Sorry, that guess is incorrect!  Your winnings will start over at $0 :(")
    return winnings,gameSolved
def printStuff(blankphrase,vowelsguessed,consonantsguessed,winnings):
    print("The phrase is: " ,''.join(blankphrase))
    print("Vowels Guessed: " ,' '.join(vowelsguessed))
    print("Consonants Guessed: " ,' '.join(consonantsguessed))
    print("Your current winnings are: $" ,winnings)
def main():
    print("Welcome to the Wheel of Fortune!")
    phrasenum,phrase = getPhrase()
    category = getCategory(phrasenum)
    phraselen,blankphrase = phrasePrint(phrase)
    winnings = 0
    print("The phrase is: " ,''.join(blankphrase))
    print("The category is: " + category)
    print("Your current winnings are: $" ,winnings)
    vowelsguessed = []
    consonantsguessed = []
    gameSolved = False
    while gameSolved != True and len(vowelsguessed)+len(consonantsguessed) != 26:
        nextmove = str(input("Would you like to Spin the Wheel (type 'spin'), Buy a Vowel (type 'vowel'), or Solve the Puzzle (type 'solve')?"))
        if nextmove == 'spin':
            winnings,consonantsguessed = spinTheWheel(phrase,blankphrase,winnings,consonantsguessed)
            printStuff(blankphrase,vowelsguessed,consonantsguessed,winnings)
        elif nextmove == 'vowel':
            winnings,vowelsguessed = buyAVowel(phrase,blankphrase,winnings,vowelsguessed)
            printStuff(blankphrase,vowelsguessed,consonantsguessed,winnings)
        elif nextmove == 'solve':
            winnings,gameSolved = solveThePuzzle(phrase,winnings,blankphrase,gameSolved)
        else:
            print("Whoops, I don't recognize that input!  Try again.")
    if len(vowelsguessed)+len(consonantsguessed) == 26:
        winnings = 0
        print("Sorry, you've lost the game. Your winnings are $" ,winnings, ". Thank you for playing the Wheel of Fortune!")
if __name__ == '__main__':
    main()
