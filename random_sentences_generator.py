import random

names = ["Stanislav", "Milena", "Ivan", "Peter", "Maria", "Georgi"]
towns = ["Sofia", "Plovdiv", "Pazardzhik", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park", "on the moon"]


def get_random_word(words: list[str]) -> str:
    return random.choice(words)


def user_input_check(command: str) -> bool:
    return command.lower() == "y" or command.lower() == "q"


print("Hello, this is your first random sentence:")

while True:
    random_name = get_random_word(names)
    random_town = get_random_word(towns)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print(f"\n{random_name} from {random_town} {random_adverb} {random_verb} {random_noun} {random_detail}.")

    while True:
        user_choice = input("\nClick [Y] to generate a new one or [Q] to quick: ")
        if user_input_check(user_choice):
            if user_choice.lower() == "y":
                break
            else:
                exit()
        else:
            print("Invalid command ! Try again !")
            continue
