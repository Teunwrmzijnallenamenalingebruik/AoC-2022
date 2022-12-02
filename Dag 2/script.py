A = "Rock"
B = "Paper"
C = "Scissors"

X = "Rock"
Y = "Paper"
Z = "Scissors"

rockPoints = 1
paperPoints = 2
ScissorsPoints = 3

points = 0

with open('input.txt') as file:
    while (line := file.readline().rstrip()):
        entries = line.split(" ")
        print(entries)
        if entries[0] == "A":  # Looking if opponent chose Rock
            if entries[1] == "X":  # Looking if the best choice is Rock
                points = points + rockPoints + 3  # Calculating points for this round, plus 3 since its a draw

            elif entries[1] == "Y":  # Looking if the best choice is Paper
                # Calculating points for this round, paper wins from rock so 6 points extra
                points = points + paperPoints + 6

            elif entries[1] == "Z":  # Looking if the best choice is Scissors
                points = points + ScissorsPoints  # Calculating points for this round

        elif entries[0] == "B":  # Looking if opponent chose Paper
            if entries[1] == "X":  # Looking if the best choice is Rock
                points = points + rockPoints  # Calculating points for this round

            elif entries[1] == "Y":  # Looking if the best choice is Paper
                points = points + paperPoints + 3  # Calculating points for this round, plus 3 since its a draw

            elif entries[1] == "Z":  # Looking if the best choice is Scissors
                # Calculating points for this round, scissors wins from paper so 6 points extra
                points = points + ScissorsPoints + 6

        elif entries[0] == "C":  # Looking if opponent chose Scissors
            if entries[1] == "X":  # Looking if the best choice is Rock
                # Calculating points for this round, rock wins from scissors so 6 points extra
                points = points + rockPoints + 6

            elif entries[1] == "Y":  # Looking if the best choice is Paper
                points = points + paperPoints  # Calculating points for this round

            elif entries[1] == "Z":  # Looking if the best choice is Scissors
                points = points + ScissorsPoints + 3  # Calculating points for this round, plus 3 since its a draw


print(points)
