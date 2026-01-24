import random

year = 1
User_starting_HP = int(100)
User_starting_attack = int(20)
Enemy_starting_HP = int(80)
Enemy_starting_damage = int(15)
Mini_boss_health = int(250)
Mini_boss_damage = int(45)
#incorperate a regen only once for the boss, cant happen more then once
Boss_health = int(350)
Boss_regen = int(20)
Boss_dmg = int(70)
ability_to_atk = 0



#This function is for the time passing giving the enemys buffs

def time_changing_post_fight():
    global Enemy_starting_HP, Enemy_starting_damage
    Enemy_starting_HP += 20
    Enemy_starting_damage += 10

def user_choice_upg():
    global User_starting_HP, User_starting_attack, ability_to_atk
    User_buff = input("Chose a buff, extra health, extra damadge, or first attack next.(type in hp,dmg,atk)")
    if User_buff == "dmg":
        User_starting_attack += 5
        print("Your attack buff now does", User_starting_attack, "dmg.")
    elif User_buff == "hp":
        User_starting_HP += 10
        print("Your new HP is", User_starting_HP)
    elif User_buff == "atk":
        ability_to_atk = 1
        print("you are going to attack first in your next encounter.")
    else:
        print("No buff applied.")
#this random number is for the amount of enemys you will fight, the larger the number, the more buffs you can apply
enemy_count = random.randint(1,5)



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
            # player's attack
            enemy_hp -= user_attack
            print("the enemy before you now has", enemy_hp)
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
        else:
            print("The battle reached the maximum number of rounds and ends.")
        
User_choice = input("You walk into a coridor, enemy's lay ahead, time to fight.")
starting_sequence()