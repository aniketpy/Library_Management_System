import mysql.connector
from mysql.connector.errors import Error
from tkinter import *
from PIL import ImageTk,Image
from functools import partial
import time

main=Tk()
student=[]
try:
    mydb = mysql.connector.connect(host='localhost', user="root", password="1234", database="lms")
except Error as e:
    print("Database Connection Failed {}".format(e))
mysql=mydb.cursor(buffered=True)


def main_window():
    global text1, text2
    main.title("Library Management System")
    # setting size of gui by taking size of image
    image_b=Image.open("lib1.jpg")
    [w,h]=image_b.size
    main.geometry(f"{w}x{h}")
    # Adding Background image to tkinter
    image=Image.open("lib1.jpg")
    image_b=ImageTk.PhotoImage(image, master=main)
    label=Label(main, image=image_b)
    label.place(relx=0,rely=0)

    frame1 = Frame(main, bg="aqua",bd=3)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1 = Label(frame1, text="Library Management System", bg="Black", fg="white", font=("Cosmic San MS",25))
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)

    label2 = Label(main, text="Id: ", fg="black", font=("Cosmic San MS",15))
    label2.place(relx=0.33,rely=0.3)
    label3 = Label(main, text="Password: ", fg="black", font=("Cosmic San MS",15))
    label3.place(relx=0.33,rely=0.4)

    text1 = Text(main, bd=5, width=18, height=1, font=("Cosmic San MS",18))
    text1.place(relx=0.43,rely=0.29)
    text2 = Entry(main, show="*", bd=5, width=18, font=("Cosmic San MS",18))
    text2.place(relx=0.43,rely=0.39)

    frame2 = Label(main, fg="aqua", bg="aqua", bd=2, width=20)
    frame2.place(relx=0.33,rely=0.55,relheight=0.07)
    butt1=Button(frame2, text="Student Login",width=12 ,height=1 , bg="black", fg="white", font=("Cosmic San MS",15), command=load_student)
    butt1.place(relx=0,rely=0)
    
    frame2 = Label(main, fg="aqua", bg="aqua", bd=2, width=20)
    frame2.place(relx=0.51,rely=0.55,relheight=0.07)
    butt2=Button(frame2, text="Admin Login",width=12 ,height=1, bg="black", fg="white", font=("Cosmic San MS",15),command=load_teacher)
    butt2.place(relx=0,rely=0)
    
    frame3 = Label(main, fg="aqua", bg="aqua", bd=2, width=35)
    frame3.place(relx=0.38,rely=0.65,relheight=0.071)
    butt3=Button(frame3, text="Request for Student Login", bg="black", fg="white", font=("Cosmic San MS",15),command=request_student)
    butt3.place(relx=0,rely=0)

    main.mainloop()

def load_student():
    global text1, text2
    a=str(text1.get("1.0",END))
    b=str(text2.get())
    a=int(a[0:len(a)-1])
    # b=b[0:len(b)-1].lower()
    # print(a,b)
    query="SELECT * FROM login_student"
    try:
        mysql.execute(query)
        mydb.commit()
    except Error as e:
        label1=Label(frame2, text="Fetching Database failed{}".format(e))
        label1.place(relx=0.2,rely=0.7)
        return 0
    for i in mysql:
        if a == i[0] and b == i[1]:
            # print(i)
            query="SELECT * FROM student_details"
            try:
                mysql.execute(query)
                mydb.commit()
                for i in mysql:
                    if a == i[0]:
                        global student
                        student = i
                        student_login()
            except Error as e:
                # global student
                student = student.append(a)
                student_login()
                print("$$$Failed to load student_detail table$$$")      
        elif a == i[0] and b != i[1]:
            label1=Label(main, text="Wrong Password",font=("Cosmic San MS",15))
            label1.place(relx=0.42,rely=0.8)
    
    label1=Label(main, text="ID Password did not match",font=("Cosmic San MS",15))
    label1.place(relx=0.38,rely=0.8)


def load_teacher():
    global text1, text2
    a=str(text1.get("1.0",END))
    b=str(text2.get())
    a=a[0:len(a)-1]
    # b=b[0:len(b)-1].lower()
    # print(a,b)
    query="SELECT * FROM login_management"
    try:
        mysql.execute(query)
        mydb.commit()
    except Error as e:
        label1=Label(frame2, text="Fetching Database failed{}".format(e))
        label1.place(relx=0.2,rely=0.7)
        return 0
    for i in mysql:
        if a == i[0] and b == i[1]:
            print(i)  
            teacher_login()   
        elif a == i[0] and b != i[1]:
            label1=Label(main, text="Wrong Password",font=("Cosmic San MS",15))
            label1.place(relx=0.42,rely=0.8)
    
    label1=Label(main, text="ID Password did not match",font=("Cosmic San MS",15))
    label1.place(relx=0.38,rely=0.8)


# Student Login Section
  
def student_login():
    # print(student)
    main.title("Library Management System")
    # setting size of gui by taking size of image
    image_b=Image.open("lib1.jpg")
    [w,h]=image_b.size
    main.geometry(f"{w}x{h}")
    # Adding Background image to tkinter
    image=Image.open("lib1.jpg")
    image_b=ImageTk.PhotoImage(image, master=main)
    label=Label(main, image=image_b)
    label.place(relx=0,rely=0)

    frame1 = Frame(main,bg="aqua",bd=3)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1 = Label(frame1, text="Library Management System", bg="Black", fg="white", font=("Cosmic San MS",25))
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame2 = Frame(main, bg="aqua",bd=5)
    frame2.place(relx=0.3,rely=0.3,relwidth=0.4,relheight=0.1)
    label2 = Label(frame2, text=f"Welcome {student[1].title()}", bg="black", fg="white", font=("Cosmic San MS",15))
    label2.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame3 = Frame(main, bg="steelblue1",bd=5)
    frame3.place(relx=0.3,rely=0.41,relwidth=0.4,relheight=0.1)
    label3 = Button(frame3, text="Return Book", bg="black", fg="white", font=("Cosmic San MS",10),command=return_book)
    label3.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame4 = Frame(main, bg="steelblue1",bd=5)
    frame4.place(relx=0.3,rely=0.52,relwidth=0.4,relheight=0.1)
    label4 = Button(frame4, text="Issue Book", bg="black", fg="white", font=("Cosmic San MS",10),command=issue_book)
    label4.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame5 = Frame(main, bg="steelblue1",bd=5)
    frame5.place(relx=0.3,rely=0.63,relwidth=0.4,relheight=0.1)
    label5 = Button(frame5, text="View List of Book", bg="black", fg="white", font=("Cosmic San MS",10),command=view_book)
    label5.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame5 = Frame(main, bg="steelblue1",bd=5)
    frame5.place(relx=0.3,rely=0.74,relwidth=0.4,relheight=0.1)
    label5 = Button(frame5, text="Search Book", bg="black", fg="white", font=("Cosmic San MS",10),command=search_book)
    label5.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame5 = Frame(main, bg="red",bd=5)
    frame5.place(relx=0.45,rely=0.85,relwidth=0.1,relheight=0.08)
    label5 = Button(frame5, text="Logout", bg="black", fg="white", font=("Cosmic San MS",12),command=main_window)
    label5.place(relx=0,rely=0,relwidth=1,relheight=1)

    main.mainloop()



