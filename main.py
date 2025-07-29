from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#B9375D"
RED = "#D25D5D"
GREEN = "#E7D3D3"
YELLOW = "#EEEEEE"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #ls

# window

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

# app title

app_title = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=RED, bg=GREEN)

# canvas image

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# buttons

btn_start = Button(text="start", width=5, height=1, padx=10, pady=5, font=(FONT_NAME, 12, "bold"), fg=YELLOW, bg=RED)
btn_reset = Button(text="reset", width=5, height=1, padx=10, pady=5, font=(FONT_NAME, 12, "bold"), fg=YELLOW, bg=RED)

# checkmark

checkmark = Label(text="✔", font=(FONT_NAME, 20, "bold"), fg=PINK, bg=GREEN)

# placement

app_title.grid(column=1, row=0)
canvas.grid(column=1, row=1)
btn_start.grid(column=0, row=2)
btn_reset.grid(column=2, row=2)
checkmark.grid(column=1, row=3)



window.mainloop()
