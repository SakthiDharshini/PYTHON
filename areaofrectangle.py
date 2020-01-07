class rectangle:
     def __init__(self, length, width):
        self.l = length
        self.w = width
        self.a = length*width
        

A = rectangle(5,15)
print(A.a)
