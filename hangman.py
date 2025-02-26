HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
lives = 7
dmg = -1
guessed = ""
string = ""
random = 'monkey'
for i in(random):
    string = string +"_"
print(string)
while lives > 0:
    guess = input('Enter a letter: ')  
    if guess == "":
        print("You have to enter a letter.")
    if guess in guessed:
        print("You have already guessed this letter")
        print("your list of guessed letters is", guessed)
    elif guess in random:
        amount = random.count(guess)
        index = random.find(guess)
        string = string[0:index]+guess + string[index + 1:]
    else:
        lives = lives - 1
        dmg += 1
        print("you have", lives, "lives left")
        print(HANGMANPICS[dmg])
    print(string)
    guessed = guessed + guess + " "
    if lives == 0:
        print("GAME OVER, YOU RAN OUT OF LIVES!!")
    elif "_" not in string and lives > 1:
        print("CONGRATULATIONS, YOU WON!!")
        break