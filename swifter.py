import sqlite3
import webbrowser
import textwrap
from datetime import datetime
from tkinter import messagebox
from tkinter import *


def createconnection():  # เชื่อมsource code กับ data base
    global conn, cursor
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()


def mainwindow():
    root = Tk()
    w = 1000
    h = 600
    # การปรับขนาดโปรมแกรมให้ขนาดเท่ากับจอผู้ใช้
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))  # แทนค่า
    root.config(bg='#ffffff')
    root.title("Swifter ")
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=10)
    root.columnconfigure(0, weight=6)
    root.columnconfigure(1, weight=1)
    root.iconbitmap("pic/Taylor3.ico")  # ใส่ไอคอนข้างๆ title
    root.resizable(width=FALSE, height=FALSE)
    return root


def taylor():  # เสร็จแล้ว
    tayframe = Frame(root)
    tayframe.grid(row=0, column=0, columnspan=2, sticky="news", rowspan=2)
    tayframe.rowconfigure(0, weight=1)
    tayframe.columnconfigure((0, 1), weight=1)
    tayframe.after(3000, lambda: tayframe.destroy())
    Label(tayframe, image=img43).grid(
        row=0, column=0, sticky="new", columnspan=2)
    Label(tayframe, text="     SWIFTER", fg="#e74fa8", font="Garamond 35 bold").grid(
        row=0, columnspan=2, sticky="s", pady=50)


def loginlayout():
    global userEntry, pwdentry, loginframe
    userinfo = StringVar()
    pwdinfo = StringVar()

    # Left side

    loginframe = Frame(root, bg='#ffffff')
    loginframe.rowconfigure((0, 1, 2, 3), weight=1)
    loginframe.columnconfigure((0, 1, 2), weight=1)
    loginframe.grid(row=0, column=0, sticky="news", rowspan=2)

    Label(loginframe, text="Login ", font="Garamond 35 bold", bg='#ffffff',
          fg='#7149C6').grid(row=0, rowspan=2, column=0, columnspan=2)
    Label(loginframe, text="Username : ", bg='#ffffff',
          fg='#7149C6', font="inter  13  ").grid(row=1, column=0, sticky="se", padx=50)
    userEntry = Entry(loginframe, bg='#FFB4B4', fg='#7149C6',
                      width=20, textvariable=userinfo, font="inter  10  ")
    userEntry.grid(row=1, column=1, sticky="sw", ipady=4)
    Label(loginframe, text="Password : ", bg='#ffffff',
          fg='#7149C6', font="inter  13  ").grid(row=2, column=0, sticky="e", padx=50)
    pwdentry = Entry(loginframe, bg='#FFB4B4', fg='#7149C6', width=20,
                     show='*', textvariable=pwdinfo, font="inter  10  ")
    pwdentry.grid(row=2, column=1, sticky="w", ipady=4)
    Button(loginframe, image=img3, border=0, bg="#ffffff", command=lambda: signinclick(userinfo.get(), pwdinfo.get())).place(x=180,y=450)

    # Right side

    signupframe = Frame(root, bg="#FFB4B4")
    signupframe.rowconfigure((0, 1, 2, 3), weight=1)
    signupframe.columnconfigure(0, weight=1)
    signupframe.grid(row=0, column=1, sticky="news", rowspan=2)
    Label(signupframe, text="New Here?", bg="#FFB4B4", fg="#ffffff",
          font="Garamond 35 bold").grid(row=0, rowspan=2, sticky="s")
    Label(signupframe, text="Sign up and make your day special \nwith everything like a gift from Taylor Swift",
          bg="#FFB4B4", fg="#ffffff", font="Garamond 15 bold").grid(row=2, pady=50)
    Button(signupframe, image=img5, border=0, bg="#FFB4B4", activebackground="#FFB4B4", command=lambda: [signuplayout(), initial()]).grid(
        row=2, sticky="s")
    Label(signupframe, image=img6, bg="#FFB4B4",
          width=10, height=135).grid(row=3, sticky="ews")


def signinclick(user, pwd):
    if user == "" or pwd == "":
        messagebox.showwarning(
            "Swifter:", "Please enter  username and password.")
        userEntry.focus_force()
    else:
        sql = "select * from login where user=?"
        cursor.execute(sql, [user])
        result = cursor.fetchall()
        if result:
            sql = "select * from login where user=? and pwd=? "
            cursor.execute(sql, [user, pwd])
            result = cursor.fetchone()
            if result:
                messagebox.showinfo("Swifter:", "sign in Successfully")
                loginframe.grid_forget()
                homepage(result)
            else:
                messagebox.showwarning("Swifter:", "Incorrect Password")
                pwdentry.select_range(0, END)
                pwdentry.focus_force()
        else:
            messagebox.showerror(
                "Swifter:", "The username not found\n Please sign up before sign in")
            userEntry.select_range(0, END)
            userEntry.focus_force()


def signuplayout():  # เหลือ hideoutframe ทำรูปและทำให้เชื่อมต่อกัน

    global leftframe, hideout1, fnEntry, lnEntry, eaEntry, newUEntry, newpwdEntry, cfpwdEntry
    fnameinfo = StringVar()
    lnameinfo = StringVar()
    emailinfo = StringVar()
    newuserinfo = StringVar()
    newpwdinfo = StringVar()
    cfpwdinfo = StringVar()

    signuprightframe = Frame(root, bg="#ffffff")
    signuprightframe.rowconfigure(
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)
    signuprightframe.columnconfigure((0, 1), weight=1)
    signuprightframe.grid(row=0, column=1, columnspan=4,
                          sticky="news", rowspan=2)

    Label(signuprightframe, text="Sign up", font="Garamond 35 bold",
          bg="#ffffff", fg="#7149C6").grid(row=0, column=0, columnspan=2)

    for i in range(len(forsignup)):
        Label(signuprightframe, text=forsignup[i], bg="#ffffff", fg="#7149C6", font="inter 10 ").grid(
            row=i+1, column=0, sticky="e", padx=30)

    fnEntry = Entry(signuprightframe, bg='#FEFAE0', fg='#7149C6',
                    width=15, textvariable=fnameinfo, font="inter  10  ")
    fnEntry.grid(row=1, column=1, sticky="w")
    lnEntry = Entry(signuprightframe, bg='#FEFAE0', fg='#7149C6',
                    width=15, textvariable=lnameinfo, font="inter  10  ")
    lnEntry.grid(row=2, column=1, sticky="w")
    eaEntry = Entry(signuprightframe, bg='#FEFAE0', fg='#7149C6',
                    width=15, textvariable=emailinfo, font="inter  10  ")
    eaEntry.grid(row=3, column=1, sticky="w")
    newUEntry = Entry(signuprightframe, bg='#FEFAE0', fg='#7149C6',
                      width=15, textvariable=newuserinfo, font="inter  10  ")
    newUEntry.grid(row=4, column=1, sticky="w")
    newpwdEntry = Entry(signuprightframe, bg='#FEFAE0', fg='#7149C6',
                        width=15, textvariable=newpwdinfo, font="inter  10  ", show='*')
    newpwdEntry.grid(row=5, column=1, sticky="w")
    cfpwdEntry = Entry(signuprightframe, bg='#FEFAE0', fg='#7149C6',
                       width=15, textvariable=cfpwdinfo, font="inter  10  ", show='*')
    cfpwdEntry.grid(row=6, column=1, sticky="w")
    Button(signuprightframe, image=img1, border=0, bg="#ffffff", activebackground="#ffffff", command=loginlayout).grid(
        row=7, rowspan=2, column=0)
    Button(signuprightframe, image=img2, border=0, bg="#ffffff", activebackground="#ffffff", command=signupclick).grid(
        row=7, rowspan=2, column=1)

    if __name__ == '__main__':
        leftframe = Frame(root, bg="red")
        leftframe.grid(row=0, column=0, rowspan=10, sticky="news")
        Label(leftframe, image=img42).place(x=0, y=0)

        hideout1 = Frame(leftframe, background='#7149C6',
                         width=2500, height=690)
        hideout1.place(x=0, y=0, width=2500, height=690)
        Label(hideout1, image=img7, height=640, bg="#7149C6").place(x=0, y=0)


def initial(t=0):  # เหลือทำให้เป็น loop
    hideout1.place(x=t, y=0)
    if t > 360:
        return
    leftframe.after(6, initial, t-1)


def signupclick():  # เสร็จแล้ว
    if fnEntry.get() == "":
        messagebox.showwarning("Swifter: ", "Please enter a firstname")
        fnEntry.focus_force()
    elif lnEntry.get() == "":
        messagebox.showwarning("Swifter : ", "Please enter a fullname")
        lnEntry.focus_force
    elif eaEntry.get() == "":
        messagebox.showwarning("Swifter : ", "Please enter an Email")
        eaEntry.focus_force
    elif newUEntry.get() == "":
        messagebox.showwarning("Swifter : ", "Please enter a username")
        newUEntry.focus_force
    elif newpwdEntry.get() == "":
        messagebox.showwarning("Swifter : ", "Please enter a password")
        newpwdEntry.focus_force
    elif cfpwdEntry.get() == "":
        messagebox.showwarning("Swifter : ", "Please enter a confirm password")
        cfpwdEntry.focus_force
    else:  # check a username is already exist???
        sql = "select * from login where user=?; "
        # execute sql query
        cursor.execute(sql, [newUEntry.get()])
        result = cursor.fetchone()  # fetch a result
        if result:
            messagebox.showerror(
                "Swifter:", "The username is already exists\n Try again")
            newUEntry.selection_range(0, END)
            newUEntry.focus_force()
        else:
            if newpwdEntry.get() == cfpwdEntry.get():  # verify a new pwd and confirm pwd are equal
                # insert into statement
                sql = "insert into login values (?,?,?,?,?);"
                # execute sql query
                cursor.execute(sql, [newUEntry.get(), newpwdEntry.get(
                ), fnEntry.get(), lnEntry.get(), eaEntry.get()])
                conn.commit()
                messagebox.showinfo("Swifter:", "Sign up Successfully")
            else:  # verify a new pwd and confirm pwd are not equal
                messagebox.showwarning(
                    "Admin: ", "Incorrect a confirm password\n Try again")
                cfpwdEntry.selection_range(0, END)
                cfpwdEntry.focus_force()


def homepage(result):
    global chatframe, chatbox, SendButton, Placeholder, ChatLog, homepageframe, homeframe, taylorframe
    # Left side
    homepageframe = Frame(root, bg='#ffffff')
    homepageframe.rowconfigure(0, weight=1)
    homepageframe.columnconfigure(0, weight=1)
    homepageframe.grid(row=1, column=0, sticky='news', rowspan=2)

    topframe = Frame(root, bg="#AD7BE9")
    topframe.rowconfigure(0, weight=1)
    topframe.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
    topframe.grid(row=0, column=0, sticky="news")

    homeframe = Frame(homepageframe, bg="red")
    homeframe.columnconfigure(0, weight=1)
    homeframe.rowconfigure(0, weight=1)
    homeframe.grid(sticky="news")

    # button inside homepage
    Button(topframe, text="Home", border=0, bg="#AD7BE9", fg="#ffffff", font='inter 12 bold', command=home).grid(
        row=0, column=0, sticky="e", padx=5)
    Button(topframe, text="Taylor Swift", border=0, bg="#AD7BE9", fg="#ffffff", font='inter 12 bold', command=TaylorSwift).grid(
        row=0, column=1, sticky="w")
    Button(topframe, text="Photogallery", border=0, bg="#AD7BE9", fg="#ffffff", font='inter 12 bold', command=photogallery).grid(
        row=0, column=2, sticky="w")
    Button(topframe, text="Merchandise", border=0, bg="#AD7BE9", fg="#ffffff", font='inter 12 bold', command=Merchandise).grid(
        row=0, column=3, sticky="w")
    home()

    # Right side
    chatframe = Frame(root, bg='#FFB4B4')
    chatframe.rowconfigure((0, 1, 2, 3), weight=1)
    chatframe.columnconfigure((0, 1), weight=1)
    chatframe.grid(row=0, column=1, sticky='news', rowspan=2)
    ChatLog = Text(chatframe, bd=0, height="8", width="50",
                   font="Helvetica", wrap="word")
    topchatframe = Frame(chatframe, bg="#7149C6")
    ChatLog.config(state=NORMAL)
    ChatLog.tag_config("right", justify="right")
    ChatLog.tag_config("small", font=("Helvetica", 7))
    ChatLog.tag_config("colour", foreground="#333333")
    ChatLog.insert(END, current_time, ("small", "colour"))
    ChatLog.window_create(END, window=Label(ChatLog, fg="#000000",
                                            wraplength=200, font=("Arial", 10), bg="#DDDDDD", bd=4, text="It's me \nHi, I'm Taylor Swift ", justify="left"))
    ChatLog.insert(END, '\n')
    ChatLog.config(state=DISABLED)

    # Bind scrollbar to Chat window
    scrollbar = Scrollbar(
        chatframe, command=ChatLog.yview, cursor="double_arrow")
    ChatLog['yscrollcommand'] = scrollbar.set

    # Create Button to send message
    SendButton = Button(chatframe, image=img10, width="8", height=5,
                        bd=0, fg="#7149C6", activebackground="#7149C6", bg="#7149C6", command=send_by_button)

    # Create the box to enter message
    chatbox = Text(chatframe, bd=0, fg="#000000", bg="#7149C6", highlightcolor="#750216",
                   width="29", height="5", font=("Arial", 10), wrap="word", padx=5)

    # Placeholder config and text:
    Placeholder = Text(chatframe, bd=0, fg="#ffffff", bg="#7149C6", highlightcolor="#750216",
                       width="29", height="5", font=("Arial", 10), wrap="word", padx=5)
    Placeholder.insert("1.0", "\n  Enter a message")

    # Header for chatbot
    Label(topchatframe, text="Taylor Swift [BOT]", image=img9, fg="#000000", compound=TOP).place(
        x=5, y=5, height=50, width=386)
    # Place all components on the screen
    scrollbar.place(x=382, y=66, height=480, width=20)
    ChatLog.place(x=6, y=66, height=480, width=376)
    chatbox.place(x=6, y=545, height=50, width=350)
    SendButton.place(x=355, y=545, height=50, width=47)
    Placeholder.place(x=9, y=545, height=50, width=276)
    topchatframe.place(x=6, y=6, height=60, width=396)
    Placeholder.bind("<FocusIn>", deletePlaceholder)
    chatbox.bind("<FocusOut>", addPlaceholder)


def home():
    global canvas
    # Create a Canvas widget to support scrolling
    canvas = Canvas(homeframe, bg="#ffffff")
    canvas.grid(row=0, column=0, sticky="news")

    # Add image and label to the canvas
    canvas.create_image(0, 0, image=img11, anchor=NW)
    canvas.create_image(50, 290, image=img12, anchor=NW)
    canvas.create_text(40, 650, text="The last night in Houston was the thirteenth \nstop of The Eras Tour! Taylor chose two \nbeautiful songs for her acoustic set, \nBegin Again and Cold As You. photos of \nboth performances are below. \nSee you in Atlanta! BEGIN AGAIN \nBESTIES #HoustonTSTheErasTour…", fill="#7d7d7d", font="inter 8 bold", anchor=NW)
    canvas.create_image(340, 290, image=img12, anchor=NW)
    canvas.create_text(330, 650, text="Last night’s Houston crowd was in a \nfairytale as Taylor performed Today Was \nA Fairytale for the first time in \nten years. The other surprise song \nwas A Place In This World from her debut \nalbum. Watch the photos below to see \nsnippets of both amazing performances! …", fill="#7d7d7d", font="inter 8 bold", anchor=NW)
    canvas.create_image(50, 790, image=img12, anchor=NW)
    canvas.create_text(45, 1120, text="Last night was the first of three \nEras Shows in the NRG Stadium in Houston, \nTexas! Taylor surprised the crowd with \nWonderland and the first performance of \nYou’re Not Sorry since 2013. Both were \nincredible and can check out photos below. \nPhotos from the show are in the gallery. \nWONDERLAND!!! #HoustonTSTheErasTour …", fill="#7d7d7d", font="inter 8 bold", anchor=NW)
    canvas.create_image(260, 930, image=img13, anchor=NW)
    canvas.create_text(300, 1145, text="Today is Record Store Day! This means \nFolklore: The Long Pond Studio Sessions \nis out on vinyl! There will only be 115,000 copies \navailable worldwide. You can find a list of \nparticipating stores here, good luck! get ready \nto return to the folklorian forest with \n‘folklore: the long pond studio sessions’ …", fill="#7d7d7d", font="inter 8 bold", anchor=NW)
    canvas.create_image(5, 1350, image=img25, anchor=NW)
    canvas.create_text(15, 1530, text="Taylor claims a new record as the first artist \nto have an exclusive release enter the Top 10 \nof Billboard 200 Albums Chart. Her Record \nStore Day 2023 Album folklore: the long pond \nstudio sessions debuted at #3 on the Billboard \nchart! Thanks to a towering debut by “Folklore: \nThe Long Pond Studio Sessions,” Taylor …", fill="#7d7d7d", font="inter 8 bold", anchor=NW)
    canvas.create_image(280, 1340, image=img26, anchor=NW)
    canvas.create_text(280, 1500, text="Taylor’s beloved third album, Speak Now, a self \nwritten album full of Taylor’s deepest emotions \nis the next album to be re-released! Taylor made \nthe announcement to a sold out crowd in Nashville \nlast night during The Eras Tour. All formats of the \nalbum, including a violet vinyl, will be available on \nJuly 7! You can preorder it now and stay tuned \nfor more news.“I think rather than me speaking \nabout it,” she said, to screams, as fans realized…", fill="#7d7d7d", font="inter 8 bold", anchor=NW)

    # Create a frame on the canvas to contain the buttons.
    buttons1_frame = Frame(canvas, bg="#fff", height=45, width=600,)
    buttons1_frame.place(x=0, y=500)
    buttons2_frame = Frame(canvas, bg="#fff", height=29, width=600,)
    buttons2_frame.place(x=0, y=500)
    buttons3_frame = Frame(canvas, bg="#fff", height=45, width=600,)
    buttons3_frame.place(x=0, y=500)
    buttons4_frame = Frame(canvas, bg="#fff", height=45, width=600,)
    buttons4_frame.place(x=0, y=500)
    buttons5_frame = Frame(canvas, bg="#fff", height=65, width=600,)
    buttons5_frame.place(x=0, y=500)
    buttons6_frame = Frame(canvas, bg="#fff", height=29, width=600,)
    buttons6_frame.place(x=0, y=500)

    # Add the buttons_frame to the canvas
    canvas.create_window((40, 600), window=buttons1_frame, anchor=NW)
    canvas.create_window((40, 750), window=buttons2_frame, anchor=NW)
    canvas.create_window((40, 1100), window=buttons3_frame, anchor=NW)
    canvas.create_window((40, 1245), window=buttons4_frame, anchor=NW)
    canvas.create_window((0, 1460), window=buttons5_frame, anchor=NW)
    canvas.create_window((25, 1630), window=buttons6_frame, anchor=NW)

    # Add a button to the buttons_frame using place method
    Button(buttons1_frame, text="The Eras Tour: Houston, \nTexas (Night 3)",
           border=0, font="inter 13 bold ", cursor="hand2", command=taxas3click, bg="#fff").place(x=0, y=0)
    Button(buttons2_frame, text="CONTINUE READING →",
           border=0, font="inter 11 bold ", cursor="hand2", command=taxas3click, bg="#fff").place(x=0, y=0)
    Button(buttons1_frame, text="The Eras Tour: Houston, \nTexas (Night 2)",
           border=0, font="inter 13 bold ", cursor="hand2", bg="#fff", command=taxas2click).place(x=290, y=0)
    Button(buttons2_frame, text="CONTINUE READING →",
           border=0, font="inter 11 bold ", cursor="hand2", bg="#fff", command=taxas2click).place(x=290, y=0)
    Button(buttons3_frame, text="The Eras Tour: Houston, \nTexas (Night 1)",
           border=0, font="inter 13 bold ", cursor="hand2", bg="#fff", command=taxas1click).place(x=0, y=0)
    Button(buttons4_frame, text="CONTINUE READING →",
           border=0, font="inter 11 bold ", cursor="hand2", bg="#fff", command=taxas1click).place(x=0, y=0)
    Button(buttons3_frame, text="‘Folklore: The Long Pond \nNow Available On Vinyl",
           border=0, font="inter 12 bold ", cursor="hand2", bg="#fff", command=Folkloreclick).place(x=280, y=0)
    Button(buttons4_frame, text="CONTINUE READING →",
           border=0, font="inter 11 bold ", cursor="hand2", bg="#fff", command=Folkloreclick).place(x=290, y=0)
    Button(buttons5_frame, text="‘Folklore: The Long Pond Studio \nSessions’ Debuts At #3 On The \nBillboard 200 Albums Charts",
           border=0, font="inter 13 bold ", cursor="hand2", bg="#fff", command=billbordclick).place(x=0, y=0)
    Button(buttons6_frame, text="CONTINUE READING →",
           border=0, font="inter 11 bold ", cursor="hand2", bg="#fff", command=billbordclick).place(x=0, y=0)
    Button(buttons5_frame, text="Taylor Announces ‘Speak Now \n(Taylor’s Version)’ Is Coming in July \nDuring The Eras Tour in Nashville",
           border=0, font="inter 12 bold ", cursor="hand2", bg="#fff", command=SpeakNowclick).place(x=280, y=0)
    Button(buttons6_frame, text="CONTINUE READING →",
           border=0, font="inter 11 bold ", cursor="hand2", bg="#fff", command=SpeakNowclick).place(x=270, y=0)

    # Configure the scrollbar
    homescroll = Scrollbar(homeframe, orient=VERTICAL,
                           command=canvas.yview, cursor="double_arrow")
    homescroll.place(x=565, y=0, height=520, width=28)

    # Set the scrollbar to scroll the canvas
    canvas.configure(yscrollcommand=homescroll.set)

    # Set the scroll region of the canvas
    canvas.configure(scrollregion=canvas.bbox("all"))


