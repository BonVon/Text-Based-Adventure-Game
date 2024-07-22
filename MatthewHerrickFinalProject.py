# INF360 - Programming in Python
# Matthew Herrick
# Midterm Project
# 07/07/2024


import random

# List of Object Names for variety
sidekickNames = [
    "Cybern", "Digita", "Quanta", "Synapt", "Techtron", "Neunet", "Zybyte", "Hyperlink", "Nexwave", "Crypnode",
    "Bytech", "Quantum", "Syntex", "Nexis", "Zynap", "Hypernet", "Crypton", "Digibyte", "Cybit", "Synergy",
    "Neutron", "Technet", "Qubit", "Digitron", "Synapse", "Cyberna", "Quantex", "Techwave", "Neuron", "Zybit",
    "Hypertech", "Cryptron", "Digitap", "Synet", "Nextron", "Techbyte", "Quantal", "Diginet", "Cytron", "Synwave",
    "Bytewave", "Quantumet", "Syntron", "Cytech", "Nexbyte", "Digilink", "Cybernode", "Synaptix", "Hypernode", "Cryptwave",
    "Digibit", "Quantan", "Technoid", "Neuwave", "Zyber", "Hypersyn", "Cryplink", "Syntexa", "Nextech", "Digicore",
    "Cytron", "Synwave", "Bytewave", "Quantumet", "Syntron", "Cytech", "Nexbyte", "Digilink", "Cybernode", "Synaptix",
    "Hypernode", "Cryptwave", "Digibit", "Quantan", "Technoid", "Neuwave", "Zyber", "Hypersyn", "Cryplink", "Syntexa",
    "Nextech", "Digicore", "Cytron", "Synwave", "Bytewave", "Quantumet", "Syntron", "Cytech", "Nexbyte", "Digilink",
    "Cybernode", "Synaptix", "Hypernode", "Cryptwave", "Digibit", "Quantan", "Technoid", "Neuwave", "Zyber", "Hypersyn"
]

weaponNames = [
    'Sword', 'Laser Pistol', 'Plasma Rifle', 'Hammer', 'Electro Whip',
    'Pulse Cannon', 'Dagger', 'Railgun', 'Bow', 'Mace',
    'Gauss Rifle', 'Blaster', 'Axe', 'Staff', 'Grenade'
]

healingItemNames = [
    'Potion', 'Antidote', 'Antivenom', 'Bandages', 'Healing Salve',
    'Copper Wire', 'Fresh CPU', 'RAM', 'Healing Goo', 'Fairy Dust',
    'Duct Tape', 'Graphics Card', 'Double-Sided Tape', 'Nord VPN', 'Tylenol'
]

# Weapong Object
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    def __str__(self):
        return f"Weapon: {self.name} - Power Level: {self.damage}"

# Healing Item Object
class HealingItem:
    def __init__(self, name, heal_amount):
        self.name = name
        self.heal_amount = heal_amount
    
    def __str__(self):
        return f"Healing Item: {self.name} - Heal Amount: {self.heal_amount}"

