from dataclasses import dataclass
from typing import List, Self

@dataclass
class Bag:
    red: int
    blue: int
    green: int

@dataclass
class Set:
    red: int = 0
    blue: int = 0
    green: int = 0

    def is_valid(self, bag: Bag) -> bool:
        return bag.red >= self.red and bag.blue >= self.blue and bag.green >= self.green

    @classmethod
    def parse(cls, s: str) -> Self:
        colorcounts = s.split(",")

        ret = cls()
        for colorcount in colorcounts:
            count, color = colorcount.strip().split( )
            ret.__setattr__(color, int(count))

        return ret


@dataclass
class Game:
    id: int
    sets: List[Set]

    @classmethod
    def parse(cls, s: str) -> Self:
        gamestr, reststr = s.split(":")

        game_id = int(gamestr.replace("Game ", ""))

        sets = []
        for setstr in reststr.split(";"):
            sets.append(Set.parse(setstr))

        return cls(id=game_id, sets=sets)

    def is_valid(self, bag: Bag):
        for set in self.sets:
            if not set.is_valid(bag):
                return False
        return True

    def power(self) -> int:
        min_red, min_blue, min_green = 0, 0, 0
        for set in self.sets:
            if set.red > min_red:
                min_red = set.red
            if set.blue > min_blue:
                min_blue = set.blue
            if set.green > min_green:
                min_green = set.green

        return min_red * min_blue * min_green


@dataclass
class Session:
    bag: Bag
    games: List[Game]

    @classmethod
    def parse(cls, file_path) -> Self:
        bag = Bag(red=12, green=13, blue=14)
        games = []
        with open(file_path) as f:
            for line in f.readlines():
                games.append(
                    Game.parse(line)
                )

        return cls(bag=bag, games=games)

    def valid_ids(self):
        ids = []
        for game in self.games:
            if game.is_valid(self.bag):
                ids.append(game.id)

        return ids

    def sum(self):
        ans = 0
        for game in self.games:
            ans += game.power()
        return ans
