"""
Evaluate postfix form to calculate final result
"""

from stack import stack


def log(a,end_="\n"):
    print("Log: "+str(a),end=end_)

def apply(arg1,arg2,op):
    log("Apllying "+str(arg1)+" "+op+" "+str(arg2))
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
            log("got number "+i)
            st.push_(int(i))
        elif i.isascii():
            log("got operator "+i)
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
