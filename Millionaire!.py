import pickle
import random
from tkinter import *

user = ''
users = {}
ranks = {'Ahmed': 500000, 'Leyla': 250000, 'Leman': 125000, 'Anar': 64000,
         'Emin': 32000, 'Rza': 16000, 'Arun': 8000, 'Timur': 4000,
         'Ildar': 2000, 'Sari': 1000, 'Raman': 500, 'Tehran': 300,
         'Asif': 200, 'Ilham': 100, 'Ziya': 1000000
         }
i = help1 = help2 = help3 = 1
a = b = c = d = e = f = correct = select = question = friend_answer = ""
money = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000,
         32000, 64000, 125000, 250000, 500000, 1000000]

try:
    with open('users.txt', 'rb') as file:
        users = pickle.loads(file.read())

except IOError as e:
    with open('users.txt', 'wb') as file:
        pickle.dump(users, file)
    with open('users.txt', 'rb') as file:
        users = pickle.loads(file.read())

try:
    with open('ranks.txt', 'rb') as file_ranks:
        ranks = pickle.loads(file_ranks.read())

except IOError as ee:
    with open('ranks.txt', 'wb') as file_ranks:
        pickle.dump(ranks, file_ranks)
    with open('ranks.txt', 'rb') as file_ranks:
        ranks = pickle.loads(file_ranks.read())

gui = Tk()
gui.geometry('750x500')
gui.resizable(FALSE, NO)
gui.title("Who Wants to be a Millionaire!")


def welcome():
    frame = Frame(gui)
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor='center')

    button_sign_in = Button(frame, text="Sign in", command=lambda: registration())
    button_sign_in.configure(font='Helvetica 18 bold', relief=RIDGE)
    button_sign_in.pack()
    button_sign_in.place(relx=0.25, rely=0.2, relheight=0.15, relwidth=0.5)

    button_sign_up = Button(frame, text="Sign up", command=lambda: login_form())
    button_sign_up.configure(font='Helvetica 18 bold', relief=RIDGE)
    button_sign_up.pack()
    button_sign_up.place(relx=0.25, rely=0.4, relheight=0.15, relwidth=0.5)

    button_play = Button(frame, text="Play as Guest", command=lambda: guest())
    button_play.configure(font='Helvetica 18 bold', relief=RIDGE)
    button_play.pack()
    button_play.place(relx=0.25, rely=0.6, relheight=0.15, relwidth=0.5)


def registration():
    global users
    label_error = None

    frame = Frame(gui)
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor='center')

    # noinspection PyUnusedLocal
    def clear_widget(event):
        if login_register == frame.focus_get() and login_register.get() == 'Enter Username':
            login_register.delete(0, END)
        elif password_register == password_register.focus_get() and password_register.get() == 'Enter Password':
            password_register.delete(0, END)
        elif password_conf_register == password_conf_register.focus_get() \
                and password_conf_register.get() == 'Repeat Password':
            password_conf_register.delete(0, END)

    # noinspection PyUnusedLocal
    def repopulate_defaults(event):
        if login_register != gui.focus_get() and login_register.get() == '':
            login_register.insert(0, 'Enter Username')
        elif password_register != gui.focus_get() and password_register.get() == '':
            password_register.insert(0, 'Enter Password')
        elif password_conf_register != gui.focus_get() and password_conf_register.get() == '':
            password_conf_register.insert(0, 'Repeat Password')

    login_register = Entry(frame, font='Helvetica 18')
    login_register.insert(0, 'Enter Username')
    login_register.bind("<FocusIn>", clear_widget)
    login_register.bind('<FocusOut>', repopulate_defaults)
    login_register.place(relx=0.25, rely=0.2, relheight=0.15, relwidth=0.5)

    password_register = Entry(frame, font='Helvetica 18')
    password_register.insert(0, 'Enter Password')
    password_register.bind("<FocusIn>", clear_widget)
    password_register.bind('<FocusOut>', repopulate_defaults)
    password_register.place(relx=0.25, rely=0.4, relheight=0.15, relwidth=0.5)

    password_conf_register = Entry(frame, font='Helvetica 18')
    password_conf_register.insert(0, 'Repeat Password')
    password_conf_register.bind("<FocusIn>", clear_widget)
    password_conf_register.bind('<FocusOut>', repopulate_defaults)
    password_conf_register.place(relx=0.25, rely=0.6, relheight=0.15, relwidth=0.5)

    button_sing_up = Button(frame, text='Sign Up', command=lambda: signup())
    button_sing_up.configure(font='Helvetica 18 bold', relief=RIDGE)
    button_sing_up.place(relx=0.25, rely=0.8, relheight=0.15, relwidth=0.5)

    button_back = Button(frame, text="Go Back!", relief=RIDGE, command=lambda: welcome())
    button_back.configure(font='Helvetica 10 bold')
    button_back.place(relx=0.9, rely=0.1, anchor=CENTER)

    def signup():
        nonlocal label_error
        error = ''

        if len(login_register.get()) == 0 or len(login_register.get()) <= 8:
            error = '*Login error. Must be less 8'
        elif login_register.get() in ranks:
            error = '*Login already exists'
        elif len(password_register.get()) < 6:
            error = '*Your Password needs to be at least 6 character'
        elif len(password_register.get()) > 14:
            error = '*Your password must be no more than 14 characters'
        elif not password_register.get() == password_conf_register.get():
            error = '*Password error'
        else:
            save()
        label_error = Label(frame, text=error, fg='red', font='Helvetica 11')
        label_error.place(relx=0.25, rely=0.1)
        label_error.after(2000, lambda: label_error.destroy())

    def save():
        users[login_register.get()] = password_register.get()
        with open('users.txt', 'wb') as file1:
            pickle.dump(users, file1)
        login_form()


