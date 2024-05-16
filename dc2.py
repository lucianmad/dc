import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import pygame
import random, time, threading

def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x ** 2 + y ** 2
        if distance <= 1:
            inside_circle += 1

    return (inside_circle / num_samples) * 4


def calculate_scores(sample_sizes):
    scores = []

    for num_samples in sample_sizes:
        start_time = time.time()
        _ = monte_carlo_pi(num_samples)
        end_time = time.time()

        elapsed_time = 1 / (end_time - start_time)
        scores.append(elapsed_time)

    return scores

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

        button_image = Image.open("button_1.png").resize((600, 250))
        self.button_image_tk = ImageTk.PhotoImage(button_image)
        self.button1 = self.canvas.create_image(1000, 870, image=self.button_image_tk, tag='event')

        self.canvas.tag_bind('event', "<Button-1>", self.switch_content)
        self.canvas.tag_bind('event', "<Enter>", lambda event: self.enter())
        self.canvas.tag_bind('event', "<Leave>", lambda event: self.leave())

        button_hover_image = Image.open("button_2.png").resize((600, 250))
        self.button_hover_image_tk = ImageTk.PhotoImage(button_hover_image)

        exit_button_image = Image.open("exit.png").resize((50,50))
        self.exit_button_image_tk = ImageTk.PhotoImage(exit_button_image)
        self.button2 = self.canvas.create_image(980,1040, image=self.exit_button_image_tk, tag='exit_button')

        self.canvas.tag_bind('exit_button', "<Button-1>", self.exit_app)
        self.canvas.tag_bind('exit_button', "<Enter>", lambda event: self.enter_exit_button())
        self.canvas.tag_bind('exit_button', "<Leave>", lambda event: self.leave_exit_button())


    def exit_app(self, event=None):
        self.controller.quit()

    def enter(self):
        self.canvas.itemconfig(self.button1, image=self.button_hover_image_tk)
        self.controller.config(cursor="hand2")

    def leave(self):
        self.canvas.itemconfig(self.button1, image=self.button_image_tk)
        self.controller.config(cursor="")

    def switch_content(self, event):
        self.controller.show_frame(AlgorithmFrame)

    def enter_exit_button(self):
        self.controller.config(cursor="hand2")

    def leave_exit_button(self):
        self.controller.config(cursor="")


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
                threading.Thread(target=self.execute_monte_carlo).start()
                return
            self.after(61, self.move_image)

    def execute_monte_carlo(self):
        monte_carlo_result = monte_carlo_pi(10000000)
        if monte_carlo_result:
            self.controller.show_frame(ResultFrame)

    def create_loading_circle(self):
        x0, y0 = self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2
        radius = 60
        self.loading_circle = self.canvas.create_oval(x0 - radius, y0 - radius, x0 + radius, y0 + radius, outline="#FFFFFF", width = 10)
        self.animate_loading_circle()

    def animate_loading_circle(self):
        self.loading_angle += 5
        self.canvas.delete(self.loading_circle)
        x0, y0 = self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2
        radius = 60
        self.loading_circle = self.canvas.create_arc(x0 - radius, y0 - radius, x0 + radius, y0 + radius,start=self.loading_angle, extent=90, outline="#FFFFFF",style="arc", width = 10)
        self.after(25, self.animate_loading_circle)
class ResultFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(self, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        image_original = Image.open("imagew3.png").resize((1920, 1080))
        self.image_tk = ImageTk.PhotoImage(image_original)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor='nw')

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

def play():
    pygame.mixer.init()
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.05)


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1920x1080")
        self.configure(bg="#FFFFFF")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartFrame, AlgorithmFrame, ResultFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if cont == AlgorithmFrame:
            frame.start_animation()


if __name__ == "__main__":
    app = MainApplication()
    app.attributes("-fullscreen", True)
    app.mainloop()