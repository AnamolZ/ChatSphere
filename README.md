## CodeX

This is a two-player programming game where time complexity plays a vital role. The objective of the game is to solve a coding challenge given to the players and be the first one to complete it. The time complexity of the program task should also be considered, and the player with the highest score in both sections will be declared the winner.

The game is implemented using customtkinter and web sockets, where web sockets are used to connect two computers.

## Getting Started
### Prerequisites
To run this game, you need to have Python 3.x installed on your computer.

## Installation

Clone the repository.

```bash
git clone https://github.com/<username>/two-way-player-programming-game.git
```

Navigate to the project directory.

```bash
cd codex
```
Install the required libraries.

```bash
pip install -r requirements.txt
```
Usage
Start the server.
```bash
python server.py
```
Start two clients, one for each player.
```bash
python client.py
```


Follow the on-screen instructions to play the game.
Game Rules
The game will start once both players have connected to the server.
The players will be given a coding challenge to solve.
The first player to complete the challenge will be declared the winner of the first section.
The time complexity of the player's program task will be calculated.
The player with the lowest time complexity will be declared the winner of the second section.
The player with the highest score in both sections will be declared the winner of the game.

## Contributing
If you want to contribute to this project, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
