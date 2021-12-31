#  This game is coded in Python
#
#  It was developed by Ciaran Merritt, Natasha Woolley, Mark Domantay & Ian Davenport
#
#  This was a team project made by the four of us after learning Python at Code Nation in Manchester.
# 
#  The request was to build an Adventure Game in Python.


import time
import random
import sys, time
import textwrap

class person:
    def __init__(self, alive, name):
        self.alive = alive
        self.name = name

class victims(person):
    def __init__(self, alive, name, trophy):
        self.alive = alive
        self.name = name
        self.trophy = trophy

class officers(person):
    pass

class police:
    def __init__(self, officers, evidence, overall_heat):
        self.officers = officers
        self.evidence = evidence
        self.overall_heat = overall_heat

class locations:
    def __init__(self, location_name, targets, local_heat):
        self.location_name = location_name
        self.targets = targets
        self.local_heat = local_heat

class main_character:
    def __init__(self, name, murder_weapon, trophy, signature, num_kills):
        self.name = name
        self.murder_weapon = murder_weapon
        self.trophy = trophy
        self.signature = signature
        self.num_kills = num_kills

class safe_house:
    def __init__(self, trophies, murder_weapons, signature):
        self.trophies = trophies
        self.murder_weapons = murder_weapons
        self.signature = signature

class game_data:
    def __init__(self, days_untill_caught, trophies_taken, num_kills, fav_weapon, fav_trophy, fav_signature):
        self.days_untill_caught = days_untill_caught
        self.trophies_taken = trophies_taken
        self.num_kills = num_kills
        self.fav_weapon = fav_weapon
        self.fav_trophy = fav_trophy
        self.fav_signature = fav_signature


def selectionSwitch(input, num_of_options):#Ciaran: Used in the requestion selection function. Makes a dicrectory of all possible options and returns 100 if the user input wasn't found in it
    switch = {}
    for i in range(1, num_of_options + 1):
        switch[str(i)] = i
    return switch.get(input, 100)

def requestSelection(text, num_of_options): #Ciaran: A adaptive function to handle the request input of any size selection needed for the game. Reduces possible errors
    valid_input = False
    while valid_input == False:
        player_choice = selectionSwitch(input(text), num_of_options)
        if player_choice == 100:
            print("That is an invalid option")
        else:
            #print(player_choice)
            valid_input = True
    return player_choice



def createWeapons(weapons): #Mark: This function fills the list of Weapons with the data required

    # weapons_name= ["Fixed Blades", "rope", "QF 3-pounder Hotchkiss"]
    # for weapons in weapons_name:
    #     print(weapons)

    # heat_level_increase= ["1", "2", "3", "4", "5"] 
    # for heatlevel in heat_level_increase:
    #     print(heatlevel)

    # clean_kill_chance= ["1", "2", "3", "4", "5"]
    # for cleankill in clean_kill_chance:
    #     print(cleankill)

    # noise_level= ["1", "2", "3", "4", "5"]
    # for noise in noise_level:
    #     print(noise)




    #Clean kill chance between 0-5. 5 being defineite clean kill
    #Noise Level between 0-5. 5 being very noisey
    weapons["Weapons Name"].append("fixed blade")
    weapons["Heat Level Increase"].append(3) 
    weapons["Clean Kill Chance"].append(2)
    weapons["Noise Level"].append(0.5)

    weapons["Weapons Name"].append("rope")
    weapons["Heat Level Increase"].append(2)
    weapons["Clean Kill Chance"].append(4)
    weapons["Noise Level"].append(1)

    weapons["Weapons Name"].append("howdah pistol")
    weapons["Heat Level Increase"].append(4)
    weapons["Clean Kill Chance"].append(5)
    weapons["Noise Level"].append(2)
    
    return weapons

def createVictims(victim_list = []): #Ciaran: This function fills the list of victims with the data required
    victim_list.append(victims(True, "Homeless man", "a lock of hair")) #0
    victim_list.append(victims(True, "Lost Child", "a lock of hair")) #1
    victim_list.append(victims(True, "Thomas Briggs", "Mayor's wax seal stamp")) #2
    victim_list.append(victims(True, "Lady of the night", "a lock of hair")) #3
    victim_list.append(victims(True, "Drunk lady", "Engagement ring")) #4
    victim_list.append(victims(True, "Drunk ladies fiancee", "Engagement rings")) #5
    victim_list.append(victims(True, "Asleep person", "a lock of hair")) #6
    victim_list.append(victims(True, "Construction Worker", "a lock of hair")) #7
    victim_list.append(victims(True, "William Beaumont", "Engineering documents")) #8
    victim_list.append(victims(True, "Barmaid", "a lock of hair")) #9
    

def createOfficers(officers_list = []): #Ciaran: This function fills the list of officers with the data required
    officers_list.append(officers(True, "Uniformed Officer"))
    officers_list.append(officers(True, "Constable Timothy"))
    officers_list.append(officers(True, "Superintendent Jerome Caminada"))

def createLocations(location_list = []): #Ciaran: This function fills the list of locations with the data required
    location_list.append(locations("Medlock Slums", [0,1], 0))
    location_list.append(locations("Manchester Town Hall", [2,3], 0))
    location_list.append(locations("Sinclair's Oyster Bar", [4,5], 0))
    location_list.append(locations("John Ryland's Library", [6,7], 0))
    location_list.append(locations("Castle Hotel", [8,9], 0))
    