def login_form():
    frame = Frame(gui)
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor='center')

    # noinspection PyUnusedLocal
    def clear_widget(event):
        if login_enter == frame.focus_get() and login_enter.get() == 'Enter Username':
            login_enter.delete(0, END)
        elif password_enter == password_enter.focus_get() and password_enter.get() == '     ':
            password_enter.delete(0, END)

    # noinspection PyUnusedLocal
    def repopulate_defaults(event):
        if login_enter != gui.focus_get() and login_enter.get() == '':
            login_enter.insert(0, 'Enter Username')
        elif password_enter != gui.focus_get() and password_enter.get() == '':
            password_enter.insert(0, '     ')

    login_enter = Entry(frame, font='Helvetica 18')
    login_enter.insert(0, 'Enter Username')
    login_enter.bind("<FocusIn>", clear_widget)
    login_enter.bind('<FocusOut>', repopulate_defaults)
    login_enter.place(relx=0.25, rely=0.2, relheight=0.15, relwidth=0.5)

    password_enter = Entry(frame, show='*', font='Helvetica 18')
    password_enter.insert(0, '     ')
    password_enter.bind("<FocusIn>", clear_widget)
    password_enter.bind('<FocusOut>', repopulate_defaults)
    password_enter.place(relx=0.25, rely=0.4, relheight=0.15, relwidth=0.5)

    button_sing_up = Button(frame, text='Sign Up', command=lambda: login_pass())
    button_sing_up.configure(font='Helvetica 18 bold', relief=RIDGE)
    button_sing_up.place(relx=0.25, rely=0.6, relheight=0.15, relwidth=0.5)

    button_back = Button(frame, text="Go Back!", relief=RIDGE, command=lambda: welcome())
    button_back.configure(font='Helvetica 10 bold')
    button_back.place(relx=0.9, rely=0.1, anchor=CENTER)

    def login_pass():
        global user
        error = ''

        if login_enter.get() in users and users[login_enter.get()] == password_enter.get():
            user = login_enter.get()
            rules()
        else:
            error = 'Login or Password error'

        label_error = Label(frame, text=error, fg='red', font='Helvetica 11')
        label_error.place(relx=0.25, rely=0.1)
        label_error.after(2000, lambda: label_error.destroy())


def guest():
    global user
    guest_number = 0
    user = "Guest"
    while user in ranks:
        user = "Guest"
        guest_number += 1
        user = user + str(guest_number)

    rules()


