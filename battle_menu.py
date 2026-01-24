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

#different buffs peoploe can chose:



#This function is for the time passing giving the enemys buffs

def time_changing_post_fight():
    for year in range:
        Enemy_starting_HP + int(20)
        Enemy_starting_damage + int(10)

def user_choice_upg():
    User_buff = input("Chose a buff, extra health, extra damadge, or first attack next.(type in hp,dmg,atk)")
    if User_buff == dmg:
        User_starting_attack + int(5)
        print("Your attack buff now does 25dmg instead of 20dmg")
    elif User_buff == hp:
        User_starting_HP + int(10)
        print("Your new HP is 110")
    elif User_buff == atk:
        ability_to_atk = int(1)
        print("you are going to attack first in your next encounter.")
#this random number is for the amount of enemys you will fight, the larger the number, the more buffs you can apply
enemy_count = random.randint(1,5)



def starting_sequence():
   # if User_choice == 1:
        print("ahead lay", enemy_count, "enemies, each current enemy has", Enemy_starting_HP, "you currently do", User_starting_attack, "per attack."  )
        Enemy_starting_HP - User_starting_attack 
        print("the enemy before you now has" , Enemy_starting_HP)
        #add a loop here to keep fighting until all enemys are defeated
        for enemy in range(enemy_count):
            while Enemy_starting_HP > 0:
                Enemy_starting_HP - User_starting_attack
                print("the enemy before you now has" , Enemy_starting_HP)
                if Enemy_starting_HP <= 0:
                    print("you have defeated the enemy!")
                    time_changing_post_fight()
                    user_choice_upg()
                    break
                User_starting_HP - Enemy_starting_damage
                print("you have", User_starting_HP, "left")
                if User_starting_HP <= 0:
                    print("you have been defeated, game over.")
                    break
        
User_choice = input("You walk into a coridor, enemy's lay ahead, time to fight.")
starting_sequence()