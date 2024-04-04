from acsi_day14 import logo , vs 
from data_day14 import data
import random
import os

print(logo)
game_over = False

person_1 = random.choice(data)
first =print(f'>>>>>  Compare A: {person_1["name"]}, a {person_1["description"]}, from {person_1["country"]}  <<<<<')

print(vs)
score  = 0
while game_over == False:
    person_2 = random.choice(data)
    if person_1 == person_2 :
        person_2 = random.choice(data)
    celebrity = person_2["name"]
    description = person_2["description"]
    country = person_2["country"]
    second = print(f'>>>>>  Againts B: {celebrity}, a {description}, from {country}  <<<<<\n')

    if person_1['follower_count'] > person_2['follower_count']:
        follow = 1
    else:
        follow = 2    

    answer = input('Who has more followers? Type \'A\' or \'B\': ').lower()
    
    os.system('cls') 
    print(logo)
    if answer == 'a':
        if follow == 1: 
            score += 1
            print(f'You are right ! current score = {score}')
            game_over = False
        else :
            print(f'Sorry, that\'s Wrong. Your score is {score}')
            game_over = True
            break
    else: 
        if follow == 2: 
            score += 1
            print(f'You are right ! current score = {score}')
            game_over = False
        else :
            print(f'Sorry, that\'s Wrong. Your score is {score}')
            game_over = True
            break
    
    print(f'>>>>>  Compare A: {celebrity}, a {description}, from {country}  <<<<<\n')
    person_1 = person_2

    print(vs)
