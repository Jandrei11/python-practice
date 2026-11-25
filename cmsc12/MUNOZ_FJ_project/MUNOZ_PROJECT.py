#Name: Francis Jandrei Munoz
#Section: G-6L
#Description: A text twist game run on Python. Makes use of functions, persistence, dictionaries, imports, iterations, nested loops, Features the complete text twist experience in Python with extra features including a penalty and bonus system for the time. 

import time
import random
import os

def display_leaderboard(leaderboard): #function that returns the current ranking for the leaderboard
    print("=======LEADERBOARD=======")
    if len(leaderboard) == 0:
        print("No scores yet!")
        return
    print ("RANK   NAME          TIME   HIGHEST STAGE CLEARED")
    rank = 1
    for entry in leaderboard:
        print(f"{rank:<7}{entry[0]:<14}{entry[1]:<7}Stage {entry[2]}") #to align texts
        rank += 1

def jumble_word(word): #function that jumbles the words from the dictionary 
    letters = list(word) #turns the word to a list
    jumbled = word #initializes jumbled with original word
    while jumbled == word: #checks if the word is still the same as the original word (that has been made as a list of letters)
        random.shuffle(letters) #shuffles the letters in word
        jumbled	= "".join(letters) #joins the jumbled word
    return jumbled.upper()

def show_word_count(valid_words): #function that shows how many words can be formed 
    for i in range(6,2,-1): #loops from 6 to 3, stepping down 1 step at a time
        count = 0 #accumulator for counting the number of words with the current length. 
        for word in valid_words: 
            if len(word) == i: #checks if length of word is equivalent to current value of i 
                count = count + 1 #increments count by 1
        print(f"The amount of {i} letter words is {count}") 

def load_leaderboard(leaderboard_file): #function that opens the leaderboard file  
    leaderboard = []
    if os.path.exists(leaderboard_file) == False: #prevents the program from crashing if file DNE
        return leaderboard
    
    view_from_leaderboard_file= open(leaderboard_file, "r") #opens the leaderboard

    for line in view_from_leaderboard_file: 
        parts = line.strip().split(",")

        if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
            leaderboard.append([parts[0], int(parts[1]), int(parts[2])])

    view_from_leaderboard_file.close()

    return leaderboard
    
def save_leaderboard(leaderboard, leaderboard_file): #auto saves the leaderboard 
    save_from_leaderboard_file = open(leaderboard_file, "w")
    for entry in leaderboard:
        save_from_leaderboard_file.write(entry[0] + "," + str(entry[1]) + "," + str(entry[2]) + "\n")
    save_from_leaderboard_file.close()

def is_better(entry1, entry2): #compares the two entry (results) which one is better
    if entry1[1]>entry2[1]:
        return True
    elif entry1[1] == entry2[1] and entry1[2] > entry2[2]:
        return True
    else:
        return False

def sort_leaderboard(leaderboard): #selection sort
    for i in range(len(leaderboard)): #goes through each position in the leaderboard
        best = i #sets i (current position) as the current best
        for j in range(i+1, len(leaderboard)): #checks the remaining elements after i
            if is_better(leaderboard[j], leaderboard[best]): #checks if the element at j is better than the current best
                best = j #sets j as the new best if True

        temp = leaderboard[i] #temporarily stores the element at i
        leaderboard[i] = leaderboard[best] #replaces the element at i with the best element found
        leaderboard[best] = temp #puts the original element at i into the previous position of the best element

def play_stage(target, valid_words, time_limit, stage_number): #function for the main game program

    jumbled = jumble_word(target) #sets the jumbled word
    print()
    print("Stage", stage_number, "you have", time_limit, "seconds.")
    input("Press enter when you are ready")
    print()
    print("========= STAGE START =========")
    print()
    print("Your jumbled word is", jumbled)
    print()
    show_word_count(valid_words)
    print("You need to find the six letter word to advance to the next stage")
    input("Press ENTER to continue ")

    found_words = [] #list to get guesses
    start_time = time.time() #sets the time

    while True: #Answer loop
        time_left = time_limit - int(time.time() - start_time) #program for timer 
        if time_left <= 0: #timer end
            print()
            print("Time's up!") 
            return 0
        print()
        print("Time Left: ", time_left, "seconds") 
        print("Words found: ", found_words)
        print()
        answer = input("Enter answer (or 1 to quit): ").lower().strip() #gets the answer

        if answer == "1":
            return -1
        answer = answer.lower().strip() #lowercases the answer
        time_left = time_limit - int(time.time() - start_time) #updates the time when you answer
        if time_left <= 0: 
            print("Time's up!")
            return 0
        if answer in found_words: #checks if the guessed word is already in the list of found_words
            print("You already found that word!")
        elif answer in valid_words: #checks if the guessed word is valid
            if answer == target: #checks if the guessed word is in the answer
                print("The word has been found with", time_left, "seconds. Onto the next level!")
                return time_left 
        
            found_words.append(answer) #appends the word to the list if valid for all checks
            print()
            print("Word found!", answer) #confirms the word if correctly answered

            if len(found_words) > 8: #adds one second for every correct answer if they already found more than 8 correct words
                print("Bonus! +1 second!")
                start_time += 1
        else:
                print()
                print("Answer not in the given words. Please try again")

                if stage_number > 3: #subtracts two seconds for wrong guesses after stage 3
                    print("Penalty! -2 seconds")
                    start_time -= 2

        print("The jumbled words are:", jumbled)

