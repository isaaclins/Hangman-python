import random
import os


def clear_terminal():
    # Clear the terminal screen for Windows
    if os.name == 'nt':
        _ = os.system('cls')
        

# List of words to choose from
word_list = ["abruptly", 
"absurd", 
"abyss", 
"affix", 
"askew", 
"avenue", 
"awkward", 
"axiom", 
"azure", 
"bagpipes", 
"bandwagon", 
"banjo", 
"bayou", 
"beekeeper", 
"bikini", 
"blitz", 
"blizzard", 
"boggle", 
"bookworm", 
"boxcar", 
"boxful", 
"buckaroo", 
"buffalo", 
"buffoon", 
"buxom", 
"buzzard", 
"buzzing", 
"buzzwords", 
"caliph", 
"cobweb", 
"cockiness", 
"croquet", 
"crypt", 
"curacao", 
"cycle", 
"daiquiri", 
"dirndl", 
"disavow", 
"dizzying", 
"duplex", 
"dwarves", 
"embezzle", 
"equip", 
"espionage", 
"euouae", 
"exodus", 
"faking", 
"fishhook", 
"fixable", 
"fjord", 
"flapjack", 
"flopping", 
"fluffiness", 
"flyby", 
"foxglove", 
"frazzled", 
"frizzled", 
"fuchsia", 
"funny", 
"gabby", 
"galaxy", 
"galvanize", 
"gazebo", 
"giaour", 
"gizmo", 
"glowworm", 
"glyph", 
"gnarly", 
"gnostic", 
"gossip", 
"grogginess", 
"haiku", 
"haphazard", 
"hyphen", 
"iatrogenic", 
"icebox", 
"injury", 
"ivory", 
"ivy", 
"jackpot", 
"jaundice", 
"jawbreaker", 
"jaywalk", 
"jazziest", 
"jazzy", 
"jelly", 
"jigsaw", 
"jinx", 
"jiujitsu", 
"jockey", 
"jogging", 
"joking", 
"jovial", 
"joyful", 
"juicy", 
"jukebox", 
"jumbo", 
"kayak", 
"kazoo", 
"keyhole", 
"khaki", 
"kilobyte", 
"kiosk", 
"kitsch", 
"kiwifruit", 
"klutz", 
"knapsack", 
"larynx", 
"lengths", 
"lucky", 
"luxury", 
"lymph", 
"marquis", 
"matrix", 
"megahertz", 
"microwave", 
"mnemonic", 
"mystify", 
"naphtha", 
"nightclub", 
"nowadays", 
"numbskull", 
"nymph", 
"onyx", 
"ovary", 
"oxidize", 
"oxygen", 
"pajama", 
"peekaboo", 
"phlegm", 
"pixel", 
"pizazz", 
"pneumonia", 
"polka", 
"pshaw", 
"psyche", 
"puppy", 
"puzzling", 
"quartz", 
"queue", 
"quips", 
"quixotic", 
"quiz", 
"quizzes", 
"quorum", 
"razzmatazz", 
"rhubarb", 
"rhythm", 
"rickshaw", 
"schnapps", 
"scratch", 
"shiv", 
"snazzy", 
"sphinx", 
"spritz", 
"squawk", 
"staff", 
"strength", 
"strengths", 
"stretch", 
"stronghold", 
"stymied", 
"subway", 
"swivel", 
"syndrome", 
"thriftless", 
"thumbscrew", 
"topaz", 
"transcript", 
"transgress", 
"transplant", 
"triphthong", 
"twelfth", 
"twelfths", 
"unknown", 
"unworthy", 
"unzip", 
"uptown", 
"vaporize", 
"vixen", 
"vodka", 
"voodoo", 
"vortex", 
"voyeurism", 
"walkway", 
"waltz", 
"wave", 
"wavy", 
"waxy", 
"wellspring", 
"wheezy", 
"whiskey", 
"whizzing", 
"whomever", 
"wimpy", 
"witchcraft", 
"wizard", 
"woozy", 
"wristwatch", 
"wyvern", 
"xylophone", 
"yachtsman", 
"yippee", 
"yoked", 
"youthful", 
"yummy", 
"zephyr", 
"zigzag", 
"zigzagging", 
"zilch", 
"zipper", 
"zodiac", 
"zombie", 
]

def hangman():
    # Select a random word from the list
    word = random.choice(word_list)
    guessed_letters = []
    tries = 6

    # Main game loop
    while tries > 0:
        clear_terminal()
        # Print current status
        print("\n")
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("\nTries left:", tries)

        # Ask for user input
        guess = input("Enter a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        # Add the letter to the guessed_letters list
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            tries -= 1

        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You won!")
            print("The word was:", word)
            return

    # If the player runs out of tries
    print("\nGame over!")
    print("The word was:", word)

# Start the game
def main():
  hangman()
  
if __name__ == '__main__':
  main()
