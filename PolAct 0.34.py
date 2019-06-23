#PolAct 0.34
#Oleg u need to upgrade it!
#Demo of GUI | have fun with code

from tkinter import * 
from tkinter import messagebox 
rq = [0x01, 0x0, 0x02, 0x03, 0x05, 0x3c] #Массив корисних елементів. #delete it and change to 1 | 2 | 3 on pady
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------


#main DEF for INPUTS | GUI for PolAct | Need Access for Selenium
def INPUTS(): #main DEF
    kq = rq
    a = (A.get())  
    b = (B.get()) 
    c = (C.get()) 
    d = (D.get()) 
    e = (E.get()) 
    f = (F.get()) 
    g = (G.get()) 
    h = (H.get()) 
    i = (I.get())
    j = (J.get())
    k = (K.get())
    l = (L.get())

    if a == "" or b == ""  or c=="" or d=="" or e == "" or f=="" or g=="" or h=="" or i=="" or j=="" or k=="" or l=="":
        messagebox.showinfo("Error", "Labels should be not empty")
    else:
        messagebox.showinfo("Success!", "Waiting for a results!")

        
#------------------------------------------------------------------------------------------------------------
#Графічне оформлення 
root = Tk()
root.title("PolAct 0.34") 
 
A = StringVar() 
B = StringVar() 
C = StringVar() 
D = StringVar()
E = StringVar() 
F = StringVar()
G = StringVar() 
H = StringVar() 
I = StringVar() 
J = StringVar()
K = StringVar() 
L = StringVar()


ZERO_label = Label(text="PERSONAL")
A_label = Label(text="1. Nazwisko(a): ") # labels
B_label = Label(text="2. Nazwisko(a) rodowe (poprzednio używane nazwisko(a)): ")
C_label = Label(text="3. Imiona: ")
D_label = Label(text="4. Data urodzenia (RRRR-MM-DD):")
#--
E_label = Label(text="5. Miejsce urodzenia:")
F_label = Label(text="6. Państwo urodzenia:")
G_label = Label(text="7. Posiadane obywatelstwo:") 
H_label = Label(text="Obywatelstwo w momencie urodzenia (jeżeli inne):")
I_label = Label(text="8. Płeć  ")
J_label = Label(text="9. Stan cywilny  ")
#--
K_label = Label(text="Miejsce urodzenia: ")
L_label = Label(text="Państwo urodzenia: ")

ZERO_label.grid(row=0, column=0, sticky="w")
A_label.grid(row=1, column=0, sticky="w") 
B_label.grid(row=2, column=0, sticky="w")
C_label.grid(row=3, column=0, sticky="w")
D_label.grid(row=4, column=0, sticky="w")
#--
E_label.grid(row=0, column=3, sticky="w")
F_label.grid(row=1, column=3, sticky="w")
G_label.grid(row=2, column=3, sticky="w") # grid for labels
H_label.grid(row=3, column=3, sticky="w")
I_label.grid(row=4, column=3, sticky="w")
J_label.grid(row=5, column=3, sticky="w")
#--
K_label.grid(row=0, column=7, sticky="w")
L_label.grid(row=1, column=7, sticky="w")

A_entry = Entry(textvariable=A, fg = "black") 
B_entry = Entry(textvariable=B, fg = "black") 
C_entry = Entry(textvariable=C, fg = "black") 
D_entry = Entry(textvariable=D, fg = "black")
#--
E_entry = Entry(textvariable=E, fg = "black")
F_entry = Entry(textvariable=F, fg = "black")
G_entry = Entry(textvariable=G, fg = "black") #entry
H_entry = Entry(textvariable=H, fg = "black") 
I_entry = Entry(textvariable=I, fg = "black") 
J_entry = Entry(textvariable=J, fg = "black")
#--
K_entry = Entry(textvariable=K, fg = "black")
L_entry = Entry(textvariable=L, fg = "black")



A_entry.grid(row=1,column=1, padx=5, pady=5)  # grid for entry
B_entry.grid(row=2,column=1, padx=5, pady=5)
C_entry.grid(row=3,column=1, padx=5, pady=5)
D_entry.grid(row=4,column=1, padx=5, pady=5)
#--
E_entry.grid(row=0,column=4, padx=5, pady=5)
F_entry.grid(row=1,column=4, padx=5, pady=5)
G_entry.grid(row=2,column=4, padx=5, pady=5)  
H_entry.grid(row=3,column=4, padx=5, pady=5)
I_entry.grid(row=4,column=4, padx=5, pady=5)
J_entry.grid(row=5,column=4, padx=5, pady=5)
#--
K_entry.grid(row=0,column=8, padx=5, pady=5)
L_entry.grid(row=1,column=8, padx=5, pady=5)


message_button = Button(text="Register",               
                        activebackground = "#000000",
                        activeforeground = "#FFFFFF",
                        command=INPUTS)

message_button.grid(row=20,column=8, padx=5, pady=5, sticky="e") 
 
root.mainloop() 
