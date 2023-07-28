from tkinter import *
import customtkinter
import qrcode
from PIL import Image
    
def generate(text):
    qr = qrcode.make(text)
    qr.save('qr.png')

    for widget in frame.winfo_children():
        widget.destroy()
    
    image_ctk = customtkinter.CTkImage(light_image=Image.open('qr.png'), size=(200, 200))
    image_label = customtkinter.CTkLabel(master=frame, image=image_ctk, text="", corner_radius=5)
    image_label.pack()

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
root.geometry('350x400')

input_label = customtkinter.CTkTextbox(master=root, border_color='red', width=200, height=40, corner_radius=5, font=("Segoe UI", 20))
input_label.place(relx=0.2, rely=0.1) 

button_label = customtkinter.CTkButton(master=root, text='Convert', command=lambda:generate(input_label.get('0.0', 'end')))
button_label.place(relx=0.3, rely=0.2)

frame = customtkinter.CTkFrame(master=root, border_width=5)
frame.place(relx=0.2, rely=0.3)

if __name__ == '__main__':
    root.mainloop()