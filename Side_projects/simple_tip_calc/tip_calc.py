import customtkinter
from tkinter import *
from tkinter import messagebox

# Creating the window
app = customtkinter.CTk()
app.title('Tip Calculator')
app.geometry('300x300')
app.config(bg = '#000')

font1 = ('Arial', 30, 'bold')
font2 = ('Arial', 18, 'bold')
font3 = ('Arial', 25, 'bold')

variable1 = StringVar()

def calculate_tip():
    try:
        tip_percent = float(variable1.get())
        bill_amount = float(bill_entry.get())
        tip = tip_percent * bill_amount
        total_bill = tip + bill_amount
        result_labe1.configure(text = 'Tip Amount : {:.2f}'.format(tip))
        result_labe2.configure(text = 'Total Bill : {:.0f}'.format(total_bill))
    except:
        messagebox.showerror('Error', 'Enter valid value!')

# Labels, Frames, Entry boxes
title_label = customtkinter.CTkLabel(app, font = font1, text = 'Tip Calculator', text_color = '#fff', bg_color ='#000')
title_label.place(x = 25, y = 15)

frame = customtkinter.CTkFrame(app, fg_color = '#341461', bg_color = '#000', width = 250, height = 150, corner_radius = 20)
frame.place(x =25, y = 60)

bill_label = customtkinter.CTkLabel(frame, font = font2, text = 'Bill Amount', text_color = '#fff', bg_color = '#341461')
bill_label.place(x = 10, y = 10)

tip_label = customtkinter.CTkLabel(frame, font = font2, text = 'Tip %', text_color = '#fff', bg_color = '#341461')
tip_label.place(x = 10, y = 70)

bill_entry = customtkinter.CTkEntry(frame, font = font2, text_color = '#000', fg_color = '#fff', width = 100)
bill_entry.place(x = 130, y = 10)

rb1 = customtkinter.CTkRadioButton(frame, text = '15%', fg_color = '#c40629', hover_color = '#c40629', font = font2, variable = variable1, value = 0.15)
rb2 = customtkinter.CTkRadioButton(frame, text = '20%', fg_color = '#c40629', hover_color = '#c40629', font = font2, variable = variable1, value = 0.20)
rb1.place(x = 100, y = 70)
rb2.place(x = 170, y = 70)

calculate_button = customtkinter.CTkButton(app, command = calculate_tip, font = font2, text_color = '#fff', text = 'Calculator Tip', fg_color = '#341461', hover_color = '#210942', bg_color = '#000', cursor = 'hand2', corner_radius = 20, width = 250)
calculate_button.place(x = 23, y = 230)

result_labe1 = customtkinter.CTkLabel(app, text = '', font = font3, text_color = '#fff', bg_color = '#000')
result_labe1.place(x = 30, y = 280)

result_labe2 = customtkinter.CTkLabel(app, text = '', font = font3, text_color = '#fff', bg_color = '#000')
result_labe2.place(x = 30, y = 320)

app.mainloop()