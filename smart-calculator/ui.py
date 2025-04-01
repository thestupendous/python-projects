from src.postfix import infix_to_postfix
from src.evaluate import evaluate_postfix
import tkinter as tk



def calculate():
    try:
        infix_string_default = '7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5'
        infix_string = input_entry.get()
        if len(infix_string) == 0 :
            infix_string = infix_string_default 

        # read_line  = input("Enter something \n default is '7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5' \n\t: ")
        
        # if len(read_line) > 4:
        #     infix_string = read_line
        
        print("postfixing this -> ",infix_string)
        postfix_expr = infix_to_postfix(infix_string)
        
        print("evaluating this -> ",postfix_expr)
        result = evaluate_postfix(postfix_expr)
        
        print("Calculated Result = ",result)
        output_field.config(text=result)

    except ValueError:
        messagebox.showerror("Invalid Input", "Input me kuch gadbad to hai")


# Create the main window
root = tk.Tk()
root.title("Simple UI")

# Create and place the input label and entry
input_label = tk.Label(root, text="Enter Line:")
input_label.pack(pady=(10, 0))

input_entry = tk.Entry(root, width=40, text='7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5')
input_entry.pack(pady=(0, 10), padx=10)

# Create and place the button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=5)

# Create and place the output label and entry
output_label = tk.Label(root, text="Uttar:")
output_label.pack(pady=(10, 0))

output_field = tk.Label(root, width=40, text="Output")
output_field.pack(pady=(0, 10), padx=10)

# Run the main event loop
root.mainloop()


