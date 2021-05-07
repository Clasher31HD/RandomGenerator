import random

big_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]
small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["@", "#", "$", "%"]
specials = ["{", "}", "[", "]", "(", ")", "/", ",", ".", ":", ";", "-", "<", ">", "_"]

print("Random Password Generator")
print("Generiert zufällige Passwörter")
min_length = int(input("Gebe die minimale Länge der Passwörter ein: "))
max_length = int(input("Gebe die maximale Länge der Passwörter ein: "))
number = int(input("Gebe die Anzahl Passwörter ein: "))
print("Zur Verfügung stehen: Grossbuchstaben, Kleinbuchstaben, Zahlen, Symbole und Spezielle Zeichen")
print("Welche sollen benutzt werden? Bitte mit 'Ja' oder 'Nein' antworten!")
question_big_letters = input("Sollen Grossbuchstaben verwendet werden? ").lower()
question_small_letters = input("Sollen Kleinbuchstaben verwendet werden? ").lower()
question_digits = input("Sollen Zahlen verwendet werden? ").lower()
question_symbols = input("Sollen Symbole verwendet werden? ").lower()
question_specials = input("Sollen Sonderzeichen verwendet werden? ").lower()
print(" ")

for o in range(number):
    random_length = random.randint(min_length, max_length)
    print(str(o + 1) + ". Passwort: ", end="")
    for i in range(random_length):
        begin_with = random.randint(1, 5)
        if begin_with == 1 and question_big_letters == "ja":
            random_big_letter = random.randint(0, len(big_letters) - 1)
            big_letter = big_letters[random_big_letter]
            print(big_letter, end="")
        elif begin_with == 2 and question_small_letters == "ja":
            random_small_letter = random.randint(0, len(small_letters) - 1)
            small_letter = small_letters[random_small_letter]
            print(small_letter, end="")
        elif begin_with == 3 and question_digits == "ja":
            random_digit = random.randint(0, len(digits) - 1)
            digit = digits[random_digit]
            print(digit, end="")
        elif begin_with == 4 and question_symbols == "ja":
            random_symbol = random.randint(0, len(symbols) - 1)
            symbol = symbols[random_symbol]
            print(symbol, end="")
        elif begin_with == 5 and question_specials == "ja":
            random_special = random.randint(0, len(specials) - 1)
            special = specials[random_special]
            print(special, end="")
        else:
            random_length += 1
    print(end="\n")

print(" ")
input("Press Enter to close")
