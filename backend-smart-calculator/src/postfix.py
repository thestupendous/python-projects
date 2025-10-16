"""
  Convert infix to postfix notation
"""

from src.stack import stack

def infix_to_postfix(ii):
    priority = { '(':0, '+':1, '-':1 ,'/':2 ,'*':2 }
    ii = list(ii.split())

    st = stack()
    oo = []

    for i in ii:
        if i.isnumeric():
            oo.append(i)
        elif i.isascii():
            if i == '(':
                st.push_(i)
                continue
            
            elif i == ')':
                while not st.empty_():
                    if st.top_() == '(':
                        st.pop_()
                        break
                    op = st.top_()
                    oo.append(op)
                    st.pop_()
                continue

            if st.empty_():
                st.push_(i)

            elif priority[i] <= priority[st.top_()]:
                while not st.empty_() :
                    if priority[i] <= priority[st.top_()]:
                        op = st.pop_()
                        oo.append(op)
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

    # testing
    # ii = '7 - 2 + 3 * 2 / 3 - 1 / 10 + 5'
    ii = '7 - 2 +  ( 3 * 2 / 3 - )  1 / 10 + 5'

    print("result: ",infix_to_postfix(ii))
    print(stack.__doc__)

