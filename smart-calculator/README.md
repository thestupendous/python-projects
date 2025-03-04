# Line Calculator
**A calculator just like python's interpreter.
You can solve expressions like these**
- `2 + 3`
- `51 * 10 - 324`
- or even this
  - `7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5`
    
## things working
- operations 4 - (+/-/÷/x)
- brackets ( `(` and `)` ) support for easy typing

## Convert the infix expression A + B * C to postfix

- Start with `A + B * C`.
- A is an operand → add to postfix: `A`.
- \+ is an operator → push it onto the stack.
- B is an operand → add to postfix: `A B`.
- \* is an operator → it has higher precedence than +, so push it onto the stack.
- C is an operand → add to postfix: `A B C`.
- End of expression, pop operators from the stack to postfix:
   - `Pop * → A B C *`.
   - `Pop + → A B C * +`.

The resulting postfix expression is: A B C * +

## things to add
 - [x] brackets support
- [ ] Input verification -> 
  - [ ] numbers checking 
     - [ ] decimal numbers
     - [ ] negative number in start
  - [ ] text without spaces (exm- 1+2, (2- 5 )\*2 )

