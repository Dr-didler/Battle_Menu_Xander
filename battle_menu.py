import random

year = 1
User_starting_HP = int(100)
User_starting_attack = int(20)
Enemy_starting_HP = int(80)
Enemy_starting_damage = int(15)
Mini_boss_health = int(140)
Mini_boss_damage = int(45)
#incorperate a regen only once for the boss, cant happen more then once
Boss_health = int(250)
Boss_regen = int(20)
Boss_dmg = int(70)
ability_to_atk = 0



#This function is for the time passing giving the enemys buffs

def time_changing_post_fight():
    global Enemy_starting_HP, Enemy_starting_damage
    Enemy_starting_HP += 20
    Enemy_starting_damage += 10
#the user should be allowed to chose their own upgs after each fight, the only issue is that the mini boss outscales the player

def user_choice_upg():
    global User_starting_HP, User_starting_attack, ability_to_atk
    User_buff = input("Chose a buff, extra health, extra damage, or first attack next.(type in hp,dmg,atk)")
    if User_buff == "dmg":
        User_starting_attack += 15
        print("Your attack buff now does", User_starting_attack, "dmg.")
    elif User_buff == "hp":
        User_starting_HP += 20
        print("Your new HP is", User_starting_HP)
    elif User_buff == "atk":
        ability_to_atk = 1
        print("you are going to attack first in your next encounter.")
    else:
        print("No buff applied.")
#this random number is for the amount of enemys you will fight, the larger the number, the more buffs you can apply

enemy_count = random.randint(1,5)

#note to self, next step is to add more enemys with diffrent stats and make sure they are replayable for buff farming, but mkae sure they are scaled appropiatly and not stronger then the mini boss

def starting_sequence():
    print("ahead lay", enemy_count, "enemies, each current enemy has", Enemy_starting_HP, "you currently do", User_starting_attack, "per attack.")
    user_hp = User_starting_HP
    user_attack = User_starting_attack
    # add a loop here to keep fighting until all enemys are defeated
    for enemy in range(enemy_count):
        enemy_hp = Enemy_starting_HP
        print("A new enemy appears with", enemy_hp, "HP.")
        # replace while-loop with a bounded for-loop to avoid infinite loops
        for turn in range(1000):
            # players attack
            enemy_hp -= user_attack
            input(f"You have {user_hp} HP left. Press Enter to continue...")
            print("the enemy in front of you has", enemy_hp,"hp")
            if enemy_hp <= 0:
                print("you have defeated the enemy")
                time_changing_post_fight()
                user_choice_upg()
                # refresh local stats in case buffs changed globals
                user_attack = User_starting_attack
                user_hp = User_starting_HP
                break
            # enemy attacks
            user_hp -= Enemy_starting_damage
            print("you have", user_hp, "left")
            if user_hp <= 0:
                print("you have been defeated, game over.")
                return
#list of current issues, the mini boss or farming sequence is called after dying, need to fix that, i need a restart function
#this is a standard fight sequence that can be called again for farming buffs
def enemy_farming():
    mini_boss_want = str(input("Do you want to fight the mini boss or farm before you fight(yes for mini boss, no for farming)."))
    if mini_boss_want == "yes":    
        mini_boss_fight()
    elif mini_boss_want == "no":
        for i in range(enemy_count):
            standard_fight_sequence()
    else:
        enemy_farming()
def enemy_farming_2():
    boss_want = str(input("Do you want to fight the boss or farm before you fight(yes for boss, no for farming)."))
    if boss_want == "yes":    
        boss_fight()
    elif boss_want == "no":
        for i in range(enemy_count):
            standard_fight_sequence()
    else:
        enemy_farming()

def standard_fight_sequence():
    for enemy in range(enemy_count):
        enemy_hp = Enemy_starting_HP
        print("A new enemy appears with", enemy_hp, "HP.")
        # replace while-loop with a bounded for-loop to avoid infinite loops
        #while loops werent working so i did whatever the monstrocity is below me
        for turn in range(1000):
            # player's attack
            enemy_hp -= user_attack
            uchoice = input("the enemy before you now has", enemy_hp)
            if enemy_hp <= 0:
                print("you have defeated the enemy")
                time_changing_post_fight()
                user_choice_upg()
                # refresh local stats in case buffs changed globals
                user_attack = User_starting_attack
                user_hp = User_starting_HP
                break
            # enemy attacks
            user_hp -= Enemy_starting_damage
            input("you have", user_hp, "left")
            if user_hp <= 0:
                print("you have been defeated, game over.")
                return
            
#if player wants to restart
def player_death_fight_choice():
    fight_choice = input("would you like to restart? (yes/no)")
    if fight_choice == "yes":
        starting_sequence()
    elif fight_choice == "no":
        print("You chose to face the mini boss.")
    else:
        print("Invalid choice, please type 'yes' or 'no'.")
        player_death_fight_choice()

def mini_boss_fight():
    print("You have reached the mini boss... get ready unc...")
    mini_boss_hp = Mini_boss_health
    user_hp = User_starting_HP
    user_attack = User_starting_attack
    print("your damage is" , user_attack, "your health is", user_hp)
    for turn in range(1000):
        # player's attack
        mini_boss_hp -= user_attack
        print("the mini boss now has", mini_boss_hp)
        if mini_boss_hp <= 0:
            print("You have defeated the mini boss")
            print("he leaves behind an eccense, you claim it and feel your strength grow")
            User_starting_attack += 10
            User_starting_HP += 20
            user_choice_upg()
            enemy_farming_2()
            return
            # mini boss attacks
        user_hp -= Mini_boss_damage
        print("you have", user_hp, "left")
        if user_hp <= 0:
            print("you have been defeated by the mini boss, game over.")
            player_death_fight_choice()
            return

def boss_fight():
    userchoice = input("The worlds fate rests on your shoulders, grabbing zangetsu, the boss walks into view. Do you wish to proceed?(press enter to proceed)")
    Boss_health = Boss_health
    user_hp = User_starting_HP
    user_attack = User_starting_attack
    print("your damage is" , user_attack, "your health is", user_hp)
    for turn in range(1000):
        # player's attack
        Boss_health -= user_attack
        print("the boss now has", Boss_health)
        if Boss_health <= 0:
            print("You have defeated the boss")
            defeat_sequence()
            return
            # mini boss attacks
        user_hp -= Boss_dmg
        print("you have", user_hp, "left")
        if user_hp <= 0:
            print("you have been defeated by the boss, game over.")
            player_death_fight_choice()
            return

def defeat_sequence():
    print("Yu have defeated all enemies and bosses! Congratulations!")
        

User_choice = input("You walk into a coridor, enemy's lay ahead, time to fight.(press enter)")
starting_sequence()
enemy_farming()
mini_boss_fight() 
boss_fight()