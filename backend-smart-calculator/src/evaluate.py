"""
Evaluate postfix form to calculate final result
"""

from src.stack import stack

def apply(arg1,arg2,op):
    if op=='+':
        return arg1+arg2
    elif op=='-':
        return arg1-arg2
    elif op=='*':
        return arg1*arg2
    elif op=='/':
        return arg1/arg2

def evaluate_postfix(ii):
    st = stack()

    for i in ii:
        if i.isnumeric():
            st.push_(int(i))
        elif i.isascii():
            num2 = st.pop_()
            num1 = st.pop_()
            result = apply(num1,num2,i)
            st.push_(result)

    return st.top_()

if __name__ == '__main__':

    # testing
    postf = ['7', '2', '-', '3', '2', '*',
             '3', '/', '+', '1', '10', '/', '-', '5', '+']

    result = evaluate_postfix(postf)

    print(result)
