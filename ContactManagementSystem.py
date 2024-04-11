from tkinter import *

from tkinter import messagebox


root = Tk()

root.title("CONTACT MANAGEMNET")

root.geometry('1200x640')

root.resizable('false','false')

root.configure(bg='saddle brown')


#Storing All Contacts in contacts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
contacts =[]

#Add Contact

def add():
    contact_display.config(state=NORMAL)

    try:
            
        Name =nameInput.get()
        Number =numberInput.get()
        Number =int(Number)
        Email =EmailInput.get()
        if Name and Number and Email:
            contact ={
                'Name':Name,
                'Number':Number,
                'Email':Email,
            }
            contacts.append(contact)
            with open('contact.txt','a') as handler:
                append =handler.write(f" {contact['Name']}           {contact['Number']}         {contact['Email']} \n ")


        display()
        
        messagebox.showinfo('','CONTACT HAS BEEN ADDED SUCCESSFULLY.......')
        nameInput.delete(0,END)
        numberInput.delete(0,END)
        EmailInput.delete(0,END)
        
    except ValueError:

        messagebox.showerror('','INSERT THE CORRECT VALUE IN THE INPUT AREA')  

    contact_display.config(state=DISABLED)

    nameInput.delete(0,END)
    numberInput.delete(0,END)
    EmailInput.delete(0,END)
    





def display():
    #Updating the text widget we first delet the old items in the widget
    contact_display.delete('1.0',END)
    
    #Looping through the contacts
    count =1
    for contact in contacts:
        contact_display.insert(END,f"{count}. {contact['Name']}           {contact['Number']}         {contact['Email']} \n ")

        count+=1




#Deleting Contact
def delete():
    contact_display.config(state=NORMAL)
    
    try:
            
        index =deleteInput.get()
        index =int(index)
        index =index -1
        if index<len(contacts) and index>=0:
            messagebox.showinfo('',' THE CONTACT HAS BEEN DELETED FORM THE LIST')
            
            contacts.pop(index)
            
            display()
        else: 
            messagebox.showerror('',"YOUR CONTACT LIST INDEX HAS'NT REACHED UP TO THE RANGE")
    except ValueError:
        messagebox.showerror('','PLEASE INSERT THE APPROPRIATE INDEX NUMBER.........')

    deleteInput.delete(0,END)









def edit():

    contact_display.config(state=NORMAL)
    try:
        index =EditInput.get()
        index =int(index)
        index = index -1

        if index<len(contacts) and index>=0:                    
            
            contact =contacts[index]

            #For chnaging the vlaue dynamically
            name_value =StringVar(value=contact["Name"])
            
            number_value =StringVar(value=contact["Number"])
         
            email_value =StringVar(value=contact["Email"])
            

            edit_window =Toplevel(root)

            edit_window.title("Edit Contact")

            edit_window.geometry('200x200')

            edit_window.resizable(False,False)

            name=Label(edit_window,text="Name:").grid(row=0,column=0)

            number=Label(edit_window,text="Number:").grid(row=1,column=0)

            email=Label(edit_window,text="Email:").grid(row=2,column=0)

            name_entry =Entry(edit_window,textvariable=name_value).grid(row=0,column=1)

            number_entry=Entry(edit_window,textvariable=number_value).grid(row=1,column=1)

            email_entry =Entry(edit_window,textvariable=email_value).grid(row=2,column=1)
            
            def save_edit():
                contact_display.config(state=NORMAL)
                contacts[index] ={
                                
                                "Name":name_value.get(),
                                  "Number":number_value.get(),
                                  "Email":email_value.get()
                                
                                  }
                
                messagebox.showinfo('','EDITED SUCCESSFULLY')
                display()
                
                edit_window.destroy()      

                
            button =Button(edit_window,text='SAVE',bg='green',command=save_edit).grid(row=4,column=1)
            
        
        else:
            messagebox.showerror('','THE CONTACT IS NOT AVAILABLE FOR THE INDEX CHOOSEN.......')
    except ValueError:
        messagebox.showerror('','INSERT AN INTEGER NUMBER BEFORE CLICKING THE EDITING BUTTON')
    contact_display.config(state=DISABLED)
    

        
        



#Title

Title =Label(root,text="CONTACT MANAGEMENT SYSTEM",font=('Calibri',30),fg='snow',bg='black')
Title.place(x=320,y=0)



#Name

name =Label(root,text="NAME:",font=('Calibri',27),fg='white',bg='saddle brown')
name.place(x=50,y=150)

#Entry
nameInput =Entry(root,bd=3,width=38,font=('Helvetica',12))
nameInput.place(x=10,y=210)



#Delete Entry
DeleteWidegt =Label(root,text="DELETE:",font=('Calibri',20),fg='white',bg='saddle brown')
DeleteWidegt.place(x=450,y=160)

#Entry
deleteInput =Entry(root,bd=3,width=7,font=('Helvetica',12))
deleteInput.place(x=450,y=210)






#Phone Number

number =Label(root,text="CONTACT NUMBER:",font=('Calibri',27),fg='white',bg='saddle brown')
number.place(x=50,y=270)


# Entry
numberInput =Entry(root,bd=3,width=38,font=('Helvetica',12))
numberInput.place(x=10,y=320)





#Edit Entry
EditWidget =Label(root,text="EDIT:",font=('Calibri',20),fg='white',bg='saddle brown')
EditWidget.place(x=450,y=270)



#Edit Entry

EditInput =Entry(root,bd=3,width=7,font=('Helvetica',12))
EditInput.place(x=450,y=320)






#Email Address

Email =Label(root,text="EMAIL ADDRESS:",font=('Calibri',27),fg='white',bg='saddle brown')
Email.place(x=50,y=380)



EmailInput =Entry(root,bd=3,width=38,font=('Helvetica',12))

EmailInput.place(x=10,y=450)


#For Hovering

def enteradd(e):
    Add.config(bg='green')


def leaveadd(e):
    Add.config(bg='saddle brown')




#Add
Add =Button(root,text="ADD",width=10,height=2,font=("Heletica",12),bg='saddle brown',fg='white',command=add)
Add.place(x=30,y=550)
Add.bind('<Enter>',enteradd)
Add.bind('<Leave>',leaveadd)







#For Hovering
def endteredit(e):
    Edit.config(bg='blue')


def leaveedit(e):
    Edit.config(bg='saddle brown')




#Edit
Edit=Button(root,text="EDIT",width=10,height=2,font=("Heletica",12),bg='saddle brown',fg='white',command=edit)
Edit.place(x=150,y=550)

Edit.bind('<Enter>',endteredit)

Edit.bind('<Leave>',leaveedit)





#For Hovering

def enterdel(e):
    Delete.config(bg='red')


def leavedel(e):
    Delete.config(bg='saddle brown')



#Delete 
Delete =Button(root,text="DELETE",width=10,height=2,font=("Heletica",12),bg='saddle brown',fg='white',command=delete)
Delete.place(x=270,y=550)
Delete.bind('<Enter>',enterdel)
Delete.bind('<Leave>',leavedel)


contact_display = Text(root,height=33,width=70,bg='black',fg='white',state=DISABLED,wrap=CHAR)
contact_display.place(x=600,y=80)















root.mainloop()







