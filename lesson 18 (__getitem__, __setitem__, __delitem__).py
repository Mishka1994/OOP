class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        return self.marks[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Индексы должны быть неотрицательным числом')
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value


s1 = Student('Sergey', [5, 5, 3, 2, 5])
s1[10] = 4

print(s1.marks)