# Hero Object(Parent Class)
class Hero:
    def __init__(self, name = "Computer", currHealth = 5, maxHealth = 5, powerLevel = 2, experience = 0, isAlive = True):
        self.name = name
        self.currHealth = currHealth
        self.maxHealth = maxHealth
        self.powerLevel = powerLevel
        self.experience = experience
        self.isAlive = isAlive
        self.inventory = {
            'gold': 0, 
            'weapon': None, 
            'healingItems': [] 
        }

        self.party = {}
        self.partySize = len(self.party)
    
    # Returns the power level of the hero pluss the power level of an equipped weapon
    def use_power(self):
        if self.inventory['weapon'] is None:
            return self.powerLevel
        else:
            return (self.powerLevel + self.inventory['weapon'].damage)
    
    # Removes health from the hero and checks if they are still alive
    def take_damage(self, damage):
        self.currHealth -= damage
        self.is_alive()

    # Adds health to the hero based on healing item use
    def heal(self):
        # Check if there are any healing items
        if self.inventory['healingItems'] == []:
                print("You have no healing items")
        else:
            print("Healing items are destroyed after use. Would you like to use one? (y/n)")
            choice = input()
            if choice == 'y':
                print("Which item would you like to use? (Enter the name)")
                for item in self.inventory['healingItems']:
                    print(f"Healing Items:\n{item.name} - Heal Amount: {item.heal_amount}")
                    choice = input()
                    # Check if the chosen item is in the list and uses it
                    for item in self.inventory['healingItems']:
                        if item.name == choice:
                            self.currHealth += item.heal_amount
                            if self.currHealth > self.maxHealth:
                                self.currHealth = self.maxHealth
                                print(f"{self.name} healed for {item.heal_amount} health points.")
                        else:
                            print("That item is not in your inventory. Try again.")                          
    
    def full_heal(self):
        self.currHealth = self.maxHealth

    def add_healing_item(self, item = HealingItem):
        # Add an item to the list of healing items.
        if len(self.inventory['healingItems']) < 3:
            self.inventory['healingItems'].append(item)
            print(f"{self.name} added healing item: {item}")
        else:
            # If the list is already full, ask the player if they want to replace an item.
            print("You already have 3 healing items and cannot add more. Would you like to replace an item? (y/n)")
            answer = input()
            if answer == "y":
                print("Which item would you like to replace?")
                print(self.inventory['healingItems'])
                oldItem = input()
                if item in self.inventory['healingItems']:
                    self.inventory['healingItems'].pop(oldItem)
                    self.inventory['healingItems'].append(item)
                else:
                    print("That item is not in your inventory.")
            else:
                print("Ok.")

    # Add a weapon to the inventory and replace the old one if user decides
    def add_weapon(self, weapon = Weapon):
        if self.inventory['weapon'] is None:
            self.inventory['weapon'] = weapon
        else:
            print("You already have a weapon equipped. Would you like to switch weapons? (y/n)")
            answer = input()
            if answer == "y":
                self.inventory['weapon'] = weapon
            else:
                print("Ok.")

    def is_alive(self):
        if self.currHealth > 0:
            self.isAlive = True
            return True
        else:
            self.isAlive = False
            return False
        
    def print_stats(self):
        print(f"\n{self.name}:")
        print(f"Health: {self.currHealth}/{self.maxHealth}HP")
        print(f"Power Level: {self.powerLevel}")
        print(f"Experience: {self.experience}XP")
        print(f"Party Members: {self.partySize}\n")
    
    def print_inventory(self):
        print(f"Gold: {self.inventory['gold']}")
        if self.inventory['weapon'] is None:
            print("Weapon: No weapon equipped.")
        else:
            print(f"Weapon: {self.inventory['weapon']}.")
        if len(self.inventory['healingItems']) == 0:
            print("Healing Items: None.")
        else:
            for item in self.inventory['healingItems']:
                print(f"Healing Items:\n{item.name} - Heal Amount: {item.heal_amount}")
    
    def print_party(self):
        if len(self.party) == 0:
            print("Party Members: None.\n")
        else:
            for sidekickName, sidekick in self.party.items():
                print(f"{sidekick.name:}\nPower Level:{sidekick.powerLevel}\nHealth: {sidekick.currHealth}/{sidekick.maxHealth}HP\n")

    def level_up(self):
        print(f"Looks like you're ready to level up!\nCurrent MaxHealth: {self.maxHealth}\nCurrent PowerLevel: {self.powerLevel}\nTotal Experince: {self.experience}\n10 Experince = PowerLevel +3\n10 experince = MaxHealth +3\n")
        print ("Would you like to level up?(y/n)")
        choice = input()
        if choice == "y":
            print("What would you like to level up?(1 for MaxHealth, 2 for PowerLevel)")
            choice = input()
            
            # Checks if the user has enough experience to level up and edits the stats.
            if choice == "1":
                if self.experience < 10:
                    print("You don't have enough experience to level up MaxHealth.")
                    return
                else:
                    self.maxHealth += 3
                    self.full_heal()
                    self.experience -= 10
                    self.print_stats()
            if choice == "2":
                if self.experience < 10:
                    print("You don't have enough experience to level up PowerLevel.")
                    return
                else:
                    self.powerLevel += 3
                    self.experience -= 10
                    self.print_stats()