def rules():
    global user

    frame = Frame(gui)
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor='center')

    text_rules = Label(frame, text="""\n
    Welcome to Who Wants to be a Millionaire!
    Ok """ + user + """ this is how the game works:

    You are asked a multiple choice question, with options A, B, C and D.
    If you get the correct answer, you earn money and move to the next question.
    If you guess incorrectly then you lose the money you have earned, although there are checkpoints 
    along the way that allow you to keep a certain amount of money should you get a question wrong further on.

    The questions increase in difficulty as you progress but you can make use of the 3 'lifelines' we will give you:
    
    (50/50)   This allows you to cut the possible answers from 4,down to 2.\t\t\t         
    (Phone a Friend)   Place a call to a predetermined friend that will hopefully help you with an answer.  
    (Ask the Audience)   The audience will vote on the correct answer and we shall show you the results.
    
    One more thing, when answering, please use either A, B, C or D or you will be disqualified!
    """, font='Helvetica 10')
    text_rules.pack()

    button_ok = Button(frame, text="Ready to get started? Lets go!", command=lambda: game())
    button_ok.configure(font='Helvetica 10 bold')
    button_ok.place(relx=0.5, rely=0.7, anchor=CENTER)

    button_back = Button(frame, text="Go Back!", relief=RIDGE, command=lambda: welcome())
    button_back.configure(font='Helvetica 10 bold')
    button_back.place(relx=0.9, rely=0.1, anchor=CENTER)


def game():
    global i, a, b, c, d, e, f, correct, question, friend_answer

    frame = Frame(gui)
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor='center')

    questions = list(open("questions.txt"))
    questions = questions.pop(random.randint(0, len(questions) - 1))
    lines = questions.split('[')
    question = lines[0]
    answers = lines[1].split(',')

    a = answers[0]
    b = answers[1]
    c = answers[2]
    d = answers[3]
    correct = answers[4]
    e = answers[5]
    f = answers[6]
    friend_answer = answers[7]

    text_numb_question = 'Question:', i, "for", money[i - 1]
    text_numb_question = Label(frame, text=text_numb_question, font='Helvetica 18 bold')
    text_numb_question.pack()
    text_numb_question.place(relx=0.5, rely=0.1, anchor=CENTER)

    text_question = Label(frame, text=question, font='Helvetica 11 bold')
    text_question.pack()
    text_question.place(relx=0.5, rely=0.2, anchor=CENTER)

    button_a = Button(frame, text=a, height=2, width=20, command=lambda: answer_a())
    button_a.configure(font='Helvetica 11 bold', activebackground='grey')
    button_a.pack()
    button_a.place(relx=0.3, rely=0.5, anchor=CENTER)

    button_b = Button(frame, text=b, height=2, width=20, command=lambda: answer_b())
    button_b.configure(font='Helvetica 11 bold', activebackground='grey')
    button_b.pack()
    button_b.place(relx=0.3, rely=0.7, anchor=CENTER)

    button_c = Button(frame, text=c, height=2, width=20, command=lambda: answer_c())
    button_c.configure(font='Helvetica 11 bold', activebackground='grey')
    button_c.pack()
    button_c.place(relx=0.7, rely=0.5, anchor=CENTER)

    button_d = Button(frame, text=d, height=2, width=20, command=lambda: answer_d())
    button_d.configure(font='Helvetica 11 bold', activebackground='grey')
    button_d.pack()
    button_d.place(relx=0.7, rely=0.7, anchor=CENTER)

    if help1 == 1:
        button_fifty = Button(frame, text="50/50", width=8, command=lambda: fifty())
        button_fifty.configure(font='Helvetica 11 bold', activebackground='grey')
        button_fifty.pack()
        button_fifty.place(relx=0.3, rely=0.3, anchor=CENTER)
    if help2 == 1:
        button_friend = Button(frame, text="Friend", width=8, command=lambda: friend())
        button_friend.configure(font='Helvetica 11 bold', activebackground='grey')
        button_friend.pack()
        button_friend.place(relx=0.5, rely=0.3, anchor=CENTER)
    if help3 == 1:
        button_audience = Button(frame, text="Audience", width=8, command=lambda: audience())
        button_audience.configure(font='Helvetica 11 bold', activebackground='grey')
        button_audience.pack()
        button_audience.place(relx=0.7, rely=0.3, anchor=CENTER)

    i += 1


def answer_a():
    global select
    select = a
    correct_answer()


def answer_b():
    global select
    select = b
    correct_answer()


def answer_c():
    global select
    select = c
    correct_answer()


def answer_d():
    global select
    select = d
    correct_answer()


def answer_e():
    global select
    select = f
    correct_answer()


def answer_f():
    global select
    select = f
    correct_answer()


def correct_answer():
    if select == correct:
        game()
    elif i >= 16:
        game_over()
    else:
        save_rank()


