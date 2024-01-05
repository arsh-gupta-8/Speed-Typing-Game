words = "words.txt"

def main():
    print("Welcome to this game to check your typing speed")
    print("Lets begin")
    print("What difficulty would you like to play on Easy/Medium/Hard")
    choice = input("---   ")
    diff = None
    while diff == None:
        if choice.upper() == "EASY" or choice.upper() == "E":
            diff = "E"
        elif choice.upper() == "MEDIUM" or choice.upper() == "M":
            diff = "M"
        elif choice.upper() == "HARD" or choice.upper() == "H":
            diff = "H"
        else:
            print("Sorry this option is unavailable")
            print("What difficulty would you like to play on Easy/Medium/Hard")
            choice = input("---   ")

    paragraph = paragraph_collect(diff)
    game(paragraph)

def game():
    pass

def paragraph_collect(diff):
    all_sen = []
    with open(words, 'r') as doc:
        for sentence in doc:
            all_sen.append(sentence)
    print(all_sen)