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