def ask_name(): #function for the name input and validation of input
    while True:
        name = input("Enter your name: ").strip()
        if name == "": #if name is blank it returns an error message
            print("Name cannot be empty")
        elif "," in name: #if name has invalid character (,)
            print("Name cannot have a comma")
        elif len(name)  > 12: #if name is more than 12 characters
            print("Name must be 12 characters or less")
        else:
            return name
        
def start_game(leaderboard, word_bank, STARTING_TIME, LEADERBOARD_FILE): #function that starts the game
    keys = list(word_bank.keys()) #gets the words from the word bank
    random.shuffle(keys) #randomizes those words

    stage = 1 #initializes stage to stage 1
    time_limit = STARTING_TIME	#initializes time to set start time
    total_time = 0 #initializes total time run
    stages_cleared = 0 #initializes total stages cleared

    while stage <= len(keys): #continues the game while there are still stages to play
        target = keys[stage - 1] #gets the word for the current stage from the keys list
        valid_words = word_bank[target] #sets the valid word as words found in the word bank
    
        time_left = play_stage(target, valid_words, time_limit, stage)
        if time_left <= 0:
               break
        total_time += time_left #adds the remaining time to the total time
        stages_cleared = stage	#updates stages cleared
        time_limit = STARTING_TIME + time_left #adds the remaining time to the starting time for the next stage
        stage += 1 #moves to the next stage
    print()
    if stages_cleared == len(keys): #checks if all stages have been cleared
        print("Congratulations! You have cleared all stages")
    else:
        print("GAME OVER The word was:", target.upper())
        print("Highest stage cleared:", stages_cleared) #highest stage cleared
        print("Time remaining:", total_time)

    name = ask_name() #sets name variable to the function
    leaderboard.append([name, total_time, stages_cleared]) #appends the name, total time, and stages cleared function to the leaderboard.
    sort_leaderboard(leaderboard) #uses the sort leaderboard function to the leaderboard
    save_leaderboard(leaderboard, LEADERBOARD_FILE) #uses the save leaderboard function to the leaderboard
    
def show_title(): #function that prints the title art
    print("+" + "=" * 34 + "+") #top border, repeats = 34 times
    print("|" + " " * 34 + "|") #blank line inside the box
    print("|       T E X T   T W I S T        |")
    print("|       W I T H A T W I S T        |") #same letters, jumbled
    print("|" + " " * 34 + "|")
    print("|  ~~ Guess the Six Letter Word ~~ |")
    print("+" + "=" * 34 + "+") #bottom border
    
