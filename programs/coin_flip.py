import random
STREAKS = 0 # main: streak's count

def simulating_flips(number_of_flips): #defines, number of flips and
    # coin_flip = ['H' if random.choice([True, False]) else 'T' for _ in range(number_of_flips)]
    # this is a little advance way to write this. I tried writing it on my own (phind helped a little)
    coin_flip = []
    for i in range(number_of_flips):
        if random.randint(0,1) == 1:
            coin_flip.append(1)
        else:
            coin_flip.append(0)

    return coin_flip

def coin_streak(coin_flip):
    main_streak = 0
    current_streak = 1

    for i in range(1, len(coin_flip)):
        if coin_flip[i] == coin_flip[i - 1]:
            current_streak += 1
        
            if current_streak == 6:
                main_streak += 1
                current_streak = 1

        else:
            current_streak = 1

    return print(f"Number of main_ streak: {main_streak}")

flips_command = int(input("Enter number of flips:")) # main: input


for _ in range(flips_command):
    flips = simulating_flips(flips_command)
    streaks = STREAKS + coin_streak(flips)
    
print(f"The total streaks is", {streaks})