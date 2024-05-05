#https://dudo.gvpt.sk/programujeme/zasobnik/stack.html
class op_stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        if len(self.values) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if not self.is_empty():
            a = self.values[:-1]
            self.values = a
            return a
        else:
            raise IndexError("Nothing in stack")

inp=input("Write your mathematical expression (or write \'enter\' to use example \"((7+6)-5*(4/3))+2\"): ")
if inp=="enter": inp="((7+6)-5*(4/3))+2"
čísla='1234567890'
znaky=['+', '-', '*', '/']

s=op_stack()
vys=[]
znakydicti={'+': 1, '-': 1, '*': 2, '/': 2}
for i in range(len(inp)):
    if inp[i] in čísla:
        vys.append(inp[i])
    elif inp[i]=='(':
        s.push('(')
    elif inp[i]==')':
        while s.values[-1]!='(':
            if s.values[-1] in znakydicti:
                vys.append(s.values[-1])
            s.pop()
        s.pop()
    elif inp[i] in znakydicti:
        temporary=['(', ')']
        if znakydicti[inp[i]]>1:
            for y in range(len(s.values[::-1])):
                if s.values[::-1][y] in temporary:
                    break
                elif znakydicti[s.values[::-1][y]]>1:
                    s.pop()
                    vys.append(s.values[::-1][y])
        else:
            for y in range(len(s.values[::-1])):
                if s.values[::-1][y] in temporary:
                    break
                elif s.values[::-1][y] in znakydicti:
                    s.pop()
                    vys.append(s.values[::-1][y])
        s.push(inp[i])
t=[i for i in s.values]
for i in range(len(t)):
    if t[i] in znakydicti:
        s.pop()
        vys.append(t[i])

operand_stack=op_stack()
for i in range(len(vys)):
     if vys[i] in čísla:
         operand_stack.push(int(vys[i]))
     if vys[i] in znaky:
        first=operand_stack.values[-1]
        operand_stack.pop()
        second=operand_stack.values[-1]
        operand_stack.pop()
        match vys[i]:
             case '+':
                v=second+first
             case '-':
                v=second-first
             case '*':
                v=second*first
             case '/':
                v=second/first
        operand_stack.push(v)

print("Result: ")
print(v)