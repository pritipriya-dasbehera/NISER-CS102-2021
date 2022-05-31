class node():
    def __init__(self,roll,name):
        self.roll = roll
        self.name = name
        self.pointer = None
        
def hash(n):
    return int(n)%10

def insert(roll,name):
    new = node(roll,name)
    n = hash(roll)
    
    if htable[n] == None:
        htable[n] = new
        print('new student added')
        return
    
    crt = htable[n]
    while crt.pointer != None:
        crt = crt.pointer
        if crt.roll == roll:
            print('roll number already exists')
            return
    if crt.roll == roll:
        print('roll number already exists')
        return
    crt.pointer = new
    print('new student added')
    
def delete(roll):
    n = hash(roll)
    
    if htable[n] == None:
        print('roll number does not exist')
        return
    
    if htable[n].roll == roll:
        htable[n] = htable[n].pointer
        print('student details deleted')
        return
    
    prev = htable[n]
    crt = htable[n]
    while crt.roll != roll:
        if crt.pointer == None:
            print('roll number does not exist')
            return
        prev = crt
        crt = crt.pointer

    prev.pointer = crt.pointer
    print('student details deleted')
    
def query(roll):
    n = hash(roll)
    
    if htable[n] == None:
        print('this roll number does not exist')
        return

    crt = htable[n]
    while crt.roll != roll:
        if crt.pointer == None:
            print('this roll number does not exist')
            return
        crt = crt.pointer
    print('The name of the student is '+crt.name)
    
def total():
    n = 0
    for key in htable:
        while key != None:
            n +=1
            key = key.pointer
    return n
    
htable = [None for i in range(10)] 
while True:
    inp = input('press a to add/insert, d to delete, s for search/query, \
n for total number of students and q to quit : ')
    if inp =='a':
        insert(int(input('enter the roll number of new student : ')),input('\
enter the name of new student : '))
    elif inp =='d':
        if 0 == total():
            print('Record is empty')
        else:
            delete(int(input('enter the roll number of student to delete : ')))
    elif inp =='s':
        query(int(input('enter the roll number of student to search : ')))
    elif inp =='n':
        print('the total number of students is ' +str(total()))
    elif inp =='q':
        break