class Sidekick(Hero):
    def __init__(self, name, currHealth, maxHealth, powerLevel, cost):
        super().__init__(name, currHealth, maxHealth, powerLevel, cost)
        self.cost = cost
    
    def print_stats(self):
        print(f"\n{self.name}:")
        print(f"Health: {self.currHealth}/{self.maxHealth}HP")
        print(f"Power Level: {self.powerLevel}")
   
    # Calculate the attack probability based on the power level.
    def use_power(self):
        if self.powerLevel <= 2:
            attackProbability = 0.35
        elif self.powerLevel > 2 and self.powerLevel <= 4:
            attackProbability = 0.5
        elif self.powerLevel > 4 and self.powerLevel <= 6:
            attackProbability = 0.65
        elif self.powerLevel > 6 and self.powerLevel <= 8:
            attackProbability = 0.8
        else:
            attackProbability = 1
        if random.random() < attackProbability:
            return self.powerLevel
        else:
            return 0

class Monster(Hero):
    def __init__(self, name, currHealth, powerLevel, experience, gold, maxHealth= None):
        super().__init__(name, currHealth, powerLevel)
        self.experience = experience
        self.gold = gold
        self.maxHealth = maxHealth
        self.powerLevel = powerLevel

     # Calculate the attack probability based on the power level.
    def use_power(self):
        if self.powerLevel <= 2:
            attackProbability = 0.45
        elif self.powerLevel > 2 and self.powerLevel <= 4:
            attackProbability = 0.55
        elif self.powerLevel > 4 and self.powerLevel <= 6:
            attackProbability = 0.70
        elif self.powerLevel > 6 and self.powerLevel <= 8:
            attackProbability = 0.85
        else:
            attackProbability = .90
        if random.random() < attackProbability:
            return self.powerLevel
        else:
            return 0
    
    # A monster will always attack the weakest sidekick first.
    def find_weakest_sidekick(self, sidekicks):
        weakest_sidekick = None
        lowest_health = float('inf')
        
        for sidekick in sidekicks:
            if sidekick.currHealth < lowest_health:
                lowest_health = sidekick.currHealth
                weakest_sidekick = sidekick
        
        return weakest_sidekick
    
    def print_stats(self):
        print(f"\n{self.name}:")
        print(f"Health: {self.currHealth}HP")
        print(f"Power Level: {self.powerLevel}")

def print_intro():
    print("""Ah! Glad to see you are operational, Computer but I have some pressing information.
Recently an evil monster known as the "Dungeon King" has taken over these lands.
Humans lack the logical prowess to take down the Dungeon King and so, we have turned to computers.
Are you ready to take on the challenge? (y/n)""")

    answer = input()
    if answer == "y":
        print("Good. Let's get started.")
    else:
        print("Sorry to disturb you then. Warning: Uncooperative systems are sent to recycling. Goodbye :D")
        exit()

def idle_menu():
    menu_choices = ["1. Check Stats", "2. Check Inventory", "3. Hire Party Member", "4. Find Dungeon", "5. Level Up", "6. Fight Dungeon King","7. Exit Adventure(You will be sent to recycling)", "8. README"]
    
    print("*" * 20)

    print("What would you like to do?(Enter a number)")
    for choice in menu_choices:
        print(choice)

    print("*" * 20)

def combat_menu():
    menu_choices = ["1. Attack!", "2. Heal", "3. Enemy Stats", "4. Party Stats", "5. RUN!!!"]
    
    print("*" * 20)

    print("What would you like to do?(Enter a number)")
    for choice in menu_choices:
        print(choice)

    print("*" * 20)

# Totals the gold and experience from an array of monsters
def dungeon_loot(monsterArray):
    totalGold = 0
    totalExperience = 0
    for monster in monsterArray:
        totalGold += monster.gold
        totalExperience += monster.experience
    return totalGold, totalExperience

# Displays loot from an array of items. Allows user to only add one to their inventory.
def item_loot(itemList, hero=Hero):
    print ("Great work! Heres What you found:")
    for item in itemList:
        if isinstance(item, Weapon):
            print(item)
        elif isinstance(item, HealingItem):
            print(item)
    print("\n You can only choose one to take with you")
    print("Enter the name of the item you want to take with you")
    print("Or press enter to keep your current inventory")
    choice = input()
    
    # Check user input
    rightChoice = False
    while rightChoice == False:
        for object in itemList:
            if object.name == choice:
                rightChoice = True
        if rightChoice == False:
            print("That item is not in your inventory. Please try again")
            choice = input()
    
    item = None
    for object in itemList:
        if object.name == choice:
            item = object
    if item == "":
        return
    elif isinstance(item, Weapon):
        hero.add_weapon(item)
    elif isinstance(item, HealingItem):
        hero.add_healing_item(item)

