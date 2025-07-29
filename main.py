from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#222831"
RED = "#393E46"
GREEN = "#00ADB5"
YELLOW = "#00FFF5"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    count_down(WORK_MIN * 60 - 1)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    time_str = get_timer_string(count)
    # time_str = f"{count // 60}:{count % 60:02d}"
    canvas.itemconfig(timer_text, text=time_str)
    if count > 0:
        window.after(1000, count_down, count - 1)


def get_timer_string(seconds):
    str_min = seconds // 60
    if str_min < 10:
        str_min = f"0{str_min}"
    str_sec = seconds % 60
    if str_sec < 10:
        str_sec = f"0{str_sec}"
    return f"{str_min}:{str_sec}"


# ---------------------------- UI SETUP ------------------------------- #ls

# window

window = Tk()
window.title("Pomodoro")
window.config(padx=40, pady=40, bg=GREEN)

# app title

title_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=PINK, bg=GREEN)

# canvas image

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# timer
timer_text = canvas.create_text(103, 130, text=get_timer_string(WORK_MIN * 60), fill="white", font=(FONT_NAME, 35, "bold"))

# buttons

btn_start = Button(text="start", width=5, height=1, padx=10, pady=5,
                   font=(FONT_NAME, 12, "bold"), fg=YELLOW, bg=RED, command=start_timer)
btn_reset = Button(text="reset", width=5, height=1, padx=10, pady=5, font=(FONT_NAME, 12, "bold"), fg=YELLOW, bg=RED)

# checkmark

checkmark = Label(text="✔", font=(FONT_NAME, 20, "bold"), fg=YELLOW, bg=GREEN)

# placement

title_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
btn_start.grid(column=0, row=2)
btn_reset.grid(column=2, row=2)
checkmark.grid(column=1, row=3)



window.mainloop()
