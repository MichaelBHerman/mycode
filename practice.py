# lab 28 ##############################################################

# my_list = ["192.168.0.5", 5060, "UP"]
# print("The first item in the list (IP): " + my_list[0])

# print("The second item in the list (port): " + str(my_list[1]))

# print("The last item in the list (state): " + my_list[2])

# iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
# print(iplist[3], iplist[4])

# lab 29 ############################################################
# proto = ["ssh", "http", "https"]
# proto.extend("dns")
# print(proto)

# proto = ["ssh", "http", "https"]
# protoa = ["ssh", "http", "https"]
# proto.append("dns")
# protoa.append("dns")
# proto2 = [ 22, 80, 443, 53 ]
# proto.extend(proto2)
# print(proto)
# proto.insert(2, "banana")
# print(proto)

#lab 30 ###############################################################
# def main():
#     list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
#     list2 = ["juniper"]
#     list1.extend(list2)
#     print(list1)
#     list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
#     list1.append(list3)
#     print(list1)
#     print(list1[4])
#     print(list1[4][0])

# main()  

# animals = ["dog", "pig", "cat", "rat", "cow", "bee"]
# print(animals)

#superhero functional dictionary (gambit)

# gambit = {"Real Name": "Remy LeBeau",
# "First Appearance": "Uncanny X-Men Annual #14 (July, 1990), Uncanny X-Men #266 (August, 1990)",
# "Creators": ["Chris Claremont", "Jim Lee"],
# "Team Affliations": 
# ["X-Factor", "X-Men", "Marauders", "Horsemen of Apocalypse,"], 
# "Base of Operations": "Salem Centre, New York"}

# print(gambit)

# SquirrelGirl={'name':'Squirrel Girl','civilian-identity':'Doreen Green','debut':'November, 1991','creators':['Will Murray','Steve Ditko'],'villains-defeated':['Doctor Doom','Abomination','Maelstrom','M.O.D.O.K.','Thanos','Terrax','Bi-Beast','Deadpool','Fin Fang Foom','Kraven the Hunter','Galactus','Brain Drain','Enigmo','Ultron']}

# a = (SquirrelGirl["name"])
# b =(SquirrelGirl["creators"][1])
# c =(SquirrelGirl["villains-defeated"][3])
# d =(SquirrelGirl["civilian-identity"])

# forged = a + " was created by " + b + ", and she has defteated " + c + "! " + "Her civilian-identity is " + d + "."
# print(forged)

#############################lab 32#######################################
# switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}
# print(switch["hostname"])
# print(switch["ip"])
# # print(switch["lynx"])
# ## request a 'fake' key with .get() method
# print( "First test - .get()" )
# print( switch.get("lynx") )

# print( "Second test - .get()" )
# print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )

# print( "Third test - .get()" )
# print( switch.get("version") )
# print( "Fourth test - .keys()" )
# print( switch.keys() )

# print( "Fifth test - .values()" )
# print( switch.values() )
# print( "Sixth test - .pop()" )
# switch.pop("version") # removes this key (and value) pair
# print( switch.keys() )   # notice the value of version is gone
# print( switch.values() ) # notice the value 1.2

# print( "Seventh test - ADD a new value" )
# switch["adminlogin"] = "karl08"
# print( switch.keys() )
# print( switch.values() )

# print( "Eighth test - ADD a new value" )
# switch["password"] = "qwerty"
# print( switch.keys() )
# print( switch.values() )

##################lab 32 challenge#################################
# Gambit={'Real Name':'Remy LeBeau','First Appearance':'Uncanny X-Men Annual #14 (July, 1990), Uncanny X-Men #266 (August, 1990)','Creators':['Chris Claremont','Jim Lee'],'Team Affliations':['X-Factor','X-Men','Marauders','Horsemen of Apocalypse,'],'Base of Operations':'Salem Centre, New York'}

# print(Gambit.keys())
# choice = input("Please enter a key: ")
# print("Gambit's " + choice + " is: " + Gambit.get(choice))
################################### lab 36 ##################################################


###################################lab 39#################################
# hostname = "MTG"
# if hostname == "MTG":
#     print("The hostname was found to be MTG")

# hostname = input("What value should we set for hostname?")
# if hostname == "MTG":
#     print("the hostname was found to be MTG")

# hostname = input("what value should we set for hostname?")
# if hostname.lower() == "mtg":
#     print("the hostname was found to be mtg")
#     print("hostname matches expected config")
# print("exiting the script")  

#################################### lab 40 ###############################
# """Alta3 Research | RZFeeser
#    Conditionals - strings test true"""

