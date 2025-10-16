"""
  Convert infix to postfix notation
"""

from stack import stack

def log(a,end_="\n"):
    print("Log: "+str(a),end=end_)

def infix_to_postfix(ii):
    priority = { '+':1, '-':1 ,'/':2 ,'*':2, '(':0 }
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
            if i == '(':
                st.push_(i)
                continue
            elif i == ')':
                while not st.empty_() :
                    if st.top_() == '(':
                        log("MIL GAYI")
                        st.pop_()
                        break
                    op = st.top_()
                    oo.append(op)
                    st.pop_()
                continue

            if st.empty_():
                st.push_(i)

            elif priority[i] <= priority[st.top_()]:
                log("At "+i+" need to pop ",end_="")
                while not st.empty_() :
                    # if st.top_() != '(' :
                    if priority[i] <= priority[st.top_()]:
                        # if not st.empty_
                        log(" Popping "+st.top_()+",",end_="")
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

    ii = '7 - 2 +  ( 3 * 2 / 3 - )  1 / 10 + 5'
    print("result: ",infix_to_postfix(ii))
    print(stack.__doc__)
