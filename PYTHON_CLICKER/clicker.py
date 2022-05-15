from tkinter import *

score = 0
power_touch = 1
auto_score = 0


def make_window():
    window.geometry("450x200")
    window['bg'] = 'yellow'
    window.title("Clicker")


def make_label_score(label):
    label['text'] = "Score: 0"
    label['bg'] = "yellow"
    label['font'] = ("Arial Bold", 20)
    label.pack()


def check_active_button():
    global button_2, button_5, button_10, score, label_score
    if score >= 500:
        button_2['state'] = 'normal'
    if score >= 5000:
        button_5['state'] = 'normal'
    if score >= 10000:
        button_10['state'] = 'normal'


def clicker_command(event):
    global label_score, score
    score += power_touch
    label_score['text'] = "Score: " + str(score)
    check_active_button()
    label_score.place(x=10, y=20)


def activate_button2():
    global power_touch, score, button_2, label_score
    power_touch += 2
    score -= 500
    temp_label = Label(text="-50 Score", font=50)
    temp_label.pack()
    if score < 500:
        button_2['state'] = 'disabled'


def activate_button5():
    global power_touch, score, button_5
    power_touch += 5
    score -= 5000
    temp_label = Label(text="-5000 Score", font=50)
    temp_label.pack()
    if score < 5000:
        button_5['state'] = 'disabled'


def activate_button10():
    global power_touch, score, button_10
    power_touch += 10
    score -= 10000
    temp_label = Label(text="-10000 Score", font=50)
    temp_label.pack()
    if score < 10000:
        button_10['state'] = 'disabled'


window = Tk()
make_window()
label_score = Label()
make_label_score(label_score)
label_score.place(x=10, y=20)
window.bind('<space>', clicker_command)
button_2 = Button(text='+2 (500 score)', state='disabled', command=activate_button2, font=("Arial Bold", 20))
button_5 = Button(text='+5 (5000 score)', state='disabled', command=activate_button5, font=("Arial Bold", 20))
button_10 = Button(text='+10 (10000 score)', state='disabled', command=activate_button10, font=("Arial Bold", 20))
button_2.pack()
button_5.pack()
button_10.pack()
window.mainloop()