# ipchk = "192.168.0.1"

# # a string tests as True
# if ipchk:
#    print("Looks like the IP address was set: " + ipchk)

# ipchk = input("apply an IP address: ")
# if ipchk:
#     print("Lookls like the IP address was set: " + ipchk)

# ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# # a provided string will test true
# if ipchk:
#    print("Looks like the IP address was set: " + ipchk) # indented under if
# else:    # if data is NOT provided
#    print("You did not provide input.") # indented under else

# ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# # if user set IP of gateway
# if ipchk == "192.168.70.1":
#    print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
# elif ipchk: # if any data is provided, this will test true
#    print("Looks like the IP address was set: " + ipchk) # indented under if
# else: # if data is NOT provided
#    print("You did not provide input.") # indented under else

###################################################lab 42##########################

# round = 0
# while True:
#     round = round + 1
#     print('Finish the movie title, "Monty Python\'s The Life of ______"')
#     answer = input("Your guess--> ")
#     if answer == "Brian":
#         print("correct")
#         break
#     elif round == 3:
#         print("sorry, the answer was Brian")
#         break
#     else: 
#         print("sorry! try again!")
        
 #!/usr/bin/python3
# """Alta3 Research | RZFeeser
#   Conditionals - Life of Brian guessing game without a while True loop."""

# round = 0
# answer = " "

# while round < 3 and answer != "Brian":
#     round += 1     # increase the round counter by 1
#     answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
#     if answer == "Brian": # logic to check if user gave correct answer
#         print("Correct!")
#     elif answer == "shrubbery":
#         print("You gave the super secret answer!")    
#     elif round == 3:    # logic to ensure round has not yet reached 3
#         print("Sorry, the answer was Brian.")    
#     else:                 # if answer was wrong
#         print("Sorry. Try again!")
       

############################### busted code warmup ##########################################
#!/usr/bin/env python
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

# def add(num1,num2):
#     print("\n" + str(num1) + " + " + str(num2) + " = " + str(calc1 + calc2))
    
# def sub():
#     print("\n" + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))


# def calculator():
   

#     while True:
       
#         calc1 = input("\nWhat is the first operator? Or, enter q to quit: ")
#         if calc1.lower() == "Q":
#             break
       
        
#         calc2 = input("\nWhat is the second operator? Or, enter q to quit: ")
#         if calc2.lower() == "q":
#          break
      
#         print("Enter an operation to perform on the two operators (+ or -): ")
#         operation = input()
#         if operation == "+":
#             add(calc1,calc2)
#         elif operation == '-':
#             sub(calc1,calc2)
#         else:
#             print("\n Not a valid entry. Restarting...")

# calculator()

# classinfo = {'all': [
#          {'name': 'Cat',
#           'skill level': 'amazing',
#           'spirit animal': 'Chinchilla',
#           'super power': 'Body Part Substitution'},
#          {'name': 'Chris',
#           'skill level': 'astonishing',
#           'spirit animal': 'Chipmunk',
#           'super power': 'Camouflage'},
#          {'name': 'Dao',
#           'skill level': 'astounding',
#           'spirit animal': 'Clam',
#           'super power': 'Bone Manipulation'},
#          {'name': 'David',
#           'skill level': 'awe-inspiring',
#           'spirit animal': 'Clownfish',
#           'super power': 'Claw Retraction'},
#          {'name': 'Henwin',
#           'skill level': 'breathtaking',
#           'spirit animal': 'Cobra',
#           'super power': 'Deflection'},
#          {'name': 'Herman',
#           'skill level': 'imposing',
#           'spirit animal': 'Condor',
#           'super power': 'Fang Retraction'},
#          {'name': 'Jose',
#           'skill level': 'inspiring',
#           'spirit animal': 'Constrictor',
#           'super power': 'Helicopter Propulsion'},
#          {'name': 'Justin',
#           'skill level': 'magnificent',
#           'spirit animal': 'Coral',
#           'super power': 'Invisibility'},
#          {'name': 'Kris',
#           'skill level': 'majestic',
#           'spirit animal': 'Cougar',
#           'super power': 'Immobility'},
#          {'name': 'Mannie',
#           'skill level': 'miraculous',
#           'spirit animal': 'Coyote',
#           'super power': 'Immutability'},
#          {'name': 'Marcos',
#           'skill level': 'spectacular',
#           'spirit animal': 'Crab',
#           'super power': 'Invulnerability'},
#          {'name': 'Marshall',
#           'skill level': 'staggering',
#           'spirit animal': 'Crane',
#           'super power': 'Jet Propulsion'},
#          {'name': 'Michael',
#           'skill level': 'stunning',
#           'spirit animal': 'Crawdad',
#           'super power': 'Invulnerability'},
#          {'name': 'Mike',
#           'skill level': 'stupefying',
#           'spirit animal': 'Crocodile',
#           'super power': 'Muscle Manipulation'},
#          {'name': 'Nikko',
#           'skill level': 'sublime',
#           'spirit animal': 'Crow',
#           'super power': 'Needle Projection'},
#          {'name': 'Phil',
#           'skill level': 'wonderful',
#           'spirit animal': 'Cuckoo',
#           'super power': 'Prehensile Tongue'},
#          {'name': 'Ryan',
#           'skill level': 'wondrous',
#           'spirit animal': 'Cicada',
#           'super power': 'Regenerative Healing Factor'},
#          {'name': 'Sachin',
#           'skill level': 'affecting',
#           'spirit animal': 'Damselfly',
#           'super power': 'Replication'},
#          {'name': 'Samekh',
#           'skill level': 'arresting',
#           'spirit animal': 'Deer',
#           'super power': 'Self-Detonation'},
#          {'name': 'Will',
#           'skill level': 'august',
#           'spirit animal': 'Dingo',
#           'super power': 'Super Strength'}]}

