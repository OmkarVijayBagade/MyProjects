from tkinter import *
from tkinter import messagebox
import wikipedia as wiki

root =Tk()
root.title("SearchWIKI")
root.configure(bg="brown")
root.resizable(0,0)

#functions 
def write():
     if input_field.get():
          input=input_field.get()
          result=wiki.summary(input,sentences=40)
          output_label.config(text=f'{result}',anchor=NW)
     else:
          messagebox.showerror('Something Went Wrong',
          "Check if you are connected to Internet / type the input correctly with no spelling mistakes")
     
def clear():
     if input_field.get()==str(''):
          messagebox.showerror('Nothing here',"There is nothing to clear")
     else:
          output_label.config(text='')    
          input_field.delete(0,END)

#creating elememts to be displayed in GUI app
output_label = Label(root,text='',width=50,height=25,bg='lightgrey',wraplength=350,justify='left')
input_field = Entry(root,width=58)
search_btn = Button(root,text="Search",width=22,command=write)
clear_btn = Button(root,text="Clear All", width=22,command=clear)

#packing the elements to the window of GUI app
output_label.pack(padx=5,pady=5,side=TOP)
input_field.pack(padx=5,pady=5)
search_btn.pack(padx=5,pady=2,side=RIGHT)
clear_btn.pack(padx=5,pady=5,side=LEFT)

root.mainloop()


