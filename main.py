class Stack:
    def __init__(self, size, _max=3):
        self.max = _max
        if size < 1:
            raise Exception("Пустой стек")
        if size > _max:
            raise Exception("Неправильные данные")
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        if self.size() > self.max:
            raise Exception("Стек переполнен")


    def pop(self):
        return self.items.pop()
        if self.size() < 1:
            raise Exception("Стек пустой")

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


print("Введите количество элементов в стеке")
n = int(input())
st = Stack(n)
for i in range(n):
    element = int(input())
    st.push(element)
print("Ваш стек", st.show_elements())


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parChecker('((()))'))
print(parChecker('(()'))
