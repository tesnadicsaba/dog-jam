import math
from Table import Table


class AI:
    # AI gets a specification of a table and makes the best moves to win the game
    def __init__(self, table, nr_round, depth):
        self.table = table
        self.newtable = table
        self.current = 2  # this means that it`s the computers turn
        self.round = nr_round
        self.depth = depth
        print(table)

    def change_current_player(self):
        if self.current == 2:
            self.current = 1
        else:
            self.current = 2

    def compare_by_free_spaces_arround(self, multiplifiers):
        player_free_position = self.newtable.free_spaces_arround(1)
        ai_free_position = self.newtable.free_spaces_arround(2)

        return ai_free_position * multiplifiers[0] - player_free_position * multiplifiers[1]

    def get_tables(self):  # , table: Table):
        ai_neighbours = self.newtable.get_neighbours(2)
        player_neighbours = self.newtable.get_neighbours(1)
        tables = []

        if self.current == 1:
            neighbours = ai_neighbours
            ai_neighbours = player_neighbours
            player_neighbours = neighbours

        modified_table = self.newtable
        for ai_neighbour in ai_neighbours:
            modified_table.move_player(ai_neighbour, 2)
            for player_neighbour in player_neighbours:
                modified_table.change_to_wall(player_neighbour)
                tables.append(modified_table)

        return tables

    def check_score(self, table):
        if table.check_winner() == 2:
            return math.inf

        if table.check_winner() == 1:
            return -math.inf

        return self.compare_by_free_spaces_arround([1, 200])

    def minimax_alg(self, alpha, beta, depth):
        score = self.newtable.check_winner()
        if score == 1 or score == 2 or self.depth == 0:
            return self.newtable, self.check_score(self.newtable)

        if depth > 0:
            if self.current == 2:  # computer`s turn

                possible_tables = self.get_tables()
                best_val = -math.inf
                for tabel in possible_tables:
                    self.change_current_player()
                    self.newtable = tabel
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
                for tabel in possible_tables:
                    self.change_current_player()
                    self.newtable = tabel
                    new_table, value = self.minimax_alg(alpha, beta, depth - 1)

                    if value < best_val:
                        best_val = value
                        self.newtable = new_table

                    beta = max(beta, value)
                    if beta <= alpha:
                        break

            self.newtable.print_table()
            return self.newtable, best_val


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
        ai = AI(mytable, 2, 3)
        mytable, val = ai.minimax_alg(-math.inf, math.inf, 3)
        mytable.current = 1

print(mytable.check_winner())