def printImage1():#Image for locations
    image = """
     _H_              _H_               _H_                  
   .=|_|===========v==|_|============v==|_|===========.    
  /                |                 |                 \ 
 /_________________|_________________|__________________|
 |=|_|_|_|  =|_|_|=|X|)^^^(|X|=|/ \|=||_|_|_|=| ||_|_|=|
 |=|_|_|_|== |_|_|=|X|\___/|X|=||_||=||_____|=|_||_|_|=|
 |=_________= ,-. =|'''''''''=''''''=|=_________== == =|
 |=|__|__|_| //O\\=|X|'''''|X|=//"\\=|=|_|_|_|_| .---.=|
 |=|__|__|_|=|| ||=|X|_____|X|=|| ||=|=|_______|=||"||=|
 |___db8b____||_||_|=_________=||_||_|__d8bod8b_=|j_j|=|
    """
    print("\n\n")
    image_split = image.splitlines()
    
    for i in range(0, len(image_split)):
        time.sleep(0.1)

        print(image_split[i])
    print("\n\n")
    time.sleep(0.5)

def printImage2():#Image for locations
    image = (r"""



				                   ^
				                  / \
                                 /___\
                                 |___|
                                 |]_[|
                                 / I \
                              JL/  |  \JL
   .^.                    i   ()   |   ()   i                    .^.
   |_|     .^.           /_\  LJ=======LJ  /_\           .^.     |_|
._/___\._./___\_._._._._.L_J_/.-.     .-.\_L_J._._._._._/___\._./___\._._._
       ., |-,-| .,       L_J  |_| [I] |_|  L_J       ., |-,-| .,        .,
       JL |-O-| JL       L_J%%%%%%%%%%%%%%%L_J       JL |-O-| JL        JL
IIIIII_HH_'-'-'_HH_IIIIII|_|=======H=======|_|IIIIII_HH_'-'-'_HH_IIIIII_HH_
-------[]-------[]-------[_]----\.=I=./----[_]-------[]-------[]--------[]-
 _/\_  ||\\_I_//||  _/\_ [_] []_/_L_J_\_[] [_] _/\_  ||\\_I_//||  _/\_  ||\
 |__|  ||=/_|_\=||  |__|_|_|   _L_L_J_J_   |_|_|__|  ||=/_|_\=||  |__|  ||-
 |__|  |||__|__|||  |__[___]__--__===__--__[___]__|  |||__|__|||  |__|  |||
IIIIIII[_]IIIII[_]IIIIIL___J__II__|_|__II__L___JIIIII[_]IIIII[_]IIIIIIII[_]
 \_I_/ [_]\_I_/[_] \_I_[_]\II/[]\_\I/_/[]\II/[_]\_I_/ [_]\_I_/[_] \_I_/ [_]
./   \.L_J/   \L_J./   L_JI  I[]/     \[]I  IL_J    \.L_J/   \L_J./   \.L_J
|     |L_J|   |L_J|    L_J|  |[]|     |[]|  |L_J     |L_J|   |L_J|     |L_J
|_____JL_JL___JL_JL____|-||  |[]|     |[]|  ||-|_____JL_JL___JL_JL_____JL_J
    """)
    print("\n\n")
    image_split = image.splitlines()
    
    for i in range(0, len(image_split)):
        time.sleep(0.1)

        #print(image_split[i])
    print((image))
    print("\n\n")
    time.sleep(0.5)

def printImage3():#Image for locations
    image = """
         _.._..,_,_
        (          )
         ]~,"-.-~~[
       .=])' (;  ([
       | ]:: '    [
       '=]): .)  ([
         |:: '    |
          ~~----~~
    """
    print("\n\n")
    image_split = image.splitlines()
    
    for i in range(0, len(image_split)):
        time.sleep(0.1)

        print(image_split[i])
    print("\n\n")
    time.sleep(0.5)

def printImage4():#Image for locations
    image = """
       __...--~~~~~-._   _.-~~~~~--...__
     //               `V'               \\
    //                 |                 \\
   //__...--~~~~~~-._  |  _.-~~~~~~--...__\\
  //__.....----~~~~._\ | /_.~~~~----.....__\\
 ====================\\|//====================
                     `---`
    """
    print("\n\n")
    image_split = image.splitlines()
    
    for i in range(0, len(image_split)):
        time.sleep(0.1)

        print(image_split[i])
    print("\n\n")
    time.sleep(0.5)

def printImage5():#Image for locations
    image = """
    #
   :#:
   : :
   : :
 .'   '.
 :_____:  .___. .___.
 |     |  |   | |   |       
 |     |  '. .' '. .'                 
 |     |    |     |      .--''''''--.
 |_____|    |     |     |'''''/      |
 :_____:   -'-   -'-    '''''/_...--'|
                            |__...--'  
    """
    print("\n\n")
    image_split = image.splitlines()
    
    for i in range(0, len(image_split)):
        time.sleep(0.1)

        print(image_split[i])
    print("\n\n")
    time.sleep(0.5)



