import tkinter as tk
from tkinter import *


class HelpPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Back",
                  command=lambda: master.switch_frame(StartingPage)).pack()


class AgainsMate(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.main_frame = tk.Frame(self, relief=tk.SUNKEN)
        self.main_frame.rowconfigure(0, minsize=5)
        self.main_frame.columnconfigure(0, minsize=5)

        self.back_b = tk.Button(self.main_frame, text="Back", command=lambda: switch_frame(StartingPage))
        self.back_b.pack()
        self.main_frame.pack()
        print(StartingPage.option)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0)
        container.grid_columnconfigure(0)

        self.frames = []

        for F in (StartingPage, HelpPage, AgainsMate):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0)

        self.switch_frame(StartingPage)

    def switch_frame(self, frame):
        new_frame = self.frames[frame]
        new_frame.tkraise()


class StartingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.master = parent
        self.main_frame = tk.Frame(self, relief=tk.SUNKEN)
        self.main_frame.rowconfigure(0, minsize=5)
        self.main_frame.columnconfigure(0, minsize=5)

        self.title = tk.Label(master=self.main_frame, font=("Times", 22), text="DOG HUNT")
        self.help_b = tk.Button(master=self.main_frame, text="Help", font=("", 12),
                                command=lambda: controller.switch_frame(HelpPage))

        self.play_against_label = tk.Label(master=self.main_frame, font=("Times", 16))
        self.play_against_label["text"] = "Play Against:"

        self.mate_b = tk.Button(master=self.main_frame, text="Mate", font=("bold", 10), width=20, bg="grey",
                                command=self.mate_selected)
        self.computer_b = tk.Button(master=self.main_frame, font=("bold", 10), text="Computer", width=20, bg="grey",
                                    command=self.computer_selected)
        self.online_b = tk.Button(master=self.main_frame, font=("bold", 10), text="Online", width=20, bg="grey",
                                  command=self.online_selected
                                  )

        self.information_label = tk.Label(master=self.main_frame, font=("Times", 16))
        self.radio_b_value = tk.IntVar()
        self.radio_b_value.set(1)

        self.radio_b_1 = tk.Radiobutton(master=self.main_frame, variable=self.radio_b_value, value=1)
        self.radio_b_2 = tk.Radiobutton(master=self.main_frame, variable=self.radio_b_value, value=2)
        self.radio_b_3 = tk.Radiobutton(master=self.main_frame, variable=self.radio_b_value, value=3)
        self.radio_b_4 = tk.Radiobutton(master=self.main_frame, variable=self.radio_b_value, value=4)

        self.title.grid(row=0, column=0, pady=10)
        self.help_b.grid(row=0, column=6, sticky="e", padx=5)
        self.play_against_label.grid(row=2, column=0, sticky="w")
        self.mate_b.grid(row=3, column=0, sticky="w", padx=5)
        self.computer_b.grid(row=3, column=1, sticky="w", padx=5)
        self.online_b.grid(row=3, column=2, sticky="w", padx=5)
        self.information_label.grid(row=4, column=0, sticky="w")

        self.play_b = tk.Button(master=self, text="PLAY", width=75, state="disabled", command=lambda: master.switch_frame(AgainsMate))

        self.main_frame.pack()
        self.play_b.pack()

    def set_radio_buttons(self, color, label_text, button_text):
        self.mate_b["bg"] = color[0]
        self.online_b["bg"] = color[1]
        self.computer_b["bg"] = color[2]

        self.information_label["text"] = label_text

        self.radio_b_value.set(1)
        self.radio_b_1["text"] = button_text[0]
        self.radio_b_2["text"] = button_text[1]
        self.radio_b_3["text"] = button_text[2]
        self.radio_b_4["text"] = button_text[3]

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
        self.set_radio_buttons(["green", "grey", "grey"], "Table Size:", ["Small", "Medium", "Large", "-"])

    def computer_selected(self):
        self.set_radio_buttons(["grey", "grey", "green"], "Difficulty", ["Easy", "Medium", "Advanced", "Invicible"])

    def online_selected(self):
        self.set_radio_buttons(["grey", "green", "grey"], "COMING SOON :)", ["-", "-", "-", "-"])


if __name__ == "__main__":
    app = App()
    app.mainloop()
