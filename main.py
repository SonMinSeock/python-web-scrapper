class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def delete_player(self, name):
        is_delete = False

        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                print(f"{self.team_name}, {player.name}님 나갔습니다.")
                is_delete = not is_delete
                break
                
        if not is_delete:
            print(f"{name}님 {self.team_name}에 존재하지 않습니다.")

    def show_players(self):
        for player in self.players:
            player.introduce()
    
    def show_xp(self):
        sum_xp = 0

        for player in self.players:
            sum_xp += player.xp

        print(f"{self.team_name}의 총 XP는 {sum_xp}입니다.")


team_red = Team("Team Red")
team_blue = Team("Team Blue")

team_red.add_player("Son")
team_red.add_player("Kim")
team_red.add_player("Lee")

team_blue.add_player("Nico")
team_blue.add_player("Lynn")
team_blue.add_player("Kue")


team_red.show_players()
team_blue.show_players()

team_red.delete_player("Kim")
team_red.show_players()

team_red.show_xp()
team_blue.show_xp()

team_red.show_xp()
team_blue.show_xp()