## Convert the infix expression A + B * C to postfix

- Start with A + B * C.
- A is an operand → add to postfix: A.
- \+ is an operator → push it onto the stack.
- B is an operand → add to postfix: A B.
- \* is an operator → it has higher precedence than +, so push it onto the stack.
- C is an operand → add to postfix: A B C.
- End of expression, pop operators from the stack to postfix:
   - Pop * → A B C *.
   - Pop + → A B C * +.

The resulting postfix expression is: A B C * +

## things to add
- [ ] Input verification -> brackets matching, integer checking etc
