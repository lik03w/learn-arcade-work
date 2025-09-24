import arcade
import random
def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the natives.")

    done = False  #wahrheitswert fuer aktionen

    camel_tieredness = 0
    miles_travelled = 0
    miles_zaehler = 20
    health = 100
    thirst = 0
    chasing_thieves_miles_travelled = 0
    flaschen = 2
    while done == False:
        zufall_zahl_thieves = random.randint(4,17)
        zufall_zahl_2 = random.randint(8, 15)
        zufall_zahl_volle_kraft = random.randint(10, 19)
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        print("what would you like to do? ")
        answer = input()
        if(answer.upper() == "Q"):
            print("Thank you for playing!")
            done = True
        elif(answer.upper() == "E"):
            print("Distance to chasing thieves: "+ str(miles_travelled + miles_zaehler - chasing_thieves_miles_travelled))
            print("Amount of bottles left: " + str(flaschen))
            print("Miles travelled: " + str(miles_travelled))
        elif (answer.upper() == "D"):
            camel_tieredness = camel_tieredness - 40
            thirst += 10
            health += 3
            chasing_thieves_miles_travelled += zufall_zahl_thieves

            if(camel_tieredness <= 0):
                camel_tieredness = 0
        elif (answer.upper() == "C"):
            camel_tieredness += random.randint(1,4)
            miles_travelled += zufall_zahl_volle_kraft
            thirst += 15
            chasing_thieves_miles_travelled = zufall_zahl_thieves
            print("You travelled " + str(zufall_zahl_volle_kraft)+ " miles!")

        elif(answer.upper() == "A"):
            health += 10
            thirst = 0
            camel_tieredness -= 5
            if(camel_tieredness <= 0):
                camel_tieredness = 0
            chasing_thieves_miles_travelled += random.randint(1,3)

        elif(answer.upper() == "B"):
            miles_travelled += zufall_zahl_2
            camel_tieredness += random.randint(1, 4)
            thirst += 15
            chasing_thieves_miles_travelled = zufall_zahl_thieves

        if (miles_travelled + miles_zaehler <= chasing_thieves_miles_travelled):
            print("The thieves catched you, you are dead meat!")
            done = True

        elif(miles_travelled == 150):
            print("You successfully escaped")
main()