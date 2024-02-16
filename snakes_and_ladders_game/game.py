import random
from typing import List, Self
from dataclasses import dataclass

def roll_dice():
    return random.randint(1, 6)

@dataclass
class Player:
    name: str
    position: int = 0

    def has_won(self):
        return self.position >= 100


@dataclass
class Snake:
    head: int
    tail: int

    def found_it(self, position: int) -> bool:
        return position == self.head

    def new_position(self, position: int) -> int:
        if self.found_it(position):
            return self.tail

        return position

    @staticmethod
    def find(snakes: List[Self], position: int) -> Self | None:
        for snake in snakes:
            if snake.found_it(position):
                return snake

@dataclass
class Ladder:
    start: int
    end: int

    def found_it(self, position: int) -> bool:
        return position == self.start

    def new_position(self, position: int) -> int:
        if self.found_it(position):
            return self.end

        return position

    @staticmethod
    def find(ladders: List[Self], position: int) -> Self | None:
        for ladder in ladders:
            if ladder.found_it(position):
                return ladder


@dataclass
class Game:
    players: List[Player]
    snakes: List[Snake]
    ladders: List[Ladder]

    counter: int = 0
    finished: bool = False

    def get_current_player(self) -> Player:
        return self.players[self.counter % len(self.players)]

    def next_turn(self):
        self.counter += 1

    @classmethod
    def build(cls, snake_positions: List[tuple], ladder_positions: List[tuple], player_names: List[str]):
        snakes = []
        for pos in snake_positions:
            snake = Snake(head=pos[0], tail=pos[1])
            snakes.append(snake)

        ladders = []
        for pos in ladder_positions:
            ladder = Ladder(start=pos[0], end=pos[1])
            ladders.append(ladder)

        players = []
        for name in player_names:
            player = Player(name=name)
            players.append(player)

        return cls(players=players, snakes=snakes, ladders=ladders)


    @classmethod
    def feed(cls, filename):
        snake_positions = []
        ladder_positions = []
        player_names = []
        with open(filename) as f:
            snakes_count = int(f.readline().strip())
            for _ in range(snakes_count):
                nos = f.readline().strip().split(" ")
                nos = [int(x) for x in nos]
                head = max(nos)
                tail = min(nos)
                snake_positions.append((head, tail))
            ladder_count = int(f.readline().strip())
            for _ in range(ladder_count):
                nos = f.readline().strip().split( )
                nos = [int(x) for x in nos]
                start = min(nos)
                end = max(nos)
                ladder_positions.append((start, end))
            player_count = int(f.readline().strip())
            for _ in range(player_count):
                name = f.readline().strip()
                player_names.append(name)
        import ipdb; ipdb.set_trace()
        return cls.build(snake_positions=snake_positions, ladder_positions=ladder_positions, player_names=player_names)

    def take_turn(self, player, dice_value) -> bool:
        current_position = player.position
        new_position = current_position + dice_value
        player.position = new_position

        if player.has_won():
            print("{} rolled {} and won the game".format(player.name, dice_value))
            self.finished = True
            return

        snake = Snake.find(self.snakes, new_position)
        if snake:
            player.position = snake.new_position(new_position)
            print("{} rolled {}, found a snake and moved to {}".format(player.name, dice_value, player.position))
            return

        ladder = Ladder.find(self.ladders, new_position)
        if ladder:
            player.position = ladder.new_position(new_position)
            print("{} rolled {}, found a ladder and moved to {}".format(player.name, dice_value, player.position))
            return

        print("{} rolled {}, moved from {} to {}".format(player.name, dice_value, current_position, new_position))


    def play(self):
        while not self.finished:
            self.next_turn()
            player = self.get_current_player()
            dice_value = roll_dice()
            self.take_turn(player=player, dice_value=dice_value)


if __name__ == "__main__":
    game = Game.feed("input.txt")
    game.play()
