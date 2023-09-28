# Tic-Tac-Toe Game

A simple command-line implementation of the classic Tic-Tac-Toe (noughts and crosses) game in Python. This game allows two players to take turns and compete against each other.

## How to Play

1. Run the Python script (`tic_tac_toe.py`) to start the game.

2. The game will prompt you to enter 'TOSS' to determine which player goes first.

3. After the toss, the winning player can choose either 'X' or 'O,' and the other player will automatically receive the remaining symbol.

4. Players take turns entering their moves by specifying the row and column where they want to place their symbol.

5. The game continues until one player wins by getting three of their symbols in a row (horizontally, vertically, or diagonally) or until the board is full (a tie).

6. The game will display the result, indicating which player won or if it's a tie.

## Rules and Controls

- Players enter their moves by providing row and column coordinates, where both row and column numbers are between 0 and 2.

- The game will check for valid input and prevent players from making moves in already occupied cells.

- The player who wins the toss goes first, and the game alternates between players until it ends.

## Example Usage

```bash
$ python tic_tac_toe.py
