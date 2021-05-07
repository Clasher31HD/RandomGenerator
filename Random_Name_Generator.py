import random

vocals = ["a", "e", "i", "o", "u", "y"]
non_vocals = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

print("Random Name Generator")
print("Generiert einen zufälligen Namen")
min_length = int(input("Gebe die minimale Länge des Namens ein: "))
max_length = int(input("Gebe die maximale Länge des Namens ein: "))
number = int(input("Gebe die Anzahl Namen ein: "))
print(" ")

for o in range(number):
    random_length = random.randint(min_length, max_length)
    begin_with = random.randint(1, 2)
    print(str(o + 1) + ". Name: ", end="")
    for i in range(random_length):
        if begin_with == 1:
            random_non_vocal = random.randint(0, len(non_vocals) - 1)
            non_vocal = non_vocals[random_non_vocal]
            begin_with = 2
            if i == 0:
                print(non_vocal.upper(), end="")
            else:
                print(non_vocal, end="")
        else:
            random_vocal = random.randint(0, len(vocals) - 1)
            vocal = vocals[random_vocal]
            begin_with = 1
            if i == 0:
                print(vocal.upper(), end="")
            else:
                print(vocal, end="")
    print(end="\n")

print(" ")
input("Press Enter to close")
