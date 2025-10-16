class stack():
    """
      stack implementation
      methods -
        push_(val)
        pop_()
        top_()
        print_()
        size_()
        empty_()
    """
    def __init__(self):
        self.data = []
        self.top = None
    def push_(self,val):
        self.data.append(val)
        self.top = val
    def pop_(self):
        # print("popping -> ",st.top_())
        if len(self.data) > 0:
            tem = self.data[-1]
            self.data.pop(-1)
            top = tem
            return tem
        else:
            return None
    def top_(self):
        return self.data[-1]
    def empty_(self):
        return len(self.data) == 0
    def print_(self):
        print(self.data)
    def size_(self):
        return len(self.data)

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

if __name__ == '__main__' :

    infix_string = '7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5'
    
    read_line  = input("Enter something \n default is '7 - 2 +  ( 3 * 2 / 3 ) -  1 / 10 + 5' \n\t: ")
    
    if len(read_line) > 4:
        infix_string = read_line
    
    print("postfixing this -> ",infix_string)
    postfix_expr = infix_to_postfix(infix_string)
    
    print("evaluating this -> ",postfix_expr)
    result = evaluate_postfix(postfix_expr)
    
    print(result)

