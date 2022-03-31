#defining the required classes
class unit():
  '''units of the linked class'''
  def __init__(self,val):
    self.val = val
    self.pointer = None


class linked():
  '''linked list implementation'''
  def __init__(self):
    self.head = None

  def add(self,val):
    new = unit(val)
    old = self.head
    crnt = self.head
    if crnt == None:
      self.head = new
    elif self.head.val >= val:
      new.pointer = self.head
      self.head = new
    else:
      while True:
        if crnt == None:
          old.pointer = new
          break
        if crnt.val < val:
          old = crnt
          crnt = crnt.pointer
        else:
          old.pointer = new
          new.pointer = crnt
          break
    
  def __str__(self):
    i=1
    crnt = self.head
    ret = ''
    if crnt==None:
      return
    while crnt.pointer != None:
      i+=1
      ret += crnt.val + ' < '
      crnt = crnt.pointer
    ret += crnt.val
    return ret

#defining the distance calculator
def hamd(a,b):
  if len(a) != len(b):
    return None
  else:
    ret = 0
    l = len(a)
    for i in range(l):
      if a[i]==b[i]:
        pass
      else:
        ret+=1
    return ret

#part1
n = int(input('type the number of strings you need in the list : '))
l = linked()
for i in range(n):
  l.add(input('type the string : '))
print(l)

#part2
n = int(input('type the number of strings you need in the list for spell checker : '))
l = []
for i in range(n):
  l.append(input('type the string : '))
target = input('enter the target string : ')
dist = {}
#calculate hamd and print result
for i in range(n):
  word = l[i]
  dist[hamd(target,word)] = word
minn = min(dist.keys())
if minn == 0:
  print('valid')
else:
  print(dist[minn])





