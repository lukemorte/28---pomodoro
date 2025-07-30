from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#222831"
RED = "#393E46"
GREEN = "#00ADB5"
YELLOW = "#00FFF5"
FONT_NAME = "Courier"

IDLE_TEXT = "Timer"
WORK_TEXT = "Work"
BREAK_TEXT = "Break"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20

WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.15
LONG_BREAK_MIN = 0.3

reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    print(reps)
    print(work_sec)
    print(short_break_sec)
    print(long_break_sec)

    if reps % 8 == 0:
        title_label.config(text=BREAK_TEXT, fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text=BREAK_TEXT, fg=RED)
        count_down(short_break_sec)
    else:
        title_label.config(text=WORK_TEXT, fg=YELLOW)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    time_str = get_timer_string(count)    
    canvas.itemconfig(timer_text, text=time_str)

    if count > 0:
        window.after(100, count_down, count - 1)
    else:
        start_timer()


def get_timer_string(seconds):
    str_min = int(seconds // 60)
    if str_min < 10:
        str_min = f"0{str_min}"
    str_sec = int(seconds % 60)
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
timer_text = canvas.create_text(103, 130, text=get_timer_string(WORK_MIN * 60), fill="white", font=(FONT_NAME, 15, "bold"))

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