def issue_book():
    global text1, text2, frame2
    main.title("Issue Book")
    # setting size of gui by taking size of image
    image_b=Image.open("lib1.jpg")
    [w,h]=image_b.size
    main.geometry(f"{w}x{h}")
    # Adding Background image to tkinter
    image=Image.open("lib1.jpg")
    image_b=ImageTk.PhotoImage(image, master=main)
    label=Label(main, image=image_b)
    label.place(relx=0,rely=0)

    frame1 = Frame(main,bg="aqua",bd=5)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1 = Label(frame1, text="Issue Books", bg="Black", fg="white", font=("Cosmic San MS",15))
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame2 = Frame(main,bg="black",bd=5)
    frame2.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.5)

    label2 = Label(frame2, text="Book ID :",bg="black", fg="white", font=("Cosmic San MS",10))
    label2.place(relx=0.1,rely=0.1)
    text1 = Text(frame2, bd=3, height=1,width=30)
    text1.place(relx=0.37,rely=0.1)

    butt1=Button(frame2, text="Issue",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=issue_book_c)
    butt1.place(relx=0.3,rely=0.5)

    butt2=Button(frame2, text="Back",bg="pink",bd=5,  fg="black", font=("Cosmic San MS",10), command=student_login)
    butt2.place(relx=0.6,rely=0.5)

    butt3=Button(main, text="Exit",bg="pink",bd=5,  fg="black", font=("Cosmic San MS",10), command=main.destroy)
    butt3.place(relx=0.94,rely=0.92)

    main.mainloop()

def issue_book_c():
    global text1, text2, frame2
    book=int(text1.get("1.0",END))
    # to=text2.get("1.0",END)
    print(book, type(book))
    mysql.execute("select * from books")
    for i in mysql:
        if i[0]==book:
            if i[3]=="yes":
                query=f"UPDATE books SET status='no', issued_to ={student[0]} WHERE ID={book}"
                try:
                    print(query)
                    mysql.execute(query)
                    mydb.commit()
                    label1=Label(frame2, text=f"Book   {i[1].title()}   Issued Sucessfully",bg="black",fg="white")
                    label1.place(relx=0.3,rely=0.7)
                    print(f"Book {i[1].title()} Issued to {student[0]}")
                    try:
                        query=f"update student_details set issued_book=concat(issued_book,',{i[0]}') where ID={student[0]};"
                        mysql.execute(query)
                        mydb.commit()
                    except Error as e:
                        label1=Label(frame2, text="Failed Updating Issue-Table- {}".format(e),bg="black",fg="white")
                        label1.place(relx=0.2,rely=0.7)
                        return 0
                    return 0
                except Error as e:
                    label1=Label(frame2, text="Failed Issuing Book - {}".format(e),bg="black",fg="white")
                    label1.place(relx=0.2,rely=0.7)
                    print("Failed issuing book - {}".format(e))
                    return 0
            else:
                print("Book is not available")
                label1=Label(frame2, text=f"Book   {i[1].title()}   is not available",bg="black",fg="white")
                label1.place(relx=0.3,rely=0.7) 
                return 0    

    label1=Label(frame2, text=f"Book is not in database",bg="black",fg="white")
    label1.place(relx=0.35,rely=0.7)


def return_book():
    global text1, text2, frame2
    main.title("Retrun Book")
    # setting size of gui by taking size of image
    image_b=Image.open("lib1.jpg")
    [w,h]=image_b.size
    main.geometry(f"{w}x{h}")
    # Adding Background image to tkinter
    image=Image.open("lib1.jpg")
    image_b=ImageTk.PhotoImage(image, master=main)
    label=Label(main, image=image_b)
    label.place(relx=0,rely=0)

    frame1 = Frame(main,bg="aqua",bd=5)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1 = Label(frame1, text="Return Books", bg="Black", fg="white", font=("Cosmic San MS",15))
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame2 = Frame(main,bg="black",bd=5)
    frame2.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.5)

    label2 = Label(frame2, text="Book ID :",bg="black", fg="white", font=("Cosmic San MS",10))
    label2.place(relx=0.1,rely=0.1)
    text1 = Text(frame2, bd=3, height=1,width=30)
    text1.place(relx=0.37,rely=0.1)

    butt1=Button(frame2, text="Return",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=return_book_c)
    butt1.place(relx=0.3,rely=0.5)

    butt2=Button(frame2, text="Back",bg="pink",bd=5,  fg="black", font=("Cosmic San MS",10), command=student_login)
    butt2.place(relx=0.6,rely=0.5)

    butt3=Button(main, text="Exit",bg="pink",bd=5,  fg="black", font=("Cosmic San MS",10), command=main.destroy)
    butt3.place(relx=0.94,rely=0.92)

    main.mainloop()

def return_book_c():
    global text1, text2, frame2
    book=int(text1.get("1.0",END))
    print(book, type(book))
    mysql.execute("select * from books")
    for i in mysql:
        print(f"\n{i[0]}")
        if i[0]==book:
            if i[3]=="no":
                query=f"UPDATE books SET status='yes', issued_to='' WHERE ID={book}"
                try:
                    print(query)
                    mysql.execute(query)
                    mydb.commit()    

                    query=f"update student_details set issued_book=replace(issued_book,',{i[0]}','') where ID={student[0]};"
                    mysql.execute(query)
                    mydb.commit()
                    label1=Label(frame2, text=f"Book   {i[1].title()}   Returned Sucessfully",bg="black",fg="white")
                    label1.place(relx=0.25,rely=0.7)
                    print(f"Book {i[1].title()} Returned from {student[1].title()}")
                    return 0
                except Error as e:
                    label1=Label(frame2, text="Failed returning Book - {}".format(e),bg="black",fg="white")
                    label1.place(relx=0.2,rely=0.7)
                    print("Failed returning book - {}".format(e))
                    return 0
            else:
                print("Book is already Returned")
                label1=Label(frame2, text=f"Book   {i[1].title()}   is already Returned",bg="black",fg="white")
                label1.place(relx=0.3,rely=0.7) 
                return 0    

    label1=Label(frame2, text=f"Book is not in database",bg="black",fg="white")
    label1.place(relx=0.35,rely=0.7)


