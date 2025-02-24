"""
  Convert infix to postfix notation
"""

from stack import stack
from time import sleep

def log(a):
    print("Log: ",a)

def infix_to_postfix(ii):
    priority = { '+':1, '-':1 ,'/':2 ,'*':2 }
    ii = list(ii.split())
    log(len(ii))
    log(ii)

    st = stack()
    oo = []

    for i in ii:
        if i.isnumeric():
            oo.append(i)
            log(i+" is Number")
        elif i.isascii():
            log(i+" is Operator")
            if st.empty_():
                st.push_(i)
            elif priority[i] <= priority[st.top_()]:
                while not st.empty_() :
                    if priority[i] <= priority[st.top_()]:
                        # if not st.empty_
                        print("Popping ",st.top_())
                        op = st.pop_()
                        oo.append(op)
                        sleep(0.5)
                    else:
                        break
                st.push_(i)

            else:       #priority[i]>priority[stack's top]
                st.push_(i)

    while not st.empty_():
        op = st.top_()
        oo.append(op)
        st.pop_()

    return oo





if __name__ == '__main__':

    ii = '7 - 2 + 3 * 2 / 3 - 1 / 10 + 5'
    print("result: ",infix_to_postfix(ii))
    print(stack.__doc__)

