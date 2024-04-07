from PyPDF2 import PdfReader
import tkinter as tk 
from tkinter import filedialog
from tkinter import scrolledtext

def open_file():
    # Open file dialog box to select the PDF file 
    file_path = filedialog.askopenfilename(filetypes=([("pdf files", "*.pdf")]))
    
    # Check if any file is selected or not  
    if file_path == '':
        print("No File Selected!")
    else:
        try:
            # Clear previous content from text area
            text_area.delete(1.0, tk.END)
            
            # Open the PDF file
            with open(file_path, 'rb') as file:
                # Create a PDF reader object 
                pdf_reader = PdfReader(file)
                
                # Iterate through each page and extract text
                for page in pdf_reader.pages:
                    text_area.insert(tk.END, page.extract_text())
        except Exception as e:
            print("Error Occurred While Reading The File", e)

def clear_content():
    # Clear the content of the text area
    text_area.delete(1.0, tk.END)

def save_content():
    # Save the content of the text area to a file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

def save_as_content():
    # Save the content of the text area to a file with a new name
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))


# Create GUI window
window = tk.Tk()
window.geometry("1000x900")
window.title("PDF Viewer")

# Create a frame to hold buttons at the top
button_frame = tk.Frame(window,bg="light blue")
button_frame.pack(side="top", fill="x")

# Create buttons
open_button = tk.Button(button_frame, text="Open PDF", command=open_file,
                        borderwidth=2, relief="raised", padx=10, pady=5, bd=0, bg="blue", fg="black", highlightbackground="gray", highlightcolor="gray")
open_button.pack(side="left", padx=10, pady=10)

clear_button = tk.Button(button_frame, text="Clear Content", command=clear_content,
                         borderwidth=2, relief="raised", padx=10, pady=5, bd=0, bg="blue", fg="black", highlightbackground="gray", highlightcolor="gray")
clear_button.pack(side="left", padx=10, pady=10)

save_button = tk.Button(button_frame, text="Save", command=save_content,
                        borderwidth=2, relief="raised", padx=10, pady=5, bd=0, bg="blue", fg="black", highlightbackground="gray", highlightcolor="gray")
save_button.pack(side="left", padx=10, pady=10)

save_as_button = tk.Button(button_frame, text="Save As", command=save_as_content,
                           borderwidth=2, relief="raised", padx=10, pady=5, bd=0, bg="blue", fg="black", highlightbackground="gray", highlightcolor="gray")
save_as_button.pack(side="left", padx=10, pady=10)

# Create a text area to display PDF content
text_area = scrolledtext.ScrolledText(window, width=100, height=40, wrap=tk.WORD, bg='light blue')
text_area.pack(expand=True, fill="both", padx=10, pady=10)  # Use expand and fill to make it responsive

# Run the tkinter's event loop  
window.mainloop()
