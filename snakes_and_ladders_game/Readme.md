# Terms

## Snake
- head_position
- tail_position
- get_new_position

## Ladder

## Player

## Board
- variables:
    - players: List[Player]
    - snakes: List[Player]
    - ladders: List[Ladder]
    - current_roll: int
- functions
    find_snake(position)
    find_ladder(position)

## Game
- roll_dice
- move(board, player, position)