def checkIfCaught(player, location_list, police_data, current_location, weapons):#Ciaran: This function does a check on whether the player is caught or not. Returning true or false
    #Killing someone adds the heat for killing that person to the local heat.
    #Overall heat is increase by one for each kill
    print("")
    is_caught = False
    if current_location != "":
        random_num =random.randint(0, 100)
        heat_level = (police_data.overall_heat + location_list[current_location].local_heat + police_data.evidence + weapons["Noise Level"][player.murder_weapon]) * 10
        if(heat_level < random_num):
            print("\033[1;31;40mDidn't get caught ")
            print(f"Chance of getting caught: %{heat_level}")
            print(f"What you rolled: {random_num}")
            is_caught = False
        else:
            print("\033[1;31;40mYou got caught")
            print(f"Chance of getting caught: %{heat_level}")
            print(f"What you rolled: {random_num}")
            is_caught = True
    else:
        print("\033[1;31;40mError on check if caught") #error
        
    print("\033[1;37;40m ")
    return is_caught


# This is the introduction. First asks the player their name.
# Then shows intro graphic and sets the background story
def introduction(player): #Ian: is the introduction to the game section

    

    
    print("")
    print("")
    print("")
    print("")
    print("This game was created by team M.I.N.C")
    print("Mark, Ian, Natasha & Ciaran \n")
    # print("""\033[1;31;40m







    #                                         =----   --
    #                                         - @@=   @@-----     ---
    #                                           =@-   @@--=@=   =@ -+@-
    #                                           =@-   @@  -@=   @@-----
    #                                            -    --   -      ---- 


    #              @@@   -@@-                            @@                         =-
    #              @==@-===@-   --=@=  -@=-=@@   ==--==  @@--=@-  -=-==   -@=-==   @@=-  ==--==  @@-=-
    #              @==@-===@-  ----@@  -@=  @@  -@-      @@  -@-  @@ --=-  --===   -@   -@= -==- @@
    #              @  =@= =@   @@--=@   @-  =@   ==--    ===  @-  -==--    ---=@-   @-   -=--    @=


    #                         -@@---@=
    #                          @@ -==-  ---=@  @@-=@=-=@= =@=--@@   ---@@   ---=@-  ==--==
    #                          @@ =@-   ---@@  @@  @=  @= =@   @@   ---@@- @@  =@- -@= -==- 
    #                          @=   @-  =@-=@  @=  @-  @- -@--=-   =@=-=@- ===-=@-  -=--
    #                                                     -@                --===    









    # """)

    title_screen = """





                                            =----   --
                                            - @@=   @@-----     ---
                                              =@-   @@--=@=   =@ -+@-
                                              =@-   @@  -@=   @@-----
                                               -    --   -      ---- 


                 @@@   -@@-                            @@                         =-
                 @==@-===@-   --=@=  -@=-=@@   ==--==  @@--=@-  -=-==   -@=-==   @@=-  ==--==  @@-=-
                 @==@-===@-  ----@@  -@=  @@  -@-      @@  -@-  @@ --=-  --===   -@   -@= -==- @@
                 @  =@= =@   @@--=@   @-  =@   ==--    ===  @-  -==--    ---=@-   @-   -=--    @=


                            -@@---@=
                             @@ -==-  ---=@  @@-=@=-=@= =@=--@@   ---@@   ---=@-  ==--==
                             @@ =@-   ---@@  @@  @=  @= =@   @@   ---@@- @@  =@- -@= -==- 
                             @=   @-  =@-=@  @=  @-  @- -@--=-   =@=-=@- ===-=@-  -=--
                                                        -@                --===    






    """

    split_title_screen = title_screen.splitlines()
    print("\033[1;31;40m")
    for i in range(0, len(split_title_screen)):
        time.sleep(0.1)

        print(split_title_screen[i])

    time.sleep(0.5)
    
    #print("\033[1;37;40mHello and welcome to our game \n\n")
    typewriter("\033[1;37;40mHello and welcome to our little game... \n\n")

    #print("The year is 1895, a new century is fast approaching and you have made a personal target – \n   try and kill 5 more people before you move onto your new adventure in France next year. \n")

    typewriter("The year is 1895, a new century is fast approaching and you have made a personal target – \n  try and kill 5 more people before you move onto your new adventure in France next year. \n")

    time.sleep(1)

    #print("It is 7 in the evening in Manchester, on a cold November night. The black smoke from the factories is pluming in the sky, \n the rain is cutting through the thick smog as it pours down on the cobbles of the city.\n")

    typewriter("It is 7 in the evening in Manchester, on a cold November night. The black smoke from the factories is pluming in the sky, \n  the rain is cutting through the thick smog as it pours down on the cobbles of the city.\n")


    time.sleep(2)
    typewriter(f"You are writing a letter to the police letting them know that after your recent hiatus you will be continuing your killing spree.\n\n")
    time.sleep(1)
    
    name_chosen = False
    #get player name
    while name_chosen == False:
        player_name = input("\n\nAt the bottom you sign your name: ")
        player_choice = requestSelection((f"\n\nAre you happy with your name {player_name} ?\n1) Yes\n2) No\nEnter here: "), 2)
        if player_choice == 1:
            player.name = player_name
            #test(player)
            #print("Playing game")
            #print(f"player name {player.name}")
            name_chosen = True
        elif player_choice == 2:
            #print("Quiting")
            name_chosen = False 
    

    
