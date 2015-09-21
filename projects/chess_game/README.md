# Chess Game

### Chess Kind
  - King:1
  - Queen:2
  - Rook:3
  - Bishop:4
  - Knight:5
  - White Pawn:6
  - Black Pawn:7

### Player
  - White: "w"
  - Black: "b"

### Naming
  - Player(w/b) + Chess Kind(1-7) + chess seq(unique)
  - ex: White Player + Rook + Left one = w3a
  - ex: Black Player + Pawn + 3rd one on the right = b7f

### An Initial Board
  - It's a 8*8 board
```sh
[   ['w3a', 'w6a', None, None, None, None, 'b7a', 'b3a'],
    ['w5a', 'w6b', None, None, None, None, 'b7b', 'b5a'],
    ['w4a', 'w6c', None, None, None, None, 'b7c', 'b4a'],
    ['w2', 'w6d', None, None, None, None, 'b7d', 'b2'],
    ['w1', 'w6e', None, None, None, None, 'b7e', 'b1'],
    ['w4b', 'w6f', None, None, None, None, 'b7f', 'b4b'],
    ['w5b', 'w6g', None, None, None, None, 'b7g', 'b5b'],
    ['w3b', 'w6h', None, None, None, None, 'b7h', 'b3b']]
```

### Testing
```sh
python chess_test.py
```