# Combat Mechanics
def combat(value, monsterArray, gold, exp, hero=Hero, dungeonKing=Monster):
    # Primary combat function.
    if value == '1':
        # Targets first living monster
        for monster in monsterArray:
            if monster.is_alive():
                target = monster
                break
        
        # If no monsters, target the Dungeon King
        if target == None:
            target = dungeonKing

        print(f"\n{target.name} stands in your way!\n")

        # Hero Attacks
        print(f"You attacked {target.name} for {hero.use_power()} damage!")
        target.take_damage(hero.use_power())
        
        # Checks if target is still alive
        if target.is_alive() == False:
            print("The enemy is dead!")
            numLeft = 0
            for monster in monsterArray:
                if monster.is_alive():
                    numLeft += 1
            if numLeft == 0:
                print(f"You have cleard the dungeon! Great work {hero.name}! You have earned {exp} experience, and {gold} gold!")
                hero.experience += exp
                hero.inventory['gold'] += gold
                return False, False
            else:
                print("But the battle continues...")
                return False, True
        
        # Party attacks
        else:
            for sidekickName, sidekick in hero.party.items():
                damage = sidekick.use_power()
                if damage > 0:
                    print(f"{sidekick.name} attacked {target.name} for {damage} damage!")
                    target.take_damage(damage)
                    if not target.is_alive():
                        print(f"{target.name} has died!")
                        
                        numLeft = 0
                        for monster in monsterArray:
                            if monster.is_alive():
                                numLeft += 1
                        if numLeft == 0:
                            print(f"You have cleard the dungeon! Great work {hero.name}! You have earned {exp} experience, and {gold} gold!")
                            hero.experience += exp
                            hero.inventory['gold'] += gold
                            return False, False
                        else:
                            print("But the battle continues...")
                            return False, True 
                else:
                    print(f"{sidekick.name} missed!")

        # Checks if target then monster attacks
        if target.is_alive():
            print("The enemy still stands!\n")               

            damage = target.use_power()
            if damage > 0:
                #Monster will only attack herio if there are no sidekicks
                if hero.partySize == 0:
                    hero.take_damage(damage)
                    print(f"{target.name} attacked {hero.name} for {damage} damage!")
                    
                    if not hero.is_alive():
                        print(f"{hero.name} is dead! You lose! We will just have to find a better computer instead...")
                        exit()
                    else:
                        return False, True
                else:
                    attack = target.find_weakest_sidekick(hero.party.values())
                    print(f"{target.name} attacked {attack.name} for {damage} damage!")
                    attack.take_damage(damage)
                    if not attack.is_alive():
                        print(f"{attack.name} is dead!")
                        hero.party.pop(attack.name, None)
                        return False, True
                    else:
                        return False, True
            else:
                print(f"{target.name} missed!")
                return False, True
        else:
            print("The enemy is dead!")
            numLeft = 0
            for monster in monsterArray:
                if monster.is_alive():
                    numLeft += 1
            if numLeft == 0:
                print(f"You have cleard the dungeon! Great work {hero.name}! You have earned {exp} experience, and {gold} gold!")
                hero.experience += exp
                hero.print_inventory['gold'] += gold
                inCombat = False, False
            else:
                print("But the battle continues...")
                targetIndex += 1
                target = monsterArray[targetIndex]
                enemyTurn = False, True

    # Uses healing item
    if value == '2':
        hero.heal()
        return False, True
    
    # Check target enemy's stats
    if value == '3':
        # Targets first living monster
        for monster in monsterArray:
            if monster.is_alive():
                target = monster
                break
         # If no monsters, target the Dungeon King
        if target == None:
            target = dungeonKing
        target.print_stats()
        return False, True
    
    # Check party stats
    if value == '4':
        hero.print_stats()
        hero.print_party()
        return False, True

    # Exit Combat
    if value == '5':
        print("You ran away!")
        hero.full_heal()
        for member in hero.party.values():
            member.full_heal()
        dungeonKing.full_heal()
        return False, False

