from random import randint

game_running = True
game_results = []

def calculate_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])

def game_ends(winner_name):
    print(f'{winner_name} won the game')


while game_running == True:
    counter = 0
    flag = 0
    new_round = True
    player = {'name': 'Opezdal', 'attack': 15, 'heal': 16, 'health': 100}
    monster = {'name': 'Zolypa', 'attack_min': 10, 'attack_max': 20, 'health': 100, 'skill': 100}

    print('---' * 7)
    print('Enter player name')
    player['name'] = input()

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + " health")
    print(monster['name'] + ' has ' + str(monster['health']) + " health")

    while new_round == True:

        counter = counter + 1
        player_won = False
        monster_won = False

        print('---' * 7)
        print("Select action)")
        print('1) attack')
        print('2) heal')
        print('3) exit')
        print('4) Show results')

        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            
            elif monster['health'] <= 30 and flag != 1:               
                try_luck = randint(1, 10)
                if try_luck <= 3:
                    monster['health'] = monster['health'] + monster['skill']
                flag = 1

            else:
                player['health'] = player['health'] - calculate_monster_attack()
                if player['health'] <=0:
                    monster_won = True


        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']
            print('healing')

            player['health'] = player['health'] - calculate_monster_attack()
            if player['health'] <= 0:
                monster_won = True
        
        elif player_choice == '3':
            new_round = False
            game_running = False

        elif player_choice == '4':
            for player_stat in game_results:
                print(player_stat)

        else:
            print('error')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' left')
            if player['health'] <= 30:
                print(player['name'] + ' low HP')
            print(monster['name'] + ' has ' + str(monster['health']) + ' left')
           
                
        elif player_won:
            game_ends(player['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False

        elif monster_won:
            game_ends(monster['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)           
            new_round = False

