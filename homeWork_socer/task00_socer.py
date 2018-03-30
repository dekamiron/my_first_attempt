class Team:
    def __init__(self, id_team, name, players):
        self.id_team = id_team
        self.name = name
        self.players = players


class Player:
    def __init__(self, id_player, name, team):
        self.id_player = id_player
        self.name = name
        self.team = team


class Match:
    def __init__(self, id_match, date, location, result, team1, team2, players):
        self.id_match = id_match
        self.date = date
        self.location = location
        self.result = result
        self.team1 = team1
        self.team2 = team2
        self.players = players
