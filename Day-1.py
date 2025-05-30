import random

Word_Choices_Easy = ["apple", "book", "chair", "dog", "fish", "grape", "hat", "ice", "jam", "kite"]
Word_Choices_Medium = ["banana", "laptop", "guitar", "mountain", "picture", "window", "bottle", "engine", "flower", "holiday"]
Word_Choices_Hard = ["adventure", "astronaut", "bicycle", "difficult", "knowledge", "psychology", "microscope", "chocolate", "elephant", "triangle"]
List_Of_Words = [Word_Choices_Easy, Word_Choices_Medium, Word_Choices_Hard]

while   True:
    Dificulty_Chosen = int(input("SELECT DIFICULTY LEVEL - TYPE - '1' FOR EASY | '2' FOR MEDIUM | '3' FOR HARD "))
    Confirmed_Dificulty = None

    if Dificulty_Chosen in [1,2,3]:
        Confirmed_Dificulty = Dificulty_Chosen
        break
    else:
        print ("Enter a valid option, Dummie!")

# Chosen_Difficulty = 0

# if Dificulty_Chosen == 1:
#     Chosen_Difficulty = 1
# elif Dificulty_Chosen == 2:
#     Chosen_Difficulty = 2
# elif Dificulty_Chosen == 3:
#     Chosen_Difficulty = 3
# else:
#     print("Enter a valid choice dummie!")

Chosen_Word = random.choice(List_Of_Words[Confirmed_Dificulty - 1])

#print(List_Of_Words)
print(Chosen_Word)

Number_Of_Dashes = len(Chosen_Word)
Hidden_Word = ["_"] * Number_Of_Dashes
print(Hidden_Word)

print (f''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
                   

        Word to Guess => {Hidden_Word}
                   ''')

Guessed_Letter = input("Enter a single letter - ")

Letter_In = Chosen_Word.find(Guessed_Letter)

print(Letter_In)

# if Letter_In == -1:
#     print("You loose one life")
