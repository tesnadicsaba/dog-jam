import tkinter as tk
from Table import *


class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.show_frame(StartPage)
        self.options = ""
        self.score = [0, 0]
        self.starts = 1

    def show_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # self.controller = controller

        self.main_frame = tk.Frame(self, relief=tk.SUNKEN)
        self.main_frame.rowconfigure(0, minsize=5)
        self.main_frame.columnconfigure(0, minsize=5)

        self.title = tk.Label(master=self.main_frame, font=("Times", 22), text="DOG HUNT")
        self.help_b = tk.Button(master=self.main_frame, text="Help", font=("", 12),
                                command=lambda: master.show_frame(HelpPage))

        self.play_against_label = tk.Label(master=self.main_frame, font=("Times", 16))
        self.play_against_label["text"] = "Play Against:"

        self.mate_b = tk.Button(master=self.main_frame, text="Mate", font=("bold", 10), width=20, bg="grey",
                                command=self.mate_selected)
        self.computer_b = tk.Button(master=self.main_frame, font=("bold", 10), text="Computer", width=20, bg="grey",
                                    command=self.computer_selected)
        self.online_b = tk.Button(master=self.main_frame, font=("bold", 10), text="Online", width=20, bg="grey",
                                  command=self.online_selected)

        self.opt = tk.IntVar()
        self.opt.set(1)

        self.radio_b_4 = tk.Radiobutton(master=self.main_frame, variable=self.opt, value=4, command=self.set)
        self.radio_b_2 = tk.Radiobutton(master=self.main_frame, variable=self.opt, value=2, command=self.set)
        self.radio_b_3 = tk.Radiobutton(master=self.main_frame, variable=self.opt, value=3, command=self.set)
        self.radio_b_1 = tk.Radiobutton(master=self.main_frame, variable=self.opt, value=1, command=self.set)

        self.information_label = tk.Label(master=self.main_frame, font=("Times", 16))

        self.title.grid(row=0, column=0, pady=10, sticky="w")
        self.help_b.grid(row=0, column=2, sticky="e", padx=5)
        self.play_against_label.grid(row=2, column=0, sticky="w")
        self.mate_b.grid(row=3, column=0, sticky="w", padx=5)
        self.computer_b.grid(row=3, column=1, sticky="w", padx=5)
        self.online_b.grid(row=3, column=2, sticky="w", padx=5)
        self.information_label.grid(row=4, column=0, sticky="w")

        self.play_b = tk.Button(master=self, text="PLAY", width=75, state="disabled",
                                command=lambda: master.show_frame(MultiPlayer))

        self.main_frame.pack()
        self.play_b.pack()

    def set_radio_buttons(self, color, label_text, button_text, value):

        self.mate_b["bg"] = color[0]
        self.online_b["bg"] = color[1]
        self.computer_b["bg"] = color[2]

        self.opt.set(1)
        self.information_label["text"] = label_text

        self.radio_b_1.config(text=button_text[0], value=value[0])
        self.radio_b_2.config(text=button_text[1], value=value[1])
        self.radio_b_3.config(text=button_text[2], value=value[2])
        self.radio_b_4.config(text=button_text[3], value=value[3])

        self.radio_b_1.grid(row=5, column=0, sticky="w")
        self.radio_b_2.grid(row=6, column=0, sticky="w")
        self.radio_b_3.grid(row=7, column=0, sticky="w")
        self.radio_b_4.grid(row=8, column=0, sticky="w")

        if button_text[0] == "-":
            self.radio_b_1.grid_forget()
        if button_text[1] == "-":
            self.radio_b_2.grid_forget()
        if button_text[2] == "-":
            self.radio_b_3.grid_forget()
        if button_text[3] == "-":
            self.radio_b_4.grid_forget()

        self.play_b["bg"] = "green"
        self.play_b["state"] = "normal"

    def mate_selected(self):
        self.set_radio_buttons(["green", "grey", "grey"], "Table Size:", ["Small", "Medium", "Large", "-"],
                               [3, 5, 7, 0])

    def computer_selected(self):
        self.set_radio_buttons(["grey", "grey", "green"], "Difficulty", ["Easy", "Medium", "Advanced", "Invicible"],
                               [3, 5, 55, 33])

    def online_selected(self):
        self.set_radio_buttons(["grey", "green", "grey"], "COMING SOON :)", ["-", "-", "-", "-"], [0, 0, 0, 0])

    def set(self):
        self.master.options = self.opt.get()


class HelpPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Help Page")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: master.show_frame(StartPage))
        button.pack()
        # here will come the useage and description


