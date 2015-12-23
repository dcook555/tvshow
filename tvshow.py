import random
def viewer():
    viewers=random.randint(0,320090000)
    leavers=random.randint(0,160045000)
def total():
    totalviewers=viewers-leavers
def final_tally():
    if totalviewers==0:
        print ("off-air")
viewer()
total()
final_tally()
print viewers-leavers
