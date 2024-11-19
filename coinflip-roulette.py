import math as m
import random as r
import time as t
import sys as s
import os as o


class c:
   #Callable exit codes so that I can just put in colors
   PUR = '\033[95m'
   CYA = '\033[96m'
   DCY = '\033[36m'
   BLU = '\033[94m'
   GRE = '\033[92m'
   YEL = '\033[93m'
   RED = '\033[91m'
   BOL = '\033[1m'
   UND = '\033[4m'
   END = '\033[0m'


Rand_CoinList_map = {
    #There is barely any organization in this table, I apologize
    "0":[0, 1],
    "1":[0, 0, 1],
    "2":[0, 1, 1],
    "3":[0, 0, 1, 1],
    "4":[0, 0, 0, 1],
    "5":[0, 0, 1, 1, 1],
    "6":[0, 1, 1, 1],        
    "7":[0, 0, 0, 1, 1],
    "8":[0, 0, 1, 1, 1, 1],
    "9":[0, 0, 0, 1, 1, 1],
    "10":[0, 0, 0, 0, 1, 1],
    "11":[0, 0, 0, 0, 1, 1, 1],
    "12":[0, 0, 0, 1, 1, 1, 1],
    "13":[0, 0, 0, 0, 1, 1, 1, 1],
    "14":[0, 0, 0, 1, 1, 1, 1, 1],
    "15":[0, 0, 0, 0, 0, 1, 1, 1],
}

player_turn=1
Coin_List=[]
Player1_HP= 5
Player2_HP= 5
def main(Coin_List, Rand_CoinList_map, Player1_HP, Player2_HP):
    #Run stuff here
    intro()
    round(Coin_List, Player1_HP, Player2_HP)
    

def pickList(Coin_List, Rand_CoinList_map):
    #uses a random number to pull from the table
    Coin_Prelist = Rand_CoinList_map[str(r.randint(0,15))]
    heads=0
    tails=0
    #determines the amount of "heads"(lives) and "tails"(blanks)
    for x in Coin_Prelist:
        if x==1: heads+=1
        if x==0: tails+=1
    list_Printout= f" There is {heads} heads and {tails} tails in this list."
    print(c.RED+c.BOL+list_Printout+c.END)
    Coin_Len = len(Coin_Prelist)
    for i in range(Coin_Len):
        #Moves a random item from the prelist to the main list, probably made a mistake here somewhere idk
        trans=r.randint(0,(len(Coin_Prelist)-1))
        Coin_List.append(Coin_Prelist[trans])
        Coin_Prelist.pop(trans)


def intro():
    print("You both have 5 HP.\n You can flip the coin at the other player by typing \'a\' or yourself by typing \'y\'.\n If it lands heads, whoever it was flipped at loses 1 HP by default.")
    

def healthCheck(Player1_HP,Player2_HP):
    print("Player 1 HP is "+c.BLU+str(Player1_HP)+c.END+" points. Player 2 HP is "+c.RED+str(Player2_HP)+c.END+" points.")


def turnSwap():
    global player_turn
    if player_turn==1: player_turn=2
    elif player_turn==2: player_turn=1


def round(Coin_List, Player1_HP, Player2_HP):
    global player_turn
    if Player1_HP>0 and Player2_HP>0:
        if len(Coin_List)==0:
            #if the list is out of items it runs coinlist again so play can continue.
            o.system('clear')
            pickList(Coin_List, Rand_CoinList_map)
        damage_amount=1
        healthCheck(Player1_HP, Player2_HP)
        coined = input(c.PUR+" PLAYER "+str(player_turn)+". "+c.END+"Choose whether to flip the coin at the other player by typing \'a\' or yourself by typing \'y\'. If you flip at yourself and get a tails, you get another turn!")
        #a for attack, y for yourself
        coined=coined.casefold()
        if coined=='a':
            if Coin_List[0]==0: 
                print("Tails! Enemy takes 0 points of damage.")
                turnSwap()
            elif Coin_List[0]==1:
                print("Heads! Enemy takes "+str(damage_amount)+" point(s) of damage!")
                if player_turn==1: Player2_HP-=damage_amount
                elif player_turn==2: Player1_HP-=damage_amount
                turnSwap()
            
        elif coined=='y': 
            if Coin_List[0]==0:
                print("Tails! You get another turn!")
            elif Coin_List[0]==1:
                print("Heads! You lose "+str(damage_amount)+" point(s) of damage!")
                if player_turn==1: Player1_HP-=damage_amount
                elif player_turn==2: Player2_HP-=damage_amount
                turnSwap()
        Coin_List.pop(0)
        round(Coin_List, Player1_HP, Player2_HP)
    elif Player1_HP<1 and Player2_HP>=1:
        print(c.GRE+c.BOL+"PLAYER 2 WINS"+c.END)
        s.exit()
    elif Player2_HP<1 and Player1_HP>=1:
        print(c.GRE+c.BOL+"PLAYER 1 WINS"+c.END)
        s.exit()
    
    
            
        
    
main(Coin_List, Rand_CoinList_map, Player1_HP, Player2_HP)