def main(): #main function 
    
    word_bank = { #a dictionary of a set of words to be randomized and jumbled
        "planet": [
            "planet",
            "plane", "plant", "panel", "petal", "plate", "pleat", "leapt",
            "pale", "plea", "leap", "peal", "pelt", "lent", "neat",
            "ante", "lane", "late", "tale", "teal",
            "ant", "apt", "ate", "eat", "tea", "tan", "net", "ten",
            "pen", "pan", "nap", "tap", "pat", "lap", "pal", "pet",
            "let", "pea", "ale", "ape"
        ],

        "garden": [
            "garden",
            "grade", "grand", "range", "anger", "raged",
            "aged", "dare", "dear", "read", "gear", "rage",
            "earn", "near", "dean", "drag",
            "age", "rag", "ran", "red", "den", "nag",
            "ear", "era", "and", "are", "gad", "erg"
        ],

        "stream": [
            "stream",
            "steam", "teams", "tames", "rates", "tears",
            "stare", "smart", "tamer",
            "team", "meat", "mate", "tame", "same", "seam",
            "east", "eats", "seat", "tear", "rate", "star",
            "arts", "rats", "mats", "mast", "rest",
            "sea", "sat", "set", "met", "mat", "ram",
            "rat", "art", "ear", "are", "tea", "eat", "ate"
        ],

        "mother": [
            "mother",
            "other", "therm", "metro", "throe",
            "home", "more", "moth", "term", "them",
            "tome", "hero", "rote", "tore",
            "the", "her", "hot", "met", "rot",
            "toe", "ore", "hem", "hoe", "ohm"
        ],

        "castle": [
            "castle",
            "least", "slate", "stale", "steal", "tales",
            "teals", "scale", "cleat",
            "case", "cast", "last", "salt", "sale",
            "seal", "seat", "east", "eats", "tale",
            "teal", "lace", "late",
            "cat", "act", "sat", "set", "tea",
            "eat", "ate", "sea", "ale", "let"
        ],

        "flower": [
            "flower",
            "lower", "rowel",
            "flow", "flew", "wolf", "wore", "role",
            "lore", "fore",
            "low", "few", "owe", "row", "foe",
            "owl", "woe", "elf", "ore", "roe"
        ],

        "market": [
            "market",
            "maker", "taker", "tamer",
            "make", "mark", "mare", "meat", "team",
            "take", "tame", "rate", "tear", "term",
            "rake", "teak",
            "arm", "are", "ark", "art", "ate",
            "ear", "eat", "era", "mat", "met",
            "rat", "tar", "tea", "ram"
        ],

        "orange": [
            "orange",
            "range", "anger", "organ",
            "near", "earn", "gear", "rage",
            "gone", "gore", "ogre",
            "one", "ore", "age", "rag", "ran",
            "nag", "nor", "ego", "roe"
        ],

        "marble": [
            "marble",
            "blame", "bream", "amber", "realm",
            "bear", "bare", "ream", "lame", "male",
            "meal", "mare", "real", "balm",
            "arm", "are", "ear", "era", "bar",
            "ram", "lab", "ale", "lea", "elm"
        ],

        "bright": [
            "bright",
            "birth", "girth", "right", "bight",
            "brig", "grit", "trig",
            "big", "bit", "hit", "rib", "rig", "git"
        ],

        "spring": [
            "spring",
            "rings", "grips", "prigs", "sprig",
            "ring", "grin", "spin", "sing", "pigs",
            "rigs", "rips", "grip", "sign",
            "pig", "pin", "sin", "sip", "rig",
            "rip", "sir", "gin", "nip"
        ],

        "thread": [
            "thread",
            "tread", "trade", "rated", "hated",
            "heart", "earth", "hater",
            "read", "dear", "dare", "date", "dart",
            "hard", "hear", "heat", "herd", "hate",
            "tear", "rate",
            "the", "her", "red", "rat", "art",
            "ear", "ate", "tea", "tad", "had", "hat"
        ],

        "listen": [
            "listen",
            "lines", "liens", "tiles", "inlet",
            "stile", "tines",
            "line", "lien", "lent", "tile", "ties",
            "site", "sent", "nest", "tens", "lets", "isle",
            "lie", "let", "lit", "tin", "tie", "sit",
            "set", "sin", "net", "ten", "nil"
        ],

        "rescue": [
            "rescue",
            "curse", "cures", "reuse",
            "user", "sure", "cure", "ruse", "rues", "cues",
            "use", "sue", "cue", "cur", "sec", "ere"
        ],

        "parrot": [
            "parrot",
            "tarot",
            "part", "trap", "tarp", "rapt", "port",
            "atop", "roar", "rota",
            "rap", "tap", "rat", "art", "tar",
            "rot", "pot", "top", "opt", "oar", "par"
        ],

        "basket": [
            "basket",
            "steak", "takes", "skate", "beaks", "beats", "beast",
            "bake", "sake", "seat", "east", "eats",
            "teas", "take", "teak", "task", "bask",
            "bets", "best",
            "ask", "ate", "eat", "tea", "sea",
            "set", "bet", "bat"
        ],

        "bridge": [
            "bridge",
            "bride", "rebid", "giber",
            "ride", "dire", "bier", "bred", "grid", "bird", "brig",
            "rid", "rib", "rig", "beg", "big", "bid",
            "die", "dig", "red", "ire", "erg"
        ]
    }
    LEADERBOARD_FILE = "leaderboard.dat"
    STARTING_TIME = 120
    leaderboard = load_leaderboard(LEADERBOARD_FILE) #loads the leaderboard function

    while True: #main game menu
        print()
        show_title()
        print()
        print("[1] Start Game")
        print("[2] View Leaderboard")
        print("[3] Exit")

        choice = input("Enter choice: ")

        if choice == "1": #starts the game, returns the start_game function
            start_game(leaderboard, word_bank, STARTING_TIME, LEADERBOARD_FILE)
        elif choice == "2": #opens the leaderboard, returns the display_leaderboard_function
            print()
            display_leaderboard(leaderboard)
        elif choice == "3": #exits the game, uses python break 
            print("Thank you for playing!")
            break
        else: #to avoid program crash if there is other input
            print("Invalid Input!")


main()

#UPDATES
#FIX GLOBAL VARIABLE 
#ADD EXIT COMMAND 
#ADD DELETE LEADERBOARD
#TRANSFER IMPORTS TO OTHER FILE (leaderboard, game program)



