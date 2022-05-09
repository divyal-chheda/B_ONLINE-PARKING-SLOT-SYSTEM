import smtplib #to send email
import tkinter
import tkinter as tk
from email.mime.multipart import MIMEMultipart#sending email with file attachment
from email.mime.text import MIMEText #sending text emails
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk, simpledialog
import mysql.connector
import qrcode
from resizeimage import resizeimage
import cv2  # read image/camera/video input
from pyzbar.pyzbar import decode #decoding the codes
import time
from tkcalendar import *
import random


global USER_INP
global newuser
global newpassword
global newcontact
global newemail
global newaddress
# global newpincode
global newverify

root = tk.Tk()
root.title("QR Code Generator And Scanner")
root.geometry("1110x690")
root.config(bg='#000000')

image_0 = Image.open('D:\\QRCode\\pycharm\\design2.png')
back_end = ImageTk.PhotoImage(image_0)
lbl = Label(root, image=back_end)
lbl.place(x=5, y=5, width=1100, height=680)

def temp(e):
   username.delete(0,"end")

def temp2(e):
   userpassword.delete(0,"end")


username = Entry(root, font=("Times New Roman", 15), bg='white')
username.insert(0, "USERNAME")
username.place(x=640, y=258, width=360, height=48)

userpassword = Entry(root, font=("Times New Roman", 15), bg='white', show='*')
userpassword.insert(0, "PASSWORD")
userpassword.place(x=640, y=346, width=360, height=48)

lbl = Label(root, text="QR Code Generator & Scanner", bg='#BEBEBE', fg="black", font=("Segoe UI Black", 18, 'bold'))
lbl.place(x=440, y=645)

username.bind("<FocusIn>", temp)
userpassword.bind("<FocusIn>", temp2)

