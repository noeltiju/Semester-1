from random import randrange

def word_printer(word,input):
    print()
    letters = []
    for i in range(len(word)):
    
        if input[i] == word[i]:
            print(input[i] + " ",end="")


        else:
            if input[i] in word:
                letters.append(input[i])
            print("_ ",end = "")

    print("\n")

    if letters:
        print(f"{letters} are there in the word but not in the correct places\n")

words = ['Abuse', 'Adult', 'Agent', 'Anger', 'Apple', 'Award', 'Basis', 'Beach', 'Birth', 'Block', 'Blood', 'Board', 'Brain', 'Bread', 'Break', 'Brown', 'Buyer', 'Cause', 'Chain', 'Chair', 'Chest', 'Chief', 'Child', 'China', 'Claim', 'Class', 'Clock', 'Coach', 'Coast', 'Court', 'Cover', 'Cream', 'Crime', 'Cross', 'Crowd', 'Crown', 'Cycle', 'Dance', 'Death', 'Depth', 'Doubt', 'Draft', 'Drama', 'Dream', 'Dress', 'Drink', 'Drive']

random_word = "noele"
tries = 5
while tries > 0:
    print(f"Tries left are: {tries}")

    word_input = input("Enter word: ").lower()

    if len(word_input) != len(random_word):
        print("INVALID INPUT")
        continue

    if random_word == word_input:
        print("You won!")
        print("GAME OVER")
        break

    word_printer(random_word,word_input)
    tries-=1

else:
    print("Correct word was: " + random_word)
    print("Chances over!")
    print("GAME OVER")


    

        
