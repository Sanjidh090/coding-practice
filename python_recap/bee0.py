WORDS = {
    "PAIR": (4, 4),
    "HAIR": (4, 4),
    "CHAIR": (5, 5),
    "GRAPH": (7, 7)
}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")
    
    for word,(points,price) in WORDS.items():
        print(f"{word} is worth {points} points {price} dollars")
    while len(WORDS) > 0:
        print(f"{len(WORDS)} left!")
        guess = input("Guess a word: ")

        if guess == "GRAPH":
            WORDS.clear()
            print("YOu've won!")
        if guess in WORDS.keys():
            print(f"Good job! You scored {WORDS.pop(guess)}")
    print("That's the game!")

if __name__ == "__main__":
    main()