def safeRoom(player, location_list, victim_list, police_data, weapons):#Mark: This is the safe room for the player. it will handle the played selecting their weapons and where they want to go hunting
    #weapon selection
    print("") #description of the options of locations <------------------------------

    print("Avaliable weapons are:")
    index = 1
    for weapon_display in weapons["Weapons Name"]:
        print(f"{index}) {weapon_display}")
        index += 1

    chosen_weapon = requestSelection("Please pick your weapon: ", len(weapons["Weapons Name"])) 
    player.murder_weapon = chosen_weapon - 1   

    print("\n\n")
    
    valid_option = False

    while valid_option == False:

    
        for i in range(0 , len(location_list)):
            if location_list[i].local_heat == 0:
                print(f"option {i+1} : {location_list[i].location_name}")
        
    
        user_response = requestSelection("\n\nPlease select your desired location: ", 5)
        if user_response == 1 and location_list[0].local_heat == 0:
            print("\nYou have selected Medlock Slums")
            typewriter("You can hear the hum of family life in the evening in the Medlock slums area. \nIt is a place filled with rats and rubbish, reflecting the most destitute citizens of Manchester. \nYou can see the privies dangling over the river. The stench is truly unimagible.\n")
            time.sleep(1) 
            valid_option = True
        elif user_response == 2 and location_list[1].local_heat == 0:
            print("\nYou have selected Manchester Town Hall")
            typewriter("Manchester's New Town Hall, a true architectural gem of Manchester inspired by 13th-century Early English Gothic architecture and completed in 1877. \nThe Manchester Bee takes pride of place throughout the building in the floor tiles as a homage to Manchester's Industrial Revolution.\n")
            time.sleep(1) 
            valid_option = True
        elif user_response == 3  and location_list[2].local_heat == 0:
            print("\nYou have selected Sinclair's Oyster Bar")
            typewriter("Sinclair's has been a staple pub of the area for hundreds of years now. \nIt is normally filled to the brim with drunkards, gamblers and those looking for a good time. \nIt is a scene engulfed with the sins of the flesh.\n")
            time.sleep(1) 
            valid_option = True
        elif user_response == 4 and location_list[3].local_heat == 0:
            print("\nYou have selected John Rylands Library")
            typewriter("The neo-Gothic building on the newly renamed Deansgate is still under construction. \nIt was commisioned by Enriqueta Rylands, the wife of the late John Rylands. \nGrey buildings with human like statues fill the area.\n")
            time.sleep(1) 
            valid_option = True
        elif user_response == 5 and location_list[4].local_heat == 0:
            print("\nYou have selected Castle Hotel")
            typewriter("A lively and popular bar located in the North of Manchester city. \nLive music, spoken word, comedy and animal exhibitions fill the area. \nA place for the working class to let their hair down.\n")
            time.sleep(1) 
            valid_option = True


    chosen_location = user_response - 1

    return chosen_location

def newsPaper(kill_list):  #Ian: This is the news update that happens every day to tell the player what has happened on their hunt and shows the news story from the day prior
    
    print("\nThe following morning the newspaper arrives at your doorstep")


    print("""
     __________
    |DAILY NEWS|
    |&&& ======|
    |=== ======|
    |=== == ##$|
    |[_] ======|
    |=== ===!##|
    |__________|

    """)

    # kill_list = {
    #     "Victim Name" : [],
    #     "Kill Weapon" : [],
    #     "Location of Kill" : []
    # }
    
    #  The below could have an EVENT DATE added if a DATE variable is already created


    if kill_list["Victim Name"][len(kill_list["Victim Name"]) - 1] == "Homeless man":
        print("\033[1m" + "Construction on John Ryland’s Library continues" + "\033[0m")
 
    elif kill_list["Victim Name"][len(kill_list["Victim Name"]) - 1] == "Lady of the night":
        print("\033[1m" + "Milk prices likely to increase" + "\033[0m")

    elif kill_list["Victim Name"][len(kill_list["Victim Name"]) - 1] == "Lost child":
        print("\033[1m" + "A child was found murdered after being separated from parents" + "\033[0m")

    elif kill_list["Victim Name"][len(kill_list["Victim Name"]) - 1] == "Thomas Briggs":
        print("\033[1m" + "Mayor of Manchester found murdered in the Town Hall" + "\033[0m")

    elif kill_list["Victim Name"][len(kill_list["Victim Name"]) - 1] == "Drunk lady":
        print("\033[1m" + "Killer spotted luring local woman found murdered from Sinclair’s Oyster Bar" + "\033[0m")

    elif kill_list["Victim Name"][len(kill_list["Victim Name"]) - 1] == "Drunk ladies fiancee":
        print("\033[1m" + "Engaged couple from Didsbury found murdered near Sinclair’s Oyster Bar" + "\033[0m")     

    elif kill_list["Victim Name"][len(kill_list["Victim Name"]) - 1] == "Asleep person":
        print("\033[1m" + "Local man found killed on public bench" + "\033[0m")

    elif kill_list["Victim Name"][len(kill_list["Victim Name"]) - 1] == "Construction Worker":
        print("\033[1m" + "Construction worker at John Ryland’s Library, Mark Smith, found slain" + "\033[0m")

    elif kill_list["Victim Name"][len(kill_list["Victim Name"]) - 1] == "William Beaumont":
        print("\033[1m" + "Local engineer William Beaumont murdered on visit home" + "\033[0m")   

    elif kill_list["Victim Name"][len(kill_list["Victim Name"]) - 1] == "Barmaid":
        print("\033[1m" + "Popular and reliable bar maid Emily Thompson killed behind pub she worked at" + "\033[0m")



