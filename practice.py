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

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# if user set IP of gateway
if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk: # if any data is provided, this will test true
   print("Looks like the IP address was set: " + ipchk) # indented under if
else: # if data is NOT provided
   print("You did not provide input.") # indented under else
   
