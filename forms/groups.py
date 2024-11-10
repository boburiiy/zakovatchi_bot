from uuid import uuid4
from datetime import *


class groups:
    def __init__(self, name: str, logo=None, played_games=0, wins=0, current_game=None,  members=0):
        self.group_id = str(uuid4())[:8]
        self.name = name
        self.logo = logo
        self.members = int(members)
        self.played_games = int(played_games)
        self.wins = int(wins)
        self.invented = datetime.now()

    def __str__(self) -> str:
        return f"{self.name} jamoasi!!!"

    def return_datas(self):
        return (self.group_id, self.name, self.logo, self.played_games,
                self.wins,  self.members, self.invented)


g1 = groups('tritium')
