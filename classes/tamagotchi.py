# import necessary libraries
import functions
from random import randint
from random import choice
import codecs

# regelafstand netjes bij elke melding 1 regel
# food file name msischien ook in game_data dict
# totaal uitslag/melding na steen papier schaar
# check of spel input gelijk is aan 1 van de keuzes. misschien net als bij get_main_menu() dat al het foute in de else terechtkomt
# clean console op juiste wijze (witregels)
# alle file reads vervangen met die codecs manier UTF-8. zie get_mood_pic()
# alle create dingen in de init
# alle functions nalopen op return None recursive functie aanroepen heet dat
# moet console telkens cleanen?


# VERDER: RANKING


class Tamagotchi(object):

    def __init__(self):
        # define vars
        self.game_data = {
            'name': '',
            'max_age': 25,
            'max_status': 13,
            'console_width': 79
        }
        self.game_status = {
            'age': 0,
            'hungry': randint(0, 4),
            'dirty': randint(0, 4),
            'unhappy': randint(0, 4),
        }
        self.game_messages = {
            'invalid_input': 'Sorry, dit is geen geldige invoer',
            'shutdown': 'Bedankt voor het spelen, tot de volgende keer.'
        }
        self.user_data = {
            'name': ''
        }
        self.food_file_name = "voeding2.txt"

        self.status_intro_msg = ''

    def start_game(self):
        # step 1: create a user
        self.create_user()

        # step 2: load start menu
        self.print_empty_line()
        self.show_start_menu()

    def create_game(self):
        # ask user for input
        user_input = input("Voer een naam in: ")

        # validate input
        if user_input == "":
            print(self.game_messages['invalid_input'])
            self.create_game()
        else:
            self.game_data['name'] = user_input

    def create_user(self):
        # ask user for input
        user_input = input("Vul hier je naam in: ")

        # validate input
        if user_input == "":
            print(self.game_messages['invalid_input'])
            self.create_user()
        else:
            self.user_data['name'] = user_input

    def get_total_status(self):
        return self.game_status['hungry'] + self.game_status['dirty'] + self.game_status['unhappy']

    def print_msg_center(self, text):
        print('\n' + text.center(self.game_data['console_width']) + '\n')

    def print_empty_line(self):
        print("")

    # menus

    def show_start_menu(self):
        # define vars
        user_choice = ''

        # print menu
        print("Wat wil je doen?\n"
              "1. Voeding toevoegen\n"
              "2. Tamagotchi spelen\n"
              "3. De ranking bekijken\n"
              "4. Afsluiten\n")

        # check if user input is valid
        try:
            user_choice = int(input("Maak een keuze: "))
        except ValueError:
            self.print_empty_line()
            print(self.game_messages['invalid_input'])
            self.print_empty_line()
            return self.show_start_menu()

        # check what user wants to do
        if user_choice == 1:
            # add new food
            self.create_food()
        elif user_choice == 2:
            # create new game
            self.print_empty_line()
            self.create_game()
            self.status_intro_msg = "Succes met spelen, {}!".format(self.user_data['name'])
            self.show_game_menu()
        elif user_choice == 3:
            print('3')
        elif user_choice == 4:
            self.print_empty_line()
            self.action_shutdown()
        else:
            self.print_empty_line()
            print(self.game_messages['invalid_input'])
            self.print_empty_line()
            self.show_start_menu()

    def show_game_menu(self):
        # define vars
        user_choice = ''

        self.clean_console()
        self.print_msg_center(self.status_intro_msg)

        self.show_status()

        # print options
        print("{:<28} {}".format("", "Wat wil je doen?"))
        print("{:<28} {}".format("", "1. Geef te eten"))
        print("{:<28} {}".format("", "2. Verschoon"))
        print("{:<28} {}".format("", "3. Speel een spelletje"))
        print("{:<28} {}".format("", "4. Afsluiten"))
        print("")

        # check if user input is valid
        try:
            user_choice = int(input("Kies een optie: "))
        except ValueError:
            self.print_empty_line()
            print(self.game_messages['invalid_input'])
            self.print_empty_line()
            self.show_game_menu()

        # check what user wants to do
        if user_choice == 1:
            self.increase_status('age', 1)
            self.action_give_food()
        elif user_choice == 2:
            self.increase_status('age', 1)
            self.action_clean()
        elif user_choice == 3:
            self.increase_status('age', 1)
            self.action_play_game()
        elif user_choice == 4:
            # shutdown game
            self.action_shutdown()
        else:
            print(self.game_messages['invalid_input'])

        self.show_game_menu()

    def show_status(self):
        # define vars
        mood_pic = self.get_mood_pic()

        print("{:<11} {}".format("Naam:", self.game_data['name']))
        print("{:<11} {}".format("Leeftijd:", self.game_status['age']))
        print("{:<11} {:<59} {}".format("Hongerig:", self.game_status['hungry'] * '*', mood_pic['top']))
        print("{:<11} {:<59} {}".format("Afval:", self.game_status['dirty'] * '*', mood_pic['middle']))
        print("{:<11} {:<59} {}".format("Ongelukkig:", self.game_status['unhappy'] * '*', mood_pic['bottom'] + "\n"))

    # status modifiers

    def increase_status(self, status_type, value):
        self.game_status[status_type] += value

    def decrease_status(self, status_type, value):
        self.game_status[status_type] -= value
        # do not decrease lower than zero
        if self.game_status[status_type] <= 0:
            self.set_status(status_type, 0)

    def set_status(self, status_type, value):
        self.game_status[status_type] = value

    def get_mood_pic(self):
        # define vars
        line_index = 0

        # get file
        data = codecs.open('pet_pictures.txt', 'r', 'UTF-8')

        if self.game_status['dirty'] > 12 or self.game_status['unhappy'] > 12:
            line_index = 30
        else:
            if self.game_status['age'] < 25 and self.game_status['hungry'] > 12:
                line_index = 6
            elif self.get_total_status() > 17:
                line_index = 5
            elif 14 <= self.get_total_status() <= 17:
                line_index = 4
            elif 10 <= self.get_total_status() <= 13:
                line_index = 3
            elif 6 <= self.get_total_status() <= 9:
                line_index = 2
            elif 0 <= self.get_total_status() <= 5:
                line_index = 1

            line_index += int(self.game_status['age'] / 7) * 6

        looks_dict = {}
        for index, line in enumerate(data):
            if index == line_index:
                line = line.strip()
                parts = line.split(';')
                looks_dict = {'top': parts[1], 'middle': parts[2], 'bottom': parts[3]}

        return looks_dict

    def clean_console(self):
        print(100 * '\n')

    # 1. action give food

    def action_give_food(self):
        # define vars
        random_food_healthy = self.get_random_food("g")
        random_food_unhealthy = self.get_random_food("o")
        user_choice = ""

        # print options
        print("\nWat geef je %s te eten?\n"
              "1. %s \n"
              "2. %s \n"
              "3. Afsluiten\n" % (self.game_data['name'], random_food_healthy['name'].title(), random_food_unhealthy['name'].title()))

        try:
            user_choice = int(input("Kies een optie: "))
        except ValueError:
            print(self.game_messages['invalid_input'])
            self.action_give_food()

        # 1. give healthy food
        if user_choice == 1:
            # hungry
            if self.game_status['hungry'] > 0:
                self.decrease_status('hungry', 2)
                self.increase_status('dirty', 1)
                # set msg
                self.status_intro_msg = 'Nomnom'
            # not hungry
            else:
                self.increase_status('unhappy', 1)
                # set msg
                self.status_intro_msg = 'Ik heb geen honger!'
        # 2. give unhealthy food
        elif user_choice == 2:
            # hungry
            if self.game_status['hungry'] > 0:
                self.decrease_status('hungry', 1)
                self.increase_status('dirty', 3)
                self.decrease_status('unhappy', 1)
                # set msg
                self.status_intro_msg = 'Nomnomnom!'
            # not hungry
            else:
                self.increase_status('unhappy', 1)
                # set msg
                self.status_intro_msg = 'Ik heb geen honger!'
        # 3. do nothing
        elif user_choice == 3:
            # hungry
            if self.game_status['hungry'] > 0:
                self.increase_status('hungry', 1)
                self.increase_status('unhappy', 1)
                # set msg
                self.status_intro_msg = 'Maar ik heb honger!'
            # not hungry
            else:
                self.increase_status('hungry', 1)
                # set msg
                self.status_intro_msg = 'Ik krijg hier wel trek van!'
        else:
            print(self.game_messages['invalid_input'])
            self.action_give_food()

    def get_random_food(self, health_type):

        # get food dict
        food_dict = self.get_food_dict(health_type)
        # pick random key
        random_choice = choice(list(food_dict))

        # return food name
        return food_dict[random_choice]

    # 2. action clean

    def action_clean(self):
        if self.game_status['dirty'] > 0:
            self.increase_status('hungry', 1)
            self.decrease_status('dirty', 2)
            self.increase_status('unhappy', 1)
            # set msg
            self.status_intro_msg = 'Fris en fruitig!'
        else:
            self.increase_status('hungry', 1)
            self.increase_status('unhappy', 2)
            # set msg
            self.status_intro_msg = 'Grmpf, het is al schoon'

    # 3. action play game

    def action_play_game(self):
        # define vars
        user_choice = ''

        # print options
        print("Welk spel wil je spelen?\n"
              "1. Kop of munt\n"
              "2. Steen, papier, schaar\n"
              "3. Toch maar niet\n")

        try:
            user_choice = int(input("Maak een keuze: "))
        except ValueError:
            print(self.game_messages['invalid_input'])
            self.action_play_game()

        if user_choice == 1:
            result_heads_or_tails = self.game_heads_or_tails()
            if result_heads_or_tails:
                self.increase_status('hungry', 1)
                self.increase_status('unhappy', 2)
            else:
                self.increase_status('hungry', 1)
                self.decrease_status('unhappy', 2)
        elif user_choice == 2:
            result_scissor_rock_paper = self.game_scissor_rock_paper()
            if result_scissor_rock_paper:
                self.increase_status('hungry', 1)
                self.increase_status('dirty', 1)
                self.increase_status('unhappy', 2)
            else:
                self.increase_status('hungry', 1)
                self.increase_status('dirty', 1)
                self.decrease_status('unhappy', 2)
        elif user_choice == 3:
            self.increase_status('hungry', 1)
            self.increase_status('unhappy', 2)
            # set msg
            self.status_intro_msg = 'Jammer.'

        self.show_game_menu()

    def game_heads_or_tails(self):
        # define vars
        char_dict = {1: 'kop', 2: 'munt'}
        user_choice = ""
        random_choice = choice(list(char_dict))

        print("\n1. Kop\n"
              "2. Munt\n")

        try:
            user_choice = int(input("Maak een keuze (1/2): "))
        except ValueError:
            print(self.game_messages['invalid_input'])
            self.game_heads_or_tails()

        if (user_choice == 1 and random_choice == 1) or (user_choice == 2 and random_choice == 2):
            self.status_intro_msg = 'Uitslag: {}. {} heeft verloren.'.format(char_dict[random_choice], self.game_data['name'])
            return True
        else:
            self.status_intro_msg = 'Uitslag: {}. {} heeft gewonnen.'.format(char_dict[random_choice], self.game_data['name'])
            return False

    def BU_game_scissor_rock_paper(self):
        # define vars
        char_dict = {1: 'steen', 2: 'papier', 3: 'schaar'}
        round = 1
        user_won = 0

        while round <= 3:
            # define vars
            user_choice = ""
            random_choice = choice(list(char_dict))

            print("\n1. Steen\n"
                  "2. Papier\n"
                  "3. Schaar\n")

            try:
                user_choice = int(input("Maak een keuze (1/2/3): "))
            except ValueError:
                self.print_msg_center(self.game_messages['invalid_input'])
                continue

            # draw
            if user_choice == random_choice:
                self.print_msg_center("Gelijkspel, allebei {}.".format(char_dict[random_choice]))
                continue
            # user wins
            elif (user_choice == 1 and random_choice == 3) or (user_choice == 2 and random_choice == 1) or (user_choice == 3 and random_choice == 2):
                self.print_msg_center("Jij wint: {} verslaat {}!".format(char_dict[user_choice], char_dict[random_choice]))
                user_won += 1
                round += 1
            # tamagotchi wins
            else:
                self.print_msg_center("Jij verliest: {} verslaat {}!".format(char_dict[random_choice], char_dict[user_choice]))
                user_won -= 1
                round += 1

        if user_won > 1:
            return True
        else:
            return False

    def game_scissor_rock_paper(self):
        # define vars
        char_dict = {1: 'steen', 2: 'papier', 3: 'schaar'}
        user_choice = ""
        random_choice = choice(list(char_dict))

        print("\n1. Steen\n"
              "2. Papier\n"
              "3. Schaar\n")

        try:
            user_choice = int(input("Maak een keuze (1/2/3): "))
        except ValueError:
            self.print_msg_center(self.game_messages['invalid_input'])
            self.game_scissor_rock_paper()

        if user_choice == random_choice:
            # draw
            # self.print_msg_center('Gelijkspel, allebei {}.'.format(char_dict[random_choice]))
            print('Gelijkspel, allebei {}.'.format(char_dict[random_choice]))
            return self.game_scissor_rock_paper()
        elif (user_choice == 1 and random_choice == 3) or (user_choice == 2 and random_choice == 1) or (
                user_choice == 3 and random_choice == 2):
            # user wins
            self.status_intro_msg = 'Jij wint: {} verslaat {}!'.format(char_dict[user_choice], char_dict[random_choice])
            return True
        else:
            # tamagotchi wins
            self.status_intro_msg = 'Jij verliest: {} verslaat {}!'.format(char_dict[random_choice], char_dict[user_choice])
            return False

    # 4. shutdown game

    def action_shutdown(self):
        print(self.game_messages['shutdown'])
        quit()

    # food logic

    def create_food(self):
        # ask user for input
        food_name = self.ask_food_name()
        food_type = self.ask_food_type()

        # write food
        print(3,food_name, food_type)
        self.write_food_to_dict(food_name, food_type)
        # print('De voeding "{}" is toegevoegd aan de lijst.'.format(food_name))
        self.print_empty_line()
        # go back to menu
        self.show_start_menu()

    def ask_food_name(self):
        food_name_input = input("Voer voeding in (voorbeeld: wortel, snickers, spitskool, etc.): ")
        self.print_empty_line()

        # strip all non alphabetic characters first before we check the rest
        food_name_input = self.strip_non_alphabetic(food_name_input).lower()

        if self.validate_food_name(food_name_input):
            return food_name_input
        else:
            # go back to menu
            return self.show_start_menu()

    def ask_food_type(self):
        food_type_input = input("Is deze voeding gezond (g) of ongezond (o)? ").lower()
        self.print_empty_line()

        if self.validate_food_type(food_type_input):
            print(1,food_type_input)
            return food_type_input
        else:
            # ask for food type input again
            return self.ask_food_type()

    def validate_food_name(self, name):
        # check if name length is outside of range 3 to 38
        if len(name) < 3 or len(name) > 38:
            print("Waarden mogen niet korter zijn dan 3 letters en niet langer dan 38 letters.")
            self.print_empty_line()
            return False
        elif self.find_food_in_dict(name):
            print("Deze voeding komt al voor in de lijst.")
            self.print_empty_line()
            return False
        elif not self.find_food_in_dict(name):
            return True

    def validate_food_type(self, type):
        print(2,type)
        if not type == "g" and not type == "o":
            print('Geen geldige optie (kies een "g" of een "o")')
            return False
        else:
            return True

    def get_food_dict(self, type=""):
        data = open(self.food_file_name).readlines()

        food_dict = {}
        for index, line in enumerate(data):
            line = line.strip()
            parts = line.split(':')
            if type.lower() != "" and parts[1] == type.lower():
                food_dict[index] = {'name': parts[0], 'type': parts[1]}
            elif type == "":
                food_dict[index] = {'name': parts[0], 'type': parts[1]}

        return food_dict

    def find_food_in_dict(self, name):
        food_dict = self.get_food_dict()
        for index, food in food_dict.items():
            food_name = food.get('name')
            if food_name == name:
                return True

        return False

    def write_food_to_dict(self, name, type):
        # open file
        with open(self.food_file_name, 'a') as file:
            # write new food at the end of file
            file.write("\n" + name + ":" + type)

        # refresh food file
        self.refresh_food_dict()

    def refresh_food_dict(self):
        # read latest data and sort it
        data = open(self.food_file_name).readlines()
        data = [line.strip() for line in data]
        data = sorted(data)
        data = sorted(data, key=len, reverse=False)

        # clean currect file
        open(self.food_file_name, 'w').close()

        # open file again
        with open(self.food_file_name, 'w') as f:
            # define counter
            count = 0
            # iterate data
            for line in data:
                if count > 0:
                    f.write("\n")

                # write food name and type to file
                f.write(line)
                # increase count
                count += 1

    # general functions

    def strip_non_alphabetic(self, string):
        valids = []
        for character in string:
            if character.isalpha():
                valids.append(character)
        return ''.join(valids)