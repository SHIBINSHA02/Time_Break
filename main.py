from tkinter import *
import math

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
ontime = "pause"
current_timer = None  # Initialize the current_timer

# Timer Reset
def reset():
    canvas.itemconfig(timer_text, text="00:00")
    global reps, ontime, current_timer
    headLabel.config(text="Timer", fg=GREEN)
    reps = 0
    ontime = "pause"
    if current_timer is not None:
        root.after_cancel(current_timer)
    current_timer = None  # Reset the current_timer

# Timer Mechanism
def starttime():
    global reps, ontime, current_timer
    if current_timer is not None:
        root.after_cancel(current_timer)  # Cancel the current timer
    ontime = "running"
    reps += 1
    if reps % 8 == 0:
        current_timer = count_down(LONG_BREAK_MIN * 60)
        headLabel.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        current_timer = count_down(SHORT_BREAK_MIN * 60)
        headLabel.config(text="Break", fg=PINK)
    else:
        headLabel.config(text="Work", fg=GREEN)
        current_timer = count_down(WORK_MIN * 60)

# Countdown Mechanism
def count_down(count):
    global ontime, current_timer
    if ontime == "running":
        sec = count % 60
        if sec < 10:
            sec = f"0{sec}"
        else:
            sec = str(sec)
        canvas.itemconfig(timer_text, text=f"{math.floor(count / 60)}:{sec}")
        if count > 0:
            current_timer = root.after(1000, count_down, count - 1)
    elif ontime == "pause":
        # Handle pause by doing nothing
        pass
    else:
        # Handle stop by resetting the timer
        canvas.itemconfig(timer_text, text="00:00")

# UI Setup
root = Tk()
root.title("Time Break")
root.config(padx=100, pady=50, bg=YELLOW)

headLabel = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
headLabel.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

labelStart = Button(text="Start", highlightthickness=0, font=("bold", 10), relief="flat", command=starttime)
labelStart.grid(row=2, column=0)

labelRestart = Button(text="Restart", highlightthickness=0, font=("bold", 10), relief="flat", command=reset)
labelRestart.grid(row=2, column=2)

labelTick = Label(text="✔", fg=GREEN, bg=YELLOW)
labelTick.grid(row=3, column=1)

root.mainloop()