def fifty():
    global help1

    frame = Frame(gui)
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor='center')

    text_numb_question = 'Question:', i - 1, "for", money[i - 2]
    text_numb_question = Label(frame, text=text_numb_question, font='Helvetica 18 bold')
    text_numb_question.pack()
    text_numb_question.place(relx=0.5, rely=0.1, anchor=CENTER)

    text_question = Label(frame, text=question, font='Helvetica 11 bold')
    text_question.pack()
    text_question.place(relx=0.5, rely=0.2, anchor=CENTER)

    button_e = Button(frame, text=e, height=2, width=20, command=lambda: answer_e())
    button_e.configure(font='Helvetica 11 bold', activebackground='grey')
    button_e.pack()
    button_e.place(relx=0.3, rely=0.5, anchor=CENTER)

    button_f = Button(frame, text=f, height=2, width=20, command=lambda: answer_f())
    button_f.configure(font='Helvetica 11 bold', activebackground='grey')
    button_f.pack()
    button_f.place(relx=0.7, rely=0.5, anchor=CENTER)

    text_50 = """
    We will select two answers to remove
    
    Leaving you with one correct and one incorrect answer
    """
    text_fifty = Label(frame, text=text_50, font='Helvetica 11 bold')
    text_fifty.pack()
    text_fifty.place(relx=0.5, rely=0.7, anchor=CENTER)

    help1 = 0


def friend():
    global help2

    frame = Frame(gui)
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor='center')

    text_numb_question = 'Question:', i - 1, "for", money[i - 2]
    text_numb_question = Label(frame, text=text_numb_question, font='Helvetica 18 bold')
    text_numb_question.pack()
    text_numb_question.place(relx=0.5, rely=0.1, anchor=CENTER)

    text_question = Label(frame, text=question, font='Helvetica 11 bold')
    text_question.pack()
    text_question.place(relx=0.5, rely=0.2, anchor=CENTER)

    button_a = Button(frame, text=a, height=2, width=20, command=lambda: answer_a())
    button_a.configure(font='Helvetica 11 bold', activebackground='grey')
    button_a.pack()
    button_a.place(relx=0.3, rely=0.5, anchor=CENTER)

    button_b = Button(frame, text=b, height=2, width=20, command=lambda: answer_b())
    button_b.configure(font='Helvetica 11 bold', activebackground='grey')
    button_b.pack()
    button_b.place(relx=0.3, rely=0.7, anchor=CENTER)

    button_c = Button(frame, text=c, height=2, width=20, command=lambda: answer_c())
    button_c.configure(font='Helvetica 11 bold', activebackground='grey')
    button_c.pack()
    button_c.place(relx=0.7, rely=0.5, anchor=CENTER)

    button_d = Button(frame, text=d, height=2, width=20, command=lambda: answer_d())
    button_d.configure(font='Helvetica 11 bold', activebackground='grey')
    button_d.pack()
    button_d.place(relx=0.7, rely=0.7, anchor=CENTER)

    text_friend = Label(frame, text=friend_answer, font='Helvetica 11 bold')
    text_friend.pack()
    text_friend.place(relx=0.5, rely=0.3, anchor=CENTER)

    help2 = 0


