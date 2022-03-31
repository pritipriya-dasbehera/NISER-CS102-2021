import copy

class node():
  '''simple nodes for stack'''
  def __init__(self,data,point=None):
    self.data = data
    self.point = point


class stack():
  '''structure with nodes pointing down'''
  def __init__(self):
    '''empty stack with None as top'''
    self.top = None

  def push(self,data):
    '''new data node pushed to top and points down'''
    new = node(data,self.top)
    self.top = new

  def pop(self):
    '''removes top element and returns it'''
    if self.top == None:
      return None
    ret = self.top.data
    self.top = self.top.point
    return ret
  
  def __str__(self):
    dupli = invert(copy.copy(self))
    '''print all in bottom to top'''
    ret = ''
    while dupli.top!=None:
      ret+=str(dupli.pop())
    return ret

def invert(inp):
  '''invert input stack and return it'''
  ret = stack()
  dupli = copy.copy(inp)
  while dupli.top != None:
    ret.push(dupli.pop())
  return ret

def binary(n):
  '''convert the input to binary and return stack'''
  bstack = stack()
  if n == 0:
    bstack.push(0)
    return invert(bstack)
  while n != 0:
    bstack.push(n%2)
    n = n//2
  return invert(bstack)

def decimal(bstack):
  '''returns the decimal value of stack of binary'''
  dupli = copy.copy(bstack)
  ret = 0
  i = 0
  while dupli.top != None:
    ret += dupli.pop() * (2**i)
    i += 1
  return ret

def add1(bstack):
  '''adds 1 to stack of binary'''
  ret = bstack
  if ret.top == None:
    ret.push(1)
    return ret
  top = ret.pop()
  if top == 0:
    ret.push(1)
    return ret
  elif top == 1:
    ret = add1(ret)
    ret.push(0) 
    return ret

inp = int(input('what number do you want to convert to binary? : '))
out = binary(inp)
print('the binary of '+str(inp)+' is : '+ str(out))
out = add1(binary(inp))
print('after adding 1 binary becomes : '+ str(out))
print('and the number in decimal becomes : ' + str(decimal(out)))