def signature(): #Natasha: The bee signature the player carves into the victims body
    print("""\033[1;31;40m
                                 &&,               %&@                        
                                    %&&@      *&&@*                           
                      @@               &&&&@&&              /&%              
                        .&&/          (&&*,,.@&&           @&@                
                           (@&&&@     .&&....#&@     ,&&&&@                   
                                ,&@   %&@(,,*%&&   /&@                        
           /@@&&&&&&&@@%,          @&@&,.@,&./,&&&&%          (&@@&&&&&&&@&.  
        ,&@.,,,,.,,,,,,,..*%@@&&@&,  @&..@,&./,*&(  (@@&&@&#,.,,,,,,,,,,,,,*&@
        &&.,,,,,,,,,,,,,,,,,,,,,,,.*&&&%,*.&.,.@&@#,,,,,,,,,,,,,,,,,,,,,,,,,&&
         (&@.,,,,,,,,,,,,,,,,,,,,,,,@&&&.,,,,,#&&&%.,,,,,,,,,,,,,,,,,,,,,,/&& 
            @&&%.,,,,,,,,,,,,,.&&&@  #&&&&&&&&&&&  /@&@(.,,,,,,,,,,,,,,@&&(   
                 %@&&&&&&&&&&&      &&,.......,.&&%     #&&&&&&&&&&@@/        
                         /@&#     &&&@..........*&&&.     @&@                 
                 (@@@&&&@.       %&.&&&&&&&&&&&&&&@&&        /@&&&@@&.        
                                 #&/&/,,,,.,.,.,,@@&&                         
                                 /&(&@@%(/***/#&@&@@&                         
                                &@ @&&&&&&&&&&&&&/.&@                        
                              @&    &@,.,,,,,,,&@   &&/                      
                           #&&*      &&&&&&&&&&&      &&@.                   
                      %&%*,           &&/,,,&&.          .,/&@*              
                                        %&&@.                         
    
    """)
    print("\033[1;37;40m")

    time.sleep(2)

