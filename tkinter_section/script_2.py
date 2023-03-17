from tkinter import *

# Define a function to convert the input value to grams, pounds, and ounces
def convert():
    # Read the value from the entry box and convert it to a float
    kg = float(kg_entry.get())
    
    # Calculate the weight in grams, pounds, and ounces using conversion formulas
    grams = kg * 1000
    pounds = kg * 2.20462
    ounces = pounds * 16
    
    # Update the result labels with the converted values, formatted to two decimal places
    grams_result.config(text = f"{grams:.2f} g")
    pounds_result.config(text = f"{pounds:.2f} lbs")
    ounces_result.config(text = f"{ounces:.2f} oz")

# Create the main window and set its title
root = Tk()
root.title("Kilogram Converter")

# Create a label and an entry box for the user to enter a weight in kilograms
kg_label = Label(root, text="Enter weight in kilograms:")
kg_label.pack()
kg_entry = Entry(root)
kg_entry.pack()

# Create a button to trigger the conversion when clicked
convert_button = Button(root, text = "Convert", command = convert)
convert_button.pack()

# Create a frame to hold the result labels
result_frame = Frame(root)

# Create labels to display the converted weights in grams, pounds, and ounces
grams_result = Label(result_frame, text = "")
grams_result.pack(side = LEFT, padx = 10)
pounds_result = Label(result_frame, text = "")
pounds_result.pack(side = LEFT, padx = 10)
ounces_result = Label(result_frame, text = "")
ounces_result.pack(side = LEFT, padx = 10)

# Pack the result frame and set a padding
result_frame.pack(pady = 10)

# Start the main event loop
root.mainloop()
