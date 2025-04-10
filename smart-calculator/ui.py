# from src.postfix import infix_to_postfix
# from src.evaluate import evaluate_postfix
import tkinter as tk
from main import calculate

input_entry = None
output_field = None


def calculate_button_function():
    # log
    print(":in ui caluclate_button")
    try:
        infix_string_default = '7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5'
        infix_string = input_entry.get()
        if len(infix_string) == 0 :
            infix_string = infix_string_default 

        # read_line  = input("Enter something \n default is '7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5' \n\t: ")
        
        # if len(read_line) > 4:
        #     infix_string = read_line


        
        # print("postfixing this -> ",infix_string)
        # postfix_expr = infix_to_postfix(infix_string)
        
        # print("evaluating this -> ",postfix_expr)
        # result = evaluate_postfix(postfix_expr)
        result = calculate(infix_string)

        
        print("Calculated Result = ",result)
        output_field.config(text=result)

    except ValueError:
        messagebox.showerror("Invalid Input", "Input me kuch gadbad to hai")

def showUI():
    global input_entry, output_field  # refer to global vars

    # log
    print(":in ui showUI()")
    # Create the main window
    root = tk.Tk()
    root.title("Simple UI")
    
    # Create and place the input label and entry
    input_label = tk.Label(root, text="Enter Line:")
    input_label.pack(pady=(10, 0))
    
    default_label = tk.Label(root, text="Default: 7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5")
    default_label.pack(pady=(10, 0))
    
    input_entry = tk.Entry(root, width=40, text='7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5')
    input_entry.pack(pady=(0, 10), padx=10)
    
    # Create and place the button
    calculate_button = tk.Button(root, text="Calculate", command=calculate_button_function)
    calculate_button.pack(pady=5)
    
    # Create and place the output label and entry
    output_label = tk.Label(root, text="Uttar:")
    output_label.pack(pady=(10, 0))
    
    output_field = tk.Label(root, width=40, text="Output")
    output_field.pack(pady=(0, 10), padx=10)
    
    # Run the main event loop
    root.mainloop()
    
if __name__ == '__main__' :
    # log
    print(":in ui main")
    showUI()
    
