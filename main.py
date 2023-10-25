from tkinter import *
from Generate import *

poem = ""


def center_window(window, wwidth, wheight):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    wx = (screen_width - wwidth) // 2
    wy = (screen_height - wheight - 50) // 2
    window.geometry(f"{width}x{height}+{wx}+{wy}")


root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
width = 900
height = 600
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry("{}x{}+{}+{}".format(width, height, x, y))

root.title("Infinite Poem")

# Create frames
main_frame = Frame(root)
generate_frame = Frame(root)

for frame in (main_frame, generate_frame):
    frame.grid(row=0, column=0, sticky="nsew")


def show_frame(cframe):
    cframe.tkraise()


def onclick_valentine():
    global poem
    poem = generate_love_poem()
    show_frame(generate_frame)
    poem_label.config(text=poem)


def onclick_birthday():
    global poem
    poem = generate_birthday_poem()
    poem_label.config(text=poem)
    show_frame(generate_frame)


def onclick_christmas():
    global poem
    poem = generate_christmas_poem()
    poem_label.config(text=poem)
    show_frame(generate_frame)


def onclick_newyear():
    global poem
    poem = generate_new_year_poem()
    poem_label.config(text=poem)
    show_frame(generate_frame)


def onclick_misses():
    global poem
    poem = generate_miss_you_poem()
    poem_label.config(text=poem)
    show_frame(generate_frame)


show_frame(main_frame)

# Main Frame

main_background_img = PhotoImage(file="Assets/main_background.png")

main_background_label = Label(main_frame, image=main_background_img)
main_background_label.image = main_background_img
main_background_label.place(x=0, y=0, relwidth=1, relheight=1)

valentine_img = PhotoImage(file="Assets/button_valentines.png")
birthday_img = PhotoImage(file="Assets/button_birthday.png")
christmas_img = PhotoImage(file="Assets/button_christmas.png")
newyear_img = PhotoImage(file="Assets/button_newyear.png")
missing_img = PhotoImage(file="Assets/button_missing.png")

valentine_button = Button(main_frame, image=valentine_img, borderwidth=0, highlightthickness=0, relief="flat",
                          command=lambda: onclick_valentine())
valentine_button.place(x=265.5, y=188, width=369, height=59)

birthday_button = Button(main_frame, image=birthday_img, borderwidth=0, highlightthickness=0, relief="flat",
                         command=lambda: onclick_birthday())
birthday_button.place(x=265.5, y=260, width=369, height=59)

christmas_button = Button(main_frame, image=christmas_img, borderwidth=0, highlightthickness=0, relief="flat",
                          command=lambda: onclick_christmas())
christmas_button.place(x=265.5, y=332, width=369, height=59)

newyear_button = Button(main_frame, image=newyear_img, borderwidth=0, highlightthickness=0, relief="flat",
                        command=lambda: onclick_newyear())
newyear_button.place(x=265.5, y=404, width=369, height=59)

missing_button = Button(main_frame, image=missing_img, borderwidth=0, highlightthickness=0, relief="flat",
                        command=lambda: onclick_misses())
missing_button.place(x=265.5, y=476, width=369, height=59)

# End of Main Frame

# Generate Frame

generate_frame.configure(bg="#d9d9d9")

generate_background_img = PhotoImage(file="Assets/generate_background.png")

generate_background_label = Label(generate_frame, image=generate_background_img)
generate_background_label.image = generate_background_img
generate_background_label.place(x=0, y=0, relwidth=1, relheight=1)

poem_label = Label(generate_frame, anchor=CENTER, background="#e7e6e7", wraplength=300, font=("Comic Sans MS", 14))
poem_label.place(x=300, y=100, width=300, height=300)

regenerate_img = PhotoImage(file="Assets/button_regenerate.png")

regenerate_button = Button(generate_frame, image=regenerate_img, borderwidth=0, highlightthickness=0, relief="flat",
                           bg="#d9d9d9", command=lambda: show_frame(main_frame))
regenerate_button.place(x=337, y=420, width=226, height=59)

root.resizable(False, False)
center_window(root, 900, 584)
root.mainloop()
