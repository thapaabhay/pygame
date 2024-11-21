import random
from design import graphics
import words

#global variables
hangmanWord=random.choice(words.wordLists)
correct=list()
blanks=list()
forbidden=list()
length=len(hangmanWord)
                 
#create a list for blanks and hangmanWord so that it would be easier to run calculations in code
for i in range(length):
    blanks.append("_")
    correct.append(hangmanWord[i])
    #for more than one words
    if correct[i]==" ": 
        blanks[i]=" "

#different actions for correct or wrong guess 
class mainGame:
    def __init__(self,myLetter,counter): 
        self.myLetter=myLetter
        self.counter=counter
        
    
    def correctPlay(self):
        for i in range(length):
            if correct[i]==self.myLetter: #checks the index of the correct letter guessed
                blanks[i]=self.myLetter   #replaces the blank "_" with the letter on that index
        for x in blanks:
            print(x,end=" ")
        
    def wrongPlay(self):
        g=graphics() #object for hangman graphics
        #check what stage the player is in and print the hangman accordingly
        match self.counter:
            case 1:
                g.stage1()
                for x in blanks:
                    print(x,end=" ")
            case 2:
                g.stage2()
                for x in blanks:
                    print(x,end=" ")
            case 3:
                g.stage3()
                for x in blanks:
                    print(x,end=" ")
            case 4:
                g.stage4()
                for x in blanks:
                    print(x,end=" ")
            case 5:
                g.stage5()
                for x in blanks:
                    print(x,end=" ")
            case 6:
                g.stage6()
                #Game Over
                print(f"\n{"="*50}\n{" "*15}GAME OVER !!\n{"="*50}\nYour word was \"{hangmanWord}\"\n{"="*50}\n\n")
                
#ACTUAL GAME           
print("Welcome to HangMan Game!")

def main():
    gameActive=True   #to run the game again and again
    counter=1         #to assign stages to player according to the number of time they've guessed wrong   

    #first print blankspace revealing the length of word if you're reading this, you're a nerd
    for x in blanks: 
            print(x,end=" ")
    while gameActive==True:
        #user can't input more than 1 letter and also can't press Enter without guessing anything
        singleDigit=True
        while singleDigit==True:
            myLetter=input("\nEnter your letter: ").lower().strip()
            if len(myLetter)!=1 or myLetter==" " or myLetter.isalpha()==False:
                print("Invalid input | Try again !!")
            else:
                singleDigit=False

        #one letter cannot be guessed twice
        if myLetter not in forbidden:
            c=mainGame(myLetter,counter)
            
            if myLetter in correct:
                c.correctPlay() #for correct gues
            else:
                if counter!=7:
                #increase the counter by 1 for every wrong guess, but this increment won't be reflected on the wrongPlay object 
                    counter+=1 
                    c.wrongPlay() #for wrong guess
            forbidden.append(myLetter)
        else:
            print("You've already guessed that letter")

        #after every play, check if we want to terminate the game
        if blanks==correct:
            print(f"\n{"="*50}\n{" "*6}Congratulations ! You won the Game\n{"="*50}")
            gameActive=False #false= terminates the game

        if counter==7:
            gameActive=False 
main()