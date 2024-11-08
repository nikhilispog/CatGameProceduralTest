import pprint
from random import *

cat_attributes = {
    "intelligence": 10,
    "energy": 23,
    "weight": 10,
    "hunger": 20
}

print("Welcome to my cat game!")
name = input("Enter name:")
colour = input ("Enter colour")
cat_attributes["name"] = name
cat_attributes["colour"] = colour
dead = False
def stat_loss(stat,lossmult):
    cat_attributes[stat] -= round(randint(round(1*lossmult),round(5*lossmult)))
def stat_gain(stat,gainmult):
    cat_attributes[stat]+= round(randint(round(2*gainmult),round(5*gainmult)))
while dead == False:
    print("""List of actions
          1) Play with cat
          2) Train cat
          3) Feed cat
          4) Put cat to sleep
          5) Stats""")
    action = input("What would you like to do?(enter number)")
    if action == "1":
        print("You played with", name, "for a while")
        stat_loss("energy",1.25)
        stat_gain("intelligence",1.75)
        stat_loss("weight",1.4)
    elif action == "2":
        print("You trained",name,"to do something cool")
        stat_loss("energy",2)
        stat_loss("hunger",1)
        stat_gain("intelligence",2.5)
    elif action == "3":
        print("You fed",name,"some nice food")
        stat_gain("hunger",1.35)
        stat_gain("weight",1.3)
        stat_loss("energy",1)
    elif action == "4":
        print("You let",name,"get some rest")
        stat_gain("energy",2.2)
        stat_loss("hunger",1)
    elif action == "5":
        pprint.pprint(cat_attributes)
    # death messages
    if cat_attributes["energy"] <= 0:
        print(name,"worked too hard")
        dead = True
    if cat_attributes["hunger"] <= 0:
        print(name,"starved")
        dead = True
    if cat_attributes["weight"]>=25:
        print(name,"is overweight")
        dead = True
print(name,"is dead")