def view_book():
    main.title("View Book")
    # setting size of gui by taking size of image
    image_b=Image.open("lib1.jpg")
    [w,h]=image_b.size
    main.geometry(f"{w}x{h}")
    # Adding Background image to tkinter
    image=Image.open("lib1.jpg")
    image_b=ImageTk.PhotoImage(image, master=main)
    label=Label(main, image=image_b)
    label.place(relx=0,rely=0)

    frame1 = Frame(main,bg="aqua",bd=3)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1 = Label(frame1, text="View List of Books", bg="Black", fg="white", font=("Cosmic San MS",15))
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame2 = Frame(main,bg="black",bd=5)
    frame2.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.5)

    butt1=Button(main, text="Back",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10))
    butt1.place(relx=0.47,rely=0.82)
    
    butt2=Button(main, text="Exit",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=main.destroy)
    butt2.place(relx=0.94,rely=0.92)
    
    label2=Label(frame2, text="----------------------------------------------------------------------------------------------------------------------------------------------",fg="white", bg="black", font=("Cosmic San MS",10))
    label2.place(relx=0.012,rely=0.02)
    label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
    label1.place(relx=0.012,rely=0.02)
    label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
    label1.place(relx=0.1,rely=0.02)
    label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
    label1.place(relx=0.556,rely=0.02)
    label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
    label1.place(relx=0.877,rely=0.02)
    label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
    label1.place(relx=0.975,rely=0.02)

    label1=Label(frame2, text="|  BID     |  Name                                                        |  Author                                   |  Status  |",fg="white", bg="black", font=("Cosmic San MS",10))
    label1.place(relx=0.017,rely=0.08)
    
    label2=Label(frame2, text="----------------------------------------------------------------------------------------------------------------------------------------------",fg="white", bg="black", font=("Cosmic San MS",10))
    label2.place(relx=0.012,rely=0.13)
    label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
    label1.place(relx=0.012,rely=0.13)
    label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
    label1.place(relx=0.1,rely=0.13)
    label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
    label1.place(relx=0.556,rely=0.13)
    label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
    label1.place(relx=0.877,rely=0.13)
    label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
    label1.place(relx=0.975,rely=0.13)
    
    mysql.execute("select * from books")
    s=0.18
    for i in mysql:

        label2=Label(frame2, text="----------------------------------------------------------------------------------------------------------------------------------------------",fg="white", bg="black", font=("Cosmic San MS",10))
        label2.place(relx=0.012,rely=s+0.045)
        label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
        label1.place(relx=0.012,rely=s+0.045)
        label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
        label1.place(relx=0.1,rely=s+0.045)
        label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
        label1.place(relx=0.556,rely=s+0.045)
        label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
        label1.place(relx=0.877,rely=s+0.045)
        label1=Label(frame2, text="+",fg="white", bg="black", font=("Cosmic San MS",10))
        label1.place(relx=0.975,rely=s+0.045)

        label3=Label(frame2, text="|",fg="white", bg="black", font=("Cosmic San MS",10))
        label3.place(relx=0.017,rely=s)
        label3=Label(frame2, text=f"{i[0]}",fg="white", bg="black", font=("Cosmic San MS",10))
        label3.place(relx=0.028,rely=s)
        label3=Label(frame2, text="|",fg="white", bg="black", font=("Cosmic San MS",10))
        label3.place(relx=0.105,rely=s)
        label3=Label(frame2, text=f"{i[1].title()}",fg="white", bg="black", font=("Cosmic San MS",10))
        label3.place(relx=0.12,rely=s)
        label3=Label(frame2, text="|",fg="white", bg="black", font=("Cosmic San MS",10))
        label3.place(relx=0.561,rely=s)
        label3=Label(frame2, text=f"{i[2].title()}",fg="white", bg="black", font=("Cosmic San MS",10))
        label3.place(relx=0.58,rely=s)
        label3=Label(frame2, text="|",fg="white", bg="black", font=("Cosmic San MS",10))
        label3.place(relx=0.882,rely=s)
        label3=Label(frame2, text=f"{i[3].title()}",fg="white", bg="black", font=("Cosmic San MS",10))
        label3.place(relx=0.9,rely=s)
        label3=Label(frame2, text="|",fg="white", bg="black", font=("Cosmic San MS",10))
        label3.place(relx=0.98,rely=s)
        s+=0.12

    main.mainloop()


def search_book():
    global frame21, text
    main.title("Search Books")
    # setting size of gui by taking size of image
    image_b=Image.open("lib1.jpg")
    [w,h]=image_b.size
    main.geometry(f"{w}x{h}")
    # Adding Background image to tkinter
    image=Image.open("lib1.jpg")
    image_b=ImageTk.PhotoImage(image, master=main)
    label=Label(main, image=image_b)
    label.place(relx=0,rely=0)

    frame1 = Frame(main,bg="aqua",bd=5)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1 = Label(frame1, text="Search Books", bg="Black", fg="white", font=("Cosmic San MS",15))
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame21 = Frame(main,bg="black",bd=5)
    frame21.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.5)
    label2=Label(frame21, text="Enter Book Name : ", bg="black", fg="white", font=("Cosmic San MS",10))
    label2.place(relx=0.02,rely=0.04)
    text = Text(frame21, bd=3, width=26, height=1)
    text.place(relx=0.3,rely=0.04)
    butt1=Button(frame21, text="Search",bg="pink", bd=3, fg="black", font=("Cosmic San Ms",10), command=search_book_c)
    butt1.place(relx=0.85,rely=0.025)

    butt2=Button(main, text="Back",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=student_login)
    butt2.place(relx=0.48,rely=0.82)
   
    butt3=Button(main, text="Exit",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=main.destroy)
    butt3.place(relx=0.94,rely=0.92)

    main.mainloop()

def search_book_c():
    global main, frame21, text
    search=str(text.get("1.0",END))
    search=search[0:len(search)-1]
    print(f"Book name = {search}")
    query="SELECT * FROM books"
    mysql.execute(query)
    s=0.39

    for i in mysql:
        b=""
        for j in i[:-1]:b+=f" {j}"
        if search in b:
            f=1

            label=Label(frame21, text="----------------------------------------------------------------------------------------------------------------------------------------------",fg="white", bg="black", font=("Cosmic San MS",10))
            label.place(relx=0.01,rely=0.3)
            
            label1=Label(frame21, text=" BID       Name                                                          Author                                     Status",fg="white", bg="black", font=("Cosmic San MS",10))
            label1.place(relx=0.02,rely=0.22)
            
            label2=Label(frame21, text=f"{i[0]}",fg="white", bg="black", font=("Cosmic San MS",10))
            label2.place(relx=0.02,rely=s)
            
            label3=Label(frame21, text=f"{i[1].title()}",fg="white", bg="black", font=("Cosmic San MS",10))
            label3.place(relx=0.11,rely=s)
            
            label4=Label(frame21, text=f"{i[2].title()}",fg="white", bg="black", font=("Cosmic San MS",10))
            label4.place(relx=0.56,rely=s)

            label5=Label(frame21, text=f"{i[3].title()}",fg="white", bg="black", font=("Cosmic San MS",10))
            label5.place(relx=0.88,rely=s)

            s+=0.15
    
    if f!=1:
        label=Label(frame2, text="No Result Found", fg="white", bg="black", font=("Cosmic San MS",10))
        label.place(relx=0.02,rely=0.6)
        print("No Result Found")
        print(b)
    
    main.mainloop()


# Teacher Login Section   