# print(classinfo["all"][12]["name"])

# name = classinfo["all"][12]["name"]
# superpower = classinfo["all"][12]["super power"]

# print('My name is ' + name + " and my superpower is " + superpower)

# for x in classinfo['all']:
#     print(x["name"])


##########################################lab 46 #############################################
# iplist = ["10.1.1.1", "10.2.2.2", "10.3.3.3"] # list of IP (str)

# for ip in iplist:
#     print(ip) 

###################################### 5/23 warmup ######################
#!/usr/bin/env python
# import sys
# import time


# def print1by1(text, delay=0.1):
#     # there's nothing wrong with this function, it's just some cool code!
#     for c in text:
#         sys.stdout.write(c)
#         sys.stdout.flush()
#         time.sleep(delay)



# def main():
#     def name_grabber():
#         while True:
#             try:
#                 name= input("What is your name?\n>")
#                 num= input("Pick a number between 1 and 3")
#                 if num in ["1","2","3"]:
#                     return name, num
#             except:
#                 print("Bad input.")




#     num_dict= {"1":"great","2":"awesome","3":"superb"}
#     # name, num= name_grabber()
#     result = name_grabber()
#     # print(result)
#     with open("horoscope.txt", "w") as fileobj:
#         fileobj.write(f"{result}, I predict today will be {num_dict[result[1]].upper()}!")

#     # not an error per se, but it's undesirable that
#     # this gets written out with no spaces
#     # fix the for loop to give a nicer output!
#     for x in ["YOUR ", "FUTURE ", "HAS ", "BEEN ", "WRITTEN ", "TO ", " HOROSCOPE.TXT..."]:
#         print1by1(x)

# main()

###################################lab 68 #############################
#!/usr/bin/python3
# """RZFeeser | Alta3 Research
#    Creating a simple dice program utilizing classes."""

# # standard library
# from random import randint

# class Player:
#     def __init__(self):
#         self.dice = []

#     def roll(self):
#         self.dice = [] # clears current dice
#         for i in range(3):  # make 3 rolls
#             self.dice.append(randint(1,6))   # 1 to 6 inclusive

#     def get_dice(self): # returns the dice rolls
#         return self.dice

# def main():
#     """called at run time"""

#     ## create our player objects
#     player1 = Player()
#     player2 = Player()

#     player1.roll()
#     player2.roll()

#     print(f"Player 1 rolled {player1.get_dice()}")
#     print(f"Player 2 rolled {player2.get_dice()}")

#     # determine which player won
#     if sum(player1.get_dice()) == sum(player2.get_dice()):
#         print("Draw!")
#     elif sum(player1.get_dice()) > sum(player2.get_dice()):
#         print("Player 1 wins!")
#     else:
#         print("Player 2 wins!")


# if __name__ == "__main__":
#     main()

############################################ ISS Morning Challenge #################
# import requests
# import datetime

# res = requests.get("http://api.open-notify.org/iss-now.json")
# data = res.json()
# print(data)
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# epoch_time = data["timestamp"]

# print("Current Location of the ISS: ")
# print("Lat: " + latitude)
# print("lon: " + longitude)

# date_time = datetime.datetime.fromtimestamp( epoch_time ) 
# print("Converted Datetime:", date_time )  
# 
# ############################################zodiac restructuring###########################
#  