def audience():
    global help3

    frame = Frame(gui)
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor='center')

    text_numb_question = 'Question:', i - 1, "for", money[i - 2]
    text_numb_question = Label(frame, text=text_numb_question, font='Helvetica 18 bold')
    text_numb_question.pack()
    text_numb_question.place(relx=0.5, rely=0.1, anchor=CENTER)

    text_question = Label(frame, text=question, font='Helvetica 11 bold')
    text_question.pack()
    text_question.place(relx=0.5, rely=0.2, anchor=CENTER)

    button_a = Button(frame, text=a, height=2, width=20, command=lambda: answer_a())
    button_a.configure(font='Helvetica 11 bold', activebackground='grey')
    button_a.pack()
    button_a.place(relx=0.3, rely=0.5, anchor=CENTER)

    button_b = Button(frame, text=b, height=2, width=20, command=lambda: answer_b())
    button_b.configure(font='Helvetica 11 bold', activebackground='grey')
    button_b.pack()
    button_b.place(relx=0.3, rely=0.7, anchor=CENTER)

    button_c = Button(frame, text=c, height=2, width=20, command=lambda: answer_c())
    button_c.configure(font='Helvetica 11 bold', activebackground='grey')
    button_c.pack()
    button_c.place(relx=0.7, rely=0.5, anchor=CENTER)

    button_d = Button(frame, text=d, height=2, width=20, command=lambda: answer_d())
    button_d.configure(font='Helvetica 11 bold', activebackground='grey')
    button_d.pack()
    button_d.place(relx=0.7, rely=0.7, anchor=CENTER)

    aud = (random.choice(list(open('asktheaudience.txt'))))
    aud = aud.split(',')

    text_aud = """
    Our audience all have remotes and will vote on what they believe to be the right answer
    Please allow a couple of seconds for the audience to select their answers
    Hopefully you found that helpful"""
    text_audience = Label(frame, text=text_aud, font='Helvetica 11 bold')
    text_audience.pack()
    text_audience.place(relx=0.5, rely=0.3, anchor=CENTER)

    text_aud1 = aud[0] + "   " + aud[1] + "\n\n\n\n\n" + aud[2] + "   " + aud[3]
    text_audience1 = Label(frame, text=text_aud1, font='Helvetica 11 bold')
    text_audience1.pack()
    text_audience1.place(relx=0.5, rely=0.62, anchor=CENTER)

    help3 = 0


def save_rank():
    global ranks
    ranks[user] = money[i - 2]
    with open('ranks.txt', 'wb') as file_ranks1:
        pickle.dump(ranks, file_ranks1)
    game_over()


def game_over():
    global ranks

    frame = Frame(gui)
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor='center')

    ranks = {k: v for k, v in sorted(ranks.items(), key=lambda item: item[1])}

    dict_list = []

    for key, value in ranks.items():
        dict_list.append([key, value])

    label_ranks_name = Label(frame, text="TOP 15 Player", font='Helvetica 18 bold')
    label_ranks_name.pack()
    label_ranks_name.place(relx=0.5, rely=0.1, anchor=CENTER)

    top1 = dict_list[-1]
    top2 = dict_list[-2]
    top3 = dict_list[-3]
    top4 = dict_list[-4]
    top5 = dict_list[-5]
    top6 = dict_list[-6]
    top7 = dict_list[-7]
    top8 = dict_list[-8]
    top9 = dict_list[-9]
    top10 = dict_list[-10]
    top11 = dict_list[-11]
    top12 = dict_list[-12]
    top13 = dict_list[-13]
    top14 = dict_list[-14]
    top15 = dict_list[-15]

    text_ranks_name = """
    """ + top1[0] + """
    """ + top2[0] + """
    """ + top3[0] + """
    """ + top4[0] + """
    """ + top5[0] + """
    """ + top6[0] + """
    """ + top7[0] + """
    """ + top8[0] + """
    """ + top9[0] + """
    """ + top10[0] + """
    """ + top11[0] + """
    """ + top12[0] + """
    """ + top13[0] + """
    """ + top14[0] + """
    """ + top15[0] + """
    """
    label_ranks_name = Label(frame, text=text_ranks_name, font='Helvetica 14')
    label_ranks_name.pack()
    label_ranks_name.place(relx=0.35, rely=0.6, anchor=CENTER)

    text_ranks_money = """
    """ + str(top1[1]) + """$
    """ + str(top2[1]) + """$
    """ + str(top3[1]) + """$
    """ + str(top4[1]) + """$
    """ + str(top5[1]) + """$
    """ + str(top6[1]) + """$
    """ + str(top7[1]) + """$
    """ + str(top8[1]) + """$
    """ + str(top9[1]) + """$
    """ + str(top10[1]) + """$
    """ + str(top11[1]) + """$
    """ + str(top12[1]) + """$
    """ + str(top13[1]) + """$
    """ + str(top14[1]) + """$
    """ + str(top15[1]) + """$
    """
    label_ranks_money = Label(frame, text=text_ranks_money, font='Helvetica 14')
    label_ranks_money.pack()
    label_ranks_money.place(relx=0.6, rely=0.6, anchor=CENTER)

    button_again = Button(frame, text="PLAY AGAIN", font='Helvetica 12 bold', command=lambda: restart())
    button_again.pack()
    button_again.place(relx=0.9, rely=0.1, anchor=CENTER)


def restart():
    global i, help1, help2, help3
    i = help1 = help2 = help3 = 1
    rules()


welcome()
gui.mainloop()
