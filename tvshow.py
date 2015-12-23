import random
def viewer():
    viewers=random.randint(0,320090000)
    leavers=random.randint(0,160045000)
    print viewers-leavers
def total():
    totalviewers=viewers-leavers
def final_tally():
    if totalviewers==0:
        print ("off-air")
viewer()
total()
final_tally()

