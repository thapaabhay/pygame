import random
from design import graphics
from words import wordLists

hangmanWord=random.choice(wordLists)
correct=[]
blanks=[]
forbidden=[]
length=len(hangmanWord)
                 

for i in range(length):
    blanks.append("_")
    correct.append(hangmanWord[i])
    
    if correct[i]==" ": 
        blanks[i]=" "



class mainGame:
    def __init__(self,myLetter,counter):
        self.myLetter=myLetter
        self.counter=counter
    
    def correctPlay(self):
        for i in range(length):
            if correct[i]==self.myLetter: 
                blanks[i]=self.myLetter   
        for x in blanks:
            print(x,end="")
        
    def wrongPlay(self):
        g=graphics() 
        match self.counter:
            case 1:
                g.stage1()
                for x in blanks:
                    print(x,end="")
            case 2:
                g.stage2()
                for x in blanks:
                    print(x,end="")
            case 3:
                g.stage3()
                for x in blanks:
                    print(x,end="")
            case 4:
                g.stage4()
                for x in blanks:
                    print(x,end="")
            case 5:
                g.stage5()
                for x in blanks:
                    print(x,end="")
            case 6:
                g.stage6()
               
                print(f"\n{"="*50}\n{" "*15}GAME OVER !!\n{"="*50}\nYour word was \"{hangmanWord}\"\n{"="*50}\n\n")
                
          
print("Welcome to HangMan Game!")

def main():
    gameActive=True   
    counter=1            

    
    for x in blanks: 
            print(x,end="")
    while gameActive==True:
        
        singleDigit=True
        while singleDigit==True:
            myLetter=input("\nEnter your letter: ").lower()
            if len(myLetter)!=1 or myLetter==" ":
                print("ERROR !!")
            else:
                singleDigit=False

        
        if myLetter not in forbidden:
            c=mainGame(myLetter,counter)
            
            if myLetter in correct:
                c.correctPlay() 
            else:
                if counter!=7:
             
                    counter+=1 
                    c.wrongPlay() 
            forbidden.append(myLetter)
        else:
            print("You've already guessed that letter")

    
        if blanks==correct:
            print(f"\n{"="*50}\n{" "*6}Congratulations ! You won the Game\n{"="*50}")
            gameActive=False

        if counter==7:
            gameActive=False 
main()