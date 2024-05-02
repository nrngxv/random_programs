import random

ht_list = [] # List that stores head and tails count
streak = 0

for i in range(10000):
    # this generates heads and tails value and stores it
    if random.randint(0,1) == 1:
        h = 1 # stores value
        ht_list.append(1) # puts value in list
    else:
        t = 0
        ht_list.append(0)

# this that counts the number of streak of 6 heads or tails  that appear in the program        
    step = 0
    next_step = 7
    addone = ht_list[step]
    addtwo = ht_list[step:next_step]
    # operand error +: "int" + "str" 
    ht_list_add = addone + addtwo #adds ht_list[0] with ht_list[0:7]
    
    if ht_list_add == 6:
        streak = streak + 1
    else:
        if ht_list_add == 0:
            streak = streak + 1
        else: # increases values in ht_list[]
            step = step + 1
            next_step = next_step + 1   

print(ht_list) # Prints heads and tails list
print(streak)