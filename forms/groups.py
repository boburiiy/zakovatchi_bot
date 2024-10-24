from uuid import uuid4


class group:
    def __init__(self, name: str, logo=None, playes_games=0, win=0, current_game=None,  members=0):
        self.name = name
        self.logo = logo
        self.members = int(members)
        self.group_id = str(uuid4())[:8]

    def __str__(self) -> str:
        return f"{self.name} jamoasi!!!"



tritium = group("tritium")