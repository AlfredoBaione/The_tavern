# This is my  game: "The tavern"

import random



def intro():
     print("""Welcome to the game named 'The tavern'. 
      To win this game both luckyness and strategy are required.
           Do you wish to play?""")
     play = input("> ")
     if "es" in play:
          start()
     else:
          print("""No problem, braveness is not for everyone!""")

          

def start():
    print("""You are an adventurer in a small city.
    It's evening and it's raining. 
     The only opened place is the tavern.
     Where do you go?  """)

    choice = input("> ")

    if "tavern"  in choice:
         the_tavern()
    else:
         print("""All the other places except from the one mentioned 
               don't host you. You better reconsider your choice.""")
         choice = input("> ")
         if "tavern"  in choice:
              the_tavern()
         else:
              print("""Nothing happens until a thunder hits you, killing you immediately.
                    Don't regret. You didn't suffer.""")



def the_tavern():
     print("""'Welcome to you!' says the host once you enter.
           'What do you prefer: sleeping or eating?'""")
     choice = input("> ")
     if "sleep" in choice and "eat" not in choice:
          sleep()                    
     elif "eat" in choice and "sleep" not in choice:
          eat()      
     elif "eat" in choice and "sleep" in choice or "both" in choice:
         print("""'I'm sorry sir, but in the past it happened that people who ate here puked in our rooms.
               So we don't allow sleeping and eating anymore'.
               What do you do?""")
         choice = input("> ")
         if "sleep" in choice:
             sleep()
         elif "eat" in choice:
             eat()
         else:
            print("""A bit shocked by the answer of the host you find yourself outside of the tavern.
                  All of a sudden a thunder hits you and kills you immediately. 
                  Don't regret. You didn't suffer.""")
     else:
         print("""You find yourself outside of the tavern.
               All of a sudden a thunder his you and kills you immediately.
               Don't regret. You didn't suffer.""")
         


def sleep():         
    print(f"""The host brings you to your room. 
                Once in front of the door he asks you for 20 silver coin.
            You open your pocket, finding {silver_coins} silver coins inside of it.
                Can you pay the host?""")
    money = input("> ")
    if "es"  in money:
               print("Do you wish to pay him?")
               choice = input("> ")
               if "es" in choice:
                  print("""You pay the host and go to sleep. 
                     You hear some noises from outside the tavern. Probably a thunderstorme, but that doesn't really bother you.
                     The morning comes, you thank the host and take your way.""")
               else:
                     sleep_negotiation()
    else:
               sleep_negotiation()


               
def eat():
    print(""" The host makes you seat at the counter. 
                ' Are eggs and pork meat fine for you?' he asks.""")
    answer = input("> ")
    if "es"  in answer:
             print(f"""The host brings you immediately the food. You eat it.
                   By the way, do you have 10 silver coins for paying it?
                   Actually in your pocket there are {silver_coins} silver coins.
                   Can you pay the host?""")
             money = input("> ")
             if "es" in money:
                 print("Do you wish to pay him?")
                 choice = input("> ")
                 if "es" in choice:
                  print(""" You pay the host, thanks him and take your way. 
                       Before going out you hear a noise coming from outside.
                       'A thunderstorme' says the host smiling at you.""")
                 else:
                     food_negotiation()
             else:
                 food_negotiation()
                 
    else:
            print("""'I'm sorry, we don't have anything else' says the host.
                      What do you do? You go away or eat eggs and meat?""")
            choice = input("> ")
            if "go" in choice:
                   print(""" You say goodbye to the host and go out from the tavern. 
                       After few steps a thunder hits you and kills you immediately.
                       Don't regret. You didn't suffer.""")
            else:
                   print(f"""'After all, eggs and pork meat are not so bad' you think.
                         By the way, do you have 10 silver coins for paying the dinner?
                         Checking your pocket, you discover {silver_coins} silver coins.
                         Can you pay the the host?""")
                   money = input("> ")
                   if "es" in money:
                       print("Do you wish to pay him?")
                       choice = input("> ")
                       if "es" in choice:
                        print(""" You pay the host, thanks him and take your way. 
                       Before going out you hear a noise coming from outside.
                       'A thunderstorme' says the host smiling at you.""")
                       else:
                             food_negotiation()
                   else:
                      food_negotiation()



def sleep_negotiation():
      print("""' Oh, I think I can't pay you!' you say.
                     In this case the host offers you to stay for the night in any case and  
                     work for him until you'll have repaid your debt.
                     Do you accept the offer?""")
      offer = input("> ")
      if "es" in offer:
                  print("You accept the offer. Wise choice.")    
      else:
                  print("""You decline the offer. 
                          Very soon you find yourself outside the tavern.
                          After few steps a thunder hits you and kills you immediately.
                         Don't regret. You didn't suffer.""")     
               

             
def food_negotiation():
      print("""'Oh, actually I ran out of money!' you say.
                       Very annoyed, the host offers you to sleep there and working for him the next days, 
                       until you'll have repaid all your debts.
                       Do you accept the offer?""")
      offer = input("> ")
      if "es" in offer:
                  print("You accept the offer. Wise choice.")    
      else:
                  print("""You decline the offer. 
                          The host invites you to follow him downstairs, while you hear a very powerful noise coming from outside.
                          'It's a thunderstorm' says the host in a ghostly tone.
                          From that night, none hears from you anymore.
                          You better regret yourself.""")      



silver_coins = random.randint(0, 25)
intro()