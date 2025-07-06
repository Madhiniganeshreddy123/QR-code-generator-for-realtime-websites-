import qrcode
from tkinter import *
from tkinter import messagebox
import os

# Creating the window
wn = Tk()
wn.title('DataFlair QR Code Generator')
wn.geometry('700x700')
wn.config(bg='#4B0082')  # dark violet background

# Function to generate the QR code and save it
def generateCode():
    try:
        qr = qrcode.QRCode(
            version=int(size.get()),
            box_size=10,
            border=5
        )
        qr.add_data(text.get())
        qr.make(fit=True)
        img = qr.make_image()

        file_path = os.path.join(loc.get(), f"{name.get()}.png")
        img.save(file_path)

        messagebox.showinfo("DataFlair QR Code Generator", "QR Code is saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Label for the window
headingFrame = Frame(wn, bg="azure", bd=5, relief=RAISED)
headingFrame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code with DataFlair", bg='azure', font=('Times', 20, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Input for text or URL
Frame1 = Frame(wn, bg="#4B0082")
Frame1.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.15)
label1 = Label(Frame1, text="Enter the text/URL:", bg="#4B0082", fg='white', font=('Courier', 13, 'bold'))
label1.pack(pady=5)
text = Entry(Frame1, font=('Century', 12), bd=4, relief=SUNKEN)
text.pack(fill=X, padx=10)

# Input for file location
Frame2 = Frame(wn, bg="#4B0082")
Frame2.place(relx=0.1, rely=0.31, relwidth=0.8, relheight=0.15)
label2 = Label(Frame2, text="Enter the location to save the QR Code:", bg="#4B0082", fg='white', font=('Courier', 13, 'bold'))
label2.pack(pady=5)
loc = Entry(Frame2, font=('Century', 12), bd=4, relief=SUNKEN)
loc.pack(fill=X, padx=10)

# Input for image name
Frame3 = Frame(wn, bg="#4B0082")
Frame3.place(relx=0.1, rely=0.47, relwidth=0.8, relheight=0.15)
label3 = Label(Frame3, text="Enter the name of the QR Code:", bg="#4B0082", fg='white', font=('Courier', 13, 'bold'))
label3.pack(pady=5)
name = Entry(Frame3, font=('Century', 12), bd=4, relief=SUNKEN)
name.pack(fill=X, padx=10)

# Input for QR code size
Frame4 = Frame(wn, bg="#4B0082")
Frame4.place(relx=0.1, rely=0.63, relwidth=0.8, relheight=0.15)
label4 = Label(Frame4, text="Enter the size from 1 to 40 (1 = 21x21):", bg="#4B0082", fg='white', font=('Courier', 13, 'bold'))
label4.pack(pady=5)
size = Entry(Frame4, font=('Century', 12), bd=4, relief=SUNKEN)
size.pack(fill=X, padx=10)

# Generate button
button = Button(wn, text='Generate Code', font=('Courier', 15), command=generateCode, bd=4, relief=RAISED)
button.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.07)

wn.mainloop()
