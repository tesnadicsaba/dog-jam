import math

import numpy as np

from Table import Table
import AI2


class AI:
    # AI gets a specification of a table and makes the best moves to win the game
    table: Table

    def __init__(self, table, depth):
        self.table = table
        self.newtable = table
        self.depth = depth
        self.value = self.compare_by_free_spaces_arround([1, 200])

    def compare_by_free_spaces_arround(self, multiplifiers):
        player_free_position = self.newtable.free_spaces_arround(1)
        ai_free_position = self.newtable.free_spaces_arround(2)

        return ai_free_position * multiplifiers[1] - player_free_position * multiplifiers[0]

    def get_tables(self):  # , table: Table):
        my_neighbours = self.table.get_neighbours(2)
        opponent_neighbours = self.table.get_neighbours(1)
        tables = []

        if self.table.current == 1:
            neighbours = my_neighbours
            my_neighbours = opponent_neighbours
            opponent_neighbours = neighbours

        for ai_neighbour in my_neighbours:

            print("mytable:")
            self.table.print_table()
            print("///")
            modified_table = self.table.move_player(ai_neighbour, self.table.current)
            for player_neighbour in opponent_neighbours:

                if modified_table.is_empty(player_neighbour):
                    new_mod = modified_table.change_to_wall(player_neighbour)
                    print("tables:")
                    new_mod.print_table()
                    tables.append(new_mod)

        return tables

    def check_score(self, table):
        if table.check_winner() == 2:
            return math.inf

        if table.check_winner() == 1:
            return -math.inf

        return self.compare_by_free_spaces_arround([1, 200])

    def minimax_alg(self, alpha, beta, depth):
        score = self.check_score(self.table)
        if score == 1 or score == 2 or self.depth == 0:
            return self.table, self.check_score(self.table)

        if depth > 0:
            if self.table.current == 2:  # computer`s turn

                possible_tables = self.get_tables()
                best_val = -math.inf
                print(possible_tables)
                for tab in possible_tables:
                    self.newtable = tab
                    self.table.change_current_player()

                    new_table, value = self.minimax_alg(alpha, beta, depth - 1)

                    if value > best_val:
                        best_val = value
                        self.newtable = new_table

                    alpha = max(alpha, value)
                    if beta <= alpha:
                        break

            else:
                possible_tables = self.get_tables()
                best_val = math.inf
                for tab in possible_tables:
                    self.newtable = tab
                    self.table.change_current_player()
                    new_table, value = self.minimax_alg(alpha, beta, depth - 1)

                    if value < best_val:
                        best_val = value
                        self.newtable = new_table

                    beta = max(beta, value)
                    if beta <= alpha:
                        break

            # self.newtable.print_table()
            return self.table, best_val


def recalc(table):
    new = np.empty((3, 3), dtype=str)
    for i in range(3):
        for j in range(3):
            if table[i][j] == 0:
                new[i][j] = 'E'
            if table[i][j] == 1:
                new[i][j] = 'P'
            if table[i][j] == 2:
                new[i][j] = 'B'
            if table[i][j] == -1:
                new[i][j] = 'W'
    return new


def rerecalc(table):
    new = np.empty((3, 3), dtype=int)
    for i in range(3):
        for j in range(3):
            if table[i][j] == 'E':
                new[i][j] = 0
            if table[i][j] == 'P':
                new[i][j] = 1
            if table[i][j] == 'B':
                new[i][j] = 2
            if tabb[i][j] == 'W':
                new[i][j] = -1
    return new


mytable = Table(3, 1)
while mytable.check_winner() == 0:
    mytable.print_table()

    if mytable.current == 1:
        x = input('X=')
        y = input('Y=')
        mytable.move_player([int(x), int(y)], 1)
        mytable.print_table()

        x = input('X=')
        y = input('Y=')
        mytable.change_to_wall([int(x), int(y)])
        mytable.print_table()
        mytable.current = 2
    else:
        ai = AI(mytable, 2)
        tab = recalc(mytable.table)
        tabb, val = AI2.minimax(tab, 3, True, -math.inf, math.inf, 3)
        mytable.table = rerecalc(tabb)
        mytable.current = 1
        mytable.print_table()

print(f'winner {mytable.check_winner()}')
