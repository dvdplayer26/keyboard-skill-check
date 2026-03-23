import random
import time
wordList = ["apple", "banana", "carrot"]
word = random.choice(wordList)

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
    print("Ending sesion...")

def keyboardSkill():
    print("Welcome user. This is a keyboard skill check. \nSelect what you would like to do. \na) Word typing practice \nb) Sentence type practice \n c)Paragraph type practice")
    menu_choice = input()
    if menu_choice == "a":
        wordType()
    elif menu_choice == "b":
        senType()
    else:
        Error1()

keyboardSkill()