def teacher_login():
    main.title("Library Management System")
    # setting size of gui by taking size of image
    image_b=Image.open("lib1.jpg")
    [w,h]=image_b.size
    main.geometry(f"{w}x{h}")
    # Adding Background image to tkinter
    image=Image.open("lib1.jpg")
    image_b=ImageTk.PhotoImage(image, master=main)
    label=Label(main, image=image_b)
    label.place(relx=0,rely=0)

    frame1 = Frame(main,bg="aqua",bd=3)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1 = Label(frame1, text="Library Management System", bg="Black", fg="white", font=("Cosmic San MS",25))
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame2 = Frame(main, bg="aqua",bd=5)
    frame2.place(relx=0.3,rely=0.3,relwidth=0.4,relheight=0.1)
    label2 = Label(frame2, text=f"Welcome Admin", bg="black", fg="white", font=("Cosmic San MS",15))
    label2.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame3 = Frame(main, bg="steelblue1",bd=5)
    frame3.place(relx=0.3,rely=0.41,relwidth=0.4,relheight=0.1)
    label3 = Button(frame3, text="Add / Delete Book", bg="black", fg="white", font=("Cosmic San MS",10),command=add_delete_book)
    label3.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame4 = Frame(main, bg="steelblue1",bd=5)
    frame4.place(relx=0.3,rely=0.52,relwidth=0.4,relheight=0.1)
    label4 = Button(frame4, text="Add / Delete Student", bg="black", fg="white", font=("Cosmic San MS",10),command=add_delete_student)
    label4.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame5 = Frame(main, bg="steelblue1",bd=5)
    frame5.place(relx=0.3,rely=0.63,relwidth=0.4,relheight=0.1)
    label5 = Button(frame5, text="Search Books / Student", bg="black", fg="white", font=("Cosmic San MS",10),command=search_book_student)
    label5.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame5 = Frame(main, bg="steelblue1",bd=5)
    frame5.place(relx=0.3,rely=0.74,relwidth=0.4,relheight=0.1)
    label5 = Button(frame5, text="View Requests", bg="black", fg="white", font=("Cosmic San MS",10),command=request_teacher)
    label5.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame5 = Frame(main, bg="red",bd=5)
    frame5.place(relx=0.45,rely=0.85,relwidth=0.1,relheight=0.08)
    label5 = Button(frame5, text="Logout", bg="black", fg="white", font=("Cosmic San MS",12),command=main_window)
    label5.place(relx=0,rely=0,relwidth=1,relheight=1)

    main.mainloop()


def add_delete_book():
    global frame2, frame4, frame2d
    main.title("Add / Delete Books")
    # setting size of gui by taking size of image
    image_b=Image.open("lib1.jpg")
    [w,h]=image_b.size
    main.geometry(f"{w}x{h}")
    # Adding Background image to tkinter
    image=Image.open("lib1.jpg")
    image_b=ImageTk.PhotoImage(image, master=main)
    label=Label(main, image=image_b)
    label.place(relx=0,rely=0)

    frame1 = Frame(main,bg="aqua",bd=5)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1 = Label(frame1, text="Add / Delete Books", bg="Black", fg="white", font=("Cosmic San MS",15))
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame4 = Frame(main,bg="black",bd=5)
    frame4.place(relx=0.55,rely=0.65,relwidth=0.4,relheight=0.25)
    label6 = Label(frame4, text="Terminal:",bg="black", fg="white", font=("Courier",10))
    label6.place(relx=0,rely=0)

    # Add Book

    frame2 = Frame(main,bg="black",bd=5)
    frame2.place(relx=0.05,rely=0.3,relwidth=0.4,relheight=0.6)

    frame3 = Frame(frame2,bg="aqua",bd=3)
    frame3.place(relx=0.266,rely=0.02,relwidth=0.5,relheight=0.15)
    label2 = Label(frame3, text="Add Book",bg="black", fg="white", font=("Cosmic San MS",15))
    label2.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    label2 = Label(frame2, text="Book ID :",bg="black", fg="white", font=("Cosmic San MS",10))
    label2.place(relx=0.1,rely=0.3)
    text1 = Text(frame2, bd=3, height=1,width=30)
    text1.place(relx=0.37,rely=0.3)

    label3 = Label(frame2, text="Name of Book :",bg="black", fg="white", font=("Cosmic San MS",10))
    label3.place(relx=0.1,rely=0.5)
    text2 = Text(frame2, bd=3, height=1,width=30)
    text2.place(relx=0.37,rely=0.5)

    label4 = Label(frame2, text="Author of Book :",bg="black", fg="white", font=("Cosmic San MS",10))
    label4.place(relx=0.1,rely=0.7)
    text3 = Text(frame2, bd=3, height=1,width=30)
    text3.place(relx=0.37,rely=0.7)

    butt1 = Button(frame2, text="Add", bg="pink",width=5 ,height=1 ,bd=5, fg="black", font=("Cosmic San MS",10),command=lambda: add_book_c(text1.get("1.0",END), text2.get("1.0",END), text3.get("1.0",END)))
    butt1.place(relx=0.45,rely=0.88)

    # Delete Book

    frame2d = Frame(main,bg="black",bd=5)
    frame2d.place(relx=0.55,rely=0.3,relwidth=0.4,relheight=0.3)

    frame3 = Frame(frame2d,bg="aqua",bd=3)
    frame3.place(relx=0.266,rely=0.02,relwidth=0.5,relheight=0.3)
    label2 = Label(frame3, text="Delete Book",bg="black", fg="white", font=("Cosmic San MS",15))
    label2.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    label2 = Label(frame2d, text="Book ID :",bg="black", fg="white", font=("Cosmic San MS",10))
    label2.place(relx=0.1,rely=0.43)
    text1d = Text(frame2d, bd=3, height=1,width=30)
    text1d.place(relx=0.37,rely=0.43)

    butt1=Button(frame2d, text="Delete",bg="pink",width=5 ,height=1 ,bd=5, fg="black", font=("Cosmic San MS",10), command=lambda: delete_book_c(text1d.get("1.0",END)))
    butt1.place(relx=0.45,rely=0.73)

    # #

    butt2=Button(main, text="Back",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=teacher_login)
    butt2.place(relx=0.48,rely=0.92)

    butt3=Button(main, text="Exit",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=main.destroy)
    butt3.place(relx=0.94,rely=0.92)


    main.mainloop()

def add_book_c(bid, name, author): 
    bid = (bid[0:len(bid)-1]).lower()
    name = (name[0:len(name)-1]).lower()
    author = (author[0:len(author)-1]).lower()
    print(f"{bid} {name} {author}")
    
    mysql.execute("select * from books")
    for i in mysql:
        if i[0] == int(bid):
            label6=Label(frame4,text="Book Already Exits",fg="white",bg="black", font=("Courier",10))
            label6.place(relx=0,rely=0.2)
            print("Book already Exits")
            return 0 
        else:
            # query = "INSERT INTO books(ID,name,author,status) VALUES (%s,'%s','%s','%s','%s')"
            query = f"INSERT INTO books(ID,name,author,status,issued_to) VALUES ({bid}, '{name}', '{author}', 'yes', '');"
            try:
                data = (bid, name, author, "yes", "")
                print(query)
                mysql.execute(query)
                mydb.commit()
                label6=Label(frame4,text="Done Uploading",fg="white",bg="black", font=("Courier",10))
                label6.place(relx=0.,rely=0.2)
                print("Done Updating")
                return 0
            except Error as e:
                label6=Label(frame4,text="Error Updating Database -",fg="white",bg="black", font=("Courier",10))
                label6.place(relx=0,rely=0.2)
                label7=Label(frame4,text="{}".format(e),fg="white",bg="black", font=("Courier",10))
                label7.place(relx=0,rely=0.33)
                print("Error updating Database - {}".format(e))
                return 0