def taxas3click():
    global taxas3canvas
    canvas.grid_forget()
    taxas3canvas = Canvas(homeframe, bg="#fff")
    taxas3canvas.grid(row=0, column=0, sticky="news")
    taxas3canvas.create_image(200, 50, image=img12, anchor=NW)
    taxas3canvas.create_text(0, 370, text="The Eras Tour: Houston, Texas (Night 3)",
                             fill="#000", font="inter 18 bold", anchor=NW)
    taxas3canvas.create_text(5, 420, text="The last night in Houston was the thirteenth stop of The Eras Tour! Taylor chose \ntwo beautiful songs for her acoustic set, Begin Again and Cold As You. photos \nof both performances are below. See you in Atlanta!", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    taxas3canvas.create_image(80, 500, image=img14, anchor=NW)
    taxas3canvas.create_text(
        85, 750, text="Begin Again. ", fill="#7d7d7d", font="inter 10 ", anchor=NW)
    taxas3canvas.create_text(160, 750, text="Photo by Jack Gorman ",
                             fill="#7d7d7d", font="inter 10 bold", anchor=NW)
    taxas3canvas.create_image(80, 780, image=img15, anchor=NW)
    taxas3canvas.create_text(82, 1030, text="You're saying I need tickets to the gun show. ",
                             fill="#7d7d7d", font="inter 10 ", anchor=NW)
    taxas3canvas.create_text(343, 1030, text="Photo by Jack Gorman ",
                             fill="#7d7d7d", font="inter 10 bold", anchor=NW)
    taxas3canvas.create_image(80, 1060, image=img16, anchor=NW)
    taxas3canvas.create_text(
        82, 1310, text="Cold As You. ", fill="#7d7d7d", font="inter 10 ", anchor=NW)
    taxas3canvas.create_text(160, 1310, text="Photo by Jack Gorman ",
                             fill="#7d7d7d", font="inter 10 bold", anchor=NW)

    # Configure the scrollbar
    taxas3scroll = Scrollbar(
        homeframe, command=taxas3canvas.yview, cursor="double_arrow")
    taxas3scroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    taxas3canvas.configure(yscrollcommand=taxas3scroll.set)

    # Set the scroll region of the canvas
    taxas3canvas.configure(scrollregion=taxas3canvas.bbox("all"))


def taxas2click():
    global taxas2canvas
    canvas.grid_forget()
    taxas2canvas = Canvas(homeframe, bg="#fff")
    taxas2canvas.grid(row=0, column=0, sticky="news")
    taxas2canvas.create_image(200, 50, image=img12, anchor=NW)
    taxas2canvas.create_text(0, 370, text="The Eras Tour: Houston, Texas (Night 2)",
                             fill="#000", font="inter 18 bold", anchor=NW)
    taxas2canvas.create_text(5, 410, text="Last night’s Houston crowd was in a fairytale as Taylor performed Today Was A \nFairytale for the first time in ten years. The other surprise song was A Place \nIn This World from her debut album. Watch the photos below to see snippets of \nboth amazing performances!", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    taxas2canvas.create_image(80, 500, image=img17, anchor=NW)
    taxas2canvas.create_text(
        78, 750, text="Everybody moved on But I stayed there. ", fill="#7d7d7d", font="inter 10 ", anchor=NW)
    taxas2canvas.create_text(305, 750, text="Photo by @the_rodeoclown ",
                             fill="#7d7d7d", font="inter 10 bold", anchor=NW)
    taxas2canvas.create_image(190, 780, image=img18, anchor=NW)
    taxas2canvas.create_text(82, 1030, text="surprise song is  “High Infidelity” ",
                             fill="#7d7d7d", font="inter 10 ", anchor=NW)
    taxas2canvas.create_text(270, 1030, text="Photo by Josh Purcell ",
                             fill="#7d7d7d", font="inter 10 bold", anchor=NW)
    taxas2canvas.create_image(80, 1060, image=img19, anchor=NW)
    taxas2canvas.create_text(
        82, 1310, text="Shot from section Section 538 ", fill="#7d7d7d", font="inter 10 ", anchor=NW)
    taxas2canvas.create_text(260, 1310, text="Photo by @BMChaney ",
                             fill="#7d7d7d", font="inter 10 bold", anchor=NW)

    # Configure the scrollbar
    taxas2scroll = Scrollbar(
        homeframe, command=taxas2canvas.yview, cursor="double_arrow")
    taxas2scroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    taxas2canvas.configure(yscrollcommand=taxas2scroll.set)

    # Set the scroll region of the canvas
    taxas2canvas.configure(scrollregion=taxas2canvas.bbox("all"))


def taxas1click():
    global taxas1canvas
    canvas.grid_forget()
    taxas1canvas = Canvas(homeframe, bg="#fff")
    taxas1canvas.grid(row=0, column=0, sticky="news")
    taxas1canvas.create_image(200, 50, image=img12, anchor=NW)
    taxas1canvas.create_text(0, 370, text="The Eras Tour: Houston, Texas (Night 1)",
                             fill="#000", font="inter 18 bold", anchor=NW)
    taxas1canvas.create_text(5, 410, text="Last night, The Eras Tour took over AT&T Stadium for Arlington Night 1! Taylor \nperformed Sad Beautiful Tragic and Ours as the surprise songs! She also sang \nThe 1 instead of Invisible String. Check out photos from the concert in our gallery!", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    taxas1canvas.create_image(80, 500, image=img20, anchor=NW)
    taxas1canvas.create_text(
        78, 755, text="The 1", fill="#7d7d7d", font="inter 10 ", anchor=NW)
    taxas1canvas.create_text(120, 755, text="Photo by Kristin Robinson ",
                             fill="#7d7d7d", font="inter 10 bold", anchor=NW)
    taxas1canvas.create_image(80, 780, image=img21, anchor=NW)
    taxas1canvas.create_text(82, 1030, text="T. Swift is an icon ",
                             fill="#7d7d7d", font="inter 10 ", anchor=NW)
    taxas1canvas.create_text(190, 1030, text="Photo by Dallas Observer",
                             fill="#7d7d7d", font="inter 10 bold", anchor=NW)
    taxas1canvas.create_image(80, 1060, image=img22, anchor=NW)
    taxas1canvas.create_text(
        82, 1335, text="A clock announced Swift's impeding arrival.", fill="#7d7d7d", font="inter 10 ", anchor=NW)
    taxas1canvas.create_text(330, 1335, text="Photo by Natalie Perez ",
                             fill="#7d7d7d", font="inter 10 bold", anchor=NW)

    # Configure the scrollbar
    taxas1scroll = Scrollbar(
        homeframe, command=taxas1canvas.yview, cursor="double_arrow")
    taxas1scroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    taxas1canvas.configure(yscrollcommand=taxas1scroll.set)

    # Set the scroll region of the canvas
    taxas1canvas.configure(scrollregion=taxas1canvas.bbox("all"))


def Folkloreclick():
    global Folklorecanvas
    canvas.grid_forget()
    Folklorecanvas = Canvas(homeframe, bg="#fff")
    Folklorecanvas.grid(row=0, column=0, sticky="news")
    Folklorecanvas.create_image(0, 70, image=img23, anchor=NW)
    Folklorecanvas.create_text(0, 370, text="Taylor To Release Vinyl Pressing Of ‘Folklore: \nThe Long Pond Studio Sessions’ For 2023 \nRecord Store Day",
                               fill="#000", font="inter 18 bold", anchor=NW)
    Folklorecanvas.create_text(5, 460, text="Record Store Day is quickly approaching and Taylor Swift, 2022’s Record Store \nDay Global Ambassador, is dropping another special edition record! This vinyl \nwill be the first and only edition of folklore: the long pond studio session. \nIt will become available on April 22 with limited quantities. This vinyl will \nbe grey and feature the tracklist below. Good luck to all those trying to get a copy!", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Folklorecanvas.create_text(5, 580, text="DISC 1\nSIDE A\n1. the 1 – the long pond studio sessions\n2. cardigan – the long pond studio sessions\n3. the last great american dynasty – the long pond studio sessions\n4. exile – the long pond studio sessions feat. Bon Iver", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Folklorecanvas.create_text(5, 730, text="DISC 1\nSIDE B\n1. my tears ricochet – the long pond studio sessions\n2. mirrorball – the long pond studio sessions\n3. seven – the long pond studio sessions\n4. august – the long pond studio sessions\n5. this is me trying – the long pond studio sessions", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Folklorecanvas.create_text(5, 890, text="DISC 2\nSIDE A\n1.illicit affairs – the long pond studio sessions\n2. invisible string – the long pond studio sessions\n3. mad woman – the long pond studio sessions\n4. epiphany – the long pond studio sessions", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Folklorecanvas.create_text(
        5, 1030, text="DISC 2\nSIDE B\n1.betty – the long pond studio sessions\n2. peace – the long pond studio sessions\n3. hoax – the long pond studio sessions\n4. the lakes – the long pond studio sessions", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Folklorecanvas.create_image(80, 1180, image=img24, anchor=NW)

    # Configure the scrollbar
    Folklorescroll = Scrollbar(
        homeframe, command=Folklorecanvas.yview, cursor="double_arrow")
    Folklorescroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    Folklorecanvas.configure(yscrollcommand=Folklorescroll.set)

    # Set the scroll region of the canvas
    Folklorecanvas.configure(scrollregion=Folklorecanvas.bbox("all"))


def billbordclick():
    global billbordcanvas
    canvas.grid_forget()
    billbordcanvas = Canvas(homeframe, bg="#fff")
    billbordcanvas.grid(row=0, column=0, sticky="news")
    billbordcanvas.create_image(0, 70, image=img27, anchor=NW)
    billbordcanvas.create_text(0, 370, text="‘Folklore: The Long Pond Studio Sessions’ Debuts \nAt #3 On The Billboard 200 Albums Charts",
                               fill="#000", font="inter 17 bold", anchor=NW, justify=LEFT)
    billbordcanvas.create_text(5, 460, text="Taylor claims a new record as the first artist to have an exclusive release enter \nthe Top 10 of Billboard 200 Albums Chart. Her Record Store Day 2023 Album \nfolklore: the long pond studio sessions debuted at #3 on the Billboard chart!", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    billbordcanvas.create_text(20, 540, text="Thanks to a towering debut by “Folklore: The Long Pond Studio Sessions,” \nTaylor Swift now has three albums in the top 10 of the Billboard 200, as the \nvinyl-only Record Store Day exclusive sold through all 75,000 of the available \ncopies to land at No. 3 for the week. The double-LP release joins two other \nalbums Swift already had in the top 10 as of last week: “Midnights,” at No. 4, \nand “Folklore,” at No. 10.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    billbordcanvas.create_text(20, 670, text="Swift becomes the first artist to pull off that feat since 2016, when three of \nPrince’s landed in the top 10 following his death, according to Billboard. \nIt’s also a rare feat for a female artist; Whitney Houston became the first \nwoman to score three albums in the top 10 in 2012.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    billbordcanvas.create_text(20, 770, text="One thing is for certain: Swift won’t be scoring a three-peat on next week’s \nBillboard charts. “Folklore: The Long Pond Studio Sessions” was only released in \nthe U.S. in a limited quantity of 75,000 for Record Store Day on April 22… and \n75,000 is the sales count that Luminate reported. That means no more copies \nto go around for “Long Pond Sessions” to chart at all in a second week on \nthe chart, give or take a few stray copies that might’ve accidentally been left \nin a stockroom or otherwise held back by retail.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    billbordcanvas.create_text(
        20, 920, text="The global pressing for the album was 115,000, leaving 40,000 copies to be \nsold outside of the U.S.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    billbordcanvas.create_text(20, 980, text="In an unusual case, the music for “Folklore: The Long Pond Studio Sessions” \nwas released digitally in late 2020, yet the album never charted as a separate \ntitle until this week. That’s because the tracks were counted as part of a deluxe \nedition for the original “Folklore” album in the digital realm, as they presumably \nwill continue to be after this week. The LP exclusive for “Long Pond Studio \nSessions” marked the first time that material had its own code to be tracked \nas a separate release.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    billbordcanvas.create_text(
        20, 1130, text="The double-LP release became Swift’s 14th album to chart in the top 10… \nand will soon set a record for being the only Swift album ever to spend just \none week there.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    billbordcanvas.create_text(20, 1200, text="The release of “Long Pond” as an LP exclusive created some panic among \nSwift fans, with some brick-and-mortar stores selling out of their stock as \nsoon as doors opened on Record Store Day, while others that had ordered or \nbeen able to obtain hundreds of copies were able to keep the title on shelves \ninto the afternoon. Per the rules of participating Record Store Day outlets, \nthe album was not allowed to be sold via the web until the following day, \nat which point very few had the title left in stock.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    billbordcanvas.create_image(90, 1350, image=img28, anchor=NW)

    # Configure the scrollbar
    billbordscroll = Scrollbar(
        homeframe, command=billbordcanvas.yview, cursor="double_arrow")
    billbordscroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    billbordcanvas.configure(yscrollcommand=billbordscroll.set)

    # Set the scroll region of the canvas
    billbordcanvas.configure(scrollregion=billbordcanvas.bbox("all"))


def SpeakNowclick():
    global SpeakNowcanvas
    canvas.grid_forget()
    SpeakNowcanvas = Canvas(homeframe, bg="#fff")
    SpeakNowcanvas.grid(row=0, column=0, sticky="news")
    SpeakNowcanvas.create_image(20, 70, image=img29, anchor=NW)
    SpeakNowcanvas.create_text(0, 330, text="Taylor Announces ‘Speak Now (Taylor’s Version)’ \nIs Coming in July During The Eras Tour in \nNashville",
                               fill="#000", font="inter 18 bold", anchor=NW, justify=LEFT)
    SpeakNowcanvas.create_text(5, 430, text="Taylor’s beloved third album, Speak Now, a self written album full of Taylor’s deepest \nemotions is the next album to be re-released! Taylor made the announcement to \na sold out crowd in Nashville last night during The Eras Tour. All formats of the \nalbum, including a violet vinyl, will be available on July 7! You can preorder it now \nand stay tuned for more news.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    SpeakNowcanvas.create_text(
        20, 540, text="Taylor Swift let fans in her hometown of Nashville to be the first to get the official \nnews: “Speak Now” will be the next album in her “Taylor’s Version” series of \nre-recorded albums.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    SpeakNowcanvas.create_text(
        20, 610, text="Swift is giving fans plenty of time to pre-order the album: She revealed that it’s \ncoming out July 7.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    SpeakNowcanvas.create_text(20, 670, text="“I think rather than me speaking about it,” she said, to screams, as fans realized from \nthe language that the long-awaited announcement was at hand, “I thought I \nwould show you, so if you would direct your attention” to the big screens…” \nThere, the album cover and release date were shown on the big screen.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    SpeakNowcanvas.create_text(
        20, 770, text="Upon the announcement at Nashville’s Nissan Stadium, the city turned on \npurple lights on the nearby bridge over the Cumberland River.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    SpeakNowcanvas.create_text(20, 840, text="Fans had a pretty strong indication of what was coming. Wristbands given out \nto fans turned purple at the end of her previous concert this past Sunday, and \nelectronic banners coming into Nissan Stadium were purple-hued.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    SpeakNowcanvas.create_text(20, 920, text="Swifties had long speculated whether “Speak Now” or “1989” would be next to \nget the re-recording-plus-bonus-tracks treatment, with the evidence increasingly \nweighing in her third album’s favor.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    SpeakNowcanvas.create_text(
        20, 990, text="The Taylor Nation account went live on Instagram to carry the spoken \nannouncement for fans, with barely a minute’s advance notice.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    SpeakNowcanvas.create_text(
        20, 1050, text="The new cover art has modern-day Swift wearing a dress similar to the one \nshe wore on the front of the original album in 2010, but with a more serious \nexpression.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    SpeakNowcanvas.create_text(20, 1130, text="So far on the Eras Tour, Swift has only been performing one song on a nightly \nbasis from the “Speak Now” album, “Enchanted,” far less than any other album \nshe’s put out except for her debut, which has no nightly representation. Rather \nthan lead fans to suspect that she disfavors the album, that peculiar choice to \nmake the album practically MIA in the three-hour-plus sets only heightened \nanticipation that she might be waiting to add more material from “Speak Now” \nuntil she was ready to announce the re-recording.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    SpeakNowcanvas.create_image(90, 1300, image=img30, anchor=NW)
    SpeakNowcanvas.create_image(90, 1600, image=img31, anchor=NW)

    # Configure the scrollbar
    SpeakNowscroll = Scrollbar(
        homeframe, command=SpeakNowcanvas.yview, cursor="double_arrow")
    SpeakNowscroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    SpeakNowcanvas.configure(yscrollcommand=SpeakNowscroll.set)

    # Set the scroll region of the canvas
    SpeakNowcanvas.configure(scrollregion=SpeakNowcanvas.bbox("all"))


def TaylorSwift():
    canvas.grid_forget()
    global Taylorcanvas
    Taylorcanvas = Canvas(homeframe, bg="#fff")
    Taylorcanvas.grid(row=0, column=0, sticky="news")
    Taylorcanvas.create_image(0, 0, image=img11, anchor=NW)
    Taylorcanvas.create_text(40, 300, text="Taylor Swift",
                             font="inter 20 bold ", anchor=NW)
    Taylorcanvas.create_text(40, 310, text=(
        "___" * 2), fill="#AD7BE9", font="inter 20 bold ", anchor=NW)
    Taylorcanvas.create_text(10, 400, text="Learn about Taylor’s past, her accomplishments, and her recent achievements.",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Taylorcanvas.create_text(10, 470, text="Learn more about all of Taylor’s albums here.",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Taylorcanvas.create_text(10, 540, text="Learn random details and trivia questions about Taylor.",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Taylorcanvas.create_text(10, 610, text="Taylor’s words of wisdom.",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Taylorcanvas.create_text(10, 680, text="Find out what Taylor’s celebrity peers think of her.",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Taylorcanvas.create_text(10, 750, text="A complete list of every award and honor Taylor has won to date.",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)

    # Create a frame on the canvas to contain the buttons.
    frameforbuttons1 = Frame(Taylorcanvas, bg="#fff", height=30, width=150,)
    frameforbuttons1.place(x=0, y=500)
    frameforbuttons2 = Frame(Taylorcanvas, bg="#fff", height=30, width=150,)
    frameforbuttons2.place(x=0, y=500)
    frameforbuttons3 = Frame(Taylorcanvas, bg="#fff", height=30, width=150,)
    frameforbuttons3.place(x=0, y=500)
    frameforbuttons4 = Frame(Taylorcanvas, bg="#fff", height=30, width=250,)
    frameforbuttons4.place(x=0, y=500)
    frameforbuttons5 = Frame(Taylorcanvas, bg="#fff", height=30, width=250,)
    frameforbuttons5.place(x=0, y=500)
    frameforbuttons6 = Frame(Taylorcanvas, bg="#fff", height=30, width=250,)
    frameforbuttons6.place(x=0, y=500)

    # Add the buttons_frame to the canvas
    Taylorcanvas.create_window((0, 365), window=frameforbuttons1, anchor=NW)
    Taylorcanvas.create_window((0, 435), window=frameforbuttons2, anchor=NW)
    Taylorcanvas.create_window((0, 505), window=frameforbuttons3, anchor=NW)
    Taylorcanvas.create_window((0, 575), window=frameforbuttons4, anchor=NW)
    Taylorcanvas.create_window((0, 645), window=frameforbuttons5, anchor=NW)
    Taylorcanvas.create_window((0, 715), window=frameforbuttons6, anchor=NW)

    # Add a button to the buttons_frame using place method
    Button(frameforbuttons1, text="Biography",
           border=0, font="inter 15 bold ", cursor="hand2", bg="#fff", command=Biographyclick).place(x=0, y=0)
    Button(frameforbuttons2, text="Discography",
           border=0, font="inter 15 bold ", cursor="hand2", bg="#fff", command=Discographyclick).place(x=0, y=0)
    Button(frameforbuttons3, text="Facts",
           border=0, font="inter 15 bold ", cursor="hand2", bg="#fff", command=Factsclick).place(x=0, y=0)
    Button(frameforbuttons4, text="Quotes From Taylor",
           border=0, font="inter 15 bold ", cursor="hand2", bg="#fff", command=FromTaylorclick).place(x=0, y=0)
    Button(frameforbuttons5, text="Quotes About Taylor",
           border=0, font="inter 15 bold ", cursor="hand2", bg="#fff", command=AboutTaylorclick).place(x=0, y=0)
    Button(frameforbuttons6, text="Awards",
           border=0, font="inter 15 bold ", cursor="hand2", bg="#fff", command=Awardsclick).place(x=0, y=0)

    # Configure the scrollbar
    Taylorscroll = Scrollbar(
        homeframe, command=Taylorcanvas.yview, cursor="double_arrow")
    Taylorscroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    Taylorcanvas.configure(yscrollcommand=Taylorscroll.set)

    # Set the scroll region of the canvas
    Taylorcanvas.configure(scrollregion=Taylorcanvas.bbox("all"))


def Biographyclick():
    global Biographycanvas
    canvas.grid_forget()
    Biographycanvas = Canvas(homeframe, bg="#fff")
    Biographycanvas.grid(row=0, column=0, sticky="news")
    Biographycanvas.create_image(0, 0, image=img32, anchor=NW)
    Biographycanvas.create_text(0, 340, text="Biography",
                                fill="#000", font="inter 18 bold", anchor=NW)
    Biographycanvas.create_text(0, 345, text=(
        "____" * 2), fill="#AD7BE9", font="inter 20 bold ", anchor=NW)
    Biographycanvas.create_text(10, 400, text="Taylor Alison Swift was born on December 13, 1989, in Reading, Pennsylvania. \nSwift spent her early years on her family’s Christmas tree farm in nearby \nWyomissing. Her grandmother had been a professional opera singer, and Swift \nsoon followed in her footsteps. By the age of 10, Swift was singing at a variety of \nlocal events, including fairs and contests. She sang “The Star-Spangled Banner” \nat a Philadelphia 76ers basketball game at the age of 11, and began writing her \nown songs and learning guitar at 12 years old.",
                                fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 550, text="To pursue her music career, Swift often visited Nashville, Tennessee, the country \nmusic capital. There she co-wrote songs and tried to land a recording contract. \nNoting her dedication, Swift and her family moved to nearby Hendersonville, \nTennessee, in an attempt to further Swift’s career.",
                                fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 640, text="A stellar performance at The Bluebird Café in Nashville helped Swift get a \ncontract with Scott Borchetta’s Big Machine Records. She released her first \nsingle, “Tim McGraw,” in 2006, and the song became a Top 10 hit on the country \ncharts. It also appeared on her self-titled debut album in October of that same \nyear, which went on to sell more than 5 million copies. More popular singles soon \nfollowed, including “Our Song,” a No. 1 country music hit. “Teardrops on My \nGuitar,” “Picture to Burn” and “Should’ve Said No” were also successful tracks.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 790, text="Swift also received critical praise for her debut effort. She won the Horizon \nAward from the Country Music Association (CMA) and the Academy of Country \nMusic (ACM) Award for Top New Female Vocalist in 2007. Swift next released \nSounds of the Season: The Taylor Swift Holiday Collection that year. Her \nrenditions of “Silent Night” and “Santa Baby” were modest hits on the country \ncharts.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_image(100, 930, image=img33, anchor=NW)
    Biographycanvas.create_text(
        110, 1180, text="Taylor Swift Was Adorable Newbies At The 2008 Grammy", fill="#7d7d7d", font="inter 8 ", anchor=NW)
    Biographycanvas.create_text(10, 1240, text="In 2008, Swift was nominated for a Grammy in the Best New Artist category and \nwon other accolades, including the ACM’s Female Vocalist of the Year Award. \nAround this same time, Swift released her next album, Fearless, which hit the top \nof both the country and pop charts and stayed there for 11 weeks. By the end of \nthe year, Swift had become the highest-selling country artist of 2008.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_image(130, 1380, image=img34, anchor=NW)
    Biographycanvas.create_text(
        130, 1860, text="Taylor Swift awarded at 2009 CMT Music Awards", fill="#7d7d7d", font="inter 8 ", anchor=NW)
    Biographycanvas.create_text(10, 1900, text="Swift netted several awards for her work on Fearless, including Video of the Year \nand Female Video of the Year for “Love Story” at the 2009 CMT Music Awards. \nThat year Swift also won the MTV Video Music Award’s Best Female Video, for \n“You Belong With Me,” making her the first country music star to earn a VMA. \nThe win stirred controversy when rapper Kanye West leaped to the stage during \nSwift’s speech, took the microphone and declared that R&B singer Beyoncé \nshould have won Swift’s award.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_image(80, 2060, image=img35, anchor=NW)
    Biographycanvas.create_text(
        80, 2310, text="when Kanye West took the microphone", fill="#7d7d7d", font="inter 8 ", anchor=NW)
    Biographycanvas.create_text(10, 2360, text="The stunned Swift was unable to make her acceptance speech, and West was \nremoved from the show. When Beyoncé accepted her award for Best Video of \nthe Year later in the show, she called Swift to the stage to finish her speech. West later \napologized to Swift privately, and made a public apology on The Jay Leno Show.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 2460, text="Swift soon became an even hotter commodity. Her concert tickets began selling \nout in less than two minutes, and she also made her second appearance on the \ncomedy show Saturday Night Live, this time as both the host and musical guest. \nAdditionally, in 2010 she became the youngest artist to win the Grammy Award \nfor Album of the Year, for Fearless.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 2580, text="That year Swift released a new album, Speak Now, which featured the hit songs \n“Mean,” “Ours” and “Sparks Fly.” The album was a success, debuting at No. 1 on \nthe Billboard 200 chart and selling more than 1 million copies in its first week. \nShe followed with Red (2012), which featured the hit single “We Are Never Ever \nGetting Back Together” and also topped 1 million in its first week of sales.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 2700, text="Swift was ranked Forbes magazine’s highest paid celebrity under 30 in 2012, \nbeating out Justin Bieber, Rihanna and Lady Gaga with earnings of $57 million. \nThe following year, the musician shared some of her fortune to help others, \nfunding the $4 million Taylor Swift Education Center at the Country Music Hall of \nFame in Nashville. The facility opened with three classrooms, a learning lab and \na space dedicated to exhibits for children. In an interview with CMT Hot 20 \nCountdown, she explained that “music education is really such an important part \nof my life. My life changed so completely when I discovered writing my own \nsongs and playing guitar, and that can’t necessarily all be taught to you in school \nbecause there aren’t enough hours in the day.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 2900, text="In 2013, Swift was also honored with the CMA Pinnacle Award for her \nachievements as a country music performer and for her “positive impact” on \ncountry music, according to the CMA website. She picked up two other wins for \nher collaboration with Tim McGraw and Keith Urban at the CMA Awards \nceremony held that November. Swift’s winning streak continued at the American \nMusic Awards, as she picked up the AMA Award for Artist of the Year for the \n third consecutive time, among other wins.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 3060, text="With her next effort, Swift seemed to step further away from her country music \nroots. She released 1989, her most pop-sounding record to date, in October \n2014. “Shake It Off” proved to be one of the catchiest tracks of the year, \nreaching the top of the pop charts, and she immediately followed with a second \nchart-topping single, “Blank Space.” In an age of low album sales, 1989 moved \nmore than 1.2 million copies in its first week, making Swift the first artist to top \nthe 1 million mark in opening-week sales for three albums.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 3220, text="Swift continued to play with her public persona with the track “Bad Blood,” which \nfeatures Kendrick Lamar. In the video for the song, which debuted at the 2015 \nBillboard Music Awards and doubles as a noir action short, she appears as a \ntough, cutthroat character called “Catastrophe.” Swift recruited other celebrities \nto appear in the video as well, including Karlie Kloss, Cindy Crawford and \nLena Dunham. ", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_image(130, 3370, image=img36, anchor=NW)
    Biographycanvas.create_text(
        140, 3790, text="The 58th Grammy Awards", fill="#7d7d7d", font="inter 8 ", anchor=NW)
    Biographycanvas.create_text(10, 3820, text="In February 2016, Swift opened up the 58th Annual Grammy Awards with another \ntrack from 1989, “Out of the Woods.” Having received pre-telecast awards for \nBest Music Video and Best Pop Vocal Album, later in the evening Swift won \nanother Grammy for Album of the Year, making music history as the first woman \nto win the award twice. ", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 3940, text="In what was seen as a sharp rebuke to a new Kanye West song in which he took \ncredit for her fame, Swift used her acceptance speech to issue an empowerment \nstatement. “I wanna say to all the young women out there, there are going to be \npeople along the way who will try to undercut your success or take credit for your \naccomplishments or your fame,” she said. “But if you just focus on the work, and \nyou don’t let those people sidetrack you, someday when you get where you’re \ngoing, you’ll look around and you will know that it was you and the people who \nloved you who put you there. And that will be the greatest feeling in the world.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 4120, text="Swift took a break from the spotlight after the massive success of 1989. However, \nshe resurfaced in August 2017 when she testified in a trial against David Mueller, \na former radio DJ she had accused of groping her in 2013. Mueller denied \nSwift’s allegations and said the incident cost him his job, which led him to sue \nSwift, her mother and a radio station employee in 2015. Swift countersued him \nfor alleged assault and battery, and a jury ruled in her favor in 2017, awarding her \n$1 in damages as a symbolic gesture.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 4280, text="Swift responded to the verdict in a statement: “I acknowledge the privilege that I \nbenefit from in life, in society and in my ability to shoulder the enormous cost of \ndefending myself in a trial like this. My hope is to help those whose voices should \nalso be heard. Therefore, I will be making donations in the near future to multiple \norganizations that help sexual assault victims defend themselves.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 4400, text="That year, Swift was also on the receiving end a lawsuit, when two songwriters \nclaimed that she stole the chorus of their song “Playas Gon’ Play” for her hit \n“Shake It Off.” Although a judge dismissed the case in early 2018, on the grounds \nthat the “allegedly infringed lyrics are short phrases that lack the modicum of \noriginality and creativity required for copyright protection,” an appeals court \nrevived the suit in October 2019.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 4540, text="In late August 2017, using an image of a snake, Swift revealed that she would \nrelease her sixth studio album, reputation, in November. The image of a snake is a \nreference to when Kim Kardashian called Swift a “snake” on Twitter in 2016, \nafter Swift denied that she granted Kanye West permission to use her name in \nhis song “Famous.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 4660, text="Swift debuted the first single, “Look What You Made Me Do,” on August 24. In the \nmusic video, Swift played characters of all her misrepresentations. The video \nhad more than 19 million views on YouTube within the first day.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 4740, text="Days before reputation‘s scheduled November 10 release, its secretive \ntracklist was leaked to social media. Swift responded by posting the complete \nlist to her Instagram page, its 15 songs including a collaborative effort with Ed \nSheeran and rapper Future, titled “End Game.” The two later appeared in the \nvideo for the track, which debuted in January 2018.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 4860, text="reputation sold 1.05 million copies in the U.S. over its first four days. Along with \ngiving the artist her fourth consecutive album to surpass 1 million in sales for its \nopening week, that total made reputation the top-selling album of 2017. Its \nsuccess continued into 2018, surpassing 2 million in sales while generating the \nrelease of seven singles. By the end of the year, reputation had been honored \nwith Favorite Pop/Rock Album at the AMAs and Top Selling Album at the \nBillboard Music Awards.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(
        10, 5010, text="Along with her musical success, Swift in 2018 was cast in a live-action \nadaptation of the famed Broadway musical Cats, along with Jennifer Hudson, \nJames Corden and Rebel Wilson.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 5090, text="On April 26, 2019, Swift debuted the duet “ME!” with Brendon Urie of Panic! at \nthe Disco, along with a video of the two singing and dancing amid a panoply of \nelaborate sets and swirling colors. In mid-June the artist dropped the single “You \nNeed to Calm Down” and revealed the name of her upcoming album, Lover.", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 5190, text="In late June, Swift revealed her dismay that her catalog of music from her first \nsix albums, up to reputation, had been sold by her first label to a company owned by \nScooter Braun, manager of artists like Justin Bieber and Ariana Grande and a \nperson she accused of bullying tactics. “Scooter has stripped me of my life’s \nwork, that I wasn’t given an opportunity to buy,” she wrote on Tumblr. “Essentially, \nmy musical legacy is about to lie in the hands of someone who tried to dismantle.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Biographycanvas.create_text(10, 5330, text="Just before the August 23 release of Lover, Swift confirmed she would rerecord \nher old music to regain artistic and financial control of her catalog. Later that year, \nshe claimed a whopping six wins at the American Music Awards, including artist \nof the year and artist of the decade honors.", fill="#7d7d7d", font="inter 12 ", anchor=NW)

    # Configure the scrollbar
    Biographyscroll = Scrollbar(
        homeframe, command=Biographycanvas.yview, cursor="double_arrow")
    Biographyscroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    Biographycanvas.configure(yscrollcommand=Biographyscroll.set)

    # Set the scroll region of the canvas
    Biographycanvas.configure(scrollregion=Biographycanvas.bbox("all"))


def Discographyclick():
    global Discographycanvas
    canvas.grid_forget()
    Discographycanvas = Canvas(homeframe, bg="#fff")
    Discographycanvas.grid(row=0, column=0, sticky="news")
    Discographycanvas.create_image(0, 0, image=img37, anchor=NW)
    Discographycanvas.create_text(0, 340, text="Discography",
                                  fill="#000", font="inter 18 bold", anchor=NW)
    Discographycanvas.create_text(0, 345, text=(
        "_____" * 2), fill="#AD7BE9", font="inter 20 bold ", anchor=NW)
    Discographycanvas.create_text(10, 400, text="Hi, I’m Taylor. I love the number 13. I was born in December on a Christmas tree \nfarm. I like imagining what life was like hundreds of years ago. I have blurry \neyesight. My favorite thing in life is writing about life, specifically the parts of life \nconcerning love. Because, as far as I’m concerned, love is absolutely everything.",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Discographycanvas.create_text(10, 500, text="I’m easily excited, thrilled, scared, and shocked. I’m 24* now, but I never stopped \njumping up and down when something wonderful happens. My biggest fear is \ngetting bad news. Or, letting someone down. I really love showing people what I \nmeant when I wrote a song, so my shows are very theatrical. I knock on wood \nconstantly. I have a cat named Meredith.She’s named after my favorite character \non Grey’s Anatomy, and she’s fantastic. I live in Nashville, a magical land where \n99% of the people are friendly and courteous drivers who let you in and don’t \nhonk at you.",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Discographycanvas.create_text(10, 670, text="I go into a trance when I’m in an antique store. I don’t like it when something or \nsomeone turns out to be different than what you originally thought. Like when \nyou’re shopping and you find a really cute dress, only to realize it’s actually a \nstrange jumpsuit situation. But I mostly don’t like it when it happens with people. \nI love my friends and I’m always making new ones. I don’t really think you can \never stop making new friends or learning about as many new things as possible. \nI also don’t think you should ever take life so seriously that you forget to play.",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Discographycanvas.create_text(10, 830, text="Music has taken me all over the world, but the fans are the reason it’s been so \nmagical. I’m so blown away by how nice they are to me. It’s strange to feel so \nunderstood by such a large group of people, but I love it. For the last two years, \nI’ve been working on an album called Red. I called it that because of the \ntumultuous, crazy adventures in love and loss that it chronicles. In my mind, when \nyou experience love that’s fast paced and out of control and mixes infatuation, \njealousy, frustration, miscommunication, and all of those lovely emotions… In \nretrospect, it all looks red.",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Discographycanvas.create_text(10, 1000, text="I can’t wait for so many things. But mostly I can’t wait to see you, whether it’s \nin a crowd or a coffee shop. Thank you for listening, showing up, reading, and \ntaking such good care of me.",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Discographycanvas.create_text(10, 1090, text="–Taylor",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Discographycanvas.create_text(10, 1130, text="* Taylor is now 31 years old.",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)

    # Configure the scrollbar
    Biographyscroll = Scrollbar(
        homeframe, command=Discographycanvas.yview, cursor="double_arrow")
    Biographyscroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    Discographycanvas.configure(yscrollcommand=Biographyscroll.set)

    # Set the scroll region of the canvas
    Discographycanvas.configure(scrollregion=Discographycanvas.bbox("all"))


def Factsclick():
    global Factscanvas
    canvas.grid_forget()
    Factscanvas = Canvas(homeframe, bg="#fff")
    Factscanvas.grid(row=0, column=0, sticky="news")
    Factscanvas.create_image(0, 0, image=img38, anchor=NW)
    Factscanvas.create_text(0, 340, text="Facts",
                            fill="#000", font="inter 18 bold", anchor=NW)
    Factscanvas.create_text(0, 345, text="____",
                            fill="#AD7BE9", font="inter 20 bold ", anchor=NW)
    Factscanvas.create_text(10, 400, text="Full Name: Taylor Alison Swift\n\nNicknames: “Tay,” “T,” “TayTay,” or “T-Swizzle”\n\nAge: 31\n\nBirthdate: December 13, 1989\n\nBirthplace: Wyomissing, Pennsylvania\n\nResidence: Nashville, Tennessee\n\nParents: Scott and Andrea\n\nSiblings: Austin\n\nSign: Sagittarius\n\nHair Color: Blonde\n\nEye Color: Blue\n\nHeight: 5’11”\n\nFavorite Food: Cheesecake\n\nFavorite Breakfast Cereal: Cinnamon Toast Crunch\n\nFavorite Holiday: Christmas\n\nFavorite Season: Summer\n\nFavorite Movie: Love Actually\n\nFavorite Book: The Hunger Games and To Kill a Mockingbird\n\nFavorite Style: Vintage, classic, feminine\n\nFavorite Flowers: Orchids and hydrangeas\n\nFavorite Number: 13\n\nFavorite TV Shows: Grey’s Anatomy, Law & Order: SVU, CSI, and Friends\n\nFavorite Vacation: Girls’ trip to Charleston, South Carolina\n\nFavorite High School Teacher: “Mr. Schwabe, my criminal justice teacher. He \nused to be a Chicago police officer and told us heaps of amazing stories. It \nwas the most exciting class I ever took.”\n\nHobbies: Cooking and baking, hiking, waterskiing, volleyball, making crafts, \nmaking jam, face-painting, playing fetch with Meredith, taking pictures, thinking \nof gifts to give to people, and going to coffee shops",
                            fill="#7d7d7d", font="inter 12 ", anchor=NW)

    # Configure the scrollbar
    Factsscroll = Scrollbar(
        homeframe, command=Factscanvas.yview, cursor="double_arrow")
    Factsscroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    Factscanvas.configure(yscrollcommand=Factsscroll.set)

    # Set the scroll region of the canvas
    Factscanvas.configure(scrollregion=Factscanvas.bbox("all"))


def FromTaylorclick():
    global FromTaylorcanvas
    canvas.grid_forget()
    FromTaylorcanvas = Canvas(homeframe, bg="#fff")
    FromTaylorcanvas.grid(row=0, column=0, sticky="news")
    FromTaylorcanvas.create_image(0, 0, image=img39, anchor=NW)
    FromTaylorcanvas.create_text(5, 340, text="Quotes From Taylor",
                                 fill="#000", font="inter 18 bold", anchor=NW)
    FromTaylorcanvas.create_text(0, 345, text=(
        "_____" * 3), fill="#AD7BE9", font="inter 20 bold ", anchor=NW)
    FromTaylorcanvas.create_text(10, 400, text="“I think for me, beauty is sincerity. I think that there are so many different ways \nthat someone can be beautiful. You know someone’s so funny that it makes them \nbeautiful no matter how they look because they’re sincere in it. Or someone’s \nreally emotional and moody and thoughtful and stoic but that makes them \nbeautiful because that’s sincerely who they are. Or you look out into the crowd \nand you see someone so happy that they’re smiling from ear-to-ear and that \nsincerity comes through, and I think that’s what makes somebody beautiful. I’ve \nnever felt like there’s just one way to be beautiful, you know, tall or short, straight \nhair or curly or whatever, some people have definitions of their “types.” You know, \nfor me, I think that when I meet someone and there’s that magical thing about them \nthat makes them unforgettable, it’s that they’re sincere in honest in whoever they \nare. Be that funny, happy, sad, going through a rough time, sarcastic, I think \nthese personality traits that come through when somebody is really sincere is \nwhat makes them beautiful.”",
                                 fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(10, 680, text="“Fans are my favorite thing in the world. I’ve never been the type of artist who has \nthat line drawn between their friends and their fans. The line’s always been really \nblurred for me. I’ll hang out with them after the show. I’ll hang out with them before \nthe show. If I see them in the mall, I’ll stand there and talk to them for 10 minutes. I \ndon’t care. I’m just a senior in high school who has a better job. Who am I to think \nI’m better than talking to people?”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(10, 810, text="“I love it when people say things to me in public and want to meet me, because I \nwant to meet them! Early on, my manager told me, “If you want to sell 500,000 \nrecords, then go out there and meet 500,000 people.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(10, 890, text="“To me, Fearless is not the absense of fear. It’s not being completely unafraid. \nTo me, Fearless is having fears. Fearless is having doubts. Lots of them. To me, \nFearless is living in spite of those things that scare you to death.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 970, text="“What I’ve learned is not to change who you are, because eventually you’re going \nto run out of new things to become.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 1030, text="“You only get so many firsts, Every one is a blessing.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 1070, text="“The only place where it’s cool to be the same as everyone else is in junior high.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(10, 1110, text="“Clubs are just not where I want to be photographed. For everything I do, I think \nabout a 6-year-old girl and her mom that I saw at my concert last night. I think \nabout what those two individuals would think if I were at a club last night. I never \nwant to be arrested, and I never want to get a DUI, those are my moral values. \nI am an over-achiever, and I want to be known for the good things in my life.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 1230, text="“People haven’t always been there for me but music always has.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(10, 1280, text="“Everybody has that point in their life where you hit a crossroads and you’ve had \na bunch of bad days and there’s different ways you can deal with it and the way I \ndealt with it was I just turned completely to music.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 1370, text="“I write blatantly obvious songs with blatantly obvious details, and then I’m like \nNO! when they find out, I dunno what’s wrong with me. I have issues.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 1440, text="“I’m not that complicated. my complications come out in my songs. All you have \nto do to be my friend is like me…and listen.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 1510, text="“When you’re singing you can hear the echo of people in the audience singing \nevery single word with you, and that was that big dream that I had for myself. It’s \nhappening.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(10, 1590, text="“I think songwriting is the ultimate form of being able to make anything that \nhappens in your life productive. If you get out of a bad relationship that was a \ncomplete waste of time, you can write about it and it can become a benefit to \nyour career. How sweet is that?”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 1690, text="“I wish all teenagers can filter through songs instead of turning to drugs and \nalcohol.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 1760, text="“Everything about this business is exciting to me.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(10, 1810, text="“I think I first realized I wanted to be in country music and be an artist when I was \n10. And I started dragging my parents to festivals, and fairs, and kareoke \ncontests, and I did that for about a year before I came to Nashville for the first \ntime. I was 11 and I had this demo CD of me singing Dixie Chicks and Leanne \nRimes songs.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 1930, text="“You know what, if they don’t want me to write bad songs about them, they shouldn’t \ndo bad things.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 2000, text="“I wrote this song last year about a guy named Stephen who I thought was cute. \nSometimes all it takes to write a song about someone is thinking that they’re cute.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 2070, text="“I hope that I stand for the girl who is 15 and is in school and doesn’t fit in. Maybe \nshe can find some sort of comfort by going home and putting on my CD.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 2140, text="“I suffer from girlnextdooritis where the guy is friends with you and that’s it.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 2190, text="(On how to sell 3 million CDs in 2008) “Go to high school and write it all down.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 2240, text="“I’m intimidated by the fear of being average.”", fill="#7d7d7d", font="inter 12 ", anchor=NW)
    FromTaylorcanvas.create_text(
        10, 2290, text="(Upon winning the CMA Horizon Award) “This is definitely the highlight of my \nsenior year!”", fill="#7d7d7d", font="inter 12 ", anchor=NW)

    # Configure the scrollbar
    FromTaylorscroll = Scrollbar(
        homeframe, command=FromTaylorcanvas.yview, cursor="double_arrow")
    FromTaylorscroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    FromTaylorcanvas.configure(yscrollcommand=FromTaylorscroll.set)

    # Set the scroll region of the canvas
    FromTaylorcanvas.configure(scrollregion=FromTaylorcanvas.bbox("all"))


def AboutTaylorclick():
    global AboutTaylorcanvas
    canvas.grid_forget()
    AboutTaylorcanvas = Canvas(homeframe, bg="#fff")
    AboutTaylorcanvas.grid(row=0, column=0, sticky="news")
    AboutTaylorcanvas.create_image(0, 0, image=img40, anchor=NW)
    AboutTaylorcanvas.create_text(5, 290, text="Quotes About Taylor",
                                  fill="#000", font="inter 18 bold", anchor=NW)
    AboutTaylorcanvas.create_text(5, 295, text=(
        "________" * 2), fill="#AD7BE9", font="inter 20 bold ", anchor=NW)
    AboutTaylorcanvas.create_text(10, 350, text="“She just seems like a really true friend, and it’s just really great to meet people in \nthis industry [like her]. A lot of people I’ve met have a preconceived idea [about \nher], at least from tabloids, but she’s one of the most amazing people I’ve ever \nmet.” – Sarah Hyland",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)
    AboutTaylorcanvas.create_text(10, 450, text="“Taylor is a musician who does things under her own name and tells her own \nstories—her songs and her albums are her.” – Emma Stone",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)
    AboutTaylorcanvas.create_text(10, 520, text="“When you hear just the dedication she’s had to her fans and how much work \nshe’s done, for a person that’s so young, that kind of awareness doesn’t always \ncome early.” – Dianna Agron",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)
    AboutTaylorcanvas.create_text(10, 610, text="“Anyone who thinks Taylor Swift isn’t good for the girl cause has to be crazy, \nbecause any woman who’s dominating the charts, the creative director of her \nown empire, and made whatever millions of dollars last year is only lifting us up. \nKilling it. And she’s super-creative, an amazing role model, beautiful…..And I \nthink it’s fake intellectuals who don’t have an interest in her. I think real \nintellectuals would be interested in what she’s doing and understand that she \nrepresents something really cool and like a great cultural shift. Anyone who tries \nto debate Taylor Swift with me, I’m like, “You are an uninformed consumer, and \nyou will be shut down. You’re not doing this.” – Lena Dunham",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)
    AboutTaylorcanvas.create_text(10, 810, text="“Taylor works her tail off. I think she is the hardest-working person in the music \nbusiness, period. I just love her to pieces.” – Reba McEntire",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)
    AboutTaylorcanvas.create_text(10, 880, text="“You know she’s one of those rare artists that come along that there’s only been \na handful of throughout the history of music, who creates such a weight behind \nher, pulls so many people into what her music is about that they discover so \nmany different artists because of what she does. She’s just a really special, \nspecial artist.” – Tim McGraw",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)
    AboutTaylorcanvas.create_text(10, 1000, text="“I think girls need to be more supportive of each other. I definitely agree with that. \nI’m all about that. Taylor has been one of those girls. We have been friends for \nfive years. She is very strong. She doesn’t care what people think and she \ninspires me.” – Selena Gomez",
                                  fill="#7d7d7d", font="inter 12 ", anchor=NW)

    # Configure the scrollbar
    FromTaylorscroll = Scrollbar(
        homeframe, command=AboutTaylorcanvas.yview, cursor="double_arrow")
    FromTaylorscroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    AboutTaylorcanvas.configure(yscrollcommand=FromTaylorscroll.set)

    # Set the scroll region of the canvas
    AboutTaylorcanvas.configure(scrollregion=AboutTaylorcanvas.bbox("all"))


def Awardsclick():
    global Awardscanvas
    canvas.grid_forget()
    Awardscanvas = Canvas(homeframe, bg="#fff")
    Awardscanvas.grid(row=0, column=0, sticky="news")
    Awardscanvas.create_image(0, 0, image=img41, anchor=NW)
    Awardscanvas.create_text(5, 290, text="Awards",
                             fill="#000", font="inter 18 bold", anchor=NW)
    Awardscanvas.create_text(5, 295, text="______",
                             fill="#AD7BE9", font="inter 20 bold ", anchor=NW)
    Awardscanvas.create_text(10, 350, text="2014",
                             fill="#7d7d7d", font="inter 12 bold", anchor=NW)
    Awardscanvas.create_text(10, 370, text="People’s Choice Awards – Favorite Country Artist\nSongwriters Hall of Fame – Johnny Mercer Award\nCMC Music Awards – International Artist of the Year\nCMC Music Awards – International Video of the Year (“Highway Don’t Care”)\nCountry Music Award Of Australia – International Top Selling Album Of The Year",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Awardscanvas.create_text(10, 480, text="2013",
                             fill="#7d7d7d", font="inter 12 bold", anchor=NW)
    Awardscanvas.create_text(10, 500, text="People’s Choice Awards – Favorite Country Artist\nGrammy Awards – Best Song Written for Visual Media (“Safe & Sound”)\nBillboard Music Awards – Top Artist\nBillboard Music Awards – Top Female Artist\nBillboard Music Awards – Top Billboard 200 Artist\nBillboard Music Awards – Top Digital Songs Artist\nBillboard Music Awards – Top Country Artist\nBillboard Music Awards – Top Billboard 200 Album (Red)\nBillboard Music Awards – Top Country Album (Red)\nBillboard Music Awards – Top Country Song (“We Are Never Ever Getting Back \nTogether”)\nBMI Awards – Winning Song (“We Are Never Ever Getting Back Together”)\nRadio Disney Music Awards – Song of the Year (“I Knew You Were Trouble”)\nRadio Disney Music Awards – Best Break Up Song (“We Are \nNever Ever Getting Back Together”)\nMetrolyrics End of the Year Awards – Break-up Lyric of the Year\nThe SiriusXM Indies Awards – International Artist of the Year\nTaiwan HITO Radio Music Awards – Top Western Song of the Year (“We Are \nNever Ever Getting Back Together”)\nMuchMusic Video Awards – Your Fave International Artist/Group\nFragrance Foundation Awards – Celebrity Fragrance of the Year (Wonderstruck \nEnchanted)\nVEVOCertified Awards – 100.000.000 Views (“I Knew You Were Trouble”)\nVEVOCertified Awards – 100.000.000 Views (“22”)\nBillboard Mid-year Music Awards – First-Half MVP\nBillboard Mid-year Music Awards – Favorite Billboard 200 No 1 Album (Red)\nBillboard Mid-year Music Awards – Best Tour (Red Tour)\nBMI Awards – Winning Song (“We Are Never Ever Getting Back Together”)\nMTV Video Music Awards – Best Female Video (“I Knew You Were Trouble”)\nMTV Video Music Awards Japan – Best Female Video (“I Knew You Were \nTrouble”)\nNashville Songwriters Association International Awards – Songwriter/Artist of the \nYear\nTeen Choice Awards – Choice Country Song (“We Are Never Ever Getting Back \nTogether”)\nCanadian Country Music Association – Top Selling Album (Red)\nYouTube Music Awards – YouTube Phenomenon (“I Knew You Were Trouble”)",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Awardscanvas.create_text(10, 1190, text="2012",
                             fill="#7d7d7d", font="inter 12 bold", anchor=NW)
    Awardscanvas.create_text(10, 1210, text="Grammy Awards – Best Country Solo Performance (“Mean”)\nGrammy Awards – Best Country Song (“Mean”)\nPeople’s Choice Awards – Favorite Country Artist\nNickelodeon Kids’ Choice Awards – The Big Help Award\nAcademy of Country Music Awards – Entertainer of the Year\nBillboard Music Awards – Billboard Woman of the Year\nTeen Choice Awards – Choice Female Artist\nTeen Choice Awards – Choice Female Country Artist\nTeen Choice Awards – Choice Voice (The Lorax)\nTeen Choice Awards – Choice Single by a Female Artist (“Eyes Open”)\nTeen Choice Awards – Choice Country Song (“Sparks Fly”)\nCanadian Country Music Association Award – Generation Award\nAmerican Music Awards – Favorite Country Female Artist\nBenBoard Music Awards – Song of the Year (“We Are Never Ever Getting Back \nTogether”)\nBenBoard Music Awards – Country Song of the Year (“We Are Never Ever \nGetting Back Together”)\nBenBoard Music Awards – Best Country Artist\nBMI Awards – Pop Award Winning Song (“Mine”)\nMTV Europe Music Awards – Best Female\nMTV Europe Music Awards – Best Live Act\nMTV Europe Music Awards – Best Look\nNashville Songwriters Association International Awards – Songwriter/Artist of the \nYear\nRipple of Hope Gala – Ripple of Hope Award\n40 Principales Awards – Best International Artist of the Year\nVEVOCertified Awards – 100.000.000 Views (“Love Story”)\nVEVOCertified Awards – 100.000.000 Views (“You Belong With Me”)\nVEVOCertified Awards – 100.000.000 Views (“Mine”)\nVEVOCertified Awards – 100.000.000 Views (“We Are Never Ever Getting \nBack Together”)",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Awardscanvas.create_text(10, 1790, text="2011",
                             fill="#7d7d7d", font="inter 12 bold", anchor=NW)
    Awardscanvas.create_text(10, 1810, text="Academy of Country Music Awards – Entertainer of the Year\nAcademy of Country Music Awards – Jim Reeves International Award\nPeople’s Choice Awards – Favorite Country Artist\nBillboard Music Awards – Top Billboard 200 Artist\nBillboard Music Awards – Top Country Artist\nBillboard Music Awards – Top Country Album (Speak Now)\nCMT Music Awards – Video of the Year (“Mine”)\nCMT Awards – Artist of the Year\nAnnual Independent Music Awards – Favorite International Solo Artist of the Year\nTeen Choice Awards – Ultimate Choice Award\nTeen Choice Awards – Choice Music Female Country Artist\nTeen Choice Awards – Choice Music Female Artist\nTeen Choice Awards – Choice Red Carpet Fashion Icon Female\nTeen Choice Awards – Choice Music Breakup Song (“Back to December”)\nTeen Choice Awards – Choice Music Country Single (“Mean”)\nNashville Songwriters Hall of Fame – Songwriter/Artist of the Year\nBMI Country Awards – Publisher of the Year (“Fearless”)\nBMI Country Awards – Publisher of the Year (“Mine”)\nBMI Country Awards – Publisher of the Year (“Back to December”)\nCountry Music Association Awards – Entertainer of the Year\nAmerican Music Awards – Artist of the Year\nAmerican Music Awards – Favorite Country Female Artist\nAmerican Music Awards – Favorite Country Album (Speak Now)\nNashville Songwriters Association International Awards – Songwriter/Artist of the \nYear",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Awardscanvas.create_text(10, 2280, text="2010",
                             fill="#7d7d7d", font="inter 12 bold", anchor=NW)
    Awardscanvas.create_text(10, 2300, text="American Music Awards – Favorite Female Country Artist\nBillboard Touring Awards – Top Package Award\nBMI Country Awards – Songwriter of the Year\nBMI Country Awards – Song of the Year (“You Belong With Me”)\nCMT Awards – Artist of the Year\nBMI Country Awards – Winning Song (“White Horse”)\nSESAC Awards – Country Performance Activities (“Fearless”)\nSESAC Awards – Country Performance Activities (“White Horse”)\nSESAC Awards – Country Performance Activities (“You Belong With Me”)\nNashville Songwriters Hall of Fame – Songwriter/Artist of the Year\nMXY Music Awards – Favorite International Music Video (“Love Story”)\nCanadian Country Music Awards – Top Selling Album (Fearless)\nTeen Choice Awards – Choice Music: Female Country Artist\nTeen Choice Awards – Choice Music: Country Song (“Fifteen”)\nTeen Choice Awards – Choice Music: Country Album (Fearless)\nTeen Choice Awards – Choice Movie: Female Breakout (Valentine’s Day)\nBMI Pop Awards – Song of the Year (“Love Story”)\nSongwriters Hall of Fame – Hal David Starlight Award\nNARM Convention – Artist of the Year\nKids Choice Awards – Song of the Year (“You Belong With Me”)\nKids Choice Awards – Favorite Female Singer\nGrammy Awards – Album of the Year (Fearless)\nGrammy Awards – Best Female Country Vocal Performance (“White Horse”)\nGrammy Awards – Best Country Song (“White Horse”)\nGrammy Awards – Best Country Album (Fearless)\nPeople’s Choice Awards – Favorite Female Artist\nNashville Songwriters Association International Awards – Songwriter/Artist of the \nYear",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Awardscanvas.create_text(10, 2830, text="2009",
                             fill="#7d7d7d", font="inter 12 bold", anchor=NW)
    Awardscanvas.create_text(10, 2850, text="American Music Awards – Favorite Female Country Artist\nAmerican Music Awards – Favorite Female Country Album (Fearless)\nAmerican Music Awards – Favorite Female Pop Artist\nAmerican Music Awards – Adult Contemporary Artist\nAmerican Music Awards – Artist of the Year\nCountry Music Association Awards – Entertainer of the Year\nCountry Music Association Awards – Top Female Vocalist\nCountry Music Association Awards – Video of the Year (“Love Story”)\nCountry Music Association Awards – Album of the Year (Fearless)\nCountry Music Association Awards – International Artist Achievement Award\nBMI Country Awards – Songwriter of the Year\nNashville Songwriters Hall of Fame – Songwriter/Artist of the Year\nNashville Music Awards – Artist of the Year\nNashville Music Awards – Best Country Album (Fearless)\nNashville Music Awards – Songwriter-Artist of the Year\nBillboard Music Awards – Artist of the Year\nBillboard Music Awards – The Billboard 200 Artists of the Year\nBillboard Music Awards – The Billboard 200 Album of the Year (Fearless)\nBillboard Music Awards – Hot Radio Songs of the Year (“Love Story”)\nBillboard Music Awards – Hot Adult Contemporary Artist of the Year\nBillboard Music Awards – Top Country Artist of the Year\nBillboard Music Awards – Top Country Album of the Year (Fearless)\nCanadian Country Music Awards – Top Selling Album (Fearless)\nMTV Video Music Awards – Best Female Video (“You Belong With Me”)\nTeen Choice Awards – Music Album Female Artist (Fearless)\nTeen Choice Awards – Music: Female Artist\nThailand Music Video Awards – Popular International New Artist\nCMT Music Awards – Video of the Year (“Love Story”)\nCMT Music Awards – Female Video of the Year (“Love Story”)\nAcademy of Country Music Awards – Album of the Year (Fearless)\nAcademy of Country Music Awards – Crystal Milestone Award\nNashville Songwriters Association International Awards – Songwriter/Artist of the \nYear\nBMI Pop Awards – Song of the Year (“Teardrops On My Guitar”)",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Awardscanvas.create_text(10, 3490, text="2008",
                             fill="#7d7d7d", font="inter 12 bold", anchor=NW)
    Awardscanvas.create_text(10, 3510, text="American Music Awards – Favorite Female Country Artist\nNashville Songwriters Hall of Fame – Songwriter/Artist of the Year\nBMI Country Awards – Songwriter of the Year\nBMI Country Awards – Winning Song (“Our Song”)\nBMI Country Awards – Winning Song (“Teardrops On My Guitar”)\nTeen Choice Awards – Breakout Artist\nAcademy of Country Music Awards – Top New Female Vocalist of the Year\nYoung Hollywood Awards – Superstar of Tomorrow Award\nCMT Music Awards – Video of the Year (“Our Song”)\nCMT Music Awards – Female Video of the Year (“Our Song”)\nCMT Online Awards – No. 1 Streamed Unplugged at Studio 330",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)
    Awardscanvas.create_text(10, 3740, text="2007",
                             fill="#7d7d7d", font="inter 12 bold", anchor=NW)
    Awardscanvas.create_text(10, 3760, text="Country Music Association Awards – Horizon Award\nBMI Country Awards – Winning Song (“Tim McGraw”)\nNashville Songwriters Association International Awards – Songwriter/Artist of the \nYear\nCMT Music Awards – Breakthrough Video of the Year (“Tim McGraw”)",
                             fill="#7d7d7d", font="inter 12 ", anchor=NW)

    # Configure the scrollbar
    Awardslorscroll = Scrollbar(
        homeframe, command=Awardscanvas.yview, cursor="double_arrow")
    Awardslorscroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    Awardscanvas.configure(yscrollcommand=Awardslorscroll.set)

    # Set the scroll region of the canvas
    Awardscanvas.configure(scrollregion=Awardscanvas.bbox("all"))


def photogallery():
    canvas.grid_forget()
    global gallerycanvas
    gallerycanvas = Canvas(homeframe, bg="#fff")
    gallerycanvas.grid(row=0, column=0, sticky="news")
    gallerycanvas.create_image(0, 0, image=img11, anchor=NW)
    gallerycanvas.create_text(40, 300, text="photogallery",
                              font="inter 20 bold ", anchor=NW)
    gallerycanvas.create_text(
        40, 310, text="___________", fill="#AD7BE9", font="inter 20 bold ", anchor=NW)

    # Create a frame on the canvas to contain the buttons.
    frameforbuttons1 = Frame(gallerycanvas, bg="#fff", height=600, width=550,)
    frameforbuttons1.place(x=0, y=500)

    # Add the buttons_frame to the canvas
    gallerycanvas.create_window((0, 365), window=frameforbuttons1, anchor=NW)

    # Add a button to the buttons_frame using place method
    Button(frameforbuttons1, text=" May 7 - Nashville, Tennessee",
           border=0, font="inter 8 bold ", cursor="hand2", bg="#fff", fg="#7d7d7d", image=img44, compound=TOP, command=May7click).place(x=50, y=0)
    Button(frameforbuttons1, text=" May 6 - Nashville, Tennessee",
           border=0, font="inter 8 bold ", cursor="hand2", bg="#fff", fg="#7d7d7d", image=img45, compound=TOP, command=May6click).place(x=300, y=0)
    Button(frameforbuttons1, text=" May 5 - Nashville, Tennessee",
           border=0, font="inter 8 bold ", cursor="hand2", bg="#fff", fg="#7d7d7d", image=img46, compound=TOP, command=May5click).place(x=50, y=200)
    Button(frameforbuttons1, text=" May 4 - Out with her mom in Nashville",
           border=0, font="inter 8 bold ", cursor="hand2", bg="#fff", fg="#7d7d7d", image=img47, compound=TOP, command=May4click).place(x=300, y=200)
    Button(frameforbuttons1, text="April 28 - Atlanta, Georgia",
           border=0, font="inter 8 bold ", cursor="hand2", bg="#fff", fg="#7d7d7d", image=img81, compound=TOP, command=April28click).place(x=50, y=400)
    Button(frameforbuttons1, text=" April 21 - Houston, Texas",
           border=0, font="inter 8 bold ", cursor="hand2", bg="#fff", fg="#7d7d7d", image=img90, compound=TOP, command=April21click).place(x=300, y=400)

    # Configure the scrollbar
    galleryscroll = Scrollbar(
        homeframe, command=gallerycanvas.yview, cursor="double_arrow")
    galleryscroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    gallerycanvas.configure(yscrollcommand=galleryscroll.set)

    # Set the scroll region of the canvas
    gallerycanvas.configure(scrollregion=gallerycanvas.bbox("all"))


def May7click():
    canvas.grid_forget()
    global May7canvas, May7Frame
    May7canvas = Canvas(homeframe, bg="#fff")
    May7canvas.grid(row=0, column=0, sticky="news")
    May7canvas.create_text(130, 50, text="May 7 - Nashville, Tennessee",
                           font="inter 18 bold ", anchor=NW)
    May7canvas.create_image(0, 90, image=img48, anchor=NW)

    # Create a frame on the canvas to contain the buttons.
    May7Frame = Frame(May7canvas, bg="#fff", height=150, width=550,)
    May7Frame.rowconfigure(0, weight=1)
    May7Frame.columnconfigure(0, weight=1)
    May7Frame.place(x=0, y=500)
    Label(May7Frame, image=img50).place(x=0, y=0)

    # Add the buttons_frame to the canvas
    May7canvas.create_window((10, 535), window=May7Frame, anchor=NW)

    # Add a button to the buttons_frame using place method
    Button(May7Frame, border=0, bg="#fff", image=img49,
           cursor="hand2", command=May7click).place(x=12, y=27)
    Button(May7Frame, border=0, bg="#fff", image=img51,
           cursor="hand2", command=pic1May7click).place(x=147, y=27)
    Button(May7Frame, border=0, bg="#fff", image=img53,
           cursor="hand2", command=pic2May7click).place(x=282, y=27)
    Button(May7Frame, border=0, bg="#fff", image=img55,
           cursor="hand2", command=pic3May7click).place(x=418, y=27)

    # Configure the scrollbar
    May7scroll = Scrollbar(
        homeframe, command=May7canvas.yview, cursor="double_arrow")
    May7scroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    May7canvas.configure(yscrollcommand=May7scroll.set)

    # Set the scroll region of the canvas
    May7canvas.configure(scrollregion=May7canvas.bbox("all"))


def pic1May7click():
    canvas.grid_forget()
    May7canvas.create_image(0, 90, image=img52, anchor=NW)


def pic2May7click():
    canvas.grid_forget()
    May7canvas.create_image(0, 90, image=img54, anchor=NW)


def pic3May7click():
    canvas.grid_forget()
    May7canvas.create_image(0, 90, image=img56, anchor=NW)


def May6click():
    canvas.grid_forget()
    global May6canvas, May6Frame
    May6canvas = Canvas(homeframe, bg="#fff")
    May6canvas.grid(row=0, column=0, sticky="news")
    May6canvas.create_text(130, 50, text="May 6 - Nashville, Tennessee",
                           font="inter 18 bold ", anchor=NW)
    May6canvas.create_image(0, 90, image=img58, anchor=NW)

    # Create a frame on the canvas to contain the buttons.
    May6Frame = Frame(May6canvas, bg="#fff", height=150, width=550,)
    May6Frame.rowconfigure(0, weight=1)
    May6Frame.columnconfigure(0, weight=1)
    May6Frame.place(x=0, y=500)
    Label(May6Frame, image=img50).place(x=0, y=0)

    # Add the buttons_frame to the canvas
    May6canvas.create_window((10, 535), window=May6Frame, anchor=NW)

    # Add a button to the buttons_frame using place method
    Button(May6Frame, border=0, bg="#fff", image=img57,
           cursor="hand2", command=May6click).place(x=12, y=27)
    Button(May6Frame, border=0, bg="#fff", image=img59,
           cursor="hand2", command=pic1May6click).place(x=147, y=27)
    Button(May6Frame, border=0, bg="#fff", image=img61,
           cursor="hand2", command=pic2May6click).place(x=282, y=27)
    Button(May6Frame, border=0, bg="#fff", image=img63,
           cursor="hand2", command=pic3May6click).place(x=418, y=27)

    # Configure the scrollbar
    May6scroll = Scrollbar(
        homeframe, command=May6canvas.yview, cursor="double_arrow")
    May6scroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    May6canvas.configure(yscrollcommand=May6scroll.set)

    # Set the scroll region of the canvas
    May6canvas.configure(scrollregion=May6canvas.bbox("all"))


def pic1May6click():
    canvas.grid_forget()
    May6canvas.create_image(0, 90, image=img60, anchor=NW)


def pic2May6click():
    canvas.grid_forget()
    May6canvas.create_image(0, 90, image=img62, anchor=NW)


def pic3May6click():
    canvas.grid_forget()
    May6canvas.create_image(0, 90, image=img64, anchor=NW)


def May5click():
    canvas.grid_forget()
    global May5canvas, May5Frame
    May5canvas = Canvas(homeframe, bg="#fff")
    May5canvas.grid(row=0, column=0, sticky="news")
    May5canvas.create_text(130, 50, text="May 5 - Nashville, Tennessee",
                           font="inter 18 bold ", anchor=NW)
    May5canvas.create_image(0, 90, image=img66, anchor=NW)

    # Create a frame on the canvas to contain the buttons.
    May5Frame = Frame(May5canvas, bg="#fff", height=150, width=550,)
    May5Frame.rowconfigure(0, weight=1)
    May5Frame.columnconfigure(0, weight=1)
    May5Frame.place(x=0, y=500)
    Label(May5Frame, image=img50).place(x=0, y=0)

    # Add the buttons_frame to the canvas
    May5canvas.create_window((10, 535), window=May5Frame, anchor=NW)

    # Add a button to the buttons_frame using place method
    Button(May5Frame, border=0, bg="#fff", image=img65,
           cursor="hand2", command=May5click).place(x=12, y=27)
    Button(May5Frame, border=0, bg="#fff", image=img67,
           cursor="hand2", command=pic1May5click).place(x=147, y=27)
    Button(May5Frame, border=0, bg="#fff", image=img69,
           cursor="hand2", command=pic2May5click).place(x=282, y=27)
    Button(May5Frame, border=0, bg="#fff", image=img71,
           cursor="hand2", command=pic3May5click).place(x=418, y=27)

    # Configure the scrollbar
    May5scroll = Scrollbar(
        homeframe, command=May5canvas.yview, cursor="double_arrow")
    May5scroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    May5canvas.configure(yscrollcommand=May5scroll.set)

    # Set the scroll region of the canvas
    May5canvas.configure(scrollregion=May5canvas.bbox("all"))


def pic1May5click():
    canvas.grid_forget()
    May5canvas.create_image(0, 90, image=img68, anchor=NW)


def pic2May5click():
    canvas.grid_forget()
    May5canvas.create_image(0, 90, image=img70, anchor=NW)


def pic3May5click():
    canvas.grid_forget()
    May5canvas.create_image(0, 90, image=img72, anchor=NW)


def May4click():
    canvas.grid_forget()
    global May4canvas, May4Frame
    May4canvas = Canvas(homeframe, bg="#fff")
    May4canvas.grid(row=0, column=0, sticky="news")
    May4canvas.create_text(30, 50, text="May 4 - Out with her mom in Nashville, Tennessee",
                           font="inter 16 bold ", anchor=NW)
    May4canvas.create_image(0, 90, image=img74, anchor=NW)

    # Create a frame on the canvas to contain the buttons.
    May4Frame = Frame(May4canvas, bg="#fff", height=150, width=550,)
    May4Frame.rowconfigure(0, weight=1)
    May4Frame.columnconfigure(0, weight=1)
    May4Frame.place(x=0, y=500)
    Label(May4Frame, image=img50).place(x=0, y=0)

    # Add the buttons_frame to the canvas
    May4canvas.create_window((10, 535), window=May4Frame, anchor=NW)

    # Add a button to the buttons_frame using place method
    Button(May4Frame, border=0, bg="#fff", image=img73,
           cursor="hand2", command=May4click).place(x=12, y=27)
    Button(May4Frame, border=0, bg="#fff", image=img75,
           cursor="hand2", command=pic1May4click).place(x=147, y=27)
    Button(May4Frame, border=0, bg="#fff", image=img77,
           cursor="hand2", command=pic2May4click).place(x=282, y=27)
    Button(May4Frame, border=0, bg="#fff", image=img79,
           cursor="hand2", command=pic3May4click).place(x=418, y=27)

    # Configure the scrollbar
    May4scroll = Scrollbar(
        homeframe, command=May4canvas.yview, cursor="double_arrow")
    May4scroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    May4canvas.configure(yscrollcommand=May4scroll.set)

    # Set the scroll region of the canvas
    May4canvas.configure(scrollregion=May4canvas.bbox("all"))


def pic1May4click():
    canvas.grid_forget()
    May4canvas.create_image(0, 90, image=img76, anchor=NW)


def pic2May4click():
    canvas.grid_forget()
    May4canvas.create_image(0, 90, image=img78, anchor=NW)


def pic3May4click():
    canvas.grid_forget()
    May4canvas.create_image(0, 90, image=img80, anchor=NW)


def April28click():
    canvas.grid_forget()
    global April28canvas, April28Frame
    April28canvas = Canvas(homeframe, bg="#fff")
    April28canvas.grid(row=0, column=0, sticky="news")
    April28canvas.create_text(170, 50, text="April 28 - Atlanta, Georgia",
                              font="inter 16 bold ", anchor=NW)
    April28canvas.create_image(0, 90, image=img83, anchor=NW)

    # Create a frame on the canvas to contain the buttons.
    April28Frame = Frame(April28canvas, bg="#fff", height=150, width=550,)
    April28Frame.rowconfigure(0, weight=1)
    April28Frame.columnconfigure(0, weight=1)
    April28Frame.place(x=0, y=500)
    Label(April28Frame, image=img50).place(x=0, y=0)

    # Add the buttons_frame to the canvas
    April28canvas.create_window((10, 535), window=April28Frame, anchor=NW)

    # Add a button to the buttons_frame using place method
    Button(April28Frame, border=0, bg="#fff", image=img82,
           cursor="hand2", command=April28click).place(x=12, y=27)
    Button(April28Frame, border=0, bg="#fff", image=img84,
           cursor="hand2", command=pic1April28click).place(x=147, y=27)
    Button(April28Frame, border=0, bg="#fff", image=img86,
           cursor="hand2", command=pic2April28click).place(x=282, y=27)
    Button(April28Frame, border=0, bg="#fff", image=img88,
           cursor="hand2", command=pic3April28click).place(x=418, y=27)

    # Configure the scrollbar
    April28scroll = Scrollbar(
        homeframe, command=April28canvas.yview, cursor="double_arrow")
    April28scroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    April28canvas.configure(yscrollcommand=April28scroll.set)

    # Set the scroll region of the canvas
    April28canvas.configure(scrollregion=April28canvas.bbox("all"))


def pic1April28click():
    canvas.grid_forget()
    April28canvas.create_image(0, 90, image=img85, anchor=NW)


def pic2April28click():
    canvas.grid_forget()
    April28canvas.create_image(0, 90, image=img87, anchor=NW)


def pic3April28click():
    canvas.grid_forget()
    April28canvas.create_image(0, 90, image=img89, anchor=NW)


def April21click():
    canvas.grid_forget()
    global April21canvas, April21Frame
    April21canvas = Canvas(homeframe, bg="#fff")
    April21canvas.grid(row=0, column=0, sticky="news")
    April21canvas.create_text(170, 50, text=" April 21 - Houston, Texas",
                              font="inter 16 bold ", anchor=NW)
    April21canvas.create_image(0, 90, image=img92, anchor=NW)

    # Create a frame on the canvas to contain the buttons.
    April21Frame = Frame(April21canvas, bg="#fff", height=150, width=550,)
    April21Frame.rowconfigure(0, weight=1)
    April21Frame.columnconfigure(0, weight=1)
    April21Frame.place(x=0, y=500)
    Label(April21Frame, image=img50).place(x=0, y=0)

    # Add the buttons_frame to the canvas
    April21canvas.create_window((10, 535), window=April21Frame, anchor=NW)

    # Add a button to the buttons_frame using place method
    Button(April21Frame, border=0, bg="#fff", image=img91,
           cursor="hand2", command=April21click).place(x=12, y=27)
    Button(April21Frame, border=0, bg="#fff", image=img93,
           cursor="hand2", command=pic1April21click).place(x=147, y=27)
    Button(April21Frame, border=0, bg="#fff", image=img95,
           cursor="hand2", command=pic2April21click).place(x=282, y=27)
    Button(April21Frame, border=0, bg="#fff", image=img97,
           cursor="hand2", command=pic3April21click).place(x=418, y=27)

    # Configure the scrollbar
    April21scroll = Scrollbar(
        homeframe, command=April21canvas.yview, cursor="double_arrow")
    April21scroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    April21canvas.configure(yscrollcommand=April21scroll.set)

    # Set the scroll region of the canvas
    April21canvas.configure(scrollregion=April21canvas.bbox("all"))


def pic1April21click():
    canvas.grid_forget()
    April21canvas.create_image(0, 90, image=img94, anchor=NW)


def pic2April21click():
    canvas.grid_forget()
    April21canvas.create_image(0, 90, image=img96, anchor=NW)


def pic3April21click():
    canvas.grid_forget()
    April21canvas.create_image(0, 90, image=img98, anchor=NW)


def Merchandise():

    global Merchcanvas, findentry
    Merchcanvas = Canvas(homeframe, bg="#fff")
    Merchcanvas.grid(row=0, column=0, sticky="news")

    Merchcanvas.create_image(0, 0, image=pic1, anchor=NW)

    # Create a frame on the canvas.
    topframe = Frame(Merchcanvas, bg="#ACB1D6", height=60, width=580)
    topframe.place(x=150, y=100)
    frameforbuttons1 = Frame(Merchcanvas, bg="#ACB1D6", height=260, width=200,)
    frameforbuttons1.place(x=150, y=100)
    frameforbuttons2 = Frame(Merchcanvas, bg="#ACB1D6", height=260, width=200,)
    frameforbuttons2.place(x=350, y=100)
    frameforbuttons3 = Frame(Merchcanvas, bg="#ACB1D6", height=260, width=200,)
    frameforbuttons3.place(x=350, y=100)
    frameforbuttons4 = Frame(Merchcanvas, bg="#ACB1D6", height=260, width=200,)
    frameforbuttons4.place(x=350, y=100)
    frameforbuttons6 = Frame(Merchcanvas, bg="#ACB1D6", height=260, width=200,)
    frameforbuttons6.place(x=350, y=100)
    frameforbuttons7 = Frame(Merchcanvas, bg="#ACB1D6", height=260, width=200,)
    frameforbuttons7.place(x=350, y=100)
    frameforbuttons8 = Frame(Merchcanvas, bg="#ACB1D6", height=260, width=200,)
    frameforbuttons8.place(x=350, y=100)
    frameforbuttons9 = Frame(Merchcanvas, bg="#ACB1D6", height=260, width=200,)
    frameforbuttons9.place(x=350, y=100)

    # Label
    Label(frameforbuttons1, image=pic2, bg="#ACB1D6").place(x=7, y=0)
    Label(frameforbuttons2, image=pic3, bg="#ACB1D6").place(x=0, y=5)
    Label(frameforbuttons3, image=pic5, bg="#ACB1D6").place(x=0, y=5)
    Label(frameforbuttons4, image=pic6, bg="#ACB1D6").place(x=10, y=15)
    Label(frameforbuttons6, image=pic8, bg="#ACB1D6").place(x=7, y=5)
    Label(frameforbuttons7, image=pic9, bg="#ACB1D6").place(x=0, y=5)
    Label(frameforbuttons8, image=pic10, bg="#ACB1D6").place(x=25, y=15)
    Label(frameforbuttons9, image=pic11, bg="#ACB1D6").place(x=35, y=0)
    Label(topframe, bg="#ACB1D6", image=pic17).place(x=20, y=13)

    # Entry
    findentry = Entry(topframe, bg='#fff', fg="#000",
                      width=65, font="inter 10", bd=0, foreground="#7D83B0")
    findentry.place(x=27, y=20)

    # button
    Button(topframe, image=pic4, bg="#ACB1D6", fg="#fff", bd=0,
           cursor="hand2", activebackground="#ACB1D6", command=searchclick).place(x=500, y=20)
    Button(topframe, image=pic18, bg="#ACB1D6", fg="#fff", bd=0,
           cursor="hand2", activebackground="#ACB1D6", command=cartclick).place(x=530, y=20)
    Button(frameforbuttons1, text="TAYLOR SWIFT THE ERAS TOUR \nGRAY CREWNECK\n$65", font="Garamond 8",
           bg="#ACB1D6", fg="#fff", bd=0, cursor="hand2", activebackground="#ACB1D6", activeforeground="#fff", justify=LEFT, command=Merch1).place(x=15, y=210)
    Button(frameforbuttons2, text="TAYLOR SWIFT THE ERAS TOUR \nBLACK T-SHIRT\n$45", font="Garamond 8",
           bg="#ACB1D6", fg="#fff", bd=0, cursor="hand2", activebackground="#ACB1D6", activeforeground="#fff", justify=LEFT, command=Merch2).place(x=15, y=210)
    Button(frameforbuttons3, text="TAYLOR SWIFT THE ERAS TOUR \n1989 ALBUM T-SHIRT\n$45", font="Garamond 8",
           bg="#ACB1D6", fg="#fff", bd=0, cursor="hand2", activebackground="#ACB1D6", activeforeground="#fff", justify=LEFT, command=Merch3).place(x=15, y=210)
    Button(frameforbuttons4, text="TAYLOR SWIFT THE ERAS TOUR \nBEIGE HOODIE\n$75", font="Garamond 8",
           bg="#ACB1D6", fg="#fff", bd=0, cursor="hand2", activebackground="#ACB1D6", activeforeground="#fff", justify=LEFT, command=Merch4).place(x=15, y=210)
    Button(frameforbuttons6, text="TAYLOR SWIFT BEJEWELED \nBRACELET\n$35", font="Garamond 8",
           bg="#ACB1D6", fg="#fff", bd=0, cursor="hand2", activebackground="#ACB1D6", activeforeground="#fff", justify=LEFT, command=Merch6).place(x=15, y=210)
    Button(frameforbuttons7, text="TAYLOR SWIFT THE ERAS TOUR \nLOVER ALBUM T-SHIRT\n$45", font="Garamond 8",
           bg="#ACB1D6", fg="#fff", bd=0, cursor="hand2", activebackground="#ACB1D6", activeforeground="#fff", justify=LEFT, command=Merch7).place(x=15, y=210)
    Button(frameforbuttons8, text="TAYLOR SWIFT THE ERAS TOUR \nEARBUD CASE\n$15", font="Garamond 8",
           bg="#ACB1D6", fg="#fff", bd=0, cursor="hand2", activebackground="#ACB1D6", activeforeground="#fff", justify=LEFT, command=Merch8).place(x=15, y=210)
    Button(frameforbuttons9, text="TAYLOR SWIFT THE ERAS TOUR \nBLACK SWEATPANTS\n$65", font="Garamond 8",
           bg="#ACB1D6", fg="#fff", bd=0, cursor="hand2", activebackground="#ACB1D6", activeforeground="#fff", justify=LEFT, command=Merch9).place(x=15, y=210)

    # Add the frame to the canvas
    Merchcanvas.create_window((0, 0), window=topframe, anchor=NW)
    Merchcanvas.create_window((60, 105), window=frameforbuttons1, anchor=NW)
    Merchcanvas.create_window((290, 105), window=frameforbuttons2, anchor=NW)
    Merchcanvas.create_window((60, 385), window=frameforbuttons3, anchor=NW)
    Merchcanvas.create_window((290, 385), window=frameforbuttons4, anchor=NW)
    Merchcanvas.create_window((60, 665), window=frameforbuttons6, anchor=NW)
    Merchcanvas.create_window((290, 665), window=frameforbuttons7, anchor=NW)
    Merchcanvas.create_window((60, 945), window=frameforbuttons8, anchor=NW)
    Merchcanvas.create_window((290, 945), window=frameforbuttons9, anchor=NW)

    # Configure the scrollbar
    galleryscroll = Scrollbar(
        homeframe, command=Merchcanvas.yview, cursor="double_arrow")
    galleryscroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    Merchcanvas.configure(yscrollcommand=galleryscroll.set)

    # Set the scroll region of the canvas
    Merchcanvas.configure(scrollregion=Merchcanvas.bbox("all"))


def Merch1():
    global Merch1Spinbox
    Merch1Frame = Frame(Merchcanvas, bg="#fff", width=450, height=300)
    Merch1Frame.place(x=60, y=100)

    Label(Merch1Frame, text="TAYLOR SWIFT THE ERAS \nTOUR GRAY CREWNECK\n\n$65", font="Garamond 12 bold",
          bg="#fff", fg="#8294C4", justify=LEFT).place(x=210, y=50)
    Label(Merch1Frame, image=pic2, bg="#fff").place(x=10, y=50)

    Merch1Spinbox = Spinbox(Merch1Frame, from_=0, to=100, width=10,
                            justify=CENTER, textvariable=Merch1Spy, fg="#8294C4")
    Merch1Spinbox.place(x=210, y=150)

    Button(Merch1Frame, image=pic12, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch1Frame.destroy()).place(x=210, y=200)
    Button(Merch1Frame, image=pic13, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=cartclick).place(x=350, y=200)
    Button(Merch1Frame, image=pic14, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch1Frame.destroy()).place(x=420, y=10)


def Merch2():
    Merch2Frame = Frame(Merchcanvas, bg="#fff", width=450, height=300)
    Merch2Frame.place(x=60, y=100)

    Label(Merch2Frame, text="TAYLOR SWIFT THE ERAS \nTOUR BLACK T-SHIRT\n\n$45", font="Garamond 12 bold",
          bg="#fff", fg="#8294C4", justify=LEFT).place(x=210, y=50)
    Label(Merch2Frame, image=pic3, bg="#fff").place(x=10, y=50)

    Merch2Spinbox = Spinbox(Merch2Frame, from_=0, to=100, width=10,
                            justify=CENTER, textvariable=Merch2Spy, fg="#8294C4")
    Merch2Spinbox.place(x=210, y=150)

    Button(Merch2Frame, image=pic12, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch2Frame.destroy()).place(x=210, y=200)
    Button(Merch2Frame, image=pic13, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=cartclick).place(x=350, y=200)
    Button(Merch2Frame, image=pic14, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch2Frame.destroy()).place(x=420, y=10)


def Merch3():
    Merch3Frame = Frame(Merchcanvas, bg="#fff", width=450, height=300)
    Merch3Frame.place(x=60, y=100)

    Label(Merch3Frame, text="TAYLOR SWIFT THE ERAS \nTOUR 1989 ALBUM T-SHIRT\n$45", font="Garamond 12 bold",
          bg="#fff", fg="#8294C4", justify=LEFT).place(x=210, y=50)
    Label(Merch3Frame, image=pic5, bg="#fff").place(x=10, y=50)

    Merch3Spinbox = Spinbox(Merch3Frame, from_=0, to=100, width=10,
                            justify=CENTER, textvariable=Merch3Spy, fg="#8294C4")
    Merch3Spinbox.place(x=210, y=150)

    Button(Merch3Frame, image=pic12, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch3Frame.destroy()).place(x=210, y=200)
    Button(Merch3Frame, image=pic13, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=cartclick).place(x=350, y=200)
    Button(Merch3Frame, image=pic14, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch3Frame.destroy()).place(x=420, y=10)


def Merch4():
    Merch4Frame = Frame(Merchcanvas, bg="#fff", width=450, height=300)
    Merch4Frame.place(x=60, y=100)

    Label(Merch4Frame, text="TAYLOR SWIFT THE ERAS \nTOUR BEIGE HOODIE\n\n$75", font="Garamond 12 bold",
          bg="#fff", fg="#8294C4", justify=LEFT).place(x=210, y=50)
    Label(Merch4Frame, image=pic6, bg="#fff").place(x=10, y=50)

    Merch4Spinbox = Spinbox(Merch4Frame, from_=0, to=100, width=10,
                            justify=CENTER, textvariable=Merch4Spy, fg="#8294C4")
    Merch4Spinbox.place(x=210, y=150)

    Button(Merch4Frame, image=pic12, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch4Frame.destroy()).place(x=210, y=200)
    Button(Merch4Frame, image=pic13, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=cartclick).place(x=350, y=200)
    Button(Merch4Frame, image=pic14, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch4Frame.destroy()).place(x=420, y=10)


def Merch6():
    Merch6Frame = Frame(Merchcanvas, bg="#fff", width=450, height=300)
    Merch6Frame.place(x=60, y=100)

    Label(Merch6Frame, text="TAYLOR SWIFT BEJEWELED \nBRACELET\n\n$35", font="Garamond 12 bold",
          bg="#fff", fg="#8294C4", justify=LEFT).place(x=210, y=50)
    Label(Merch6Frame, image=pic8, bg="#fff").place(x=10, y=50)

    Merch6Spinbox = Spinbox(Merch6Frame, from_=0, to=100, width=10,
                            justify=CENTER, textvariable=Merch6Spy, fg="#8294C4")
    Merch6Spinbox.place(x=210, y=150)

    Button(Merch6Frame, image=pic12, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch6Frame.destroy()).place(x=210, y=200)
    Button(Merch6Frame, image=pic13, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=cartclick).place(x=350, y=200)
    Button(Merch6Frame, image=pic14, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch6Frame.destroy()).place(x=420, y=10)


def Merch7():
    Merch7Frame = Frame(Merchcanvas, bg="#ECC9EE", width=480, height=300)
    Merch7Frame.place(x=60, y=100)

    Label(Merch7Frame, text="TAYLOR SWIFT THE ERAS \nTOUR LOVER ALBUM T-SHIRT\n\n$45", font="Garamond 12 bold",
          bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=210, y=50)
    Label(Merch7Frame, image=pic9, bg="#ECC9EE").place(x=10, y=50)

    Merch7Spinbox = Spinbox(Merch7Frame, from_=0, to=100, width=10,
                            justify=CENTER, textvariable=Merch7Spy, fg="#8294C4")
    Merch7Spinbox.place(x=210, y=150)

    Button(Merch7Frame, image=pic12, bd=0, cursor="hand2", activebackground="#ECC9EE",
           activeforeground="#fff", bg="#ECC9EE", command=lambda: Merch7Frame.destroy()).place(x=210, y=200)
    Button(Merch7Frame, image=pic13, bd=0, cursor="hand2", activebackground="#ECC9EE",
           activeforeground="#fff", bg="#ECC9EE", command=cartclick).place(x=350, y=200)
    Button(Merch7Frame, image=pic14, bd=0, cursor="hand2", activebackground="#ECC9EE",
           activeforeground="#fff", bg="#ECC9EE", command=lambda: Merch7Frame.destroy()).place(x=450, y=10)


def Merch8():
    Merch8Frame = Frame(Merchcanvas, bg="#fff", width=450, height=300)
    Merch8Frame.place(x=60, y=100)

    Label(Merch8Frame, text="TAYLOR SWIFT THE ERAS \nTOUR EARBUD CASE\n\n$15", font="Garamond 12 bold",
          bg="#fff", fg="#8294C4", justify=LEFT).place(x=210, y=50)
    Label(Merch8Frame, image=pic10, bg="#fff").place(x=10, y=50)

    Merch8Spinbox = Spinbox(Merch8Frame, from_=0, to=100, width=10,
                            justify=CENTER, textvariable=Merch8Spy, fg="#8294C4")
    Merch8Spinbox.place(x=210, y=150)

    Button(Merch8Frame, image=pic12, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch8Frame.destroy()).place(x=210, y=200)
    Button(Merch8Frame, image=pic13, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=cartclick).place(x=350, y=200)
    Button(Merch8Frame, image=pic14, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch8Frame.destroy()).place(x=420, y=10)


def Merch9():
    Merch9Frame = Frame(Merchcanvas, bg="#fff", width=450, height=300)
    Merch9Frame.place(x=60, y=100)

    Label(Merch9Frame, text="TAYLOR SWIFT THE ERAS \nTOUR BLACK SWEATPANTS\n\n$65", font="Garamond 12 bold",
          bg="#fff", fg="#8294C4", justify=LEFT).place(x=210, y=50)
    Label(Merch9Frame, image=pic11, bg="#fff").place(x=40, y=40)

    Merch9Spinbox = Spinbox(Merch9Frame, from_=0, to=100, width=10,
                            justify=CENTER, textvariable=Merch9Spy, fg="#8294C4")
    Merch9Spinbox.place(x=210, y=150)

    Button(Merch9Frame, image=pic12, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch9Frame.destroy()).place(x=210, y=200)
    Button(Merch9Frame, image=pic13, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=cartclick).place(x=350, y=200)
    Button(Merch9Frame, image=pic14, bd=0, cursor="hand2", activebackground="#fff",
           activeforeground="#fff", bg="#fff", command=lambda: Merch9Frame.destroy()).place(x=420, y=10)


def searchclick():  # เสร็จแล้ว
    global findbox, SearchFrame
    SearchFrame = Frame(homeframe, bg="#fff")
    SearchFrame.grid(row=0, column=0, sticky="news", columnspan=2, rowspan=10)

    # create top frame for searching
    topside = Frame(SearchFrame, bg="#ACB1D6", height=60, width=600)
    topside.place(x=0, y=0)
    Label(topside, bg="#ACB1D6", image=pic17).place(x=20, y=13)
    findbox = Entry(topside, bg='#fff', fg="#000",
                    width=65, font="inter 10", bd=0, foreground="#7D83B0")
    findbox.place(x=27, y=20)
    Button(topside, image=pic4, bg="#ACB1D6", fg="#fff", bd=0,
           cursor="hand2", activebackground="#ACB1D6", command=findboxclick).place(x=500, y=20)
    Button(topside, image=pic18, bg="#ACB1D6", fg="#fff", bd=0,
           cursor="hand2", activebackground="#ACB1D6", command=cartclick).place(x=530, y=20)

    print(findentry.get())

    # define sql command or sql statement for searching
    sql = "select * from Merch where Name=?;"
    # execute sql using cursor
    cursor.execute(sql, [findentry.get()])
    # fetch result
    result = cursor.fetchone()

    if findentry.get() == "TAYLOR SWIFT THE ERAS TOUR GRAY CREWNECK" or findentry.get() == "GRAY CREWNECK":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS TOUR \nGRAY CREWNECK\n$65",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic2, bg="#ACB1D6").place(x=10, y=20)
        Merch1Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch1Spy, fg="#8294C4")
        Merch1Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findentry.get() == "TAYLOR SWIFT THE ERAS TOUR BLACK T-SHIRT" or findentry.get() == "BLACK T-SHIRT":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS TOUR \nBLACK T-SHIRT\n$45",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic3, bg="#ACB1D6").place(x=0, y=20)
        Merch2Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch2Spy, fg="#8294C4")
        Merch2Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findentry.get() == "TAYLOR SWIFT THE ERAS TOUR 1989 ALBUM T-SHIRT" or findentry.get() == "1989 ALBUM T-SHIRT" or findentry.get() == "1989 ALBUM":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS \nTOUR 1989 ALBUM T-SHIRT\n$45",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic5, bg="#ACB1D6").place(x=0, y=20)
        Merch3Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch3Spy, fg="#8294C4")
        Merch3Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findentry.get() == "TAYLOR SWIFT THE ERAS TOUR BEIGE HOODIE" or findentry.get() == "BEIGE HOODIE":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS \nTOUR BEIGE HOODIE\n$35",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic6, bg="#ACB1D6").place(x=10, y=20)
        Merch4Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch4Spy, fg="#8294C4")
        Merch4Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findentry.get() == "TAYLOR SWIFT BEJEWELED BRACELET" or findentry.get() == "BRACELET":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT BEJEWELED \nBRACELET\n$35",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic8, bg="#ACB1D6").place(x=10, y=20)
        Merch6Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch6Spy, fg="#8294C4")
        Merch6Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findentry.get() == "TAYLOR SWIFT THE ERAS TOUR LOVER ALBUM T-SHIRT" or findentry.get() == "LOVER T-SHIRT":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS \nTOUR LOVER ALBUM T-SHIRT\n$45",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic9, bg="#ACB1D6").place(x=0, y=20)
        Merch7Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch7Spy, fg="#8294C4")
        Merch7Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findentry.get() == "TAYLOR SWIFT THE ERAS TOUR EARBUD CASE" or findentry.get() == "EARBUD CASE":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS \nTOUR EARBUD CASE\n$15",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic10, bg="#ACB1D6").place(x=25, y=20)
        Merch8Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch8Spy, fg="#8294C4")
        Merch8Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findentry.get() == "TAYLOR SWIFT THE ERAS TOUR BLACK SWEATPANTS" or findentry.get() == "BLACK SWEATPANTS":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS \nTOUR BLACK SWEATPANTS\n$65",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic11, bg="#ACB1D6").place(x=40, y=0)
        Merch9Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch9Spy, fg="#8294C4")
        Merch9Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    else:
        Label(SearchFrame, text="OOPS!", font="inter 20 bold",
              bg="#fff", fg="#ACB1D6").place(x=250, y=100)
        Label(SearchFrame, image=pic27).place(x=170, y=150)
        Label(SearchFrame, text="There is no Merch found. Please click below for go back to Merchandise",
              font="inter 13", bg="#fff", fg="#ACB1D6").place(x=40, y=400)
        Button(SearchFrame, image=pic28, bd=0, cursor="hand2", activebackground="#fff",
               activeforeground="#ACB1D6", bg="#fff", command=Merchandise).place(x=220, y=450)


def findboxclick():  # เสร็จแล้ว
    # define sql command or sql statement for searching
    sql = "select * from Merch where Name=?;"
    # execute sql using cursor
    cursor.execute(sql, [findentry.get()])
    # fetch result
    result = cursor.fetchone()

    if findbox.get() == "TAYLOR SWIFT THE ERAS TOUR GRAY CREWNECK" or findbox.get() == "GRAY CREWNECK":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS TOUR \nGRAY CREWNECK\n$65",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic2, bg="#ACB1D6").place(x=10, y=20)
        Merch1Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch1Spy, fg="#8294C4")
        Merch1Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findbox.get() == "TAYLOR SWIFT THE ERAS TOUR BLACK T-SHIRT" or findbox.get() == "BLACK T-SHIRT":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS TOUR \nBLACK T-SHIRT\n$45",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic3, bg="#ACB1D6").place(x=0, y=20)
        Merch2Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch2Spy, fg="#8294C4")
        Merch2Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findbox.get() == "TAYLOR SWIFT THE ERAS TOUR 1989 ALBUM T-SHIRT" or findbox.get() == "1989 ALBUM T-SHIRT" or findbox.get() == "1989 ALBUM":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS \nTOUR 1989 ALBUM T-SHIRT\n$45",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic5, bg="#ACB1D6").place(x=0, y=20)
        Merch3Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch3Spy, fg="#8294C4")
        Merch3Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findbox.get() == "TAYLOR SWIFT THE ERAS TOUR BEIGE HOODIE" or findbox.get() == "BEIGE HOODIE":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS \nTOUR BEIGE HOODIE\n$35",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic6, bg="#ACB1D6").place(x=10, y=20)
        Merch4Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch4Spy, fg="#8294C4")
        Merch4Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findbox.get() == "TAYLOR SWIFT BEJEWELED BRACELET" or findbox.get() == "BRACELET":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT BEJEWELED \nBRACELET\n$35",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic8, bg="#ACB1D6").place(x=10, y=20)
        Merch6Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch6Spy, fg="#8294C4")
        Merch6Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findbox.get() == "TAYLOR SWIFT THE ERAS TOUR LOVER ALBUM T-SHIRT" or findbox.get() == "LOVER T-SHIRT":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS \nTOUR LOVER ALBUM T-SHIRT\n$45",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic9, bg="#ACB1D6").place(x=0, y=20)
        Merch7Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch7Spy, fg="#8294C4")
        Merch7Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findbox.get() == "TAYLOR SWIFT THE ERAS TOUR EARBUD CASE" or findbox.get() == "EARBUD CASE":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS \nTOUR EARBUD CASE\n$15",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic10, bg="#ACB1D6").place(x=25, y=20)
        Merch8Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch8Spy, fg="#8294C4")
        Merch8Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    elif findbox.get() == "TAYLOR SWIFT THE ERAS TOUR BLACK SWEATPANTS" or findbox.get() == "BLACK SWEATPANTS":
        M1Frame = Frame(SearchFrame, bg="#ACB1D6", height=250, width=470)
        M1Frame.place(x=60, y=100)
        Label(M1Frame, text="TAYLOR SWIFT THE ERAS \nTOUR BLACK SWEATPANTS\n$65",
              font="Garamond 12 bold", bg="#ACB1D6", fg="#fff", justify=LEFT).place(x=200, y=30)
        Label(M1Frame, image=pic11, bg="#ACB1D6").place(x=40, y=0)
        Merch9Spinbox = Spinbox(M1Frame, from_=0, to=100, width=10,
                                justify=CENTER, textvariable=Merch9Spy, fg="#8294C4")
        Merch9Spinbox.place(x=200, y=100)
        Button(M1Frame, image=pic15, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=Merchandise).place(x=200, y=150)
        Button(M1Frame, image=pic16, bd=0, cursor="hand2", activebackground="#ACB1D6",
               activeforeground="#ACB1D6", bg="#ACB1D6", command=cartclick).place(x=350, y=150)
        findbox.insert(0, result[1])

    else:
        Label(SearchFrame, text="OOPS!", font="inter 20 bold",
              bg="#fff", fg="#ACB1D6").place(x=250, y=100)
        Label(SearchFrame, image=pic27).place(x=170, y=150)
        Label(SearchFrame, text="There is no Merch found. Please click below for go back to Merchandise",
              font="inter 13", bg="#fff", fg="#ACB1D6").place(x=40, y=400)
        Button(SearchFrame, image=pic28, bd=0, cursor="hand2", activebackground="#fff",
               activeforeground="#ACB1D6", bg="#fff", command=Merchandise).place(x=220, y=450)


def cartclick():  # เสร็จแล้ว
    global cartcanvas
    cartcanvas = Canvas(homeframe, bg="#ECC9EE")
    cartcanvas.grid(row=0, column=0, sticky="news", rowspan=10)
    cartcanvas.create_text(230, 50, text="Your Cart",
                           fill="#8294C4", font="inter 20 bold", anchor=NW)
    cartcanvas.create_text(40, 110, text="Merch",
                           fill="#8294C4", font="inter 12", anchor=NW)
    cartcanvas.create_text(180, 110, text="Description",
                           fill="#8294C4", font="inter 12", anchor=NW)
    cartcanvas.create_text(370, 110, text="Quantity",
                           fill="#8294C4", font="inter 12", anchor=NW)
    cartcanvas.create_text(500, 110, text="Price",
                           fill="#8294C4", font="inter 12", anchor=NW)
    cartcanvas.create_text(0, 110, text=("___"*15),
                           fill="#D4ADFC", font="inter 18 ", anchor=NW)

    total = 0
    total += (Merch1Spy.get()*65) + (Merch2Spy.get()*45) + (Merch3Spy.get()*45) + (Merch4Spy.get()*75) + \
        (Merch6Spy.get()*35) + (Merch7Spy.get()*45) + \
        (Merch8Spy.get()*15) + (Merch9Spy.get()*65)
    for i, merch in enumerate(MerchName):

        if Merch1Spy.get() > 0:
            Merch1Frame = Frame(cartcanvas, bg="#ECC9EE",
                                width=550, height=100)
            Merch1Frame.place(x=0, y=i+100)
            cartcanvas.create_window((0, i+150), window=Merch1Frame, anchor=NW)
            Label(Merch1Frame, text="TAYLOR SWIFT THE ERAS \nTOUR GRAY CREWNECK", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=130, y=20)
            Label(Merch1Frame, image=pic19,
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=20, y=10)
            Merch1Spinbox = Spinbox(Merch1Frame, from_=0, to=100, width=10,
                                    justify=CENTER, textvariable=Merch1Spy, fg="#8294C4")
            Merch1Spinbox.place(x=360, y=30)
            Label(Merch1Frame, text="$65", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=505, y=30)
            i += 150

        if Merch2Spy.get() > 0:
            Merch2Frame = Frame(cartcanvas, bg="#ECC9EE",
                                width=550, height=100)
            Merch2Frame.place(x=0, y=i+100)
            cartcanvas.create_window((0, i+150), window=Merch2Frame, anchor=NW)
            Label(Merch2Frame, text="TAYLOR SWIFT THE ERAS \nTOUR BLACK T-SHIRT", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=130, y=20)
            Label(Merch2Frame, image=pic20,
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=20, y=10)
            Merch2Spinbox = Spinbox(Merch2Frame, from_=0, to=100, width=10,
                                    justify=CENTER, textvariable=Merch2Spy, fg="#8294C4")
            Merch2Spinbox.place(x=360, y=30)
            Label(Merch2Frame, text="$45", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=505, y=30)
            i += 150

        if Merch3Spy.get() > 0:
            Merch3Frame = Frame(cartcanvas, bg="#ECC9EE",
                                width=550, height=100)
            Merch3Frame.place(x=0, y=i+150)
            cartcanvas.create_window((0, i+150), window=Merch3Frame, anchor=NW)
            Label(Merch3Frame, text="TAYLOR SWIFT THE ERAS \nTOUR 1989 ALBUM T-SHIRT", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=130, y=20)
            Label(Merch3Frame, image=pic21,
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=20, y=10)
            Merch3Spinbox = Spinbox(Merch3Frame, from_=0, to=100, width=10,
                                    justify=CENTER, textvariable=Merch3Spy, fg="#8294C4")
            Merch3Spinbox.place(x=360, y=30)
            Label(Merch3Frame, text="$45", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=505, y=30)
            i += 150

        if Merch4Spy.get() > 0:
            Merch4Frame = Frame(cartcanvas, bg="#ECC9EE",
                                width=550, height=100)
            Merch4Frame.place(x=0, y=i+150)
            cartcanvas.create_window((0, i+150), window=Merch4Frame, anchor=NW)
            Label(Merch4Frame, text="TAYLOR SWIFT THE ERAS \nTOUR BEIGE HOODIE", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=130, y=20)
            Label(Merch4Frame, image=pic22,
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=20, y=10)
            Merch4Spinbox = Spinbox(Merch4Frame, from_=0, to=100, width=10,
                                    justify=CENTER, textvariable=Merch4Spy, fg="#8294C4")
            Merch4Spinbox.place(x=360, y=30)
            Label(Merch4Frame, text="$75", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=505, y=30)
            i += 150

        if Merch6Spy.get() > 0:
            Merch6Frame = Frame(cartcanvas, bg="#ECC9EE",
                                width=550, height=100)
            Merch6Frame.place(x=0, y=i+150)
            cartcanvas.create_window((0, i+150), window=Merch6Frame, anchor=NW)
            Label(Merch6Frame, text="TAYLOR SWIFT BEJEWELED \nBRACELET", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=130, y=20)
            Label(Merch6Frame, image=pic23,
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=20, y=10)
            Merch6Spinbox = Spinbox(Merch6Frame, from_=0, to=100, width=10,
                                    justify=CENTER, textvariable=Merch6Spy, fg="#8294C4")
            Merch6Spinbox.place(x=360, y=30)
            Label(Merch6Frame, text="$35", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=505, y=30)
            i += 150

        if Merch7Spy.get() > 0:
            Merch7Frame = Frame(cartcanvas, bg="#ECC9EE",
                                width=550, height=100)
            Merch7Frame.place(x=0, y=i+150)
            cartcanvas.create_window((0, i+150), window=Merch7Frame, anchor=NW)
            Label(Merch7Frame, text="TAYLOR SWIFT THE ERAS \nTOUR LOVER ALBUM T-SHIRT", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=130, y=20)
            Label(Merch7Frame, image=pic24,
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=20, y=10)
            Merch7Spinbox = Spinbox(Merch7Frame, from_=0, to=100, width=10,
                                    justify=CENTER, textvariable=Merch7Spy, fg="#8294C4")
            Merch7Spinbox.place(x=360, y=30)
            Label(Merch7Frame, text="$45", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=505, y=30)
            i += 150

        if Merch8Spy.get() > 0:
            Merch8Frame = Frame(cartcanvas, bg="#ECC9EE",
                                width=550, height=100)
            Merch8Frame.place(x=0, y=i+150)
            cartcanvas.create_window((0, i+150), window=Merch8Frame, anchor=NW)
            Label(Merch8Frame, text="TAYLOR SWIFT THE ERAS \nTOUR EARBUD CASE", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=130, y=20)
            Label(Merch8Frame, image=pic25,
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=20, y=10)
            Merch8Spinbox = Spinbox(Merch8Frame, from_=0, to=100, width=10,
                                    justify=CENTER, textvariable=Merch8Spy, fg="#8294C4")
            Merch8Spinbox.place(x=360, y=30)
            Label(Merch8Frame, text="$15", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=505, y=30)
            i += 150

        if Merch9Spy.get() > 0:
            Merch9Frame = Frame(cartcanvas, bg="#ECC9EE",
                                width=550, height=100)
            Merch9Frame.place(x=0, y=i+150)
            cartcanvas.create_window((0, i+150), window=Merch9Frame, anchor=NW)
            Label(Merch9Frame, text="TAYLOR SWIFT THE ERAS \nTOUR BLACK SWEATPANTS", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=130, y=20)
            Label(Merch9Frame, image=pic26,
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=40, y=10)
            Merch9Spinbox = Spinbox(Merch9Frame, from_=0, to=100, width=10,
                                    justify=CENTER, textvariable=Merch9Spy, fg="#8294C4")
            Merch9Spinbox.place(x=360, y=30)
            Label(Merch9Frame, text="$65", font="inter 10 ",
                  bg="#ECC9EE", fg="#8294C4", justify=LEFT).place(x=505, y=30)
            i += 150

        if Merch1Spy.get() > 0 or Merch2Spy.get() > 0 or Merch3Spy.get() > 0 or Merch4Spy.get() > 0 or Merch6Spy.get() > 0 or Merch7Spy.get() > 0 or Merch8Spy.get() > 0 or Merch9Spy.get() > 0:
            ButtonFrame = Frame(cartcanvas, bg="#ECC9EE",
                                width=570, height=160)
            ButtonFrame.place(x=0, y=i+150)
            cartcanvas.create_window((0, i+100), window=ButtonFrame, anchor=NW)
            Button(ButtonFrame, image=pic28, bg="#ECC9EE", fg="#fff", bd=0,
                   cursor="hand2", activebackground="#ECC9EE", command=Merchandise).place(x=120, y=120)
            Button(ButtonFrame, image=pic29, bg="#ECC9EE", fg="#fff", bd=0,
                   cursor="hand2", activebackground="#ECC9EE", command=Checkout).place(x=320, y=120)
            Label(ButtonFrame, text=("___"*15), fg="#D4ADFC",
                  bg="#ECC9EE", font="inter 18 ").place(x=0, y=10)
            Label(ButtonFrame, text="Total Price : "+"\nShipping : ", fg="#8294C4",
                  bg="#ECC9EE", font="inter 10 bold", justify=RIGHT).place(x=20, y=50)
            Label(ButtonFrame, text="$"+str(total)+"\nFree", fg="#8294C4",
                  bg="#ECC9EE", font="inter 10 bold", justify=RIGHT).place(x=350, y=50)

        else:
            emptyframe = Frame(cartcanvas, bg="#fff",
                               width=600, height=550)
            emptyframe.place(x=0, y=0)

            Label(emptyframe, image=pic30, bg="#fff",
                  font="inter 18 ").place(x=30, y=0)
            Button(emptyframe, text="Back to \nMerchandise", bg="#267dfa", fg="#ffffff",
                   bd=0, activebackground="#267dfa", activeforeground="#fff", font="inter 11 bold",
                   command=Merchandise).place(x=260, y=426)

    # Configure the scrollbar
    cartscroll = Scrollbar(
        homeframe, command=cartcanvas.yview, cursor="double_arrow")
    cartscroll.place(x=565, y=0, height=520, width=25)

    # Set the scrollbar to scroll the canvas
    cartcanvas.configure(yscrollcommand=cartscroll.set)

    # Set the scroll region of the canvas
    cartcanvas.configure(scrollregion=cartcanvas.bbox("all"))


def Checkout():
    global Checkoutcanvas
    Checkoutcanvas = Canvas(homeframe, bg="#ECC9EE")
    Checkoutcanvas.grid(row=0, column=0, sticky="news", rowspan=10)

    # checkbox
    CheckBTFrame = Frame(Checkoutcanvas, bg="#ECC9EE", height=100, width=600)
    CheckBTFrame.place(x=0, y=0)
    Checkoutcanvas.create_window((0, 0), window=CheckBTFrame, anchor=NW)
    Button(CheckBTFrame, image=pic32, bg="#ECC9EE", font="inter 15 ",
           activebackground="#ECC9EE", border=0,command=finalclick).place(x=50, y=30)
    Button(CheckBTFrame, image=pic33, bg="#ECC9EE", font="inter 15 ",
           activebackground="#ECC9EE", border=0, command=Add_Address_click).place(x=350, y=30)


def Add_Address_click():
    global Namebox,Numberbox,Addressbox,Districtbox,Provincetbox,Pincodebox
    AddressFrame = Frame(Checkoutcanvas, bg="#ECC9EE", height=450, width=600)
    AddressFrame.grid(row=0, column=0, sticky="news", columnspan=2, rowspan=10)
    Checkoutcanvas.create_window((0, 100), window=AddressFrame, anchor=NW)

    Label(AddressFrame,text="Name :",bg="#ECC9EE",fg="#6241C0",font="inter 12 ").place(x=150,y=50)
    Label(AddressFrame,text="Phone Number :",bg="#ECC9EE",fg="#6241C0",font="inter 12 ").place(x=90,y=100)
    Label(AddressFrame,text="Address (Area and Street) :",bg="#ECC9EE",fg="#6241C0",font="inter 12 ").place(x=10,y=150)
    Label(AddressFrame,text="District :",bg="#ECC9EE",fg="#6241C0",font="inter 12 ").place(x=140,y=200)
    Label(AddressFrame,text="Province :",bg="#ECC9EE",fg="#6241C0",font="inter 12 ").place(x=130,y=250)
    Label(AddressFrame,text="Pincode :",bg="#ECC9EE",fg="#6241C0",font="inter 12 ").place(x=130,y=300)
    Label(AddressFrame,image=pic34,bg="#ECC9EE").place(x=240,y=43)
    Namebox = Entry(AddressFrame, bg='#fff', fg="#000",
                    width=33, font="inter 12", bd=0, foreground="#6241C0",background="#fff")
    Namebox.place(x=250, y=50)
    Label(AddressFrame,image=pic34,bg="#ECC9EE").place(x=240,y=93)
    Numberbox = Entry(AddressFrame, bg='#fff', fg="#000",
                    width=33, font="inter 12", bd=0, foreground="#6241C0",background="#fff")
    Numberbox.place(x=250, y=100)
    Label(AddressFrame,image=pic34,bg="#ECC9EE").place(x=240,y=143)
    Addressbox = Entry(AddressFrame, bg='#fff', fg="#000",
                    width=33, font="inter 12", bd=0, foreground="#6241C0",background="#fff")
    Addressbox.place(x=250, y=150)
    Label(AddressFrame,image=pic34,bg="#ECC9EE").place(x=240,y=193)
    Districtbox = Entry(AddressFrame, bg='#fff', fg="#000",
                    width=33, font="inter 12", bd=0, foreground="#6241C0",background="#fff")
    Districtbox.place(x=250, y=200)
    Label(AddressFrame,image=pic34,bg="#ECC9EE").place(x=240,y=243)
    Provincetbox = Entry(AddressFrame, bg='#fff', fg="#000",
                    width=33, font="inter 12", bd=0, foreground="#6241C0",background="#fff")
    Provincetbox.place(x=250, y=250)
    Label(AddressFrame,image=pic35,bg="#ECC9EE").place(x=240,y=293)
    Pincodebox = Entry(AddressFrame, bg='#fff', fg="#000",
                    width=6, font="inter 12", bd=0, foreground="#6241C0",background="#fff")
    Pincodebox.place(x=250, y=300)
    Button(AddressFrame, image=pic36, bg="#ECC9EE",
           activebackground="#ECC9EE", border=0, command=cartclick).place(x=150, y=370)
    Button(AddressFrame, image=pic37, bg="#ECC9EE",
           activebackground="#ECC9EE", border=0,command=purchaseclick).place(x=300, y=370)
    
    # define sql command or sql statement for add result
    sql = "select * from login where user=?;"
    # execute sql using cursor
    cursor.execute(sql, [userEntry.get()])
    # fetch result
    result = cursor.fetchone()
    Namebox.insert(0,result[2]+"        "+result[3])
    
        
def purchaseclick() :
    # define sql command or sql statement for searching
    sql = "select * from login where user=?;"
    # execute sql using cursor
    cursor.execute(sql, [userEntry.get()])
    # fetch result
    result = cursor.fetchone()
    

    if Numberbox.get() == "" or Addressbox.get() == "" or Districtbox.get() == "" or Provincetbox.get() == "" or Pincodebox.get() == "":
        messagebox.showwarning("Swifter: ","Please fullfill all of data")
        Numberbox.focus_force()

    elif result:
            #define insert command for insert a new record into the table
            sql = "insert into shipping_address (Phone_number,Address,District,Province,Pincode) values(?,?,?,?,?);"
            #execute step
            cursor.execute(sql,[Numberbox.get(),Addressbox.get(),Districtbox.get(),Provincetbox.get(),Pincodebox.get()])
            #commit step
            conn.commit()
            messagebox.showinfo("Swifter:","Add Shipping Address successfully")
            FinalFrame = Frame(Checkoutcanvas,width=600,height=550,bg="red")
            FinalFrame.grid(row=0, column=0, sticky="news", columnspan=2, rowspan=6)
            Checkoutcanvas.create_window((0, 0), window=FinalFrame, anchor=NW)
            Label(FinalFrame,image=pic38).place(x=0,y=0)


def finalclick():
    FinalFrame = Frame(Checkoutcanvas,width=600,height=550,bg="red")
    FinalFrame.grid(row=0, column=0, sticky="news", columnspan=2, rowspan=6)
    Checkoutcanvas.create_window((0, 0), window=FinalFrame, anchor=NW)
    Label(FinalFrame,image=pic38).place(x=0,y=0)


def send_by_button():
    getmsg = chatbox.get("1.0", 'end-1c').strip()
    msg = textwrap.fill(getmsg, 30)
    chatbox.delete("0.0", END)

    if msg == 'hello' or msg == 'Hello' or msg == 'hi' or msg == 'Hi' or msg == 'Hi!' or msg == 'hi!':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg,
                                                wraplength=200, font=("Arial", 10), bg="#FFB4B4", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "left")
        ChatLog.config(foreground="#000", font=("Helvetica", 9))
        ChatLog.yview(END)

        res = "Hi, Gorgeous"
        ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res,
                                                wraplength=200, font=("Arial", 10), bg="#DDDDDD", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "right")
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

    elif msg == 'I love you Taylor':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg,
                                                wraplength=200, font=("Arial", 10), bg="#FFB4B4", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "left")
        ChatLog.config(foreground="#000", font=("Helvetica", 9))
        ChatLog.yview(END)

        res = "I love you too"
        ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res,
                                                wraplength=200, font=("Arial", 10), bg="#DDDDDD", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "right")
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

    elif msg == 'Congrat! On the new album':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg,
                                                wraplength=200, font=("Arial", 10), bg="#FFB4B4", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "left")
        ChatLog.config(foreground="#000", font=("Helvetica", 9))
        ChatLog.yview(END)

        res = "Aww, thank you\nThank you for saying that"
        ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res,
                                                wraplength=200, font=("Arial", 10), bg="#DDDDDD", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "right")
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

    elif msg == 'Who is this?':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg,
                                                wraplength=200, font=("Arial", 10), bg="#FFB4B4", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "left")
        ChatLog.config(foreground="#000", font=("Helvetica", 9))
        ChatLog.yview(END)

        res = "It's me, Hi I'm Taylor Swift"
        ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res,
                                                wraplength=200, font=("Arial", 10), bg="#DDDDDD", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "right")
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

    elif msg == 'What this app for?':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg,
                                                wraplength=200, font=("Arial", 10), bg="#FFB4B4", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "left")
        ChatLog.config(foreground="#000", font=("Helvetica", 9))
        ChatLog.yview(END)

        res = "For everything Taylor Swift"
        ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res,
                                                wraplength=200, font=("Arial", 10), bg="#DDDDDD", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "right")
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

    elif msg == 'What your favorite food?':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg,
                                                wraplength=200, font=("Arial", 10), bg="#FFB4B4", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "left")
        ChatLog.config(foreground="#000", font=("Helvetica", 9))
        ChatLog.yview(END)

        res = "definitely Cheesecake!"
        ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res,
                                                wraplength=200, font=("Arial", 10), bg="#DDDDDD", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "right")
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

    elif msg == 'Which film is your cup of tea?':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg,
                                                wraplength=200, font=("Arial", 10), bg="#FFB4B4", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "left")
        ChatLog.config(foreground="#000", font=("Helvetica", 9))
        ChatLog.yview(END)

        res = " Love Actually is my favorite"
        ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res,
                                                wraplength=200, font=("Arial", 10), bg="#DDDDDD", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "right")
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)    

    else:
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, current_time+' ', ("small", "right", "greycolour"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=msg,
                                                wraplength=200, font=("Arial", 10), bg="#FFB4B4", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "left")
        ChatLog.config(foreground="#000", font=("Helvetica", 9))
        ChatLog.yview(END)

        res = "I'm sorry, I'm not sure what you are talking about. "
        ChatLog.insert(END, current_time+' ', ("small", "greycolour", "left"))
        ChatLog.window_create(END, window=Label(ChatLog, fg="#000000", text=res,
                                                wraplength=200, font=("Arial", 10), bg="#DDDDDD", bd=4, justify="left"))
        ChatLog.insert(END, '\n ', "right")
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


def deletePlaceholder(event):
    Placeholder.place_forget()
    chatbox.focus_set()


def addPlaceholder(event):
    if placeholderFlag == 1:
        Placeholder.place(x=6, y=421, height=70, width=265)


def update():
    global placeholderFlag
    if (chatbox.get("1.0", 'end-1c').strip() == ''):
        SendButton['state'] = DISABLED
        placeholderFlag = 1
    elif chatbox.get("1.0", 'end-1c').strip() != '':
        SendButton['state'] = ACTIVE
        placeholderFlag = 0
    chatframe.after(100, update)


createconnection()
root = mainwindow()

pic1 = PhotoImage(file="pic/sky1.png")
pic2 = PhotoImage(file="pic/taymerch1.png")
pic3 = PhotoImage(file="pic/taymerch2.png")
pic4 = PhotoImage(file="pic/search.png")
pic5 = PhotoImage(file="pic/taymerch3.png")
pic6 = PhotoImage(file="pic/taymerch4.png")
pic7 = PhotoImage(file="pic/taymerch5.png")
pic8 = PhotoImage(file="pic/taymerch6.png")
pic9 = PhotoImage(file="pic/taymerch7.png")
pic10 = PhotoImage(file="pic/taymerch8.png")
pic11 = PhotoImage(file="pic/taymerch9.png")
pic12 = PhotoImage(file="pic/continueshopping.png")
pic13 = PhotoImage(file="pic/Checkout.png")
pic14 = PhotoImage(file="pic/exitbutton.png")
pic15 = PhotoImage(file="pic/continueshoppingwhite.png")
pic16 = PhotoImage(file="pic/Checkoutwhite.png")
pic17 = PhotoImage(file="pic/Entry.png")
pic18 = PhotoImage(file="pic/Cart.png")
pic19 = PhotoImage(file="pic/taymerch1.png").subsample(3, 3)
pic20 = PhotoImage(file="pic/taymerch2.png").subsample(3, 3)
pic21 = PhotoImage(file="pic/taymerch3.png").subsample(3, 3)
pic22 = PhotoImage(file="pic/taymerch4.png").subsample(3, 3)
pic23 = PhotoImage(file="pic/taymerch6.png").subsample(3, 3)
pic24 = PhotoImage(file="pic/taymerch7.png").subsample(3, 3)
pic25 = PhotoImage(file="pic/taymerch8.png").subsample(3, 3)
pic26 = PhotoImage(file="pic/taymerch9.png").subsample(3, 3)
pic27 = PhotoImage(file="pic/Businessman.png")
pic28 = PhotoImage(file="pic/backtomerch.png")
pic29 = PhotoImage(file="pic/Checkoutfromcart.png")
pic30 = PhotoImage(file="pic/emptycart.png")
pic31 = PhotoImage(file="pic/Thankful.png")
pic32 = PhotoImage(file="pic/AddedShip.png")
pic33 = PhotoImage(file="pic/Add_shipping_address.png")
pic34 = PhotoImage(file="pic/EntryAddress.png")
pic35 = PhotoImage(file="pic/EntryForPin.png")
pic36 = PhotoImage(file="pic/backtocart.png")
pic37 = PhotoImage(file="pic/purchasebt.png")
pic38 = PhotoImage(file="pic/Enjoy_your_Merchs.png")



img1 = PhotoImage(file="pic/back_to_login.png")
img2 = PhotoImage(file="pic/Sign_up_purple.png")
img3 = PhotoImage(file="pic/sign_in_button.png")
img4 = PhotoImage(file="pic/Forgot_password_button.png")
img5 = PhotoImage(file="pic/Sign_up_button.png")
img6 = PhotoImage(file="pic/forest.png")
img7 = PhotoImage(file="pic/Coversignup.png")
img8 = PhotoImage(file="pic/Taylor4.png").subsample(5, 5)
img9 = PhotoImage(file="pic/Taybot.png")
img10 = PhotoImage(file="pic/sendbutton.png")
img11 = PhotoImage(file="pic/Taybanner.png")
img12 = PhotoImage(file="pic/TheErasTourposter.png")
img13 = PhotoImage(file="pic/2023recordstoreday.png").subsample(2, 2)
img14 = PhotoImage(file="pic/taxas(3).png")
img15 = PhotoImage(file="pic/hou-art-20230421-ts-body1.png")
img16 = PhotoImage(file="pic/hou-art-20230421-ts-body12.png")
img17 = PhotoImage(file="pic/tayview.png")
img18 = PhotoImage(file="pic/taytaxas.png")
img19 = PhotoImage(file="pic/taytax2.png")
img20 = PhotoImage(file="pic/taytax3.png")
img21 = PhotoImage(file="pic/taytax4.png")
img22 = PhotoImage(file="pic/taytax5.png")
img23 = PhotoImage(file="pic/2023recordstoreday1.png")
img24 = PhotoImage(file="pic/folklore1.png")
img25 = PhotoImage(file="pic/billboard.png").subsample(2, 2)
img26 = PhotoImage(file="pic/speaknow.png").subsample(2, 2)
img27 = PhotoImage(file="pic/billboard.png")
img28 = PhotoImage(file="pic/folklore2.png")
img29 = PhotoImage(file="pic/speaknow.png")
img30 = PhotoImage(file="pic/speaknow1.png")
img31 = PhotoImage(file="pic/speaknow2.png")
img32 = PhotoImage(file="pic/Taylor5.png")
img33 = PhotoImage(file="pic/Taylor6.png")
img34 = PhotoImage(file="pic/Taylor7.png")
img35 = PhotoImage(file="pic/taylorandkanye.png")
img36 = PhotoImage(file="pic/Taylor8.png")
img37 = PhotoImage(file="pic/Taylor9.png")
img38 = PhotoImage(file="pic/Taylor10.png")
img39 = PhotoImage(file="pic/Taylor11.png")
img40 = PhotoImage(file="pic/Taylor12.png")
img41 = PhotoImage(file="pic/Taylor13.png")
img42 = PhotoImage(file="pic/SignIn.png")
img43 = PhotoImage(file="pic/Taylor3.png")
img44 = PhotoImage(file="pic/Taylor14.png").subsample(3, 3)
img45 = PhotoImage(file="pic/Taylor15.png").subsample(3, 3)
img46 = PhotoImage(file="pic/Taylor16.png").subsample(3, 3)
img47 = PhotoImage(file="pic/Taylor17.png").subsample(3, 3)
img48 = PhotoImage(file="pic/Taylor14.png")
img49 = PhotoImage(file="pic/Taylor14.png").subsample(5, 6)
img50 = PhotoImage(file="pic/flim-removebg-preview.png")
img51 = PhotoImage(file="pic/Taylor18.png").subsample(5, 6)
img52 = PhotoImage(file="pic/Taylor18.png")
img53 = PhotoImage(file="pic/Taylor19.png").subsample(5, 6)
img54 = PhotoImage(file="pic/Taylor19.png")
img55 = PhotoImage(file="pic/Taylor20.png").subsample(5, 6)
img56 = PhotoImage(file="pic/Taylor20.png")
img57 = PhotoImage(file="pic/Taylor15.png").subsample(5, 6)
img58 = PhotoImage(file="pic/Taylor15.png")
img59 = PhotoImage(file="pic/Taylor21.png").subsample(5, 6)
img60 = PhotoImage(file="pic/Taylor21.png")
img61 = PhotoImage(file="pic/Taylor22.png").subsample(5, 6)
img62 = PhotoImage(file="pic/Taylor22.png")
img63 = PhotoImage(file="pic/Taylor23.png").subsample(5, 6)
img64 = PhotoImage(file="pic/Taylor23.png")
img65 = PhotoImage(file="pic/Taylor16.png").subsample(5, 6)
img66 = PhotoImage(file="pic/Taylor16.png")
img67 = PhotoImage(file="pic/Taylor24.png").subsample(5, 6)
img68 = PhotoImage(file="pic/Taylor24.png")
img69 = PhotoImage(file="pic/Taylor25.png").subsample(5, 6)
img70 = PhotoImage(file="pic/Taylor25.png")
img71 = PhotoImage(file="pic/Taylor26.png").subsample(5, 6)
img72 = PhotoImage(file="pic/Taylor26.png")
img73 = PhotoImage(file="pic/Taylor17.png").subsample(5, 6)
img74 = PhotoImage(file="pic/Taylor17.png")
img75 = PhotoImage(file="pic/Taylor27.png").subsample(5, 6)
img76 = PhotoImage(file="pic/Taylor27.png")
img77 = PhotoImage(file="pic/Taylor28.png").subsample(5, 6)
img78 = PhotoImage(file="pic/Taylor28.png")
img79 = PhotoImage(file="pic/Taylor29.png").subsample(5, 6)
img80 = PhotoImage(file="pic/Taylor29.png")
img81 = PhotoImage(file="pic/Taylor30.png").subsample(3, 3)
img82 = PhotoImage(file="pic/Taylor30.png").subsample(5, 6)
img83 = PhotoImage(file="pic/Taylor30.png")
img84 = PhotoImage(file="pic/Taylor31.png").subsample(5, 6)
img85 = PhotoImage(file="pic/Taylor31.png")
img86 = PhotoImage(file="pic/Taylor32.png").subsample(5, 6)
img87 = PhotoImage(file="pic/Taylor32.png")
img88 = PhotoImage(file="pic/Taylor33.png").subsample(5, 6)
img89 = PhotoImage(file="pic/Taylor33.png")
img90 = PhotoImage(file="pic/Taylor34.png").subsample(3, 3)
img91 = PhotoImage(file="pic/Taylor34.png").subsample(5, 6)
img92 = PhotoImage(file="pic/Taylor34.png")
img93 = PhotoImage(file="pic/Taylor35.png").subsample(5, 6)
img94 = PhotoImage(file="pic/Taylor35.png")
img95 = PhotoImage(file="pic/Taylor36.png").subsample(5, 6)
img96 = PhotoImage(file="pic/Taylor36.png")
img97 = PhotoImage(file="pic/Taylor37.png").subsample(5, 6)
img98 = PhotoImage(file="pic/Taylor37.png")

var1 = IntVar()
var2 = IntVar()
Merch1Spy, Merch2Spy, Merch3Spy, Merch4Spy, Merch6Spy, Merch7Spy, Merch8Spy, Merch9Spy = IntVar(
), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()

Addresslist = ["Name :",
               "Phone Number :",
               "Address(Area and Street)",
               "District",
               "Province",
               "Pincode"]

MerchName = ["TAYLOR SWIFT THE ERAS TOUR GRAY CREWNECK",
             "TAYLOR SWIFT THE ERAS TOUR BLACK T-SHIRT",
             "TAYLOR SWIFT THE ERAS TOUR 1989 ALBUM T-SHIRT",
             "TAYLOR SWIFT THE ERAS TOUR BEIGE HOODIE",
             "TAYLOR SWIFT BEJEWELED BRACELET",
             "TAYLOR SWIFT THE ERAS TOUR LOVER ALBUM T-SHIRT",
             "TAYLOR SWIFT THE ERAS TOUR EARBUD CASE",
             "TAYLOR SWIFT THE ERAS TOUR BLACK SWEATPANTS"]


forsignup = ["First Name : ",
             "last Name : ", 
             "Email Address : ",
             "Username : ", 
             "Password : ", 
             "Confirm Password : "]

now = datetime.now()
current_time = now.strftime("%D - %H:%M \n")
loginlayout()
#taylor()
# chatframe.bind('<Return>', send)
# update()
root.mainloop()