def out_hunting(player, location_list, victim_list, police_data, chosen_location, weapons): #Natasha: This function handles all the possible encounters of each location
    is_caught = False
    victim_name = ""
    weapon_used = weapons["Weapons Name"][player.murder_weapon]
    location_of_kill = ""
    player.trophy = ""
    
    heat_debuf = 2
    murder_descriptions = ["","",""]
    
    #trying to kill someone
    #location description of whats happening
    #location_list contains ( list location data (name, targets, location_heat) )
    if location_list[chosen_location].location_name == "Medlock Slums":
        #printImage1()
        typewriter(textwrap.dedent(f"""

        You slowly pace down the dimly lit slums. 
        Down a ginnel is a homeless man sleeping heavily in a dark corner, at the ginnel entrance a child is
        wandering around and crying for his parents. 
        Who are you going to choose to be your victim {player.name}? 
        1) Homeless man
        2) Lost child
        """))
        user_input = requestSelection("Enter: ",2)
        if user_input == 1:
            #kill someone
            print(f"You murder the homeless person with your {weapon_used}")
            location_list[chosen_location].local_heat += 1 / heat_debuf #homeless person heat
             #check if caught
             #could add later a variable for them possible shouting out
            if checkIfCaught(player,location_list, police_data, chosen_location, weapons) == True:
                #caught
                is_caught = True
                print("Caught")
            else:
                #not caught
                victim_name = "Homeless man"
                weapon_used = weapons["Weapons Name"][player.murder_weapon]
                location_of_kill = "Medlock Slums"
                police_data.overall_heat += 1 / heat_debuf
                #claim trophie
                user_input = requestSelection(("\n\nWould like to pick up a trophy?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    player.trophy = victim_list[0].trophy
                    print(f"You took {victim_list[0].trophy} from the corpse")

                #leave signature
                user_input = requestSelection(("\n\nWould like to leave a signature?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    print("You carve the Manchester bee into their flesh")
                    signature()
                    police_data.overall_heat += 1 / heat_debuf
        else:
            print(f"You murder the lost child with your {weapon_used}")
            location_list[chosen_location].local_heat += 3 / heat_debuf
            if checkIfCaught(player,location_list, police_data, chosen_location, weapons) == True:
                is_caught = True
                print("Caught")
            else:
                victim_name = "Lost child"
                weapon_used = weapons["Weapons Name"][player.murder_weapon]
                location_of_kill = "Medlock Slums"
                police_data.overall_heat += 3 / heat_debuf
                user_input = requestSelection(("\n\nWould like to pick up a trophy?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    player.trophy = victim_list[1].trophy
                    print(f"You took {victim_list[1].trophy} from the corpse")
                
                user_input = requestSelection(("\n\nWould like to leave a signature?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    print("You carve the Manchester bee into their flesh")
                    signature()
                    police_data.overall_heat += 1 / heat_debuf
    

    if location_list[chosen_location].location_name == "Manchester Town Hall":
        #printImage2()
        typewriter(textwrap.dedent(f"""

        To the right of the Town Hall entrance a lady of the night is looking for punters, she looks exhausted and is clearly fed up. 
        To the left Thomas Briggs, the Mayor of Manchester is walking into the main doors with a sense of urgency. 
        Who are you going to choose to be your next victim {player.name}?
        1) Thomas Briggs
        2) Lady of the night
        """))
        user_input = requestSelection("Enter: ",2)
        if user_input == 1:
            print(f"You murder Thomas Briggs with your {weapon_used}")
            location_list[chosen_location].local_heat += 5 / heat_debuf
            if checkIfCaught(player,location_list, police_data, chosen_location, weapons) == True:
                is_caught = True
                print("Caught")
            else:
                victim_name = "Thomas Briggs"
                weapon_used = weapons["Weapons Name"][player.murder_weapon]
                location_of_kill = "Manchester Town Hall"
                police_data.overall_heat += 1 / heat_debuf
                user_input = requestSelection(("\n\nWould you like to pick up a trophy?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    player.trophy = victim_list[2].trophy
                    print(f"You took {victim_list[2].trophy} from the corpse")

                user_input = requestSelection(("\n\nWould you like to leave a signature?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    print("You carve the Manchester bee into their flesh")
                    signature()
                    police_data.overall_heat += 1 / heat_debuf
        else:
            print(f"You murder the lady of the night with your {weapon_used}")
            location_list[chosen_location].local_heat += 1 / heat_debuf
            if checkIfCaught(player,location_list, police_data, chosen_location, weapons) == True:
                is_caught = True
                print("Caught")
            else:
                victim_name = "Lady of the night"
                weapon_used = weapons["Weapons Name"][player.murder_weapon]
                location_of_kill = "Manchester Town Hall"
                police_data.overall_heat += 1 / heat_debuf
                user_input = requestSelection(("\n\nWould you like to pick up a trophy?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    player.trophy = victim_list[3].trophy
                    print(f"You took {victim_list[3].trophy} from the corpse")
                
                user_input = requestSelection(("\n\nWould you like to leave a signature?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    print("You carve the Manchester bee into their flesh")
                    signature()
                    police_data.overall_heat += 1 / heat_debuf


    if location_list[chosen_location].location_name == "Sinclair's Oyster Bar""":
        printImage3()
        typewriter(textwrap.dedent(f"""

        A woman stumbles out into the courtyard in front of Sinclair’s Oyster Bar.
        You approach her to lure her away, but she starts shouting back to a man who looks at you both and says he will come out once he finishes his drink. 
        What will you do {player.name}?    
        1) Lure the drunk woman away and murder her
        2) Wait for the man to join and kill them both
        """))
        user_input = requestSelection("Enter: ",2)
        if user_input == 1:
            print(f"You murder the drunk woman with your {weapon_used}")
            location_list[chosen_location].local_heat += 3 / heat_debuf
            if checkIfCaught(player,location_list, police_data, chosen_location, weapons) == True:
                is_caught = True
                print("Caught")
            else:
                victim_name = "Drunk lady"
                weapon_used = weapons["Weapons Name"][player.murder_weapon]
                location_of_kill = "Sinclair's Oyster Bar"
                police_data.overall_heat += 1 / heat_debuf
                user_input = requestSelection(("\n\nWould you like to pick up a trophy?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    player.trophy = victim_list[4].trophy
                    print(f"You took {victim_list[4].trophy} from the corpse")

                user_input = requestSelection(("\n\nWould you like to leave a signature?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    print("You carve the Manchester bee into their flesh")
                    signature()
                    police_data.overall_heat += 1 / heat_debuf
        else:
            print(f"You murder the drunk man and woman with your {weapon_used}")
            location_list[chosen_location].local_heat += 2 / heat_debuf
            if checkIfCaught(player,location_list, police_data, chosen_location, weapons) == True:
                is_caught = True
                print("Caught")
            else:
                victim_name = "Drunk ladies fiancee"
                weapon_used = weapons["Weapons Name"][player.murder_weapon]
                location_of_kill = "Sinclair's Oyster Bar"
                police_data.overall_heat += 1 / heat_debuf
                user_input = requestSelection(("\n\nWould you like to pick up a trophy?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    player.trophy = victim_list[5].trophy
                    print(f"You took {victim_list[5].trophy} from the corpse")
                
                user_input = requestSelection(("\n\nWould you like to leave a signature?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    print("You carve the Manchester bee into their flesh")
                    signature()
                    police_data.overall_heat += 1 / heat_debuf


    if location_list[chosen_location].location_name == "John Ryland's Library":
        printImage4()
        typewriter(textwrap.dedent(f"""

        You are checking out the progress of the construction of John Ryland’s library, maybe you could dump your victims here so police find them quicker? 
        As you are circling the building you spot a lone construction worker late inside and opposite a man sleeping on a bench. 
        Who are you going to choose to be your next victim {player.name}?
        1) Construction worker
        2) Sleeping man
        """))
        user_input = requestSelection("Enter: ",2)
        if user_input == 1:
            print(f"You murder the construction worker with your {weapon_used}")
            location_list[chosen_location].local_heat += 2 / heat_debuf
            if checkIfCaught(player,location_list, police_data, chosen_location, weapons) == True:
                is_caught = True
                print("Caught")
            else:
                victim_name = "Construction Worker"
                weapon_used = weapons["Weapons Name"][player.murder_weapon]
                location_of_kill = "John Ryland's Library"
                police_data.overall_heat += 1 / heat_debuf
                user_input = requestSelection(("\n\nWould you like to pick up a trophy?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    player.trophy = victim_list[6].trophy
                    print(f"You took {victim_list[6].trophy} from the corpse")

                user_input = requestSelection(("\n\nWould you like to leave a signature?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    print("You carve the Manchester bee into their flesh")
                    signature()
                    police_data.overall_heat += 1 / heat_debuf
        else:
            print(f"You murder the sleeping man with your {weapon_used}")
            location_list[chosen_location].local_heat += 3 / heat_debuf
            if checkIfCaught(player,location_list, police_data, chosen_location, weapons) == True:
                is_caught = True
                print("Caught")
            else:
                victim_name = "Asleep person"
                weapon_used = weapons["Weapons Name"][player.murder_weapon]
                location_of_kill = "John Ryland's Library"
                police_data.overall_heat += 1 / heat_debuf
                user_input = requestSelection(("\n\nWould you like to pick up a trophy?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    player.trophy = victim_list[7].trophy
                    print(f"You took {victim_list[7].trophy} from the corpse")
                
                user_input = requestSelection(("\n\nWould you like to leave a signature?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    print("You carve the Manchester bee into their flesh")
                    signature()
                    police_data.overall_heat += 1 / heat_debuf

    if location_list[chosen_location].location_name == "Castle Hotel":
        printImage5()
        typewriter(textwrap.dedent(f"""

        It is a surprisingly quiet night at the Castle Hotel. 
        A man at the bar is talking to the bar maid about an automotive engineering project he is working on and that he is back in Manchester for a few nights. 
        The bar maid goes to pour him a new pint and realises the barrel needs changing, she says she’ll go out back to sort it. 
        The man says there is no rush as he is going to the bathroom. 
        Who do you follow {player.name}?
        1) Bar maid
        2) The engineer
        """))
        user_input = requestSelection("Enter: ",2)
        if user_input == 1:
            print(f"You murder the bar maid with your {weapon_used}")
            location_list[chosen_location].local_heat += 2 / heat_debuf
            if checkIfCaught(player,location_list, police_data, chosen_location, weapons) == True:
                is_caught = True
                print("Caught")
            else:
                victim_name = "Barmaid"
                weapon_used = weapons["Weapons Name"][player.murder_weapon]
                location_of_kill = "Castle Hotel"
                police_data.overall_heat += 1 / heat_debuf
                user_input = requestSelection(("\n\nWould like to pick up a trophy?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    player.trophy = victim_list[8].trophy
                    print(f"You took {victim_list[8].trophy} from the corpse")

                user_input = requestSelection(("\n\nWould you like to leave a signature?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    print("You carve the Manchester bee into their flesh")
                    signature()
                    police_data.overall_heat += 1 / heat_debuf
        else:
            print(f"You murder William Beaumont with your {weapon_used}")
            location_list[chosen_location].local_heat += 4 / heat_debuf
            if checkIfCaught(player,location_list, police_data, chosen_location, weapons) == True:
                is_caught = True
                print("Caught")
            else:
                victim_name = "William Beaumont"
                weapon_used = weapons["Weapons Name"][player.murder_weapon]
                location_of_kill = "Castle Hotel"
                police_data.overall_heat += 1 / heat_debuf
                user_input = requestSelection(("\n\nWould you like to pick up a trophy?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    player.trophy = victim_list[9].trophy
                    print(f"You took {victim_list[9].trophy} from the corpse")
                
                user_input = requestSelection(("\n\nWould you like to leave a signature?\n1) Yes\n2) No\nEnter: "), 2)
                if user_input == 1:
                    print("You carve the Manchester bee into their flesh")
                    signature()
                    police_data.overall_heat += 1 / heat_debuf



    if is_caught == False:
        print("\nYou safely return home without being caught.\n")

    return is_caught, victim_name, weapon_used, location_of_kill



def escapeToFrance(police_data, safe_house_info):#Ian+Ciaran: Handles the event when the player tries to escape to France
    escaped = False
    captured = False
    print("\n\nYou've had your fill here and elected to escape to France. You head to Liverpool to catch a ship.")
    time.sleep(1)
    print("...")
    time.sleep(1)

    # Establish the player preference to Keep or Dump. If DUMP then the trophies variable is wiped
    print("You reach the ship to France, but unbeknownst to you there has been an increase of people smugglers in the area so they are randomly searching passengers before they board. \nYou might be searched... do you keep you beloved trophies, your pride and joy, or do you dump them?")
    print("\n 1) Dump your trophies \n 2) Keep your trophies and try sneak past")

    # If KEEP then variable has contents
    # Points higher for risk of KEEPING

    keep_trophies = requestSelection("\nPlease pick your choice: ",2)
    if keep_trophies == 1:
        print("You have chosen to dump your trophies")
        safe_house_info.trophies.clear
        # clear the variable which holds Trophies count value and item names
    else:
        print("You have chosen to keep hold of your trophies and try sneak past the police")
        # You now move onto the boarding ramp >>>
    

    random_num =random.randint(0, 100)
    heat_level = (police_data.overall_heat + police_data.evidence) * 10
    if(heat_level < random_num):
        print("You were able to get onto the boat with your trophies")
        escaped = True
    else:
        print("There are police at the ferry checking peoples bags")
        if keep_trophies == 1:
            escaped = True
        else:
            escaped = False
            captured = True

    return escaped, captured

    # Have a random number so have a 50/50 of getting caught IF have trophies
    # let caught_chance = (random.randint(1,2))
    #    if (caught_chance = 2) is_caught = True
    #    run the endgame function    

    
    # if checkIfCaught(player,location_list, police_data, chosen_location, weapons) == True:
    # is_caught = True
    # print("Caught")
    # victim_list[0-9].trophy



    # 
    # Board ship

    # > endgame()




def endGame(player, game_stats, captured, escaped, kill_list, safe_house_info):#Ciaran: This prints out the end results of the game. It will change depending on whether the player was caught or was able to escaped to france

    # print("\033[1;31;40mDid get caught")
    # print("Tough luck")
    # print(kill_list)
    # print(safe_house_info.trophies)
    # print("\033[1;37;40m")

    if captured == True:
        print("")

        print("""

     __________
    |DAILY NEWS|
    |&&& ======|
    |=== ======|
    |=== == ##$|
    |[_] ======|
    |=== ===!##|
    |__________|


    """)

        print(f"The notrious killer {player.name} has been arrested and put in prison")
        
        if len(kill_list["Victim Name"]) > 1:
            victim_news = kill_list["Victim Name"][0]
            for i in range(1, len(kill_list["Victim Name"])):
                victim_news = victim_news + (", " + kill_list["Victim Name"][i])
            print(f"Their victims were {victim_news}")
        elif len(kill_list["Victim Name"]) == 1:
            victim_news = kill_list["Victim Name"][0]
            print(f"Their victims were {victim_news}")
        else:
            print("They were caught before they could continue to kill after warning police with a letter of their intentions")

        
        
            
    elif escaped == True:
        
        if len(safe_house_info.trophies) == 0:
            print("You achieved your dreams but had to give up your precious trophies to start your new adventure. Maybe once you arrive you can start a new collection?\n")

            victim_news = kill_list["Victim Name"][0]
            for i in range(1, len(kill_list["Victim Name"])):
                victim_news = victim_news + (", " + kill_list["Victim Name"][i])
            print(f"Your victims were {victim_news}")
        else:
            print("You have achieved your wildest dreams and took your precious trophies with you on your new adventure. Maybe once you arrive you can expand your collection?\n")

            victim_news = kill_list["Victim Name"][0]
            for i in range(1, len(kill_list["Victim Name"])):
                victim_news = victim_news + (", " + kill_list["Victim Name"][i])
            print(f"Your victims were {victim_news}")


# If caught with trophies > After all you got away with you let your trophies get in the way of your escape. Kiss your freedom goodbye.


# This function displays any reports or news stories in a teleprinter / typewriter style
# The text to be printed needs to be stored under variable name 'message'
def typewriter(message): #Ian: Creates the typewriter effect when printing to the terminal
    for char in message:
	    sys.stdout.write(char)
	    sys.stdout.flush()
	    time.sleep(0.01)



def game():#Ciaran: This handles all of the game functions inside it and checks if the game is still running
    escaped = False
    captured = False

    player = main_character("", 0, 0, "", 0)
    game_stats = game_data(0, 0, 0, " ", " ", " ")
    weapons = {
    "Weapons Name" : [], #weapon name MUST BE A STRING
    "Heat Level Increase" : [], #heat level it increases MUST BE AN INT 1-3
    "Clean Kill Chance" : [], #chance of a clean kill MUST BE AN INT 1-3
    "Noise Level": [] #how loud it was MUST BE AN INT 
    }
    weapons = createWeapons(weapons)

    safe_house_info = safe_house([], weapons, "")

    victim_list = []
    createVictims(victim_list)

    officer_list = []
    createOfficers(officer_list)

    location_list = []
    createLocations(location_list)
    #print(f"Location: {location_list[0].location_name} \nPeople at this location: {victim_list[location_list[0].targets[0]].name} and {victim_list[location_list[0].targets[1]].name}")

    police_data = police(officer_list, 0, 0)

    kill_list = {
        "Victim Name" : [],
        "Kill Weapon" : [],
        "Location of Kill" : []
    }

    introduction(player)
    num_kills = 0

    while (escaped == False and captured == False):
        #safeRoom(player, location_list, victim_list, police_data, weapons)
        chosen_location = 0 #needds to get this from the saferoom function
        chosen_location = safeRoom(player, location_list, victim_list, police_data, weapons)
        #print(f"Going out on the hunt to {chosen_location}")
        hunting_outing = out_hunting(player, location_list, victim_list, police_data, chosen_location, weapons)
        captured = hunting_outing[0]
        
        #will need to return whether or not the play was caught from out hunting
        if captured == False:
            num_kills += 1
            kill_list["Victim Name"].append(hunting_outing[1])
            kill_list["Kill Weapon"].append(hunting_outing[2])
            kill_list["Location of Kill"].append(hunting_outing[3])
            safe_house_info.trophies.append(player.trophy)
            newsPaper(kill_list)
            #Possibly add whether they left a signature or not
            
        else:
            endGame(player, game_stats, captured, escaped, kill_list, safe_house_info)

        if num_kills == 5:
            results = escapeToFrance(police_data, safe_house_info)
            escaped = results[0]
            captured = results[1]
            endGame(player, game_stats, captured, escaped, kill_list, safe_house_info)

            
        print()

    del player
    del game_stats
    weapons.clear
    victim_list.clear
    officer_list.clear
    location_list.clear

    



def main_menu():#Ciaran: This function just checks if the player wants to play the game or quit
    game_running = True
    print("\033[1;37;") #set text to white so errors and checks can be in red to make sure they are visible
    #test1 = 10
    #test2 = "test"
    #requestSelection((f"testing f function :\n{test1}\n{test2}"))
    times_played = 0 
    while game_running == True:
        if times_played == 0:
            player_choice = requestSelection((f"Are you ready to play?\n1) Yes\n2) No\nEnter here: "), 2)
            times_played += 1
        else:
            player_choice = requestSelection((f"Are you ready to play again?\n1) Yes\n2) No\nEnter here: "), 2)
            times_played += 1

        if player_choice == 1:
            #print("Playing game")
            game()
        elif player_choice == 2:
            print("Quiting")
            game_running = False 

main_menu()






