#Simple Match
print("Welcome to todays game, Manchester United vs Chelsea")
from collections import namedtuple
from faker import Faker
faker = Faker()
Player = namedtuple('Player', ['first_name','second_name'])
#Function to generate a list of players
def generate_players(team_name, num_players=11):
    players = []
    for _ in range(num_players):
        full_name = faker.name().split()
        player = Player(first_name=full_name[0], second_name=full_name[1])
        players.append(player)
    return players
# Function to replace three players at the 75th minute
def replace_players(players):
    for _ in range(3):
        index_to_replace = faker.random_int(min=0, max=len(players)-1)
        new_player = generate_players("Replacement")[0] 
        players[index_to_replace] = new_player
manchester_united_players= generate_players("Manchester United", num_players=11)
chelsea_players = generate_players("Chelsea",num_players=11)
#Print players
print("Manchester United Starting 11")
for i, player in enumerate(manchester_united_players, start=1):
    print(f"Player {i}: {player}")

print("\nChelsea Starting 11:")
for i, player in enumerate(chelsea_players, start=1):
    print(f"Player {i}: {player}")
# Replace three players at the 75th minute
if 1 <= 75 <= 90:  # Assuming the match duration is 90 minutes
    replace_players(manchester_united_players)
    replace_players(chelsea_players)

# Print the final players
print("\nFinal Manchester United Players:")
for i, player in enumerate(manchester_united_players, start=1):
    print(f"Player {i}: {player}")

print("\nFinal Chelsea Players:")
for i, player in enumerate(chelsea_players, start=1):
    print(f"Player {i}: {player}")


