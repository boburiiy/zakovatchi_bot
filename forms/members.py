import datetime
from groups import *


class members:
    def __init__(self, id: int, full_name: str, birth_date: datetime, interests: list, started_school_at: int, plays_in: groups) -> str:
        self.id = id
        self.full_name = full_name
        self.age = datetime.now().year-birth_date
        self.grade = self.age - started_school_at+1
        self.interests = interests
        self.plays_in = plays_in

    def __str__(self) -> str:
        output = f"""To`liq ismi:{self.full_name}
Yoshi:{self.age}
Sinfi:{self.grade}
Qiziqishlari:{", ".join(self.interests)}
{self.plays_in} a`zosi"""
        return output


a1 = members("Bobur qadamov", 2009, ["it", 'box'], 7, g1.name)
print(a1)