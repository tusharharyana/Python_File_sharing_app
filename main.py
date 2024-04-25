from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.title("Let's Share")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)

#Action for Send and Receive button
def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg = "#f4fdfe")
    window.resizable(False,False)

    # --- Select file button action ---

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir = os.getcwd(),
                                              title = 'Select Image File',
                                              filetype = (('file_type','*.txt'),('all files','*.*')))
    # --- Send file button action ---

    def sender():
        s = socket.socket()
        host = socket.gethostbyname(socket.gethostname())
        port = 8000
        s.bind((host,port))
        s.listen(1)
        print(host)
        print('waiting for any incomming connections...')
        conn,addr = s.accept()
        file = open(filename,'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully")
    

    #Icon of send window
    image_icon1 = PhotoImage(file = "Images/SEND1.png")
    window.iconphoto(False,image_icon1)

    #Send background image and buttons
    Sbackground = PhotoImage(file = "Images/sendbg.png")
    Label(window,image = Sbackground).place(x=-2,y=0)

    Mbackground = PhotoImage(file = "Images/connectings.png")
    Label(window,image = Mbackground).place(x=-2,y=180)

    #For ID to connect will shown in Mbackground image
    host = socket.gethostbyname(socket.gethostname())
    Label(window,text = f'ID: {host}',bg = 'white',font=('Helvetica', 16)).place(x=120,y=230)

    #Buttons select file and send
    Button(window,text = "+ select file",width=10,height=1,font = 'arial 14 bold',bg="#fff",fg="#000",command = select_file).place(x=180,y=80)
    Button(window,text = "SEND",width=8,height=1,font='arial 14 bold', bg='#000',fg="#fff",command=sender).place(x=320,y=80)
    

    window.mainloop()

def Receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry('450x560+500+200')
    main.configure(bg = "#f4fdfe")
    main.resizable(False,False)

    # --- Receiver button action ---

    def receiver():
        ID = SenderID.get()
        filename1 = incoming_file.get()

        s = socket.socket()
        port = 8000
        s.connect((ID,port))
        file = open(filename1,'wb')
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")
    

    #Icon of receiver window
    image_icon1 = PhotoImage(file = "Images/RECIEVEs.png")
    main.iconphoto(False,image_icon1)

    #Background image in Reciever window
    Hbackground = PhotoImage(file = "Images/background.png")
    Label(main,image=Hbackground).place(x=-2,y=0)

    #Reciever profile picture
    logo = PhotoImage(file = 'Images/myid.png')
    Label(main,image=logo,bg = "#f4fdfe").place(x=100,y=250)


    #Input Fields for reciever to enter sender ID
    Label(main,text = "Receiver",font = ('arial',20),bg = "#f4fdfe").place(x=200,y=270)
    
    Label(main,text = "Input sender ip address",font = ('arial',10,'bold'),bg="#f4fdfe").place(x=90,y=340)
    SenderID = Entry(main,width = 25,fg = "black",border = 2,bg = 'white',font = ('arial',15))
    SenderID.place(x=90,y=370)
    SenderID.focus()

    Label(main,text = "Filename for the incoming file",font = ('arial',10,'bold'),bg="#f4fdfe").place(x=90,y=400)
    incoming_file = Entry(main,width = 25,fg = "black",border = 2,bg = 'white',font = ('arial',15))
    incoming_file.place(x=90,y=430)

    #Recieve button
    button_image = PhotoImage(file = "Images/Buttons.png")
    rr = Button(main,image = button_image,bg = "#f4fdfe",bd = 0,command = receiver)
    rr.place(x = 90,y = 480)
    
    main.mainloop()


#icon of main window
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

#File transfer name label
Label(root,text="File Transfer",font = ('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)

#Send and recieve button with action
send_image = PhotoImage(file = "Images/SEND1.png")
send = Button(root,image = send_image,bg = "#f4fdfe",bd = 0,command = Send)
send.place(x = 50,y = 100)

receive_image = PhotoImage(file = "Images/RECIEVEs.png")
send = Button(root,image = receive_image,bg = "#f4fdfe",bd = 0,command = Receive)
send.place(x = 300,y = 100)

#Send and recieve label
Label(root,text="Send",font = ('Acumin Variable Concept',17,'bold'),bg = "#f4fdfe").place(x=58,y=180)
Label(root,text="Receive",font = ('Acumin Variable Concept',17,'bold'),bg = "#f4fdfe").place(x=294,y=180)


#Main Background Image
background = PhotoImage(file = "Images/mainbg.png")
Label(root,image = background).place(x=-2,y=260)




root.mainloop()
