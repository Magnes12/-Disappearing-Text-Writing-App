import tkinter as tk

app = tk.Tk()
app.title('Disappearing text writing app')
app.geometry('400x400')


def clear_entry():
    global timer_id
    entry_1.delete(0, tk.END)
    timer_id = None


def start_timer():
    global timer_id
    timer_id = app.after(5000, clear_entry)


def on_entry_change(event):
    global timer_id
    if timer_id is not None:
        entry_1.after_cancel(timer_id)

    start_timer()


app_font = ('times', 18, 'bold')

label_1 = tk.Label(app, text='Write your text below', font=app_font)
label_1.pack()

entry_1 = tk.Entry(app, width=50)
entry_1.pack()

label_2 = tk.Label(app, text='All text disappear if You wont type anything in 5 sek',
                   font=app_font)
label_2.pack()

timer_id = None

entry_1.bind("<Key>", on_entry_change)

app.mainloop()