def delete_book_c(delete):
    global frame2d, frame4
    lst1=[]
    delete=int(delete)
    print(delete,type(delete))

    mysql.execute("select * from books")
    for i in mysql:
            if i[0]==delete and i[3]=="yes":
                query=f"DELETE FROM books WHERE ID={delete}"
                try:
                    mysql.execute(query)
                    mydb.commit()
                    label1=Label(frame4, text="Book Deleted Sucessfully.",bg="black",fg="white", font=("Courier",10))
                    label1.place(relx=0,rely=0.2)
                    print("Book Deleted Sucessfully")
                    return 0
                except Error as e:
                    label1=Label(frame4, text="Error Deleting Book - ",bg="black",fg="white", font=("Courier",10))
                    label1.place(relx=0,rely=0.2)
                    label1=Label(frame4, text="{}.".format(e),bg="black",fg="white", font=("Courier",10))
                    label1.place(relx=0,rely=0.33)
                    print("Error Deleting Book - {}".format(e))
                    return 0
            elif i[0]==delete and i[3]=="no":
                label1=Label(frame4, text="Book is issued by someone.",bg="black",fg="white", font=("Courier",10))
                label1.place(relx=0,rely=0.2)
                print("Book is issued by someone.")
                return 0

    label1=Label(frame4, text="Book is not in database.",bg="black",fg="white", font=("Courier",10))
    label1.place(relx=0,rely=0.2)


def add_delete_student():
    global frame2, frame4, frame2dd
    main.title("Add / Delete Students")
    # setting size of gui by taking size of image
    image_b=Image.open("lib1.jpg")
    [w,h]=image_b.size
    main.geometry(f"{w}x{h}")
    # Adding Background image to tkinter
    image=Image.open("lib1.jpg")
    image_b=ImageTk.PhotoImage(image, master=main)
    label=Label(main, image=image_b)
    label.place(relx=0,rely=0)

    frame1 = Frame(main,bg="aqua",bd=5)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1 = Label(frame1, text="Add / Delete Student", bg="Black", fg="white", font=("Cosmic San MS",15))
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame4 = Frame(main,bg="black",bd=5)
    frame4.place(relx=0.55,rely=0.65,relwidth=0.4,relheight=0.25)
    label6 = Label(frame4, text="Terminal:",bg="black", fg="white", font=("Courier",10))
    label6.place(relx=0,rely=0)

    # Add Book

    frame2 = Frame(main,bg="black",bd=5)
    frame2.place(relx=0.05,rely=0.3,relwidth=0.4,relheight=0.6)

    frame3 = Frame(frame2,bg="aqua",bd=3)
    frame3.place(relx=0.266,rely=0.02,relwidth=0.5,relheight=0.15)
    label2 = Label(frame3, text="Add Student",bg="black", fg="white", font=("Cosmic San MS",15))
    label2.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    label2 = Label(frame2, text="Student ID :",bg="black", fg="white", font=("Cosmic San MS",10))
    label2.place(relx=0.1,rely=0.22)
    text1 = Text(frame2, bd=3, height=1,width=30)
    text1.place(relx=0.37,rely=0.22)

    label3 = Label(frame2, text="Name of Student :",bg="black", fg="white", font=("Cosmic San MS",10))
    label3.place(relx=0.1,rely=0.4)
    text2 = Text(frame2, bd=3, height=1,width=30)
    text2.place(relx=0.37,rely=0.4)

    label4 = Label(frame2, text="Roll No of Student :",bg="black", fg="white", font=("Cosmic San MS",10))
    label4.place(relx=0.1,rely=0.58)
    text3 = Text(frame2, bd=3, height=1,width=30)
    text3.place(relx=0.37,rely=0.58)

    label5 = Label(frame2, text="Year :",bg="black", fg="white", font=("Cosmic San MS",10))
    label5.place(relx=0.1,rely=0.76)
    text4 = Text(frame2, bd=3, height=1,width=30)
    text4.place(relx=0.37,rely=0.76)

    butt1 = Button(frame2, text="Add", bg="pink",width=5 ,height=1 ,bd=5, fg="black", font=("Cosmic San MS",10),command=lambda: add_student_c(text1.get("1.0",END), text2.get("1.0",END), text3.get("1.0",END), text4.get("1.0",END), 1))
    butt1.place(relx=0.45,rely=0.88)

    # Delete Book

    frame2d = Frame(main,bg="black",bd=5)
    frame2d.place(relx=0.55,rely=0.3,relwidth=0.4,relheight=0.3)

    frame3 = Frame(frame2d,bg="aqua",bd=3)
    frame3.place(relx=0.266,rely=0.02,relwidth=0.5,relheight=0.3)
    label2 = Label(frame3, text="Delete Student",bg="black", fg="white", font=("Cosmic San MS",15))
    label2.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    label2 = Label(frame2d, text="Student ID :",bg="black", fg="white", font=("Cosmic San MS",10))
    label2.place(relx=0.1,rely=0.43)
    text1d = Text(frame2d, bd=3, height=1,width=30)
    text1d.place(relx=0.37,rely=0.43)

    butt1=Button(frame2d, text="Delete",bg="pink",width=5 ,height=1 ,bd=5, fg="black", font=("Cosmic San MS",10), command=lambda: delete_student_c(text1d.get("1.0",END)))
    butt1.place(relx=0.45,rely=0.73)

    # #

    butt2=Button(main, text="Back",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=teacher_login)
    butt2.place(relx=0.48,rely=0.92)

    butt3=Button(main, text="Exit",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=main.destroy)
    butt3.place(relx=0.94,rely=0.92)


    main.mainloop()