def my_options():
    print("Options function")
    optionsframe = Frame()
    optionsframe.place(x=0, y=0, width=1280, height=720)
    optionsframe.config(bg='black')

    global img
    path = "D:\\QRCode\pycharm\\regid17.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(optionsframe, image=img)
    panel.place(x=5, y=5, height=660, width=1095)

    def destroy():
        root.destroy()

    btn_back = Button(root, text='SHUTDOWN',command=destroy,
                      font=("Segoe UI Black", 15, 'bold'), bg='white', fg="#187bcd")
    btn_back.place(x=2, y=2, width=150, height=40)

    def my_qr():
        print("Generation function")
        generationframe = Frame()
        generationframe.place(x=0, y=0, width=1280, height=720)
        generationframe.config(bg='black')

        global img
        path = "D:\\QRCode\pycharm\\regid5.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(generationframe, image=img)
        panel.place(x=5, y=5, width=1095)

        # code = Entry(root, font=("Segoe UI Black", 15), bg='lightyellow')
        # code.insert(0,"PRODUCT CODE")
        # code.place(x=50, y=50, width=350, height=70)

        text_font = ('Segoe UI Black', '15')

        lst3 = ['140-Grocery', '145-Clothing', '158-Bathroom Essentials', '165-FootWear']

        comboBox3 = ttk.Combobox(root, values=lst3, font=text_font)
        comboBox3.set('Select Category & Code')
        comboBox3.place(x=50, y=50, width=350, height=70)

        # company = Entry(root, font=("Segoe UI Black", 15), bg='lightyellow')
        # company.insert(0,"NAME OF COMPANY")
        # company.place(x=50, y=150, width=350, height=70)
        lst = ['Amul', 'Bata', 'Dabur', 'Britania', 'Too Yumm', 'Kellogs', 'Saffola', 'Nutella', 'Wibs', 'Patanjali',
               'Colgate', 'Oral-B', 'Atlantic Collection']
        text_font = ('Segoe UI Black', '15')

        comboBox = ttk.Combobox(root, values=lst, font=text_font)
        comboBox.set('Select Company')
        comboBox.place(x=50, y=150, width=350, height=70)

        # product = Entry(root, font=("Segoe UI Black", 15), bg='lightyellow')
        # product.insert(0,"NAME OF PRODUCT")
        # product.place(x=50, y=250, width=350, height=70)

        lst2 = ['Milk', 'Cheese', 'Chocolates', 'Dips', 'Chavanprash', 'Cream & Onion Chips', 'Tomato Chips',
                'Banana Chips', 'Salted Chips', 'Hazelnut Flavour', 'Ferroro Rocher Flavour', 'Healthy Oil',
                'Olive oil',
                'Brown Bread', 'White Bread', 'Chococs', 'Dant Kanti', 'Formal Shoes', 'Scandals', 'Tooth Brush',
                'Tooth Paste', 'Whitening Tooth Paste', 'TShirt', 'Shirt', 'Jeans', 'Trouser', 'Honey', 'Good Day',
                'Marie Gold', 'Vita Marie']
        comboBox2 = ttk.Combobox(root, values=lst2, font=text_font)
        comboBox2.set('Select Product')
        comboBox2.place(x=50, y=250, width=350, height=70)

        def temp_text10(e):
            quantity.delete(0,"end")

        quantity = Entry(root, font=("Segoe UI Black", 15), bg='lightyellow')
        quantity.insert(0, "ENTER QUANTITY")
        quantity.place(x=50, y=350, width=350, height=70)

        quantity.bind("<FocusIn>", temp_text10)

        def temp_text11(e):
            description.delete(0,"end")

        description = Entry(root, font=("Segoe UI Black", 15), bg='lightyellow')
        description.insert(0, "WRITE DESCRIPTION OF PRODUCT")
        description.place(x=50, y=450, width=350, height=70)

        description.bind("<FocusIn>", temp_text11)

        # manufacture = Entry(root, font=("Segoe UI Black", 15), bg='lightyellow')
        # manufacture.insert(0,"ENTER DATE OF MANUFACTURE")
        # manufacture.place(x=50, y=550, width=350, height=70)

        lbl_20 = Label(root, text="SELECT DATE OF MANUFACTURE", bg='white', fg="#187bcd",
                        font=("Segoe UI Black", 15))
        lbl_20.place(x=450, y=170)

        cal2 = DateEntry(root, selectmode='day', font=text_font)
        cal2.place(x=450, y=200, width=350, height=70)

        # expiry = Entry(root, font=("Segoe UI Black", 15), bg='lightyellow')
        # expiry.insert(0,"ENTER DATE OF EXPIRY")
        # expiry.place(x=450, y=50, width=350, height=70)

        lbl_21 = Label(root, text="SELECT DATE OF EXPIRY", bg='white', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_21.place(x=450, y=40)

        cal3 = DateEntry(root, selectmode='day', font=text_font)
        cal3.place(x=450, y=70, width=350, height=70)

        def temp_text12(e):
            price.delete(0,"end")

        price = Entry(root, font=("Segoe UI Black", 15), bg='lightyellow')
        price.insert(0, "PER UNIT PRICE OF PRODUCT")
        price.place(x=50, y=570, width=350, height=70)

        price.bind("<FocusIn>", temp_text12)

        btn_back = Button(root, text='BACK', command=my_options,
                          font=("Segoe UI Black", 15, 'bold'), bg='white', fg="#187bcd")
        btn_back.place(x=2, y=2, width=150, height=40)

        def maker_qr():
            if comboBox3.get() == '' or comboBox.get() == '' or comboBox2.get() == '' or quantity.get() == '' or description.get() == '' or cal2.get() == '' or cal3.get() == '' or price.get() == '':
                messagebox.showerror("Generate QR Code", "All Fields Are Required To Generate Your QR Code!!!!")

            else:
                qr_data = (
                    f"Code Of Product:- {comboBox3.get()}\nName Of Company:-{comboBox.get()}\nName Of Product:- {comboBox2.get()}\nQuantity:- {quantity.get()}\nDescription Of Product:- {description.get()}\nDate Of Manufacture:- {cal2.get()}\nDate Of Expiry:- {cal3.get()}\nPrice Per Unit:- {price.get()}")
                qr_code = qrcode.make(qr_data)
                print(qr_code)
                qr_code = resizeimage.resize_cover(qr_code, [180, 180])
                root.im = ImageTk.PhotoImage(qr_code)
                root.qr_code.config(image=root.im)

                # Product QR Code window

        qr_Frame = Frame(root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=500, y=300, width=250, height=250)

        Product_title = Label(qr_Frame, text=" QR Code", font=("Segoe UI Black", 20), bg='#043256',
                              fg='white').place(x=0, y=0, relwidth=1)

        root.qr_code = Label(qr_Frame, text='No QR\nAvailable', font=('Segoe UI Black', 15), bg='#3f51b5',
                             fg='white', bd=1, relief=RIDGE)
        root.qr_code.place(x=25, y=55, width=200, height=180)

        btn_maker = Button(root, text='GENERATE QR CODE', command=maker_qr,
                           font=("Segoe UI Black", 15, 'bold'), bg='white', fg="#187bcd").place(x=780, y=320, width=250,
                                                                                                height=70)

        def save_qr():
            if comboBox3.get() == "" or comboBox.get() == "" or comboBox2.get() == "" or quantity.get() == "" or description.get() == "" or cal2.get() == "" or cal3.get() == "" or price.get() == "":
                messagebox.showerror("QR Code Generator & Scanner", "All Fields Are Required!!")

            else:

                ProductCode = comboBox3.get()
                Company = comboBox.get()
                Product = comboBox2.get()
                Quantity = quantity.get()
                Description = description.get()
                ManufactureDate = cal2.get()
                ExpiryDate = cal3.get()
                Price = price.get()
                mysqldb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="qrcodegenerator"
                )
                mycursor = mysqldb.cursor()
                try:
                    sql = "INSERT INTO qrdetails (ProductCode,Company,Product,Quantity,Description,ManufactureDate,ExpiryDate,Price) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (ProductCode, Company, Product, Quantity, Description, ManufactureDate, ExpiryDate, Price)
                    mycursor.execute(sql, val)
                    mysqldb.commit()
                    messagebox.showinfo("Information", "QR Details Saved Successfully")

                except Exception as e:
                    print(e)
                    mysqldb.rollback()
                    mysqldb.close()

                comboBox3.delete(0,tkinter.END)
                comboBox.delete(0,tkinter.END)
                comboBox2.delete(0,tkinter.END)
                quantity.delete(0,tkinter.END)
                description.delete(0,tkinter.END)
                cal2.delete(0,tkinter.END)
                cal3.delete(0,tkinter.END)
                price.delete(0,tkinter.END)

        btn_saver = Button(root, text='SAVE QR DETAILS', command=save_qr,
                           font=("Segoe UI Black", 15, 'bold'), bg='white', fg="#187bcd").place(x=780, y=410, width=250,
                                                                                                height=70)

    btn_generate = Button(root, text='GENERATE NEW QR CODE', font=("Segoe UI Black", 15, 'bold'), bg='#F10066',
                          fg="white", command=my_qr,
                          ).place(x=425, y=100, width=300, height=80)

    def document():
        print("Document function")
        documentframe = Frame()
        documentframe.place(x=0, y=0, width=1280, height=720)
        documentframe.config(bg='black')

        lbl_30 = Label(root, text="QR CODE GENERATOR & SCANNER", bg='BLACK', fg="white",
                       font=("Segoe UI Black", 25))
        lbl_30.place(x=280, y=5)

        lbl_31 = Label(root, text="HOW TO GENERATE A QRCODE FOR A PRODUCT ?", bg='BLACK', fg="yellow",
                       font=("Segoe UI Black", 20))
        lbl_31  .place(x=5, y=55)

        lbl_32 = Label(root, text="To generate a new QR Code, select the generate new qr code option from the options menu.On clicking"
                                  , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_32.place(x=5, y=95)

        lbl_33 = Label(root,
                       text="the button you will see a display on screen where you have to fill all the details to generate your"
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_33.place(x=5, y=125)

        lbl_34 = Label(root,
                       text="qr codee.After entring all the details click on generate qr code button & the qr code will be"
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_34.place(x=5, y=155)

        lbl_35 = Label(root,
                       text="displayed in the frame.If the user wants to save the details of the generated qr code , then click"
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_35.place(x=5, y=185)

        lbl_36 = Label(root,
                       text="on save qr details & the details will be saved.Click back button to return to main menu"
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_36.place(x=5, y=215)

        lbl_37 = Label(root,
                       text="How to scan a QR Code through our system ?"
                       , bg='BLACK', fg="yellow",
                       font=("Segoe UI Black", 20))
        lbl_37.place(x=5, y=245)


        lbl_38 = Label(root,
                       text="To scan a QR Code through our system , click on scan QR/Bar code button from the main menu. The"
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_38.place(x=5, y=285)

        lbl_38 = Label(root,
                       text="camera of your device will be turned on within a few minutes. After the camera is ON, place the "
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_38.place(x=5, y=315)

        lbl_38 = Label(root,
                       text="QR Code on front of the camera. If the QR Code is not used then you will see message on the screen"
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_38.place(x=5, y=345)

        lbl_39 = Label(root,
                       text="saying that the QR Code is valid and you can use it . Further it will show you the information"
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_39.place(x=5, y=375)

        lbl_40 = Label(root,
                       text="stored in the QR Code through a pop-up box. If the QR Code is already used, it will show you a "
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_40.place(x=5, y=405)

        lbl_41 = Label(root,
                       text="error that the QR COde is already used & you can't use it further. To return to the main menu,"
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_41.place(x=5, y=435)

        lbl_42 = Label(root,
                       text="press Q from the kerboard or click on close button on the right most top of the camera window."
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_42.place(x=5, y=465)

        lbl_43 = Label(root,
                       text="How to get admin access ?"
                       , bg='BLACK', fg="yellow",
                       font=("Segoe UI Black", 25))
        lbl_43.place(x=5, y=495)

        lbl_44 = Label(root,
                       text="Click on the admin access button from the option menu. You will see a screen asking for your "
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_44.place(x=5, y=540)

        lbl_45 = Label(root,
                       text="adminusername & adminpassword. Enter your correct credentials & click on login button. After "
                       , bg='BLACK', fg="#187bcd",
                       font=("Segoe UI Black", 15))
        lbl_45.place(x=5, y=570)

        btn_con = Button(root, text='BACK', font=("Segoe UI Black", 15, 'bold'), bg='white',
                         fg="#187bcd", command=my_options
                         ).place(x=900, y=5, width=200, height=50)

        def newdoc():
            print("Document function")
            document2frame = Frame()
            document2frame.place(x=0, y=0, width=1280, height=720)
            document2frame.config(bg='black')

            lbl_46 = Label(root, text="QR CODE GENERATOR & SCANNER", bg='BLACK', fg="white",
                           font=("Segoe UI Black", 25))
            lbl_46.place(x=280, y=5)

            lbl_47 = Label(root,
                           text="logging in you will see a admin dashboard where admin will have three options registerd users,"
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_47.place(x=5, y=50)

            lbl_48 = Label(root,
                           text="generated QR's & Admins. By clicking on registered users, admin will see details of all the "
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_48.place(x=5, y=80)

            lbl_49 = Label(root,
                           text="regsitered users. Admin can also register new user,update details of registered users & can delete"
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_49.place(x=5, y=110)

            lbl_50 = Label(root,
                           text="a registered user. Clicking on generated QR's admin will see details of all the generated QR codes."
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_50.place(x=5, y=140)

            lbl_51 = Label(root,
                           text="Admin can update the details to a generated QR, delete the details of the generated QR. Clicking on"
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_51.place(x=5, y=170)

            lbl_52 = Label(root,
                           text="Admins, admin can add or delete a new admin. To exit from the admin access function, click on logout "
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_52.place(x=5, y=200)

            lbl_53 = Label(root,
                           text="button on the top right corner of the screen & you will return to main menu."
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_53.place(x=5, y=230)

            lbl_54 = Label(root,
                           text="How to contact us & Give your feedback ?"
                           , bg='BLACK', fg="yellow",
                           font=("Segoe UI Black", 25))
            lbl_54.place(x=5, y=260)

            lbl_55 = Label(root,
                           text="In case the user needs to contact us, they can click on contact us button from the main menu. On"
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_55.place(x=5, y=300)

            lbl_56 = Label(root,
                           text="clicking the button, the user will see a screen containing the address of the company & the contact"
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_56.place(x=5, y=330)

            lbl_57 = Label(root,
                           text="details. If a user is facing any difficulties, he can append his name, email-ID & his problem in the fields "
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_57.place(x=5, y=360)

            lbl_58 = Label(root,
                           text="available on the screen & then click on submit button. User can also give us his feedback by clicking on the "
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_58.place(x=5, y=390)

            lbl_59 = Label(root,
                           text="write the review button on the main menu. On clicking the button the user will see the screen containg few"
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_59.place(x=5, y=420)

            lbl_60 = Label(root,
                           text="questions. The user have to answer the questions. They can also suggest some changes that they would like"
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_60.place(x=5, y=450)

            lbl_61 = Label(root,
                           text="to see in the suggestion box given below."
                           , bg='BLACK', fg="#187bcd",
                           font=("Segoe UI Black", 15))
            lbl_61.place(x=5, y=480)

            btn_con = Button(root, text='BACK', font=("Segoe UI Black", 15, 'bold'), bg='white',
                              fg="#187bcd", command=document
                              ).place(x=900, y=5, width=200, height=50)



        btn_continue = Button(root, text='Continue to read', font=("Segoe UI Black", 15, 'bold'), bg='white',
                                    fg="#187bcd", command= newdoc
                                    ).place(x=900, y=630, width=200, height=50)

    btn_documentation = Button(root, text='USER MANUAL', font=("Segoe UI Black", 15, 'bold'), bg='#187bcd',
                          fg="white",command=document
                          ).place(x=900, y=5, width=200, height=50)



    def scan():
        print("Scan Function")
        cap = cv2.VideoCapture(0)
        cap.set(3, 640) #3 width
        cap.set(4, 480) #4 height
        used_codes = []
        camera = True
        while camera == True:
            success, frame = cap.read()

            for code in decode(frame):
                if code.data.decode('utf-8') not in used_codes: #utf8 to get the code decoded properly

                    condition = messagebox.showinfo("QR Code Generator & Scanner", "Approved,You Can Enter!")

                    message = messagebox.showinfo("QR Code Generator & Scanner", code.data.decode('utf-8'))
                    # scanid = simpledialog.askfloat(title="Test", prompt="Enter Product ID.")
                    # scandescription = simpledialog.askstring(title="Test", prompt="Enter Description Of Product.")
                    # scanprice = simpledialog.askstring(title="Test", prompt="Enter Price Of Product.")
                    #
                    # idscan = scanid.get()
                    used_codes.append(code.data.decode('utf-8'))
                    time.sleep(5) #no scan for 5 seconds
                elif code.data.decode('utf-8') in used_codes:
                    # print('Sorry!!! This code has been already used!')
                    messagebox.showerror("QR Code Generator & Scanner", "Sorry!!! This code has been already used!")
                    time.sleep(5)
                else:
                    pass
            cv2.imshow('Scan QR/Bar Code', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    btn_scan = Button(root, text='SCAN QR/BAR CODE', font=("Segoe UI Black", 15, 'bold'), bg='#00021E', fg="white",
                      command=scan, ).place(x=425, y=200, width=300, height=80)

    def myadmin():
        print("Admin Function")
        myadminframe = Frame()
        myadminframe.place(x=0, y=0, width=1280, height=720)
        myadminframe.config(bg='white')

        global img
        path = "D:\\QRCode\pycharm\\regid8.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(myadminframe, image=img)
        panel.place(x=5, y=5, height=680)

        lbl_2 = Label(root, text="ADMIN DASHBOARD", bg='white', fg="#187bcd", font=("Segoe UI Black", 30, 'bold'))
        lbl_2.place(x=425, y=10)

        btn_back = Button(root, text='BACK', command=my_options,
                          font=("Segoe UI Black", 15, 'bold'), bg='white', fg="#187bcd")
        btn_back.place(x=2, y=2, width=150, height=40)

        def show():
            mysqldb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qrcodegenerator"
            )
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT EmployeeID,FullName,Contact,Address FROM registeredusers")
            records = mycursor.fetchall()
            print(records)

            cols = ('ID', 'UserName', 'Contact', 'Address')
            listBox = ttk.Treeview(columns=cols, show='headings')

            for col in cols:
                listBox.heading(col, text=col)
                listBox.grid(row=1, column=0, columnspan=1)
                listBox.place(x=50, y=320)

            for i, (EmployeeID, FullName, Contact, Address) in enumerate(records, start=1):
                listBox.insert("", "end", values=(EmployeeID, FullName, Contact, Address))
                mysqldb.close()

        def users():
            print("Registered Users")
            userframe = Frame()
            userframe.place(x=0, y=0, width=1280, height=720)
            userframe.config(bg='#000000')
            show()

            global img
            path = "D:\\QRCode\pycharm\\regid8.png"
            img = ImageTk.PhotoImage(Image.open(path))
            panel = Label(userframe, image=img)
            panel.place(x=5, y=5, height=680)

            cols = ('ID', 'UserName', 'Contact', 'Address')
            listBox = ttk.Treeview(userframe, columns=cols, show='headings')

            for col in cols:
                listBox.heading(col, text=col)
                listBox.grid(row=1, column=0, columnspan=1)
                listBox.place(x=50, y=320)

            lbl = Label(root, text="ID", bg='white', fg="#187bcd",
                        font=("Segoe UI Black", 22, 'bold'))
            lbl.place(x=430, y=10)

            lbl_new = Label(root, text="USERNAME", bg='white', fg="#187bcd",
                            font=("Segoe UI Black", 22, 'bold'))
            lbl_new.place(x=430, y=70)

            lbl_new1 = Label(root, text="CONTACT", bg='white', fg="#187bcd",
                             font=("Segoe UI Black", 22, 'bold'))
            lbl_new1.place(x=430, y=130)

            lbl_new1 = Label(root, text="ADDRESS", bg='white', fg="#187bcd",
                             font=("Segoe UI Black", 22, 'bold'))
            lbl_new1.place(x=430, y=190)

            # lbl_new1 = Label(root, text="PINCODE", bg='white', fg="#187bcd",
            #                  font=("Segoe UI Black", 22, 'bold'))
            # lbl_new1.place(x=430, y=250)

            id = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            id.place(x=720, y=10, width=320, height=50)

            username = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            username.place(x=720, y=70, width=320, height=50)

            contact = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            contact.place(x=720, y=130, width=320, height=50)

            address = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            address.place(x=720, y=190, width=320, height=50)

            # pincode = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            # pincode.place(x=720, y=250, width=320, height=50)

            btn_back = Button(root, text='BACK', command=myadmin,
                              font=("Segoe UI Black", 15, 'bold'), bg='white', fg="#187bcd")
            btn_back.place(x=2, y=2, width=150, height=40)

            def add():
                ID = id.get()
                Username = username.get()
                Contact = contact.get()
                Address = address.get()
                # Pincode = pincode.get()

                if id.get() == "" or username.get() == "" or contact.get() == "" or address.get() == "" :
                    messagebox.showerror("QR Code Generator & Scanner", "All fields are required")
                else:
                    mysqldb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="qrcodegenerator"
                    )
                    mycursor = mysqldb.cursor()
                    try:
                        sql = "INSERT INTO registeredusers (EmployeeID,FullName,Contact,Address) VALUES (%s,%s,%s,%s)"
                        val = (ID, Username, Contact, Address)
                        mycursor.execute(sql, val)
                        mysqldb.commit()
                        messagebox.showinfo("QR Code Generator & Scanner", "User Registered Successfully")
                        ID.delete(0, END)
                        Username.delete(0, END)
                        Contact.delete(0, END)
                        Address.delete(0, END)
                        # Pincode.delete(0, END)

                        ID.focus_set()
                    except Exception as e:
                        print(e)
                        mysqldb.rollback()
                        mysqldb.close()

                    listBox.bind('<Double-Button-1>', getvalue)

            btn_addusersid = Button(root, text='ADD USER', font=("Segoe UI Black", 15, 'bold'), command=add,
                                    bg='#187bcd', fg="white")
            btn_addusersid.place(x=5, y=70, width=250, height=50)

            def update():
                employeeid = id.get()
                Username = username.get()
                Contact = contact.get()
                Address = address.get()
                # Pincode = pincode.get()
                if id.get() == "" or username.get() == "" or contact.get() == "" or address.get() == "":
                    messagebox.showerror("QR Code Generator & Scanner", "All fields are required")
                else:
                    mysqldb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="qrcodegenerator"
                    )
                    mycursor = mysqldb.cursor()
                    try:
                        sql = "UPDATE registeredusers set FullName = %s, Contact = %s, Address = %s WHERE EmployeeID = %s"
                        val = (Username, Contact, Address, employeeid)
                        mycursor.execute(sql, val)
                        mysqldb.commit()
                        messagebox.showinfo("QR Code Generator & Scanner", "User Details Updated Successfully")
                        employeeid.delete(0, END)
                        Username.delete(0, END)
                        Contact.delete(0, END)
                        Address.delete(0, END)
                        # Pincode.delete(0, END)

                        Username.focus_set()
                    except Exception as e:
                        print(e)
                        mysqldb.rollback()
                        mysqldb.close()
                        listBox.bind('<Double-Button-1>', getvalue)

            btn_update = Button(root, text='UPDATE USER DETAILS', font=("Segoe UI Black", 15, 'bold'), command=update,
                                bg='#187bcd', fg="white")
            btn_update.place(x=5, y=130, width=250, height=50)

            def getvalue():
                id.delete(0, END)
                username.delete(0, END)
                contact.delete(0, END)
                address.delete(0, END)
                # pincode.delete(0, END)

                row_id = listBox.selection()[0]
                select = listBox.set(row_id)

                id.insert(0, select['ID'])
                username.insert(0, select['UserName'])
                contact.insert(0, select['Contact'])
                address.insert(0, select['Address'])
                # pincode.insert(0, select['PinCode'])

                listBox.bind('<Double-Button-1>', getvalue)

            def delete():
                employeeid = id.get()
                mysqldb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="qrcodegenerator"
                )
                mycursor = mysqldb.cursor()
                if id.get() == "":
                    messagebox.showerror("QR Code Generator & Scanner", "EmPloyee ID is required!!!")
                else:
                    try:
                        sql = "DELETE from registeredusers WHERE EmployeeID = %s"
                        val = (employeeid,)
                        mycursor.execute(sql, val)
                        mysqldb.commit()
                        messagebox.showinfo("QR Code Generator & Scanner", "User Deleted Successfully")

                    except Exception as e:
                        print(e)
                        mysqldb.rollback()
                        mysqldb.close()

            btn_deleteuser = Button(root, text='DELETE USER DETAILS', font=("Segoe UI Black", 15, 'bold'),
                                    command=delete,
                                    bg='#187bcd', fg="white")
            btn_deleteuser.place(x=5, y=200, width=250, height=50)

            listBox.bind('<Double-Button-1>', getvalue)

        btn_users = Button(root, text='REGISTERED USERS', font=("Segoe UI Black", 15, 'bold'), command=users,
                           bg='#187bcd', fg="white")
        btn_users.place(x=425, y=175, width=450, height=70)

        def adminload():
            mysqldb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qrcodegenerator"
            )
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT ProductCode,Company,Product,ExpiryDate,Price FROM qrdetails")
            records = mycursor.fetchall()
            print(records)

            cols = ('Product Code', 'Company', 'Product', 'Date Of Expiry', 'Price')
            listBox = ttk.Treeview(columns=cols, show='headings')

            for col in cols:
                listBox.heading(col, text=col)
                listBox.grid(row=1, column=0, columnspan=1)
                listBox.place(x=50, y=320)

            for i, (ProductCode, Company, Product, ExpiryDate, Price) in enumerate(records, start=1):
                listBox.insert("", "end", values=(ProductCode, Company, Product, ExpiryDate, Price))
                mysqldb.close()

        def admin():
            print("Registered Users")
            adminqrframe = Frame()
            adminqrframe.place(x=0, y=0, width=1280, height=720)
            adminqrframe.config(bg='#000000')
            adminload()

            global img
            path = "D:\\QRCode\pycharm\\regid8.png"
            img = ImageTk.PhotoImage(Image.open(path))
            panel = Label(adminqrframe, image=img)
            panel.place(x=5, y=5, height=680)

            def editqr():
                if code.get() == "" or company.get() == "" or product.get() == "" or expiry.get() == "" or price.get() == "":
                    messagebox.showerror("QR Code Generator & Scanner", "All Fields Are Required!!!")
                else:
                    procode = code.get()
                    Company = company.get()
                    Product = product.get()
                    Expiry = expiry.get()
                    Price = price.get()
                    mysqldb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="qrcodegenerator"
                    )
                    mycursor = mysqldb.cursor()
                    try:
                        sql = "UPDATE qrdetails set Company = %s, Product = %s, ExpiryDate = %s, Price = %s WHERE ProductCode = %s"
                        val = (Company, Product, Expiry, Price, procode)
                        mycursor.execute(sql, val)
                        mysqldb.commit()
                        messagebox.showinfo("QR Code Generator & Scanner", "Product Details Updated Successfully")
                        procode.delete(0, END)
                        Company.delete(0, END)
                        Product.delete(0, END)
                        Expiry.delete(0, END)
                        Price.delete(0, END)

                        procode.focus_set()
                    except Exception as e:
                        print(e)
                        mysqldb.rollback()
                        mysqldb.close()

            btn_editqr = Button(root, text='EDIT QR DETAILS', font=("Segoe UI Black", 15, 'bold'), command=editqr,
                                bg='#187bcd', fg="white")
            btn_editqr.place(x=5, y=200, width=250, height=50)

            def deleteqr():
                if code.get() == "":
                    messagebox.showerror("QR Code Generator & Scanner", "Product Code Required")
                else:
                    procode = code.get()
                    mysqldb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="qrcodegenerator"
                    )
                    mycursor = mysqldb.cursor()

                    try:
                        sql = "DELETE from qrdetails WHERE ProductCode = %s"
                        val = (procode,)
                        mycursor.execute(sql, val)
                        mysqldb.commit()
                        messagebox.showinfo("QR Code Generator & Scanner", "QR Code Details Deleted Successfully")

                    except Exception as e:
                        print(e)
                        mysqldb.rollback()
                        mysqldb.close()

            btn_deleteqr = Button(root, text='DELETE QR DETAILS', font=("Segoe UI Black", 15, 'bold'), command=deleteqr,
                                  bg='#187bcd', fg="white")
            btn_deleteqr.place(x=5, y=100, width=250, height=50)

            cols = ('Product Code', 'Company', 'Product', 'Date Of Expiry', 'Price')
            listBox = ttk.Treeview(adminqrframe, columns=cols, show='headings')

            for col in cols:
                listBox.heading(col, text=col)
                listBox.grid(row=1, column=0, columnspan=1)
                listBox.place(x=50, y=320)

            lbl = Label(root, text="PRODUCT CODE", bg='white', fg="#187bcd",
                        font=("Segoe UI Black", 22, 'bold'))
            lbl.place(x=370, y=10)

            lbl_5 = Label(root, text="NAME OF COMPANY", bg='white', fg="#187bcd",
                          font=("Segoe UI Black", 22, 'bold'))
            lbl_5.place(x=370, y=70)

            lbl_6 = Label(root, text="NAME OF PRODUCT", bg='white', fg="#187bcd",
                          font=("Segoe UI Black", 22, 'bold'))
            lbl_6.place(x=370, y=130)

            lbl_7 = Label(root, text="DATE OF EXPIRY", bg='white', fg="#187bcd",
                          font=("Segoe UI Black", 22, 'bold'))
            lbl_7.place(x=370, y=190)

            lbl_8 = Label(root, text="PRICE", bg='white', fg="#187bcd",
                          font=("Segoe UI Black", 22, 'bold'))
            lbl_8.place(x=370, y=250)

            code = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            code.place(x=720, y=10, width=320, height=50)

            company = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            company.place(x=720, y=70, width=320, height=50)

            product = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            product.place(x=720, y=130, width=320, height=50)

            expiry = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            expiry.place(x=720, y=190, width=320, height=50)

            price = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            price.place(x=720, y=250, width=320, height=50)

            btn_back = Button(root, text='BACK', command=myadmin,
                              font=("Segoe UI Black", 15, 'bold'), bg='white', fg="#187bcd")
            btn_back.place(x=2, y=2, width=150, height=40)

        btn_past = Button(root, text='GENERATED QRs', font=("Segoe UI Black", 15, 'bold'), command=admin,
                          bg='#187bcd', fg="white")
        btn_past.place(x=425, y=300, width=450, height=70)

        def admindataload():
            mysqldb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qrcodegenerator"
            )
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT ID,UserName,Password FROM admins")
            records = mycursor.fetchall()
            print(records)

            cols = ('ID', 'UserName', 'Password')
            listBox = ttk.Treeview(columns=cols, show='headings')

            for col in cols:
                listBox.heading(col, text=col)
                listBox.grid(row=1, column=0, columnspan=1)
                listBox.place(x=100, y=320)

            for i, (ID, UserName, Password) in enumerate(records, start=1):
                listBox.insert("", "end", values=(ID, UserName, Password))
                mysqldb.close()

        def adminnew():
            print("Admin Function")
            adminnewframe = Frame()
            adminnewframe.place(x=0, y=0, width=1280, height=720)
            adminnewframe.config(bg='white')
            admindataload()
            global img
            path = "D:\\QRCode\pycharm\\regid8.png"
            img = ImageTk.PhotoImage(Image.open(path))
            panel = Label(adminnewframe, image=img)
            panel.place(x=5, y=5, height=680)

            def addadmin():
                # adminid = adminID.get()
                adminname = adminusername.get()
                adminpasswd = adminpassword.get()

                if adminusername.get() == "" or adminpassword.get() == "":
                    messagebox.showerror("QR Code Generator & Scanner", "All fields are required")

                else:
                    mysqldb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="qrcodegenerator"
                    )
                    mycursor = mysqldb.cursor()
                    try:
                        sql = "INSERT INTO admins (Username,Password) VALUES (%s,%s)"
                        val = (adminname, adminpasswd)
                        mycursor.execute(sql, val)
                        mysqldb.commit()
                        messagebox.showinfo("QR Code Generator & Scanner", "Admin Added Successfully")

                        adminname.delete(0, END)
                        adminpasswd.delete(0, END)

                        adminusername.focus_set()
                    except Exception as e:
                        print(e)
                        mysqldb.rollback()
                        mysqldb.close()

            btn_addadmin = Button(root, text='ADD ADMIN', font=("Segoe UI Black", 15, 'bold'), command=addadmin,
                                  bg='#187bcd', fg="white")
            btn_addadmin.place(x=5, y=100, width=250, height=50)

            def deleteadmin():
                adminid = adminID.get()

                if adminID.get() == "":
                    messagebox.showerror("QR Code Generator & Scanner", "Admin ID is required")

                else:
                    mysqldb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="qrcodegenerator"
                    )
                    mycursor = mysqldb.cursor()
                    try:
                        sql = "DELETE from admins WHERE ID = %s"
                        val = (adminid,)
                        mycursor.execute(sql, val)
                        mysqldb.commit()
                        messagebox.showinfo("QR Code Generator & Scanner", "Admin Deleted Successfully")

                    except Exception as e:
                        print(e)
                        mysqldb.rollback()
                        mysqldb.close()

            btn_deleteadmin = Button(root, text='DELETE ADMIN', font=("Segoe UI Black", 15, 'bold'),
                                     command=deleteadmin,
                                     bg='#187bcd', fg="white")
            btn_deleteadmin.place(x=5, y=200, width=250, height=50)

            lbl_10 = Label(root, text="ADMIN ID", bg='white', fg="#187bcd",
                           font=("Segoe UI Black", 22, 'bold'))
            lbl_10.place(x=370, y=10)

            lbl_9 = Label(root, text="ADMIN USERNAME", bg='white', fg="#187bcd",
                          font=("Segoe UI Black", 22, 'bold'))
            lbl_9.place(x=370, y=90)

            lbl_9 = Label(root, text="ADMIN PASSWORD", bg='white', fg="#187bcd",
                          font=("Segoe UI Black", 22, 'bold'))
            lbl_9.place(x=370, y=170)

            adminID = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            adminID.place(x=720, y=10, width=320, height=50)

            # def temp_text8(e):
            #     adminusername.delete(0, "end")

            adminusername = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            adminusername.place(x=720, y=90, width=320, height=50)

            adminpassword = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
            adminpassword.place(x=720, y=170, width=320, height=50)

            btn_back = Button(root, text='BACK', command=myadmin,
                              font=("Segoe UI Black", 15, 'bold'), bg='white', fg="#187bcd")
            btn_back.place(x=2, y=2, width=150, height=40)

            # adminusername.bind("<FocusIn>",temp_text8())

            cols = ('ID', 'UserName', 'Password')
            listBox = ttk.Treeview(adminnewframe, columns=cols, show='headings')

            for col in cols:
                listBox.heading(col, text=col)
                listBox.grid(row=1, column=0, columnspan=1)
                listBox.place(x=100, y=320)

        btn_access = Button(root, text='ADMINS', font=("Segoe UI Black", 15, 'bold'), command=adminnew,
                            bg='#187bcd', fg="white")
        btn_access.place(x=425, y=425, width=450, height=70)

    def my_admin():
        print("Admin Function")
        adminframe = Frame()
        adminframe.place(x=0, y=0, width=1280, height=720)
        adminframe.config(bg='white')

        global img
        path = "D:\\QRCode\pycharm\\regid6.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(adminframe, image=img)
        panel.place(x=5, y=5, height=650)

        lbl_2 = Label(root, text="ADMIN LOGIN", bg='white', fg="#187bcd", font=("Segoe UI Black", 25, 'bold'))
        lbl_2.place(x=632, y=160)

        lbl_3 = Label(root, text="QR CODE GENERATOR", bg='yellow', fg="#187bcd", font=("Segoe UI Black", 25, 'bold'))
        lbl_3.place(x=590, y=450)

        lbl_4 = Label(root, text="& SCANNER", bg='yellow', fg="#187bcd", font=("Segoe UI Black", 25, 'bold'))
        lbl_4.place(x=660, y=500)

        def temp_text8(e):
            adminusername.delete(0, "end")

        adminusername = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
        adminusername.insert(0, "USERNAME")
        adminusername.place(x=625, y=240, width=260, height=50)

        def temp_text9(e):
            adminusername.delete(0, "end")

        adminpassword = Entry(root, font=("Times New Roman", 15), bg='lightyellow', show='*')
        adminpassword.insert(0, "PASSWORD")
        adminpassword.place(x=625, y=300, width=260, height=50)

        btn_back = Button(root, text='BACK', command=my_options,
                          font=("Segoe UI Black", 15, 'bold'), bg='white', fg="#187bcd")
        btn_back.place(x=2, y=2, width=150, height=40)

        adminusername.bind("<FocusIn>", temp_text8)
        adminpassword.bind("<FocusIn>", temp_text9)

        def admin():
            if adminusername.get() == "" or adminpassword.get() == "":
                messagebox.showerror("QR Code Generator & Scanner", "All Fields Are Required!!!")
            mysqldb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qrcodegenerator"
            )
            mycursor = mysqldb.cursor()
            adminname = adminusername.get()
            adminpass = adminpassword.get()

            sql = "select * from admins where Username = %s and Password = %s"
            mycursor.execute(sql, [(adminname), (adminpass)])
            results = mycursor.fetchall()
            if results:
                messagebox.showinfo("QR Code Generator & Scanner", "Logged In SuccessFully")
                myadmin()

            else:
                messagebox.showinfo("QR Code Generator & Scanner", "InCorrect UserName or Password")

        btn_admin = Button(root, text='LOGIN', command=admin,
                           font=("Segoe UI Black", 15, 'bold'), bg='#003400', fg="white").place(x=629, y=370, width=260,
                                                                                                height=50)

    btn_admin = Button(root, text='ADMIN ACCESS', font=("Segoe UI Black", 15, 'bold'), bg='#FF6200', fg="white",
                       command=my_admin).place(x=425, y=300, width=300, height=80)

    # btn_about = Button(root, text='ABOUT US', font=("Segoe UI Black", 15, 'bold'), bg='#640064', fg="white",command=about_us, ).place(x=45, y=465, width=300, height=70)

    def contact():
        contactframe = Frame()
        contactframe.place(x=0, y=0, width=1280, height=720)
        contactframe.config(bg='#42a5f5')

        global img
        path = "D:\\QRCode\pycharm\\regid14.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(contactframe, image=img)
        panel.place(x=5, y=5, height=680)

        def clear1(e):
            name.delete(0, "end")

        name = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
        name.insert(0, 'Name')
        name.place(x=37, y=350, width=235, height=45)

        def clear2(e):
            email.delete(0, "end")

        email = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
        email.insert(0, 'Email-ID')
        email.place(x=37, y=400, width=235, height=45)

        def clear3(e):
            message.delete(0, "end")

        message = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
        message.insert(0, 'Message')
        message.place(x=37, y=450, width=235, height=120)

        name.bind("<FocusIn>", clear1)
        email.bind("<FocusIn>", clear2)
        message.bind("<FocusIn>", clear3)

        lbl_15 = Label(root, text="SEND A MESSAGE", bg='#D5F3FE', fg="#00021E",
                       font=("Segoe UI Black", 20, 'bold'))
        lbl_15.place(x=37, y=300)

        lbl_16 = Label(root, text="ADDRESS", bg='#D5F3FE', fg="#00021E",
                       font=("Segoe UI Black", 15, 'bold'))
        lbl_16.place(x=37, y=20)

        lbl_17 = Label(root, text="7TH FLOOR", bg='#D5F3FE', fg="#00021E",
                       font=("Segoe UI Black", 15, 'bold'))
        lbl_17.place(x=37, y=60)

        lbl_18 = Label(root, text="KOHINOOR SQUARE,N.C.KELKAR MARG,", bg='#D5F3FE', fg="#00021E",
                       font=("Segoe UI Black", 15, 'bold'))
        lbl_18.place(x=37, y=100)

        lbl_18 = Label(root, text="SHIVAJI PARK,DADAR WEST,", bg='#D5F3FE', fg="#00021E",
                       font=("Segoe UI Black", 15, 'bold'))
        lbl_18.place(x=37, y=140)

        lbl_19 = Label(root, text="MUMBAI 400028", bg='#D5F3FE', fg="#00021E",
                       font=("Segoe UI Black", 15, 'bold'))
        lbl_19.place(x=37, y=180)

        btn_back = Button(root, text='BACK', command=my_options,
                          font=("Segoe UI Black", 15, 'bold'), bg='white', fg="#187bcd")
        btn_back.place(x=900, y=2, width=150, height=40)

        def send():
            sendername = name.get()
            senderemail = email.get()
            sendermessage = message.get()

            mysqldb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qrcodegenerator"
            )
            mycursor = mysqldb.cursor()
            if name.get() == "" or email.get() == "" or message.get() == "":
                messagebox.showerror("QR Code Generator & Scanner", "All Fields Are Required!!!")

            else:
                try:
                    sql = "INSERT INTO queries (Name,Email,Message) VALUES (%s,%s,%s)"
                    val = (sendername, senderemail, sendermessage)
                    mycursor.execute(sql, val)
                    mysqldb.commit()
                    messagebox.showinfo("Information", "Response Submitted Successfully")

                except Exception as e:
                    print(e)
                    mysqldb.rollback()
                    mysqldb.close()

                name.delete(0,tkinter.END)
                email.delete(0,tkinter.END)
                message.delete(0,tkinter.END)

        btn_send = Button(root, text='SEND', font=("Segoe UI Black", 15, 'bold'), bg='#00021E', fg="white",
                          command=send)
        btn_send.place(x=37, y=575, width=235, height=70)

    btn_contact = Button(root, text='CONTACT US', font=("Segoe UI Black", 15, 'bold'), bg='#F10066', fg="white",
                         command=contact).place(x=425, y=400, width=300, height=80)

    def reviews():
        reviewframe = Frame()
        reviewframe.place(x=0, y=0, width=1280, height=720)
        reviewframe.config(bg='#c7e0f4')

        # global img
        # path = "D:\\QRCode\pycharm\\regid18.png"
        # img = ImageTk.PhotoImage(Image.open(path))
        # panel = Label(reviewframe, image=img)
        # panel.place(x=5, y=5, height=680)

        lbl_20 = Label(root, text="Review Your Experience By Answering following Questions", bg='#c7e0f4',
                       fg="#00021E",
                       font=("Segoe UI Black", 20))
        lbl_20.place(x=50, y=45)

        lbl_21 = Label(root, text="Q)How was your experience with the system?", bg='#c7e0f4', fg="#00021E",
                       font=("Segoe UI Black", 17))
        lbl_21.place(x=30, y=110)

        lbl_22 = Label(root, text="Q)How did it helped you at supermarket?", bg='#c7e0f4', fg="#00021E",
                       font=("Segoe UI Black", 17))
        lbl_22.place(x=30, y=210)

        lbl_23 = Label(root, text="Q)How easy was it for the user to operate the system?", bg='#c7e0f4', fg="#00021E",
                       font=("Segoe UI Black", 17))
        lbl_23.place(x=30, y=310)

        lbl_24 = Label(root, text="Q)Would you recommend it to other supermarkets?", bg='#c7e0f4', fg="#00021E",
                       font=("Segoe UI Black", 17))
        lbl_24.place(x=30, y=410)

        lbl_25 = Label(root, text="Q)Suggest any recommendations that you would like to see in future?", bg='#c7e0f4', fg="#00021E",
                       font=("Segoe UI Black", 17))
        lbl_25.place(x=30, y=510)

        suggestion = Entry(root, font=("Segoe UI Black", 15), bg='lightyellow')
        suggestion.place(x=30, y=550, width=750, height=120)

        experience = StringVar()
        b1 = Radiobutton(root, text="VERY GOOD", variable=experience, value="VERY GOOD",#bg='#c7e0f4',
                         font=("Segoe UI Black", 15))
        b1.place(x=50, y=155)

        b2 = Radiobutton(root, text="GOOD", variable=experience, value="GOOD",
                         font=("Segoe UI Black", 15))
        b2.place(x=250, y=155)

        b3 = Radiobutton(root, text="AVERAGE", variable=experience, value="AVERAGE",
                         font=("Segoe UI Black", 15))
        b3.place(x=450, y=155)

        b4 = Radiobutton(root, text="CAN BE BETTER", variable=experience, value="CAN BE BETTER",
                         font=("Segoe UI Black", 15))
        b4.place(x=650, y=155)

        b5 = Radiobutton(root, text="WORST", variable=experience, value="WORST",
                         font=("Segoe UI Black", 15))
        b5.place(x=900, y=155)

        experience2 = StringVar()
        b6 = Radiobutton(root, text="VERY MUCH", variable=experience2, value="VERY MUCH",
                         font=("Segoe UI Black", 15))
        b6.place(x=50, y=255)

        b7 = Radiobutton(root, text="AVERAGE", variable=experience2, value="AVERAGE",
                         font=("Segoe UI Black", 15))
        b7.place(x=250, y=255)

        b8 = Radiobutton(root, text="DIDN'T HELPED A LOT", variable=experience2, value="DIDN'T HELPED A LOT",
                         font=("Segoe UI Black", 15))
        b8.place(x=450, y=255)

        experience3 = StringVar()
        b9 = Radiobutton(root, text="VERY EASY", variable=experience3, value="VERY EASY",
                         font=("Segoe UI Black", 15))
        b9.place(x=50, y=355)

        b10 = Radiobutton(root, text="EASY", variable=experience3, value="EASY",
                          font=("Segoe UI Black", 15))
        b10.place(x=250, y=355)

        b11 = Radiobutton(root, text="AVERAGE", variable=experience3, value="AVERAGE",
                          font=("Segoe UI Black", 15))
        b11.place(x=450, y=355)

        b12 = Radiobutton(root, text="DIFFICULT", variable=experience3, value="DIFFICULT",
                          font=("Segoe UI Black", 15))
        b12.place(x=650, y=355)

        b13 = Radiobutton(root, text="EXTREMELY DIFFICULT", variable=experience3, value="EXTREMELY DIFFICULT",
                          font=("Segoe UI Black", 15))
        b13.place(x=820, y=355)

        experience4 = StringVar()
        b14 = Radiobutton(root, text="DEFINITELY", variable=experience4, value="DEFINITELY",
                          font=("Segoe UI Black", 15))
        b14.place(x=50, y=455)

        b15 = Radiobutton(root, text="WOULD THINK", variable=experience4, value="WOULD THINK",
                          font=("Segoe UI Black", 15))
        b15.place(x=250, y=455)

        b16 = Radiobutton(root, text="WOULD NOT RECOMMEND", variable=experience4, value="WOULD NOT RECOMMEND",
                          font=("Segoe UI Black", 15))
        b16.place(x=500, y=455)

        btn_back = Button(root, text='BACK', command=my_options,
                          font=("Segoe UI Black", 15, 'bold'), bg='white', fg="#187bcd")
        btn_back.place(x=2, y=2, width=150, height=40)

        def submit():
            exp = experience.get()
            exp2 = experience2.get()
            exp3 = experience3.get()
            exp4 = experience4.get()
            sugg = suggestion.get()
            mysqldb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qrcodegenerator"
            )
            mycursor = mysqldb.cursor()
            if experience.get() == "" or experience2.get() == "" or experience3.get() == "" or experience4.get() == "" or suggestion.get() == "":
                messagebox.showerror("QR Code Generator & Scanner", "Please Answer All The Questions")
            else:
                try:
                    sql = "INSERT INTO reviews (Experience,Helped,Easiness,Recommendation,Suggestions) VALUES (%s,%s,%s,%s,%s)"
                    val = (exp, exp2, exp3, exp4, sugg)
                    mycursor.execute(sql, val)
                    mysqldb.commit()
                    messagebox.showinfo("QR Code Generator & Scanner", "Thank You for your feedback!!!")

                except Exception as e:
                    print(e)
                    mysqldb.rollback()
                    mysqldb.close()

                suggestion.delete(0,tkinter.END)

        btn_submit = Button(root, text='SUBMIT', command=submit,
                            font=("Segoe UI Black", 15, 'bold'), bg='#187bcd', fg="white")
        btn_submit.place(x=800, y=570, width=250, height=70)

    btn_contact = Button(root, text='WRITE A REVIEW', font=("Segoe UI Black", 20, 'bold'), bg='#002100', fg="white",
                         command=reviews).place(x=425, y=500, width=300, height=80)


def my_login():
    if username.get() == "" or userpassword.get() == "":
        messagebox.showerror("QR Code Generator & Scanner", "All Fields Are Required!!!")

    else:
        mysqldb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="qrcodegenerator"
        )
        mycursor = mysqldb.cursor()
        fullname = username.get()
        password = userpassword.get()

        sql = "select * from registeredusers where FullName = %s and password = %s"
        mycursor.execute(sql, [(fullname), (password)])
        results = mycursor.fetchall()
        if results:
            messagebox.showinfo("QR Code Generator & Scanner", "Logged In SuccessFully")
            my_options()
            return True

        else:
            messagebox.showinfo("QR Code Generator & Scanner", "InCorrect UserName or Password")
            return False

        username.delete(0,tkinter.END)
        userpassword.delete(0,tkinter.END)


btn_login = Button(root, text='SIGN IN', font=("Segoe UI Black", 15, 'bold'), bg='#F10066', fg="white",
                   command=my_login, ).place(x=600, y=434, width=400, height=100)


def my_register():
    print("Register function")
    registerframe = Frame()
    registerframe.place(x=0, y=0, width=1280, height=720)
    registerframe.config(bg='white')

    global img
    path = "D:\\QRCode\pycharm\\regid2.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(registerframe, image=img)
    panel.place(x=5, y=5, height=650)

    lbl_2 = Label(root, text="SIGN UP", bg='white', fg="#187bcd", font=("Segoe UI Black", 40, 'bold'))
    lbl_2.place(x=795, y=5)

    def temp_text(e):
        newuser.delete(0,"end")

    # def checkusername(name):
    #     if name.isalpha():
    #         return True
    #     else:
    #         messagebox.showerror("QR Code Generator & Scanner","Enter Valid Username")


    newuser = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
    newuser.insert(0, "CREATE USERNAME")
    newuser.place(x=700, y=120, width=360, height=50)

    # validate_name = root.register(tk.checkusername)
    # newuser.config(validate='key',validatecommand=(validate_name,'%P'))

    def temp_text2(e):
        newpassword.delete(0,"end")

    newpassword = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
    newpassword.insert(0, "CREATE PASSWORD")
    newpassword.place(x=700, y=190, width=360, height=50)

    def temp_text3(e):
        newcontact.delete(0,"end")



    newcontact = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
    newcontact.insert(0, "CONTATCT NUMBER")
    newcontact.place(x=700, y=260, width=360, height=50)


    def temp_text4(e):
        newemail.delete(0,"end")

    newemail = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
    newemail.insert(0, "EMAIL-ID")
    newemail.place(x=700, y=330, width=360, height=50)

    def temp_text5(e):
        newaddress.delete(0,"end")

    newaddress = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
    newaddress.insert(0, "ADDRESS")
    newaddress.place(x=700, y=410, width=360, height=50)

    # def temp_text6(e):
    #     newpincode.delete(0,"end")

    # newpincode = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
    # newpincode.insert(0, "PINCODE")
    # newpincode.place(x=700, y=480, width=360, height=50)

    # def temp_text6(e):
    #     newpincode.delete(0,"end")

    # def temp_text7(e):
    #      newverify.delete(0,"end")

    # newverify = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
    # newverify.insert(0, "ENTER AADHAR/PAN CARD NUMBER")
    # newverify.place(x=700, y=550, width=360, height=50)

    lbl_2 = Label(root, text="QR Code Generator & Scanner", bg='#BEBEBE', fg="black",
                  font=("Segoe UI Black", 18, 'bold'))
    lbl_2.place(x=440, y=645)

    newuser.bind("<FocusIn>", temp_text)
    newpassword.bind("<FocusIn>", temp_text2)
    newcontact.bind("<FocusIn>", temp_text3)
    newemail.bind("<FocusIn>", temp_text4)
    newaddress.bind("<FocusIn>", temp_text5)
    # newpincode.bind("<FocusIn>", temp_text6)
    # newverify.bind("<FocusIn>", temp_text7)

    # def checkname(name):
    #     if name.isalpha():
    #         return True
    #     else:
    #         messagebox.showerror("QR Code Generator & Scanner","Enter Valid Username")

    def my_connection():
        if newuser.get() == "" or newcontact.get() == "" or newaddress.get() == "" or  newpassword.get() == "" or newemail.get()=="":
            messagebox.showerror("QR Code Generator & Scanner", "All Fields Are Required!!!")


        else:
            fullname = newuser.get()
            contact = newcontact.get()
            address = newaddress.get()
            password = newpassword.get()
            # verification = newverify.get()
            email = newemail.get()
            mysqldb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qrcodegenerator"
            )
            mycursor = mysqldb.cursor()
            try:
                sql = "INSERT INTO registeredusers (EmployeeID,FullName	,Contact,Address,password,Email) VALUES (%s,%s,%s,%s,%s,%s)"
                val = ("", fullname, contact, address, password, email)
                mycursor.execute(sql, val)
                mysqldb.commit()
                messagebox.showinfo("Information", "Registered Your Account Successfully")
                my_options()

            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()

            # newuser.delete(0,tkinter.END)
            # newcontact.delete(0, tkinter.END)
            # newaddress.delete(0, tkinter.END)
            # newpincode.delete(0, tkinter.END)
            # newpassword.delete(0, tkinter.END)
            # newverify.delete(0, tkinter.END)
            # newemail.delete(0, tkinter.END)



    def check():
        otp = random.randint(100001, 900001)
        if otp:
            server_email = "qrcodegenerato@gmail.com"
            user_email = newemail.get()

            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Link"
            msg['From'] = server_email
            msg['To'] = user_email
            text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
            html = f"""
            <html>
            <head>
            </head>
            <body>
            <H1 style="color:#00c2ff;text-align:center;"> QRCODEGENERATO </H1><br><br>
            
            <H2> OTP for registration is : {otp} </H2>
            <H4 style="text-align:left;"> Thanks for Registration,<br><span style="color:#00c2ff;">QRCODEGENERATO</span> Team </H4>
            </body>
            </html>
            """
            # moneybag image == <img src="https://i.ibb.co/wSkMR8W/et-img.png" alt="et-img" style="width:100px;height:100px;">

            part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')

            msg.attach(part1)
            msg.attach(part2)

            mail = smtplib.SMTP('smtp.gmail.com', 587)

            mail.ehlo()

            mail.starttls()

            mail.login('qrcodegenereto@gmail.com', 'posenapubcqkipmx')
            mail.sendmail(server_email, user_email, msg.as_string())
            mail.quit()
            print("email sent")

            def get_otp():
                global USER_INP
                USER_INP = simpledialog.askstring(title="Test", prompt="Enter OTP sent to emialID.")
                # get_otp()
                if USER_INP == str(otp):
                    messagebox.showinfo("Message", "Email Verified Successfully")
                    my_connection()
                else:
                    messagebox.showinfo('Error', 'Wrong OTP')

            get_otp()


    btn_register = Button(root, text='REGISTER ME', command=check,
                          font=("Segoe UI Black", 15, 'bold'), bg='#F10066', fg="white").place(x=700, y=550,
                                                                                               width=375, height=70)


btn_newregister = Button(root, text='SIGN UP', command=my_register,
                         font=("Segoe UI Black", 15, 'bold'), bg='#187bcd', fg="white").place(x=710, y=34,
                                                                                              width=375, height=50)

def forgot():
    print("Forgot Password function")
    forgotframe = Frame()
    forgotframe.place(x=0, y=0, width=1280, height=720)
    forgotframe.config(bg='white')

    global img
    path = "D:\\QRCode\pycharm\\regid19.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(forgotframe, image=img)
    panel.place(x=5, y=5, height=650)

    def temp_t(e):
        phone.delete(0, "end")

    phone = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
    phone.insert(0, "ENTER YOUR USERNAME")
    phone.place(x=630, y=280, width=400, height=70)

    # def temp_te(e):
    #     registeredemail.delete(0, "end")

    registeredemail = Entry(root,font=("TImes New Roman",15),bg='lightyellow')
    registeredemail.insert(0,"ENTER YOUR REGISTERED EMAIL ID")
    registeredemail.place(x=630,y=370,width=420,height=70)

    phone.bind("<FocusIn>", temp_t)
    # registeredemail.bind("<FocusIn>", temp_te)

    def confirm():
        if phone.get() == "" or registeredemail.get() == "":
            messagebox.showerror("QR Code Generator & Scanner", "All Fields Are Required!!!")

        else:
            mysqldb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="qrcodegenerator"
            )
        mycursor = mysqldb.cursor()
        number = phone.get()
        email = registeredemail.get()

        sql = "select * from registeredusers where FullName = %s and Email = %s"
        mycursor.execute(sql, [(number), (email)])
        results = mycursor.fetchall()
        if results:
            messagebox.showinfo("QR Code Generator & Scanner", "User OTP sent successfully")


            def check():
                otp = random.randint(100001, 900001)
                if otp:
                    server_email = "qrcodegenerato@gmail.com"
                    user_email = registeredemail.get()

                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = "Link"
                    msg['From'] = server_email
                    msg['To'] = user_email
                    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
                    html = f"""
                    <html>
                    <head>
                    </head>
                    <body>
                    <H1 style="color:#FFD700;text-align:center;"> QRCODEGENERATO </H1><br><br>

                    <H2> OTP for registration is : {otp} </H2>
                    <H4 style="text-align:left;"> Thanks for Registration,<br><span style="color:#00c2ff;">QRCODEGENERATO</span> Team </H4>
                    </body>
                    </html>
                    """
                    # moneybag image == <img src="https://i.ibb.co/wSkMR8W/et-img.png" alt="et-img" style="width:100px;height:100px;">

                    part1 = MIMEText(text, 'plain')
                    part2 = MIMEText(html, 'html')

                    msg.attach(part1)
                    msg.attach(part2)

                    mail = smtplib.SMTP('smtp.gmail.com', 587)

                    mail.ehlo()

                    mail.starttls()

                    mail.login('qrcodegenereto@gmail.com', 'posenapubcqkipmx')
                    mail.sendmail(server_email, user_email, msg.as_string())
                    mail.quit()
                    print("email sent")

                    def get_otp():
                        global USER_INP
                        USER_INP = simpledialog.askstring(title="Test", prompt="Enter OTP sent to emialID.")
                        # get_otp()
                        if USER_INP == str(otp):
                            messagebox.showinfo("Message", "Email Verified Successfully")

                            def reset():
                                print("Forgot Password function")
                                forgotframe = Frame()
                                forgotframe.place(x=0, y=0, width=1280, height=720)
                                forgotframe.config(bg='white')

                                global img
                                path = "D:\\QRCode\pycharm\\regid19.png"
                                img = ImageTk.PhotoImage(Image.open(path))
                                panel = Label(forgotframe, image=img)
                                panel.place(x=5, y=5, height=650)

                                def tem(e):
                                    usernamecnf.delete(0, "end")

                                def tem2(e):
                                    cnfpasswd.delete(0, "end")

                                usernamecnf = Entry(root, font=("Times New Roman", 15), bg='lightyellow')
                                usernamecnf.insert(0, "ENTER USERNAME")
                                usernamecnf.place(x=630, y=280, width=400, height=70)

                                cnfpasswd = Entry(root, font=("TImes New Roman", 15), bg='lightyellow')
                                cnfpasswd.insert(0, "CONFIRM NEW PASSWORD")
                                cnfpasswd.place(x=630, y=370, width=420, height=70)

                                usernamecnf.bind("<FocusIn>", tem)
                                userpassword.bind("<FocusIn>", tem2)

                                def resetpasswd():
                                    newpassword1 = cnfpasswd.get()
                                    cnfuser = usernamecnf.get()
                                    if cnfpasswd.get()=="" or usernamecnf.get()=="":
                                        messagebox.showerror("QR Code Generator & Scanner", "All fields are required")

                                    else:
                                        mysqldb = mysql.connector.connect(
                                                host="localhost",
                                                user="root",
                                                password="",
                                                database="qrcodegenerator"
                                                )
                                        mycursor = mysqldb.cursor()

                                        try:
                                            sql = "UPDATE registeredusers set password = %s WHERE FullName = %s"
                                            val = (newpassword1,cnfuser)
                                            mycursor.execute(sql, val)
                                            mysqldb.commit()
                                            messagebox.showinfo("QR Code Generator & Scanner",
                                                                "Password Updated Successfully")
                                            usernamecnf.delete(0,tkinter.END)
                                            cnfpasswd.delete(0,tkinter.END)
                                            my_options()

                                        except Exception as e:
                                            print(e)
                                            mysqldb.rollback()
                                            mysqldb.close()


                                btn_rese = Button(root, text='RESET PASSWORD', command=resetpasswd,
                                                   font=("Segoe UI Black", 15, 'bold'), bg='#187bcd', fg="white")
                                btn_rese.place(x=600, y=540, width=395, height=50)

                            reset()
                        else:
                            messagebox.showinfo('Error', 'Wrong OTP')


                    get_otp()



            check()
            return True

        else:
            messagebox.showinfo("QR Code Generator & Scanner", "InCorrect UserName or Email ID")
            return False

    username.delete(0, tkinter.END)
    userpassword.delete(0, tkinter.END)

    btn_reset = Button(root, text='RECEIVE OTP', command=confirm,
                                     font=("Segoe UI Black", 15, 'bold'), bg='#187bcd', fg="white")
    btn_reset.place(x=630, y=480,width=405,height=50)

btn_forgot_password = Button(root, text='FORGOT PASSWORD???',command=forgot,
                         font=("Segoe UI Black", 15, 'bold'), bg='#187bcd', fg="white").place(x=600, y=540,
                                                                                              width=395, height=50)

root.resizable(False, False)
root.mainloop()