# Creates combat environments(monsters and loot)    
def combat_loop(value, hero=Hero, dungeonKing=Monster):
    if value == "1":
        print("You have entered a Gilded Cave. Data suggests this will be a high risk, high reward dungeon. Be careful and goodluck!\n")
        gildedMonsters = [
            # Creates an array of Monster objects (name, currHealth, powerLevel, experience, gold)
            Monster("Goblin Jr.", random.randint(4, 5), random.randint(3, 4), random.randint(0, 1), random.randint(1, 3)),
            Monster("Goblin Sr.", random.randint(5, 6), random.randint(4, 5), random.randint(1, 2), random.randint(2, 5)),
            Monster("Mrs.Goblin", random.randint(7, 8), random.randint(5, 6), random.randint(2, 3), random.randint(3, 5)),
            Monster("Goblin Boss", random.randint(8, 12), random.randint(6, 8), random.randint(3, 5), random.randint(5, 7)),
        ]
        totalGold, totalExperience = dungeon_loot(gildedMonsters)
        
        inDungeon = True
        while inDungeon:
            inCombat = True
            combat_menu()
            choice = input()
            while inCombat:
                inCombat, inDungeon = combat(choice, gildedMonsters, totalGold, totalExperience, hero)
    
    if value == "2":
        print("You have entered the Haunted Junkyard. Data suggests we might find some useful tools here but be careful and goodluck!\n")
        junkyardMonsters = [
            # Creates an array of Monster objects (name, currHealth, powerLevel, experience, gold)
            Monster("Spooky Ghost", random.randint(4, 5), random.randint(3, 4), random.randint(0, 1), random.randint(0, 1)),
            Monster("Scary Ghost", random.randint(5, 6), random.randint(4, 5), random.randint(1, 2), random.randint(1, 2)),
            Monster("Crazy Ghost", random.randint(7, 8), random.randint(5, 6), random.randint(2, 3), 2),
            Monster("Terrifying Ghost", random.randint(8, 12), random.randint(6, 8), random.randint(3, 5), random.randint(2, 3)),
        ]
        junkyardItems = [
            # Creates an array of Item and HealingItem objects (name, powerLevel/healAmount)
            Weapon(random.choice(weaponNames), random.randint(1, 5)),
            Weapon(random.choice(weaponNames), random.randint(1, 5)),
            HealingItem(random.choice(healingItemNames), random.randint(1, 4)),
            HealingItem(random.choice(healingItemNames), random.randint(1, 4)),
        ]
        totalGold, totalExperience = dungeon_loot(junkyardMonsters)
        
        inDungeon = True
        while inDungeon:
            inCombat = True
            combat_menu()
            choice = input()
            while inCombat:
                inCombat, inDungeon = combat(choice, junkyardMonsters, totalGold, totalExperience, hero)
        item_loot(junkyardItems, hero)

    if value == "6":
        print("You approach the Dungeon King's lair. Goodluck!\n")
        dungeonKingList = [dungeonKing]
        totalGold, totalExperience = dungeonKing.gold, dungeonKing.experience
        inDungeon = True
        while inDungeon:
            inCombat = True
            combat_menu()
            choice = input()
            while inCombat:
                inCombat, inDungeon = combat(choice, dungeonKingList, totalGold, totalExperience, hero)

# Generates three sidekicks of with increasing random stats and cost
def party_shop(hero=Hero):
    print("Here are some fellow computers ready for adventure!\n")
    purchased = False
    
    weakSidekick = Sidekick(random.choice(sidekickNames), 5, 5, random.randint(1, 2), random.randint(3, 5))
    print("Level 1: Operating System")
    weakSidekick.print_stats()
    
    print(f"Cost: {weakSidekick.cost} Gold")

    mediumSidekick = Sidekick(random.choice(sidekickNames), 7, 7, random.randint(2, 4), random.randint(5, 7))
    print("Level 2: Operating System")
    mediumSidekick.print_stats()
    print(f"Cost: {mediumSidekick.cost} Gold")

    strongSidekick = Sidekick(random.choice(sidekickNames), 10, 10, random.randint(4, 6), random.randint(8, 10))
    print("Level 3: Operating System")
    strongSidekick.print_stats()
    print(f"Cost: {strongSidekick.cost} Gold")
    
    # Allows the user to choose which sidekick to add to their party
    while purchased == False:
        print("\nWhich would you like to hire?(Enter 1, 2, 3, or 4 to exit the shop.)")
        choice = input()
        if choice == "1":
            purchased = add_party_member(hero, weakSidekick)
        elif choice == "2":
            purchased = add_party_member(hero, mediumSidekick)
        elif choice == "3":
            purchased = add_party_member(hero, strongSidekick)
        elif choice == "4":
            purchased = True