def add_student_c(sid, name, roll_no, year, flag):
    if flag==1:  
        sid = int(sid[0:len(sid)-1])
        name = str(name[0:len(name)-1]).lower()
        roll_no = int(roll_no[0:len(roll_no)-1])
        year = int(year[0:len(year)-1])
    
    if len(str(roll_no))!=9:
        label6=Label(frame4,text="Incorrect Roll no. It must be 6 digit.",fg="white",bg="black", font=("Courier",10))
        label6.place(relx=0.,rely=0.2)
        return 0
    # print(year,type(year))
    if year!=1 and year!=2:
        if year!=3 and year!=4:
            label6=Label(frame4,text="Incorrect year. Enter either 1, 2, 3 or 4.",fg="white",bg="black", font=("Courier",10))
            label6.place(relx=0,rely=0.2)
            return 0

    # print(f"{sid} {name} {roll_no} {year}")

    mysql.execute("select * from student_details")
    for i in mysql:
        if i[0] == int(sid):
            label6=Label(frame4,text="Student Already Exits",fg="white",bg="black", font=("Courier",10))
            label6.place(relx=0,rely=0.2)
            print("Student already Exits")
            return 0 
        else:
            # query = "INSERT INTO student_details(ID,name,roll_no,year) VALUES (%s,'%s','%s','%s','%s')"
            query = f"INSERT INTO student_details(ID,name,roll_no,year,issued_book) VALUES ({sid}, '{name}', '{roll_no}', '{year}', '');"
            try:
                data = (sid, name, roll_no, year, "")
                # print(query)
                mysql.execute(query)
                mydb.commit()
                print("Done Updating")
                if flag==0:
                    # butt1r["state"]=DISABLED
                    # butt2r["state"]=DISABLED
                    label6=Label(frame4,text=f"{name.title()} added sucessfully.",fg="white",bg="black", font=("Courier",10))
                    label6.place(relx=0,rely=0.2)
                    request_delete(sid, name, roll_no, year, flag)
                return 0
                label6=Label(frame4,text="Done Uploading",fg="white",bg="black", font=("Courier",10))
                label6.place(relx=0,rely=0.2)
            except Error as e:
                label6=Label(frame4,text="Error Updating Database -",fg="white",bg="black", font=("Courier",10))
                label6.place(relx=0,rely=0.2)
                label7=Label(frame4,text="{}".format(e),fg="white",bg="black", font=("Courier",10))
                label7.place(relx=0,rely=0.33)
                print("Error updating Database - {}".format(e))
                return 0
    
    # if flag==0:
        # butt1r["status"]=DISABLED
        # butt2r["status"]=DISABLED

def delete_student_c(delete):
    global frame2d, frame4
    lst1=[]
    delete=int(delete)
    print(delete,type(delete))

    mysql.execute("select * from student_details")
    for i in mysql:
            if i[0]==delete and i[4]=="":
                query=f"DELETE FROM student_details WHERE ID={delete}"
                try:
                    mysql.execute(query)
                    mydb.commit()
                    label1=Label(frame4, text="Student Deleted Sucessfully.",bg="black",fg="white", font=("Courier",10))
                    label1.place(relx=0,rely=0.2)
                    print("Student Deleted Sucessfully")
                    return 0
                except Error as e:
                    label1=Label(frame4, text="Error Deleting Student - ",bg="black",fg="white", font=("Courier",10))
                    label1.place(relx=0,rely=0.2)
                    label1=Label(frame4, text="{}.".format(e),bg="black",fg="white", font=("Courier",10))
                    label1.place(relx=0,rely=0.33)
                    print("Error Deleting Student - {}".format(e))
                    return 0
            elif i[0]==delete and i[4]!="":
                label1=Label(frame4, text="Student is issued a book.",bg="black",fg="white", font=("Courier",10))
                label1.place(relx=0,rely=0.2)
                print("Student is issued a book.")
                return 0

    label1=Label(frame4, text="Student is not in database.",bg="black",fg="white", font=("Courier",10))
    label1.place(relx=0,rely=0.2)


def search_book_student():
    global frame21,frame2
    main.title("Search Books / Student")
    # setting size of gui by taking size of image
    image_b=Image.open("lib1.jpg")
    [w,h]=image_b.size
    main.geometry(f"{w}x{h}")
    # Adding Background image to tkinter
    image=Image.open("lib1.jpg")
    image_b=ImageTk.PhotoImage(image, master=main)
    label=Label(main, image=image_b)
    label.place(relx=0,rely=0)

    frame1 = Frame(main,bg="aqua",bd=5)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1 = Label(frame1, text="Search Books / Student", bg="Black", fg="white", font=("Cosmic San MS",15))
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)

    # Book search

    frame2 = Frame(main,bg="black",bd=5)
    frame2.place(relx=0.03,rely=0.3,relwidth=0.45,relheight=0.5)

    frame3 = Frame(frame2,bg="aqua",bd=3)
    frame3.place(relx=0.266,rely=0.02,relwidth=0.5,relheight=0.15)
    label2 = Label(frame3, text="Search Book",bg="black", fg="white", font=("Cosmic San MS",15))
    label2.place(relx=0,rely=0,relwidth=1,relheight=1)

    label2=Label(frame2, text="Enter Book Name : ", bg="black", fg="white", font=("Cosmic San MS",10))
    label2.place(relx=0.02,rely=0.25)

    text = Text(frame2, bd=3, width=26, height=1)
    text.place(relx=0.3,rely=0.25)

    butt1=Button(frame2, text="Search",bg="pink", bd=3, fg="black", font=("Cosmic San Ms",10), command=lambda: search_book_ct(text.get("1.0",END)))
    butt1.place(relx=0.85,rely=0.25)
   
    butt2=Button(main, text="Exit",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=main.destroy)
    butt2.place(relx=0.94,rely=0.92)

    # Student Search
    
    frame21 = Frame(main,bg="black",bd=5)
    frame21.place(relx=0.53,rely=0.3,relwidth=0.45,relheight=0.5)

    frame3 = Frame(frame21,bg="aqua",bd=3)
    frame3.place(relx=0.266,rely=0.02,relwidth=0.5,relheight=0.15)
    label2 = Label(frame3, text="Search Student",bg="black", fg="white", font=("Cosmic San MS",15))
    label2.place(relx=0,rely=0,relwidth=1,relheight=1)

    label2=Label(frame21, text="Enter Student Name : ", bg="black", fg="white", font=("Cosmic San MS",10))
    label2.place(relx=0.02,rely=0.25)

    text = Text(frame21, bd=3, width=26, height=1)
    text.place(relx=0.3,rely=0.25)

    butt1=Button(frame21, text="Search",bg="pink", bd=3, fg="black", font=("Cosmic San Ms",10), command=lambda: search_student_c(text.get("1.0",END)))
    butt1.place(relx=0.85,rely=0.25)
    
    ##
    
    butt2=Button(main, text="Back",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=teacher_login)
    butt2.place(relx=0.48,rely=0.92)

    butt3=Button(main, text="Exit",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=main.destroy)
    butt3.place(relx=0.94,rely=0.92)

    main.mainloop()

def search_book_ct(search):
    global main, frame21, frame2
    search=str(search)
    search=search[0:len(search)-1]
    print(f"Book name = {search}")
    query="SELECT * FROM books"
    mysql.execute(query)
    s=0.47

    for i in mysql:
        b=""
        for j in i[:-1]:b+=f" {j}"
        if search in b:
            f=1

            label=Label(frame2, text="--------------------------------------------------------------------------------------------------------------------------------",fg="white", bg="black", font=("Cosmic San MS",10))
            label.place(relx=0,rely=0.4)
            
            label1=Label(frame2, text="BID       Name                                                 Author                                   Status",fg="white", bg="black", font=("Cosmic San MS",10))
            label1.place(relx=0.02,rely=0.35)
            
            label2=Label(frame2, text=f"{i[0]}",fg="white", bg="black", font=("Cosmic San MS",10))
            label2.place(relx=0.01,rely=s)
            
            label3=Label(frame2, text=f"{i[1].title()}",fg="white", bg="black", font=("Cosmic San MS",10))
            label3.place(relx=0.1,rely=s)
            
            label4=Label(frame2, text=f"{i[2].title()}",fg="white", bg="black", font=("Cosmic San MS",10))
            label4.place(relx=0.53,rely=s)

            label5=Label(frame2, text=f"{i[3].title()}",fg="white", bg="black", font=("Cosmic San MS",10))
            label5.place(relx=0.87,rely=s)

            s+=0.1
    
    if f!=1:
        label=Label(frame2, text="No Result Found", fg="white", bg="black", font=("Cosmic San MS",10))
        label.place(relx=0.02,rely=0.6)
        print("No Result Found")
        print(b)
    
    main.mainloop()

