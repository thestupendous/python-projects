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

if __name__ == "__main__":
  # natural language processing - XD
  # aa = input() # say 2 + 3 * 5 - 3
  
  # testing
  st = stack()
  st.push_(3)
  st.push_("a")
  st.push_(3.93)
  st.print_()
  st.push_(-24)
  st.push_("ifodsf o odfsdoif odsf")
  st.print_()
  st.pop_()
  st.print_()
  st.pop_()
  st.print_()
  popped=st.pop_()
  print("popped is ",popped)
  
  print("stack.print_(): ",end='')
  st.print_()
  print("stack.size(): ",st.size_())
  print("stack.top_(): ",st.top_())

  while not st.empty_():
      print("popped ",st.pop_())
      st.print_()

