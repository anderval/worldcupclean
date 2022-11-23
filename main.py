import requests
import json


def group_view(index):

    request = requests.get("https://worldcupjson.net/teams")
    group = json.loads(request.content)

    print("NAME  P-W-D-L")

    aproveitamento = 0.0

    for x in range(4):
        name = (group['groups'][index]['teams'][x]['country'])
        points = (group['groups'][index]['teams'][x]['group_points'])
        wins = (group['groups'][index]['teams'][x]['wins'])
        draws = (group['groups'][index]['teams'][x]['draws'])
        losses = (group['groups'][index]['teams'][x]['losses'])
        games_played = (group['groups'][index]['teams'][x]['games_played'])

        if games_played != 0:
            aproveitamento = wins/(wins+losses+draws)*100

        print(name, " ", points, wins, draws, losses, "%", aproveitamento)


def match_view():
    request = requests.get("https://worldcupjson.net/matches")
    match = json.loads(request.content)
    x = 0

    for x in range(64):
        if match[x]['stage_name'] == "First stage":
            home = (match[x]['home_team']['name'])
            home_goals = (match[x]['home_team']['goals'])
            away = (match[x]['away_team']['name'])
            away_goals = (match[x]['away_team']['goals'])

            if home_goals is None:
                break
            else:
                print(home, home_goals, " X", away_goals, away)



if __name__ == '__main__':

    option = int(input("Choice a Option:\n1 - View Matches\n2 - View Groups\n"))

    if option == 1:
        match_view()
    elif option == 2:
        opt = (input("Choose a group between A and H: "))
        if opt == "A":
            group_view(0)
        elif opt == "B":
            group_view(1)
        elif opt == "C":
            group_view(2)
        elif opt == "D":
            group_view(3)
        elif opt == "E":
            group_view(4)
        elif opt == "F":
            group_view(5)
        elif opt == "G":
            group_view(6)
        elif opt == "H":
            group_view(7)
        else:
            print("Group invalid!")
    else:
        print("Invalid Option")