class MultiPlayer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.menubar = tk.Menu(self)
        self.menubar.add_command(label="Back", command=lambda: master.show_frame(StartPage))
        self.menubar.add_command(label="New Game", command=lambda: self.new_game(master))
        self.menubar.add_command(label="Restart", command=lambda: self.restart(master))
        master.config(menu=self.menubar)

        # ----------------------- Create a table ------------------------------
        self.mytable = Table(int(master.options), master.starts)

        self.score_frame = tk.Frame(master=self, relief=tk.SUNKEN)
        self.score_label = tk.Label(master=self.score_frame, text=str(f'Player1  {master.score[0]} - {master.score[1]}  Player2'), font=("bold", 14))
        self.score_frame.pack()
        self.score_label.pack()

        self.main_frame = tk.Frame(master=self, relief=tk.SUNKEN)
        self.main_frame.rowconfigure(0, minsize=5)
        self.main_frame.columnconfigure(0, minsize=5)
        self.main_frame.pack(fill=tk.X)

        self.instruction_frame = tk.Frame(master=self, relief=tk.SUNKEN)
        self.instruction_label = tk.Label(master=self.instruction_frame, text=str(f'Player{self.mytable.current}`s  turn'), font=("bold", 12))
        self.instruction_frame.pack()
        self.instruction_label.pack()

        self.draw_table_buttons()
        self.order = 0
        self.wins = master.score

    def draw_table_buttons(self):
        self.buttons = []
        nr = -1

        for i in range(self.mytable.size):
            for j in range(self.mytable.size):
                nr += 1
                self.button = tk.Button(master=self.main_frame, height=3, width=7,
                                        command=lambda x=nr: self.selected(x))

                if self.mytable.get_item([i, j]) == 1 or self.mytable.get_item([i, j]) == 2:
                    self.button.config(text=str(f'P{self.mytable.get_item([i, j])}'))

                if self.mytable.is_empty([i, j]):
                    self.button["bg"] = "green"
                elif self.mytable.is_wall([i, j]):
                    self.button["bg"] = "black"
                else:
                    self.button["bg"] = "red"
                self.buttons.append(self.button)
                self.button.grid(row=i + 4, column=j + 1, padx=2, pady=2)

    def redraw(self):
        for i in range(self.mytable.size):
            for j in range(self.mytable.size):
                if self.mytable.get_item([i, j]) == 1 or self.mytable.get_item([i, j]) == 2:
                    self.buttons[self.mytable.size * i + j].config(text=str(f'P{self.mytable.get_item([i, j])}'))
                else:
                    self.buttons[self.mytable.size * i + j].config(text="")

                if self.mytable.is_empty([i, j]):
                    self.buttons[self.mytable.size * i + j]["bg"] = "green"
                elif self.mytable.is_wall([i, j]):
                    self.buttons[self.mytable.size * i + j]["bg"] = "black"
                else:
                    self.buttons[self.mytable.size * i + j]["bg"] = "red"

        if self.mytable.check_winner() != 0:
            self.deactivate_buttons()
            self.instruction_label["text"] = str(f'Player{self.mytable.check_winner()} wins')

            if self.mytable.check_winner() == 1:
                self.wins[0] += 1
            else:
                self.wins[1] += 1

            self.score_label["text"] = str(f'Player1 {self.wins[0]} - {self.wins[1]} Player2')
            return 0

        return 1

    def selected(self, button):

        self.instruction_label["text"] = str(f'Player{self.mytable.current}`s  turn')
        position = [int(button / self.mytable.size), int(button % self.mytable.size)]

        if self.order == 0:
            if self.mytable.move_player(position, self.mytable.current) == 1:
                if self.redraw() == 0:
                    return
                self.order += 1

        if self.order == 1:
            if self.mytable.change_to_wall(position) == 1:
                if self.redraw() == 0:
                    return
                self.order = 0

                if self.mytable.current == 1:
                    self.mytable.current = 2
                else:
                    self.mytable.current = 1

        return position

    def deactivate_buttons(self):
        for i in range(self.mytable.size):
            for j in range(self.mytable.size):
                self.buttons[self.mytable.size*i + j].config(state="disabled")

    def restart(self, master):
        master.score = [0, 0]
        master.starts = 1
        master.show_frame(MultiPlayer)

    def new_game(self, master):
        if master.starts == 1:
            master.starts = 2
        else:
            master.starts = 1

        master.show_frame(MultiPlayer)


if __name__ == "__main__":
    app = App()
    app.geometry("600x400")
    app.mainloop()
