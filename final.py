import random
import time
wordList = ["apple", "banana", "carrot", "durian", "eggplant", "fruit", ]
senList = ["Apple seeds need cold stratification before being planted.", "A banana is scientifically considered a berry.", "A carrot is actually the root of the carrot plant!", "People say durians do not smell very pleasant.", "Not many people cook eggplant nowadays.", "Peppers, Tomatoes, and Cucumbers are actually fruits!", ]
word = random.choice(wordList)
sen = random.choice(senList)

def Error1():
    print("Invalid choice!")
    time.sleep(2)
    print("Sending back to menu...")

def wordType():
    isWrong = False
    while isWrong == False:
        word = random.choice(wordList)
        print(word)
        typedWord = input()
        if typedWord != word:
            print ("Wrong!")
            isWrong = True
    time.sleep(2)
    print("Ending session...")

def senType():
    isWrong = False
    while isWrong == False:
        sen = random.choice(senList)
        print(sen)
        typedSen = input()
        if typedSen != sen:
            print ("Wrong!")
            isWrong = True
    time.sleep(2)
    print("Ending session...")

def keyboardSkill():
    print("Welcome user. This is a keyboard skill check. \nSelect what you would like to do. \na) Word typing practice \nb) Sentence type practice")
    menu_choice = input()
    if menu_choice == "a":
        wordType()
    elif menu_choice == "b":
        senType()
    else:
        Error1()

keyboardSkill()