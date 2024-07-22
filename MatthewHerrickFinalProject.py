
1
# INF360 - Programming in Python
# Matthew Herrick
# Midterm Project
# 07/07/2022
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

