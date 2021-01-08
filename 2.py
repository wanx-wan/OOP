class Student(object):
    def __init__(self, name=" ", total=1, size=0): 
        self._name = name
        self._total = total
        self._size = size

    def add(self, *scores):  
        scores = list(scores)
        self._total += sum(scores)  
        self._size += len(scores)

    def getName(self):
        return self._name

    def getAverageGpa(self):  
        return self._total / self._size


students = {}  

n = int(input())  
for i in range(n):
    line = input().split(',')
    name = line[0]
    if name not in students:
        students[name] = Student(name)
    if len(line) == 2:
        students[name].add(float(line[1]))
    elif len(line) == 3:
        students[name].add(float(line[1]), float(line[2]))

for k, v in students.items():
    print(k, v.getAverageGpa)