def add_party_member(hero=Hero, member=Sidekick):
    if member.cost > hero.inventory['gold']:
                print("You don't have enough gold to hire this member.")
                return False
    elif hero.partySize >= 3:
        print("Your party is already full. Would you like to replace a member? (y/n)")
        choice = input()
        if choice == "y":
            print("Which member would you like to replace? Please enter the name of the member. Type 'quit' to exit.\n")
            hero.print_party()
            choice = input()
            if choice == "quit":
                return False
            if choice not in hero.party:
                print("That member is not in your party.")
                return False
            hero.party.pop(choice, None)
            hero.party[member.name] = member
            hero.inventory['gold'] -= member.cost
            print(f"You have hired {member.name}!")
            return True
    else:
        hero.party[member.name] = member
        hero.partySize += 1
        hero.inventory['gold'] -= member.cost
        print(f"You have hired {member.name}!\n")
        return True

def adventure_choice(value, hero=Hero, dungeonKing=Monster):
        # Shows user thier stats, party stats, and Dungeon King stats
        if value == "1":
            hero.print_stats()
            hero.print_party()

            print(f"{dungeonKing.name}:")
            print(f"Health: {dungeonKing.currHealth}HP")
            print(f"Power Level: {dungeonKing.powerLevel}")
            print(f"Experience: {dungeonKing.experience}XP\n")
        
        # Prints user inventory
        if value == "2":
            hero.print_inventory()

        # Takes user to party shop
        if value == "3":
            party_shop(hero)
        
        # Takes user to dungeons
        if value == "4":
            print("What kind of dungeon would you like to explore?(Enter a number)")
            print("1. Gilded Cave\n2. Haunted Junkyard")
            dungeonType = input()
            combat_loop(dungeonType, hero)
        
        # Level up
        if value == "5":
            hero.level_up()

        # Final Boss
        if value == "6":
            combat_loop("6", hero, dungeonKing)

        # Exit program
        if value == "7":
            exit()

        # Rules 
        if value == "8":
            print_rules()

def print_rules():
    print("\nRULES OF THE GAME:")
    print("*" * 20)
    print("\nCombat:\nYou and your party will always attack first. You will always land an attack but, your party and monsters only have a chance to atttack based on their power level. You can always run away which heals you and your party\n")
    print("The Dungeon King:\nEvery players starts at the same level but The Dungeon King will have a random ammount of health and power. You can always check his stats by checking your own\n")
    print("Inventory:\nYou can only hold onto one weapon and three healing items at a time. Weapons permanently increase your base power level and healing items increase your current health and disappear after use\n")

#Creates the dungeon king.
dkMaxHealth = random.randint(35, 50)
dungeonKing = Monster("Dungeon King", dkMaxHealth, random.randint(20, 35), 1000000, 1000000, dkMaxHealth)

print_intro()
print("What should I call you?")
name = input()
newHero = Hero(name)
selectedHero = newHero

#Creates "god" hero for testing.
print(f"Would you like to be a god, {newHero.name}? Used for testing. (y/n)")
god = input()
if god == "y":
    godHero = Hero("God", 20, 20, 20)
    godHero.inventory['gold'] = 1000
    godHero.inventory['healingItems'].append(HealingItem("Healing potion", 5))
    godHero.party['Flesh Sheild'] = Sidekick("Flesh Sheild", 3, 3, 3, 3)
    godHero.experience = 1000
    selectedHero = godHero
print("\nI highly recommend reading your user manual(The rules of the game) before playing.")


#Starts the adventure, only exits if the dungeon king is dead.
adventure = True
while adventure:
    idle_menu()
    idleChoice = input()
    adventure_choice(idleChoice, selectedHero, dungeonKing,)
    if dungeonKing.is_alive() == False:
        print("You have beaten the dungeon king. Congrats!")
        adventure = False