def search_student_c(search):
    global main, frame21
    search=str(search)
    search=search[0:len(search)-1]
    print(f"Book name = {search}")
    query="SELECT * FROM student_details"
    mysql.execute(query)
    s=0.45

    for i in mysql:
        b=""
        for j in i:b+=f" {j}"        # save all student in b
        print(b)
        if search in b:
            f=1

            label=Label(frame21, text="--------------------------------------------------------------------------------------------------------------------------------",fg="white", bg="black", font=("Cosmic San MS",10))
            label.place(relx=0,rely=0.4)
        
            label1=Label(frame21, text=" SID          Name                                     Roll No                   Year        Issued Book",fg="white", bg="black", font=("Cosmic San MS",10))
            label1.place(relx=0.01,rely=0.35)
            
            label2=Label(frame21, text=f"{i[0]}",fg="white", bg="black", font=("Cosmic San MS",10))
            label2.place(relx=0.01,rely=s)
            
            label3=Label(frame21, text=f"{i[1].title()}",fg="white", bg="black", font=("Cosmic San MS",10))
            label3.place(relx=0.13,rely=s)
            
            label4=Label(frame21, text=f"{i[2]}",fg="white", bg="black", font=("Cosmic San MS",10))
            label4.place(relx=0.47,rely=s)

            label5=Label(frame21, text=f"{i[3]}",fg="white", bg="black", font=("Cosmic San MS",10))
            label5.place(relx=0.7,rely=s)

            label6=Label(frame21, text=f"{i[4]}",fg="white", bg="black", font=("Cosmic San MS",10))
            label6.place(relx=0.81,rely=s)

            s+=0.15
    
    if f!=1:
        label=Label(frame2, text="No Result Found", fg="white", bg="black", font=("Cosmic San MS",10))
        label.place(relx=0.02,rely=0.6)
        print("No Result Found")
        print(b)
    
    main.mainloop()


def request_teacher():
    global frame2, frame4
    main.title("View Requests")
    # setting size of gui by taking size of image
    image_b=Image.open("lib1.jpg")
    [w,h]=image_b.size
    main.geometry(f"{w}x{h}")
    # Adding Background image to tkinter
    image=Image.open("lib1.jpg")
    image_b=ImageTk.PhotoImage(image, master=main)
    label=Label(main, image=image_b)
    label.place(relx=0,rely=0)

    frame1 = Frame(main,bg="aqua",bd=5)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1 = Label(frame1, text="All Requests", bg="Black", fg="white", font=("Cosmic San MS",15))
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame2 = Frame(main,bg="black",bd=3)
    frame2.place(relx=0.05,rely=0.27,relwidth=0.4,relheight=0.72)
    label2 = Label(frame2, text="Requests :",bg="black", fg="white", font=("Courier",10))
    label2.place(relx=0,rely=0)
    
    frame3 = Frame(main,bg="black",bd=3)
    frame3.place(relx=0.53,rely=0.27,relwidth=0.4,relheight=0.5)

    frame4 = Frame(main,bg="black",bd=5)
    frame4.place(relx=0.53,rely=0.79,relwidth=0.4,relheight=0.18)
    label3 = Label(frame4, text="Terminal:",bg="black", fg="white", font=("Courier",10))
    label3.place(relx=0,rely=0)

    mysql.execute("SELECT * FROM request")
    s1=0.16
    s2=0.16
    for j,i in enumerate(mysql):
        if j<=8:
            label=Label(frame2, text="---------------------------------------------------------------------------------------------------------------------",fg="white", bg="black", font=("Cosmic San MS",10))
            label.place(relx=0,rely=0.11)
            label1=Label(frame2, text=" SID             Name                      Roll No            Year           Action",fg="white", bg="black", font=("Cosmic San MS",10))
            label1.place(relx=0.01,rely=0.06) 
            printa(i,s1,frame2)      
            s1+=0.095
        elif j>8 and j<=14:
            label=Label(frame3, text="---------------------------------------------------------------------------------------------------------------------",fg="white", bg="black", font=("Cosmic San MS",10))
            label.place(relx=0,rely=0.09)
            label1=Label(frame3, text=" SID             Name                      Roll No            Year           Action",fg="white", bg="black", font=("Cosmic San MS",10))
            label1.place(relx=0.01,rely=0.03) 
            printa(i,s2,frame3)      
            s2+=0.136
        else:
            label = Label(frame3, text=".....many more", fg="white", bg="black", font=("Cosmin San MS", 10))
            label.place(relx=0.81,rely=0.945)
    butt3=Button(main, text="Back",bg="pink",bd=5,  fg="black", font=("Cosmic San MS",10), command=teacher_login)
    butt3.place(relx=0.47,rely=0.92)

    butt4=Button(main, text="Exit",bg="pink",bd=5,  fg="black", font=("Cosmic San MS",10), command=main.destroy)
    butt4.place(relx=0.95,rely=0.92)
    main.mainloop()

def printa(i,s,f):
    global butt1r, butt2r
    label2=Label(f, text=f"{i[0]}",fg="white", bg="black", font=("Cosmic San MS",10))
    label2.place(relx=0.01,rely=s+0.01)
    
    label3=Label(f, text=f"{i[1].title()}",fg="white", bg="black", font=("Cosmic San MS",10))
    label3.place(relx=0.17,rely=s+0.01)
    
    label4=Label(f, text=f"{i[2]}",fg="white", bg="black", font=("Cosmic San MS",10))
    label4.place(relx=0.43,rely=s+0.01)

    label5=Label(f, text=f"{i[3]}",fg="white", bg="black", font=("Cosmic San MS",10))
    label5.place(relx=0.64,rely=s+0.01)

    butt1r=Button(f, text="Accept",bg="pink",bd=5, fg="black", state=NORMAL, font=("Cosmic San MS",10), command=lambda: request_add(i[0], i[1], i[2], i[3], 0))
    butt1r.place(relx=0.75,rely=s)
    
    butt2r=Button(f, text="Delete",bg="pink",bd=5,  fg="black", state=NORMAL, font=("Cosmic San MS",10), command=lambda: request_delete(i[0], i[1], i[2], i[3], 0))
    butt2r.place(relx=0.88,rely=s)


