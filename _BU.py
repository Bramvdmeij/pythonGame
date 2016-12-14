import functions
from classes.food import Food
from classes.user import User
from classes.menu import Menu
from classes.ranking import Ranking
from classes.tamagotchi import Tamagotchi

def main():

    # create food object
    food = Food()

    # food.ask_food()

    # create objects
    user = User("Bram")

    # create a menu object
    menu = Menu()

    # create a menu object
    tamagotchi = Tamagotchi("Pikachu")

    # menu_choice = menu.get_menu_choice()
    # print(menu_choice)

    # if menu_choice == 1:

    # test = functions.read_colon_file("voeding.txt", True)

    # test = tamagotchi.get_food_dict()

    # food.write_food_to_dict('brab', 'o')

    # print(test)



if __name__ == "__main__":
    main()






import functions

class Food(object):

    def __init__(self):
        self.food_file_name = "voeding2.txt"

    def give_food(self):
        # ask user for input
        self.ask_food_name()
        self.ask_food_type()

    def ask_food_name(self):
        food_name_input = input("Voer voeding in (voorbeeld: wortel, snickers, spitskool, etc.): ")

        if not self.validate_food_name(food_name_input):
            self.ask_food_name()

    def ask_food_type(self):
        food_type_input = input("Is deze voeding gezond (g) of ongezond (o)? ").lower()

        if not self.validate_food_type(food_type_input):
            self.ask_food_type()

    def validate_food_name(self, name):
        name = functions.strip_non_alphabetic(name).lower()

        # check if name length is outside of range 3 to 38
        if len(name) < 3 or len(name) > 38:
            print("Dit is geen geldige invoer, de bewerking is afgebroken.")
        elif name in self.get_food_dict():
            print("niet toevoegen")
        elif not name in self.get_food_dict():
            print("wel toevoegen")

    def validate_food_type(self, type):

        if type != "g" or type != "o":
            return False

    def get_food_dict(self, type=""):
        data = open('voeding2.txt').readlines()

        food_dict = {}
        for index, line in enumerate(data):
            line = line.strip()
            parts = line.split(':')
            if type.lower() != "" and parts[1] == type.lower():
                food_dict[index] = {'name': parts[0], 'type': parts[1]}
            elif type == "":
                food_dict[index] = {'name': parts[0], 'type': parts[1]}

        # print(food_dict)
        return food_dict

    def find_food_in_dict(self, name):
        food_dict = self.get_food_dict()
        for index, food in food_dict.items():
            food_name = food.get('name')
            if food_name == name:
                print('yes')

    def write_food_to_dict(self, name, type):
        # open file
        with open(self.food_file_name, 'a') as file:
            # write new food at the end of file
            file.write("\n" + name + ":" + type)

        # refresh food file
        self.refresh_food_dict()

    # refresh food file so that is becomes sorted by length and alphabetic again
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

                # import necessary libraries
                from random import randint
                from random import choice
                from classes.food import Food
                import codecs

                # regelafstand netjes bij elke melding 1 regel
                # totaal uitslag/melding na steen papier schaar
                # check of spel input gelijk is aan 1 van de keuzes. misschien net als bij get_main_menu() dat al het foute in de else terechtkomt
                # clean console op juiste wijze (witregels)
                # alle file reads vervangen met die codecs manier UTF-8. zie get_mood_pic()


                class Tamagotchi(object):

                    def __init__(self, name=""):
                        # define vars
                        self.game_config = {
                            'name': name,
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

                        self.game_errors = {
                            'invalid_input': "Sorry, dit is geen geldige invoer"
                        }

                        # check if game name is empty
                        if self.game_config['name'] == "":
                            # get game name by input
                            self.ask_game_name()
                        else:
                            self.print_msg_center("Succes met spelen!")
                            self.get_main_menu()

                    def ask_game_name(self):
                        # ask user for input
                        user_input = input("Voer een naam in: ")

                        # validate input
                        if user_input == "":
                            self.ask_user_name()
                        else:
                            self.game_config['name'] = user_input

                    def get_total_status(self):
                        return self.game_status['hungry'] + self.game_status['dirty'] + self.game_status['unhappy']

                    def print_msg_center(self, text):
                        print('\n' + text.center(self.game_config['console_width']) + '\n')

                    def get_main_menu(self):

                        # self.clean_console()
                        self.print_status()

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
                            print(self.game_errors['invalid_input'])
                            self.get_main_menu()

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
                            return False
                        else:
                            print(self.game_errors['invalid_input'])

                        self.get_main_menu()

                    def increase_status(self, status_type, value):
                        self.game_status[status_type] += value

                    def decrease_status(self, status_type, value):
                        self.game_status[status_type] -= value
                        # do not decrease lower than zero
                        if self.game_status[status_type] <= 0:
                            self.set_status(status_type, 0)

                    def set_status(self, status_type, value):
                        self.game_status[status_type] = value

                    def print_status(self):

                        mood_pic = self.get_mood_pic()

                        print("{:<11} {}".format("Naam:", self.game_config['name']))
                        print("{:<11} {}".format("Leeftijd:", self.game_status['age']))
                        print("{:<11} {:<59} {}".format("Hongerig:", self.game_status['hungry'] * '*', mood_pic['top']))
                        print("{:<11} {:<59} {}".format("Afval:", self.game_status['dirty'] * '*', mood_pic['middle']))
                        print("{:<11} {:<59} {}".format("Ongelukkig:", self.game_status['unhappy'] * '*',
                                                        mood_pic['bottom'] + "\n"))

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

                    def get_console_center(self, text):
                        return (self.game_config['console_width'] / 2) - (len(text) / 2)

                    # action give food

                    def action_give_food(self):
                        # define vars
                        random_food_healthy = self.get_random_food("g")
                        random_food_unhealthy = self.get_random_food("o")
                        user_choice = ""

                        # print options
                        print("\nWat geef je %s te eten?\n"
                              "1. %s \n"
                              "2. %s \n"
                              "3. Afsluiten\n" % (self.game_config['name'], random_food_healthy['name'].title(),
                                                  random_food_unhealthy['name'].title()))

                        try:
                            user_choice = int(input("Kies een optie: "))
                        except ValueError:
                            print(self.game_errors['invalid_input'])
                            self.action_give_food()

                        # 1. give healthy food
                        if user_choice == 1:
                            # hungry
                            if self.game_status['hungry'] > 0:
                                self.decrease_status('hungry', 2)
                                self.increase_status('dirty', 1)
                                # set msg
                                self.print_msg_center("Nomnom")
                            # not hungry
                            else:
                                self.increase_status('unhappy', 1)
                                # set msg
                                self.print_msg_center("Ik heb geen honger!")
                        # 2. give unhealthy food
                        elif user_choice == 2:
                            # hungry
                            if self.game_status['hungry'] > 0:
                                self.decrease_status('hungry', 1)
                                self.increase_status('dirty', 3)
                                self.decrease_status('unhappy', 1)
                                # set msg
                                self.print_msg_center("Nomnomnom!")
                            # not hungry
                            else:
                                self.increase_status('unhappy', 1)
                                # set msg
                                self.print_msg_center("Ik heb geen honger!")
                        # 3. do nothing
                        elif user_choice == 3:
                            # hungry
                            if self.game_status['hungry'] > 0:
                                self.increase_status('hungry', 1)
                                self.increase_status('unhappy', 1)
                                # set msg
                                self.print_msg_center("Maar ik heb honger!")
                            # not hungry
                            else:
                                self.increase_status('hungry', 1)
                                # set msg
                                self.print_msg_center("Ik krijg hier wel trek van!")
                        else:
                            print(self.game_errors['invalid_input'])
                            self.action_give_food()

                    def get_random_food(self, health_type):
                        # import classes
                        food = Food()

                        # get food dict
                        food_dict = food.get_food_dict(health_type)
                        # pick random key
                        random_choice = choice(list(food_dict))

                        # return food name
                        return food_dict[random_choice]

                    # action clean

                    def action_clean(self):
                        if self.game_status['dirty'] > 0:
                            self.increase_status('hungry', 1)
                            self.decrease_status('dirty', 2)
                            self.increase_status('unhappy', 1)
                            # set msg
                            self.print_msg_center("Fris en fruitig!")
                        else:
                            self.increase_status('hungry', 1)
                            self.increase_status('unhappy', 2)
                            # set msg
                            self.print_msg_center("Grmpf, het is al schoon")

                    # action play game

                    def action_play_game(self):
                        # print options
                        print("Welk spel wil je spelen?\n"
                              "1. Kop of munt\n"
                              "2. Steen, papier, schaar\n"
                              "3. Toch maar niet\n")

                        try:
                            user_choice = int(input("Maak een keuze: "))
                        except ValueError:
                            print(self.game_errors['invalid_input'])
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
                            self.print_msg_center("Jammer.")

                        self.get_main_menu()

                    def game_heads_or_tails(self):
                        # define vars
                        char_dict = {1: 'kop', 2: 'munt'}
                        user_choice = ""

                        print("\n1. Kop\n"
                              "2. Munt\n")

                        try:
                            user_choice = int(input("Maak een keuze (1/2): "))
                        except ValueError:
                            print(self.game_errors['invalid_input'])
                            self.game_heads_or_tails()

                        random_choice = choice(list(char_dict))

                        if (user_choice == 1 and random_choice == 1) or (user_choice == 2 and random_choice == 2):
                            self.print_msg_center("Uitslag: {}. {} heeft verloren.".format(char_dict[random_choice],
                                                                                           self.game_config['name']))
                            return True
                        else:
                            self.print_msg_center("Uitslag: {}. {} heeft gewonnen.".format(char_dict[random_choice],
                                                                                           self.game_config['name']))
                            return False

                    def BU_game_scissor_rock_paper(self):
                        # define vars
                        char_dict = {1: 'steen', 2: 'papier', 3: 'schaar'}
                        round = 1
                        user_won = 0

                        while round <= 3:
                            # define vars
                            user_choice = ""

                            print("\n1. Steen\n"
                                  "2. Papier\n"
                                  "3. Schaar\n")

                            try:
                                user_choice = int(input("Maak een keuze (1/2/3): "))
                            except ValueError:
                                self.print_msg_center(self.game_errors['invalid_input'])
                                continue

                            random_choice = choice(list(char_dict))

                            # draw
                            if user_choice == random_choice:
                                self.print_msg_center("Gelijkspel, allebei {}.".format(char_dict[random_choice]))
                                continue
                            # user wins
                            elif (user_choice == 1 and random_choice == 3) or (
                                    user_choice == 2 and random_choice == 1) or (
                                    user_choice == 3 and random_choice == 2):
                                self.print_msg_center("Jij wint: {} verslaat {}!".format(char_dict[user_choice],
                                                                                         char_dict[random_choice]))
                                user_won += 1
                                round += 1
                            # tamagotchi wins
                            else:
                                self.print_msg_center("Jij verliest: {} verslaat {}!".format(char_dict[random_choice],
                                                                                             char_dict[user_choice]))
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

                        print("\n1. Steen\n"
                              "2. Papier\n"
                              "3. Schaar\n")

                        try:
                            user_choice = int(input("Maak een keuze (1/2/3): "))
                        except ValueError:
                            self.print_msg_center(self.game_errors['invalid_input'])
                            self.game_scissor_rock_paper()

                        random_choice = choice(list(char_dict))

                        # draw
                        if user_choice == random_choice:
                            self.print_msg_center("Gelijkspel, allebei {}.".format(char_dict[random_choice]))
                            self.game_scissor_rock_paper()
                        # user wins
                        elif (user_choice == 1 and random_choice == 3) or (user_choice == 2 and random_choice == 1) or (
                                        user_choice == 3 and random_choice == 2):
                            self.print_msg_center(
                                "Jij wint: {} verslaat {}!".format(char_dict[user_choice], char_dict[random_choice]))
                            return True
                        # tamagotchi wins
                        else:
                            self.print_msg_center(
                                "Jij verliest: {} verslaat {}!".format(char_dict[random_choice],
                                                                       char_dict[user_choice]))
                            return False

                        class User(object):

                            def __init__(self, name=""):
                                # define vars
                                self.user_name = name

                                # check if user name is empty
                                if self.user_name == "":
                                    # get user name by input
                                    self.ask_user_name()

                            def ask_user_name(self):
                                # ask user for input
                                self.user_name = input("Vul hier je naam in: ")

                                # validate input
                                if not self.validate_user_name(self.user_name):
                                    self.ask_user_name()

                            def validate_user_name(self, name):
                                # check if name is empty
                                if name == "":
                                    return False
                                else:
                                    return True






class Menu(object):

    def __init__(self):
        # define vars
        self.menu_choice = ""

    def get_menu_choice(self):
        # print menu
        self.print_menu()

        # get user choice by input
        self.ask_menu_choice()

        return self.menu_choice

    def ask_menu_choice(self):

        # ask user for input
        self.menu_choice = int(input("Maak een keuze: "))

        # validate input
        if not self.validate_menu_choice(self.menu_choice):
            self.ask_menu_choice()

    def validate_menu_choice(self, choice):
        # check if choice is empty
        if choice == "":
            return False
        # check if choice is outside of range 1 to 4
        elif choice < 1 or choice > 4:
            return False
        else:
            return True

    def print_menu(self):
        # print menu
        print("Wat wil je doen?\n"
            "1. Voeding toevoegen\n"
            "2. Tamagotchi spelen\n"
            "3. De ranking bekijken\n"
            "4. Afsluiten\n")