import random
#Function to determine the winner after every game

def winner(user_input, comp_input):
    if (user_input == 'R' and comp_input == 'P') or (user_input == 'P' and comp_input == 'S') or (user_input == 'S' and comp_input == 'R'):
        return 'comp'
    elif (user_input == 'P' and comp_input == 'R') or (user_input == 'S' and comp_input == 'P') or (user_input == 'R' and comp_input == 'S'):
        return 'user'
    else:
        return 'tie'

my_dict = {'R': "Rock", 'P': "Paper", 'S': "Scissors"}
user_count = 0
comp_count = 0

games = int(input("\nEnter the number of games you want to play: "))

while comp_count + user_count < games:
    user_input = input("\nUser's Input: ")[0].upper()

    if user_input not in my_dict.keys():
        print("INVALID INPUT")
        continue

    comp_input = random.choice(list(my_dict.keys()))
    print("Computer's Input: ", my_dict[comp_input])

    winner = winner(user_input, comp_input)
    if winner == 'comp':
        comp_count += 1
    elif winner == 'user':
        user_count += 1

    print("\nSCORE:")
    print("User Score:", user_count, "\tComputer Score:", comp_count, "\n")

print("\n\t\tFINAL SCORE:")
print("User Score:", user_count, "\t\t\tComputer Score:", comp_count, "\n")
if user_count > comp_count:
    print("\n\tCONGRATULATIONS! YOU WON!")
elif user_count < comp_count:
    print("\n\t\tSORRY! YOU LOST!")
else:
    print("\n\t\tOOPS! IT'S A TIE!")
