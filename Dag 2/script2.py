A = "Rock"
B = "Paper"
C = "Scissors"

rockPoints = 1
paperPoints = 2
ScissorPoints = 3

points = 0

X = "Lose"
Y = "Draw"
Z = "Win"

# Functions for calculating the answer for the actions


def Lose(input):
    if input == "A":
        return("C")
    elif input == "B":
        return("A")
    elif input == "C":
        return("B")


def Draw(input):
    if input == "A":
        return("A")
    elif input == "B":
        return("B")
    elif input == "C":
        return("C")


def Win(input):
    if input == "A":
        return("B")
    elif input == "B":
        return("C")
    elif input == "C":
        return("A")


def calculatePoints(points, choice, option):

    if choice == "A":
        points = points + 1
    elif choice == "B":
        points = points + 2
    elif choice == "C":
        points = points + 3

    if option == "X":
        points = points
    elif option == "Y":
        points = points + 3
    elif option == "Z":
        points = points + 6

    print(points)
    return(points)


with open('input.txt') as file:
    while (line := file.readline().rstrip()):
        entries = line.split(" ")
        print(entries)
        if entries[0] == "A":  # Looking if opponent chose Rock
            if entries[1] == "X":  # Seeing if losing is the best option
                choice = Lose(entries[0])
                points = calculatePoints(points, choice, entries[1])

            elif entries[1] == "Y":  # Seeing if drawing is the best option
                choice = Draw(entries[0])
                points = calculatePoints(points, choice, entries[1])

            elif entries[1] == "Z":  # Seeing if winning is the best option
                choice = Win(entries[0])
                points = calculatePoints(points, choice, entries[1])

        elif entries[0] == "B":  # Looking if opponent chose Paper
            if entries[1] == "X":  # Seeing if losing is the best option
                choice = Lose(entries[0])
                points = calculatePoints(points, choice, entries[1])

            elif entries[1] == "Y":  # Seeing if drawing is the best option
                choice = Draw(entries[0])
                points = calculatePoints(points, choice, entries[1])

            elif entries[1] == "Z":  # Seeing if winning is the best option
                choice = Win(entries[0])
                points = calculatePoints(points, choice, entries[1])

        elif entries[0] == "C":  # Looking if opponent chose Scissors
            if entries[1] == "X":  # Seeing if losing is the best option
                choice = Lose(entries[0])
                points = calculatePoints(points, choice, entries[1])

            elif entries[1] == "Y":  # Seeing if drawing is the best option
                choice = Draw(entries[0])
                points = calculatePoints(points, choice, entries[1])

            elif entries[1] == "Z":  # Seeing if winning is the best option
                choice = Win(entries[0])
                points = calculatePoints(points, choice, entries[1])


print(points)
