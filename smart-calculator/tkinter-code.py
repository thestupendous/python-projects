import tkinter as tk

# Function to calculate the output
def calculate_output():
    # Get the input string
    input_text = string_input.get()
    # Calculate the output (here, we simply calculate the length of the input string)
    output_text = len(input_text)
    # Update the result_output field with the output
    result_output.config(state=tk.NORMAL)  # Enable the output field to change its content
    result_output.delete(1.0, tk.END)  # Clear previous content
    result_output.insert(tk.END, f"Length of input: {output_text}")  # Insert new output
    result_output.config(state=tk.DISABLED)  # Disable it again so it cannot be edited

# Create the main window
root = tk.Tk()
root.title("String Length Calculator")  # Set the window title

# Create and place the string_input (Entry widget)
string_input_label = tk.Label(root, text="Enter a string:")
string_input_label.pack(pady=5)

string_input = tk.Entry(root, width=40)
string_input.pack(pady=5)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_output)
calculate_button.pack(pady=5)

# Create and place the result_output (Text widget) for output
result_output_label = tk.Label(root, text="Result:")
result_output_label.pack(pady=5)

result_output = tk.Text(root, height=5, width=40, wrap=tk.WORD, state=tk.DISABLED)
result_output.pack(pady=5)

# Run the main event loop
root.mainloop()

# ------------------------------ main -------------------------------
from src.postfix import infix_to_postfix
from src.evaluate import evaluate_postfix

infix_string = '7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5'

read_line  = input("Enter something \n default is '7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5' \n\t: ")

if len(read_line) > 4:
    infix_string = read_line

print("postfixing this -> ",infix_string)
postfix_expr = infix_to_postfix(infix_string)

print("evaluating this -> ",postfix_expr)
result = evaluate_postfix(postfix_expr)

print("Result = ",result)

