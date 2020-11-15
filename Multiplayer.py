from Table import Table


class Multiplayer:

    def __init__(self, starts, size, wins):
        self.starts = starts
        self.size = size
        self.table = Table(self.size, self.starts)
        self.position = []
        self.current = self.table.current
        self.whats_next = 'Move to a free neighbour field'
        self.p1_wins = wins[0]
        self.p2_wins = wins[1]
        self.winner = 0

    def set_position(self, position):
        self.position = position

    def send_whos_turn_is(self):
        return f'Player`s{self.current} turn'

    def change_whats_next(self):
        if self.whats_next == 'Move to a free neighbour field':
            self.whats_next = "Select a free field to make block it"
        else:
            self.whats_next = 'Move to a free neighbour field'

    def send_what_to_do(self):
        return self.whats_next

    def check_winner(self):
        self.winner = self.table.check_winner()
        if self.winner == 1:
            self.p1_wins += 1
            self.winner = 1
            return "WIN"

        elif self.winner == 2:
            self.p2_wins += 1
            self.winner = 2
            return "WIN"
        return "OK"

    def play(self, position):

        if self.check_winner() == "WIN":
            return "WIN"
        else:
            self.position = position

            if self.whats_next == "Move to a free neighbour field":
                if self.table.move_player(self.position, self.current) != 1:
                    return f'Error:  {self.position} is not neighbour or is not a free field'
                else:
                    self.whats_next = "Select a free field"
                    return self.check_winner()
            else:
                if self.table.change_to_wall(self.position) != 1:
                    return f'Error:  {self.position} is not a free field'
                else:
                    if self.check_winner() != "WIN":
                        self.whats_next = "Move to a free neighbour field"
                        self.table.change_current_player()
                        self.current = self.table.current
                        return self.check_winner()
                    return self.check_winner()