def request_delete(sid, name, roll_no, year ,flag):
    print("request delete called")
    # print(f"{sid} {name} {roll_no} {year}")
    # butt1r["state"]=DISABLED

    # mysql.execute("select * from request")
    # for i in mysql:
    #     query=f"DELETE FROM request WHERE ID={sid}"
    #     try:
    #         mysql.execute(query)
    #         mydb.commit()
    #         label1=Label(frame4, text="Request Deleted Sucessfully.",bg="black",fg="white", font=("Courier",10))
    #         label1.place(relx=0,rely=0.2)
    #         print("Request Deleted Sucessfully")
    #         return 0
    #     except Error as e:
    #         label1=Label(frame4, text="Error Deleting Request - ",bg="black",fg="white", font=("Courier",10))
    #         label1.place(relx=0,rely=0.2)
    #         label1=Label(frame4, text="{}.".format(e),bg="black",fg="white", font=("Courier",10))
    #         label1.place(relx=0,rely=0.33)
    #         print("Error Deleting Request - {}".format(e))
    #         return 0
    

def request_add(sid, name, roll_no, year, flag):
    print("request add called")
    # print(f"{sid} {name} {roll_no} {year} {flag}")
    a=add_student_c(sid, name, roll_no, year, flag)
    # if a==0:
    #     butt1r["state"]=DISABLED


# Request for student login

def request_student():
    global frame2,frame4, frame2d, text1d
    main.title("View Book")
    # setting size of gui by taking size of image
    image_b=Image.open("lib1.jpg")
    [w,h]=image_b.size
    main.geometry(f"{w}x{h}")
    # Adding Background image to tkinter
    image=Image.open("lib1.jpg")
    image_b=ImageTk.PhotoImage(image, master=main)
    label=Label(main, image=image_b)
    label.place(relx=0,rely=0)

    frame1 = Frame(main,bg="aqua",bd=5)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1 = Label(frame1, text="Request for Student Login", bg="Black", fg="white", font=("Cosmic San MS",15))
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame4 = Frame(main,bg="black",bd=5)
    frame4.place(relx=0.55,rely=0.3,relwidth=0.4,relheight=0.6)
    label6 = Label(frame4, text="Terminal:",bg="black", fg="white", font=("Courier",10))
    label6.place(relx=0,rely=0)

    # #

    frame2 = Frame(main,bg="black",bd=5)
    frame2.place(relx=0.05,rely=0.3,relwidth=0.4,relheight=0.6)

    frame3 = Frame(frame2,bg="aqua",bd=3)
    frame3.place(relx=0.266,rely=0.02,relwidth=0.5,relheight=0.15)
    label2 = Label(frame3, text="Request Form",bg="black", fg="white", font=("Cosmic San MS",15))
    label2.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    label2 = Label(frame2, text="Student ID :",bg="black", fg="white", font=("Cosmic San MS",10))
    label2.place(relx=0.1,rely=0.22)
    text1 = Text(frame2, bd=3, height=1,width=30)
    text1.place(relx=0.37,rely=0.22)

    label3 = Label(frame2, text="Name of Student :",bg="black", fg="white", font=("Cosmic San MS",10))
    label3.place(relx=0.1,rely=0.4)
    text2 = Text(frame2, bd=3, height=1,width=30)
    text2.place(relx=0.37,rely=0.4)

    label4 = Label(frame2, text="Roll No of Student :",bg="black", fg="white", font=("Cosmic San MS",10))
    label4.place(relx=0.1,rely=0.58)
    text3 = Text(frame2, bd=3, height=1,width=30)
    text3.place(relx=0.37,rely=0.58)

    label5 = Label(frame2, text="Year :",bg="black", fg="white", font=("Cosmic San MS",10))
    label5.place(relx=0.1,rely=0.76)
    text4 = Text(frame2, bd=3, height=1,width=30)
    text4.place(relx=0.37,rely=0.76)

    butt1 = Button(frame2, text="Request", bg="pink",width=5 ,height=1 ,bd=5, fg="black", font=("Cosmic San MS",10),command=lambda: request_c(text1.get("1.0",END), text2.get("1.0",END), text3.get("1.0",END), text4.get("1.0",END)))
    butt1.place(relx=0.45,rely=0.88)

    # #

    butt2=Button(main, text="Back",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=main_window)
    butt2.place(relx=0.48,rely=0.92)

    butt3=Button(main, text="Exit",bg="pink",bd=5, fg="black", font=("Cosmic San MS",10), command=main.destroy)
    butt3.place(relx=0.94,rely=0.92)


    main.mainloop()

def request_c(sid, name, roll_no, year):
    # sid = text1.get("1.0",END)
    # name = text2.get("1.0",END)
    # roll_no = text3.get("1.0",END)
    # year = text4.get("1.0",END)
    
    sid = int(sid[0:len(sid)-1])
    name = str(name[0:len(name)-1]).lower()
    roll_no = int(roll_no[0:len(roll_no)-1])
    year = int(year[0:len(year)-1])
    
    if len(str(roll_no))!=9:
        label6=Label(frame4,text="Incorrect Roll no. It must be 6 digit.",fg="white",bg="black", font=("Courier",10))
        label6.place(relx=0.,rely=0.2)
        return 0
    print(year,type(year))
    if year!=1 and year!=2:
        if year!=3 and year!=4:
            label6=Label(frame4,text="Incorrect year. Enter either 1, 2, 3 or 4.",fg="white",bg="black", font=("Courier",10))
            label6.place(relx=0,rely=0.2)
            return 0

    print(f"{sid} {name} {roll_no} {year}")

    mysql.execute("select * from request")
    for i in mysql:
        print(i)
        if i[0] == int(sid):
            label6=Label(frame4,text="Your Already Requested wait for Management Response.",fg="white",bg="black", font=("Courier",10))
            label6.place(relx=0,rely=0.2)
            print("Your Already Requested wait for Management Response.")
            return 0 
        else:
            # query = "INSERT INTO request(ID,name,roll_no,year) VALUES (%s,'%s','%s','%s')"
            query = f"INSERT INTO request(ID,name,Roll_no,year) VALUES ({sid}, '{name}', '{roll_no}', '{year}');"
            try:
                data = (sid, name, roll_no, year)
                print(query)
                mysql.execute(query)
                mydb.commit()
                label6=Label(frame4,text="Done Uploading",fg="white",bg="black", font=("Courier",12))
                label6.place(relx=0,rely=0.15)
                label7=Label(frame4,text=f"Sid:       {sid}",fg="white",bg="black", font=("Courier",12))
                label7.place(relx=0,rely=0.3)
                label7=Label(frame4,text=f"Name:      {name}",fg="white",bg="black", font=("Courier",12))
                label7.place(relx=0,rely=0.4)
                label7=Label(frame4,text=f"Roll No:   {roll_no}",fg="white",bg="black", font=("Courier",12))
                label7.place(relx=0,rely=0.5)
                label7=Label(frame4,text=f"Year:      {year}",fg="white",bg="black", font=("Courier",12))
                label7.place(relx=0,rely=0.6)
                print("Done Updating")
                return 0
            except Error as e:
                label6=Label(frame4,text="Error Updating Database -",fg="white",bg="black", font=("Courier",10))
                label6.place(relx=0,rely=0.2)
                label7=Label(frame4,text="{}".format(e),fg="white",bg="black", font=("Courier",10))
                label7.place(relx=0,rely=0.33)
                print("Error updating Database - {}".format(e))
                return 0




if __name__=="__main__":
    teacher_login()
    # student_login()
    # main_window()