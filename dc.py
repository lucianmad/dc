import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import pygame
import random, time, threading
import numpy as np


def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x ** 2 + y ** 2
        if distance <= 1:
            inside_circle += 1

    return (inside_circle / num_samples) * 4


def calculate_scores1(sample_sizes):
    score = 0

    for num_samples in sample_sizes:
        start_time = time.time()
        _ = monte_carlo_pi(num_samples)
        end_time = time.time()

        elapsed_time = 1 / (end_time - start_time)
        score = score + elapsed_time

    return score


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def find_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def calculate_scores2(sample_sizes, n, x):
    score = 0

    for num_samples in sample_sizes:
        start_time = time.time()
        _ = monte_carlo_pi(num_samples)
        __ = fibonacci(n)
        ___ = find_primes(x)
        end_time = time.time()

        elapsed_time = 1 / (end_time - start_time)
        score = score + elapsed_time

    return score


class StartFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(self, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        image_original = Image.open("image_1.png").resize((1920, 1080))
        self.image_tk = ImageTk.PhotoImage(image_original)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor='nw')

        image2_original = Image.open("image_3.png").resize((600, 700))
        self.image2_tk = ImageTk.PhotoImage(image2_original)
        self.canvas.create_image(0, 380, image=self.image2_tk, anchor='nw')

        image3_original = Image.open("image_2.png").resize((301, 484))
        self.image3_tk = ImageTk.PhotoImage(image3_original)
        self.canvas.create_image(1570, 630, image=self.image3_tk, anchor='nw')

        image4_original = Image.open("image_4.png").resize((223, 199))
        self.image4_tk = ImageTk.PhotoImage(image4_original)
        self.canvas.create_image(1000, 290, image=self.image4_tk, anchor='nw')

        image5_original = Image.open("image_5.png").resize((450, 321))
        self.image5_tk = ImageTk.PhotoImage(image5_original)
        self.canvas.create_image(310, 320, image=self.image5_tk, anchor='nw')

        image6_original = Image.open("image_6.png").resize((1802, 83))
        self.image6_tk = ImageTk.PhotoImage(image6_original)
        self.canvas.create_image(60, 40, image=self.image6_tk, anchor='nw')

        image7_original = Image.open("image_7.png").resize((215, 181))
        self.image7_tk = ImageTk.PhotoImage(image7_original)
        self.canvas.create_image(430, 390, image=self.image7_tk, anchor='nw')

        button_image = Image.open("button_short.png").resize((400, 200))
        self.button_image_tk1 = ImageTk.PhotoImage(button_image)
        self.button1 = self.canvas.create_image(650, 700, image=self.button_image_tk1, anchor='nw', tag='event_button1')

        button_hover_image = Image.open("button_short_hover.png").resize((400, 200))
        self.button_hover_image_tk1 = ImageTk.PhotoImage(button_hover_image)

        self.canvas.tag_bind('event_button1', "<Button-1>", lambda event: self.switch_content(AlgorithmFrame))
        self.canvas.tag_bind('event_button1', "<Enter>", lambda event: self.b1_enter())
        self.canvas.tag_bind('event_button1', "<Leave>", lambda event: self.b1_leave())

        button2_image = Image.open("button_long.png").resize((400, 200))
        self.button_image_tk2 = ImageTk.PhotoImage(button2_image)
        self.button2 = self.canvas.create_image(1150, 700, image=self.button_image_tk2, anchor='nw', tag='event_button2')

        button2_hover_image = Image.open("button_long_hover.png").resize((400, 200))
        self.button_hover_image_tk2 = ImageTk.PhotoImage(button2_hover_image)

        self.canvas.tag_bind('event_button2', "<Button-1>", lambda event: self.switch_content(AlgorithmFrameLong))
        self.canvas.tag_bind('event_button2', "<Enter>", lambda event: self.b2_enter())
        self.canvas.tag_bind('event_button2', "<Leave>", lambda event: self.b2_leave())

        exit_button_image = Image.open("exit.png").resize((50, 50))
        self.exit_button_image_tk = ImageTk.PhotoImage(exit_button_image)
        button3 = self.canvas.create_image(980, 1040, image=self.exit_button_image_tk, tag='exit_button')

        self.canvas.tag_bind('exit_button', "<Button-1>", self.exit_app)
        self.canvas.tag_bind('exit_button', "<Enter>", lambda event: self.enter_exit_button())
        self.canvas.tag_bind('exit_button', "<Leave>", lambda event: self.leave_exit_button())

    def enter_exit_button(self):
        self.controller.config(cursor="hand2")

    def leave_exit_button(self):
        self.controller.config(cursor="")
    def b1_enter(self):
        self.canvas.itemconfig(self.button1, image=self.button_hover_image_tk1)
        self.controller.config(cursor="hand2")

    def b1_leave(self):
        self.canvas.itemconfig(self.button1, image=self.button_image_tk1)
        self.controller.config(cursor="")

    def exit_app(self, event=None):
        self.controller.quit()

    def b2_enter(self):
        self.canvas.itemconfig(self.button2, image=self.button_hover_image_tk2)
        self.controller.config(cursor="hand2")

    def b2_leave(self):
        self.canvas.itemconfig(self.button2, image=self.button_image_tk2)
        self.controller.config(cursor="")

    def switch_content(self, frame_class):
        self.controller.show_frame(frame_class)


class AlgorithmFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(self, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        image1_original = Image.open("imagew2.png").resize((1920, 1080))
        self.image_tk = ImageTk.PhotoImage(image1_original)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor='nw')

        image2_original = Image.open("image_3.png").resize((600, 700))
        self.image2_tk = ImageTk.PhotoImage(image2_original)
        self.image_item = None

        image6_original = Image.open("image_9.png").resize((1802, 83))
        self.image6_tk = ImageTk.PhotoImage(image6_original)
        self.canvas.create_image(60, 40, image=self.image6_tk, anchor='nw')

        self.move_image()

        self.loading_circle = None
        self.loading_angle = 0
        self.create_loading_circle()

        exit_button_image = Image.open("exit.png").resize((50, 50))
        self.exit_button_image_tk = ImageTk.PhotoImage(exit_button_image)
        button2 = self.canvas.create_image(980, 1040, image=self.exit_button_image_tk, tag='exit_button')

        self.canvas.tag_bind('exit_button', "<Button-1>", self.exit_app)
        self.canvas.tag_bind('exit_button', "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind('exit_button', "<Leave>", lambda event: self.leave())

    def start_animation(self):
        play()
        self.image_item = self.canvas.create_image(0, -600, image=self.image2_tk, anchor='nw')
        self.move_image()

    def exit_app(self, event=None):
        self.controller.quit()

    def enter(self):
        self.controller.config(cursor="hand2")

    def leave(self):
        self.controller.config(cursor="")

    def move_image(self):
        if self.image_item:
            self.canvas.move(self.image_item, 0, 5)
            x0, y0, x1, y1 = self.canvas.bbox(self.image_item)
            if y1 >= 1080:
                threading.Thread(target=self.execute_algorithms).start()
                return
            self.after(61, self.move_image)

    def execute_algorithms(self):
        sample_sizes = [100000, 500000, 1000000]
        score = calculate_scores1(sample_sizes)
        if score:
            self.controller.show_frame(ResultFrame, score=score)

    def create_loading_circle(self):
        x0, y0 = self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2
        radius = 60
        self.loading_circle = self.canvas.create_oval(x0 - radius, y0 - radius, x0 + radius, y0 + radius,
                                                      outline="#FFFFFF", width=10)
        self.animate_loading_circle()

    def animate_loading_circle(self):
        self.loading_angle += 5
        self.canvas.delete(self.loading_circle)
        x0, y0 = self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2
        radius = 60
        self.loading_circle = self.canvas.create_arc(x0 - radius, y0 - radius, x0 + radius, y0 + radius,
                                                     start=self.loading_angle, extent=90, outline="#FFFFFF",
                                                     style="arc", width=10)
        self.after(25, self.animate_loading_circle)


class AlgorithmFrameLong(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(self, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        image1_original = Image.open("imagew2.png").resize((1920, 1080))
        self.image_tk = ImageTk.PhotoImage(image1_original)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor='nw')

        image2_original = Image.open("image_3.png").resize((600, 700))
        self.image2_tk = ImageTk.PhotoImage(image2_original)
        self.image_item = None

        image6_original = Image.open("image_9.png").resize((1802, 83))
        self.image6_tk = ImageTk.PhotoImage(image6_original)
        self.canvas.create_image(60, 40, image=self.image6_tk, anchor='nw')

        self.move_image()

        self.loading_circle = None
        self.loading_angle = 0
        self.create_loading_circle()

        exit_button_image = Image.open("exit.png").resize((50, 50))
        self.exit_button_image_tk = ImageTk.PhotoImage(exit_button_image)
        button2 = self.canvas.create_image(980, 1040, image=self.exit_button_image_tk, tag='exit_button')

        self.canvas.tag_bind('exit_button', "<Button-1>", self.exit_app)
        self.canvas.tag_bind('exit_button', "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind('exit_button', "<Leave>", lambda event: self.leave())

    def start_animation(self):
        play()
        self.image_item = self.canvas.create_image(0, -600, image=self.image2_tk, anchor='nw')
        self.move_image()

    def exit_app(self, event=None):
        self.controller.quit()

    def enter(self):
        self.controller.config(cursor="hand2")

    def leave(self):
        self.controller.config(cursor="")

    def move_image(self):
        if self.image_item:
            self.canvas.move(self.image_item, 0, 5)
            x0, y0, x1, y1 = self.canvas.bbox(self.image_item)
            if y1 >= 1080:
                threading.Thread(target=self.execute_algorithms).start()
                return
            self.after(61, self.move_image)

    def execute_algorithms(self):
        sample_sizes1 = [100000, 500000, 1000000]
        score = calculate_scores2(sample_sizes1, 20, 100000)
        if score:
            self.controller.show_frame(ResultFrame, score=score)

    def create_loading_circle(self):
        x0, y0 = self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2
        radius = 60
        self.loading_circle = self.canvas.create_oval(x0 - radius, y0 - radius, x0 + radius, y0 + radius,
                                                      outline="#FFFFFF", width=10)
        self.animate_loading_circle()

    def animate_loading_circle(self):
        self.loading_angle += 5
        self.canvas.delete(self.loading_circle)
        x0, y0 = self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2
        radius = 60
        self.loading_circle = self.canvas.create_arc(x0 - radius, y0 - radius, x0 + radius, y0 + radius,
                                                     start=self.loading_angle, extent=90, outline="#FFFFFF",
                                                     style="arc", width=10)
        self.after(25, self.animate_loading_circle)


class ResultFrame(Frame):
    def __init__(self, parent, controller, score=None):
        Frame.__init__(self, parent)
        self.controller = controller
        self.score = score

        self.canvas = tk.Canvas(self, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        image_original = Image.open("imagew3.png").resize((1920, 1080))
        self.image_tk = ImageTk.PhotoImage(image_original)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor='nw')

        image6_original = Image.open("image_8.png").resize((359, 48))
        self.image6_tk = ImageTk.PhotoImage(image6_original)
        self.canvas.create_image(779, 365, image=self.image6_tk, anchor='nw')

        self.text_score = self.canvas.create_text(945, 850, text=f" {self.score} points", font=("Arial", 23),
                                                  fill="yellow", anchor="center")

        exit_button_image = Image.open("exit.png").resize((50, 50))
        self.exit_button_image_tk = ImageTk.PhotoImage(exit_button_image)
        button1 = self.canvas.create_image(980, 1040, image=self.exit_button_image_tk, tag='exit_button')

        self.canvas.tag_bind('exit_button', "<Button-1>", self.exit_app)
        self.canvas.tag_bind('exit_button', "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind('exit_button', "<Leave>", lambda event: self.leave())

    def exit_app(self, event=None):
        self.controller.quit()

    def enter(self):
        self.controller.config(cursor="hand2")

    def leave(self):
        self.controller.config(cursor="")

    def update_score(self, score=None):
        if score is not None:
            self.score = score
        self.canvas.itemconfigure(self.text_score, text=f" {self.score} points")


def play():
    pygame.mixer.init()
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.02)


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        score = None
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1920x1080")
        self.configure(bg="#FFFFFF")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartFrame, AlgorithmFrame, AlgorithmFrameLong, ResultFrame):
            if F == ResultFrame:
                frame = F(container, self, score=score)
            else:
                frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartFrame)

    def show_frame(self, cont, score=None):
        frame = self.frames[cont]
        frame.tkraise()
        if cont in (AlgorithmFrame, AlgorithmFrameLong):
            frame.start_animation()
        elif cont == ResultFrame:
            frame.update_score(score)


if __name__ == "__main__":
    app = MainApplication()
    app.attributes("-fullscreen", True)
    app.mainloop()
