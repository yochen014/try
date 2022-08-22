# Precident election
import math
import time
import random

def poll_initialization(player_data, com_data, area, bonus):
    pass

def poll_maker(party_data):
    pass

player_name = input("Please input the player's name: ")

print("Hello!", player_name, "\n")
while True:
    first_turn = True
    print("It's a new turn!")
    player_party = input("Which party would you like to join in?(Democracy or Republican or quit): ")
    special_bonus = ["+1percentgrow", "+1.5percentpopulation"]

    random.seed(100)
    #地區選票總人口
    area = [
        ["台北", random.randint(1500000, 1650000)],
        ["台中", random.randint(1430000, 1600000)],
        ["新北", random.randint(2100000, 2300000)],
        ["桃園", random.randint(1200000, 1320000)],
        ["基隆", random.randint(237000, 250000)],
        ["新竹", random.randint(1000000, 1300000)],
        ["苗栗", random.randint(650000, 670000)],
        ["宜蘭", random.randint(650000, 680000)],
        ["花蓮", random.randint(300000, 310000)],
        ["南投", random.randint(510000, 530000)],
        ["彰化", random.randint(1000000, 1200000)],
        ["雲林", random.randint(680000, 710000)],
        ["嘉義", random.randint(270000, 300000)],
        ["台南", random.randint(1300000, 1400000)],
        ["高雄", random.randint(1800000, 2011022)],
        ["屏東", random.randint(700000, 810000)]
    ]
    #Democracy: index[voter_population, growth_rate]
    democracy = [
        [52, 1.1],#台北
        [55, 1.4],#台中
        [56, 1.4],#新北
        [47, 1.1],#桃園
        [49, 1.2],#基隆
        [53, 1.4],#新竹
        [57, 1.5],#苗栗
        [46, 1.2],#宜蘭
        [70, 1.5],#花蓮
        [55, 1.1],#南投
        [48, 1.2],#彰化
        [46, 1.2],#雲林
        [35, 1.2],#嘉義
        [37, 1.0],#台南
        [42, 1.0],#高雄
        [41, 1.1] #屏東
    ]
    republican = [
        []
    ]

    #choice party
    if player_party[0].lower() == "r":
        player_party = republican
        special_bonus = special_bonus[0]
        print("\nYou got a special bonus: +1% vote growth rate!\n")
    elif player_party[0].lower() == "q":
        break
    else:
        player_party = democracy
        special_bonus = special_bonus[1]
        print("\nBecause the government has an advantage...")
        print("You got a special bonus: +1.5% population vote!\n")

    #reveal the amount of voters
    for i in range(len(area)):
        print(f"{area[i][0]}: {area[i][1]}")
    if first_turn:
        first_turn = False
        poll_initialization(player_party, com_party, area, special_bonus)
    print("Here is a poll:")

