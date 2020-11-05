import math
import numpy as np


class Table:
    size: int
    starting: int
    current: int

    def __init__(self, size, starting):
        self.size = size
        self.starting = starting
        self.current = starting
        self.table = np.zeros((size, size), dtype=int)
        self.table[0][int(self.size / 2)] = 1
        self.table[size - 1][int(self.size / 2)] = 2

    # check if a position is between the limits of the table
    def is_correct_position(self, position):
        if 0 <= position[0] < self.size and 0 <= position[1] < self.size:
            return True
        return False

    # check if a positon is free
    def is_empty(self, position):
        if self.table[position[0]][position[1]] == 0:
            return True
        return False

    # check if a position is wall
    def is_wall(self, position):
        if self.table[position[0]][position[1]] == -1:
            return True
        return False

    # change a free spacer to wall
    def change_to_wall(self, position):
        if self.is_empty(position):
            self.table[position[0]][position[1]] = -1

            return 1

        return 0

    # returns the players position
    def get_player_position(self, player):
        for i in range(self.size):
            for j in range(self.size):
                if self.table[i][j] == player:
                    return i, j

        return None

    # returns a list of neighbours that a player has
    def get_neighbours(self, player):
        if player == 1:
            x, y = self.get_player_position(1)
        else:
            x, y = self.get_player_position(2)

        neighbours = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1], [x, y + 1], [x + 1, y - 1],
                      [x + 1, y], [x + 1, y + 1]]

        return [neighbour for neighbour in neighbours if
                self.is_correct_position(neighbour) and self.is_empty(neighbour)]

    # returns a list of neighbours that a positon has
    def get_neighbours_by_position(self, position):
        x = position[0]
        y = position[1]
        neighbours = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1], [x, y + 1], [x + 1, y - 1],
                      [x + 1, y], [x + 1, y + 1]]

        return [neighbour for neighbour in neighbours if
                self.is_correct_position(neighbour) and self.is_empty(neighbour)]

    # returns how many free spaces are arroun a player
    def free_spaces_arround(self, player):
        neighbours = self.get_neighbours(player)
        return len(neighbours)

    # returns how many free spaces are arroun a position
    def free_spaces_arround_bt_position(self, position):
        neighbours = self.get_neighbours_by_position(position)
        return len(neighbours)

    # move a player (player can be moved to a neighbour position)
    def move_player(self, position, player):
        if self.free_spaces_arround(player) == 0:
            return -1
        neighbours = self.get_neighbours(player)
        player_position = self.get_player_position(player)
        if position in neighbours:
            self.table[player_position[0]][player_position[1]] = 0
            self.table[position[0]][position[1]] = player

            return 1

        return 0

    # check who wins
    def check_winner(self):
        if self.current == 1 and self.free_spaces_arround(2) == 0:
            return 1

        if self.current == 2 and self.free_spaces_arround(1) == 0:
            return 2

        return 0

    def get_item(self, position):
        return self.table[position[0]][position[1]]

    # gets a list of neighbours selects the ones with max free spaces arround
    def neighbours_with_max_free_spaces_arround(self, neighbours):
        _max = -math.inf
        neighbour_with_MFSA = []
        for neighbour in neighbours:
            free_spaces = self.get_neighbours_by_position(neighbour)
            if free_spaces >= _max:
                _max = free_spaces

        for neighbour in neighbours:
            if self.get_neighbours_by_position(neighbour) == _max:
                neighbour_with_MFSA.append(neighbour)

        return neighbour_with_MFSA

    def print_table(self):
        print(self.current)
        print('\n')
        for i in range(self.size):
            for j in range(self.size):
                print(f'{self.get_item([i, j])}', end=" ")
            print('\n')


