class a():
    def __init__(self):
        self.name = ''
        self.age = -10
        pass
    # def __init__(self,name1):
    #     self.name = name1
    #     self.age=98;
    def set_data(self,name1,age1):
        self.name = name1
        self.age = age1;
    def get_data(self):
        return print(self.name,self.age)

record1 = a()
record2 = a()

record1.set_data('nabso',31)
record2.set_data('tion',21)

# record1.set_data('nabso',31,2)
# record2.set_data('tion',21,5)

record1.get_data()
record2.get_data()
