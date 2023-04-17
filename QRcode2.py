
import pyqrcode
from tkinter import * 
from tkinter import filedialog
import png
from PIL import Image,ImageTk

root = Tk()

root.title('qrcode2Generation')
root.geometry('400x400')

def create_code(): 
     #file dialog 
     input_path=filedialog.asksaveasfilename(title="Save Images",
     filetyp=(("PNG File",".png"),("All Files",".")))

     if input_path:
          if input_path.endswith(".png"):
               get_code=pyqrcode.create(entry_box.get())
               get_code.png(input_path,scale=5)
          else:
               input_path=f'{input_path}.png'
               get_code=pyqrcode.create(entry_box.get())
               get_code.png(input_path,scale=5)

          global get_img 
          get_img=ImageTk.PhotoImage(Image.open(input_path))
          lbl.config(image=get_img)

          entry_box.delete(0,END)
          entry_box.insert(0,"Finished!")

def clear():
     # print('clearing')
     entry_box.delete(0,END)
     lbl.config(image='')

#creation of GUI
entry_box = Entry(root,font=('Arial',18))
entry_box.pack(pady=20)
btn1=Button(root,text='Create QR Code',command=create_code).pack()
btn2=Button(root,text='Clear',command=clear).pack(pady=10)
lbl=Label(root,text='')
lbl.pack(pady=20)

root.mainloop()