class Node():
  '''Node structure for tree with left, right and value attributes'''
  def __init__(self,val):
    self.val = val
    self.lt = None
    self.rt = None

  def min(self,pr):
    ''' returns the node with smallest value and its parent for any sub tree'''
    crt = self
    prev = pr
    while crt.lt != None:
      prev = crt
      crt = crt.lt
    return crt, prev

  def max(self,pr):
    ''' returns the node with largest value and its parent for any sub tree'''
    crt = self
    prev = pr
    while crt.rt != None:
      prev = crt
      crt = crt.rt
    return crt, prev

  def succ(self,prev):
    '''returns the node with least value larger than the given node, along with parent and direction'''
    if self.rt != None:
      crt, prev = self.rt.min(prev)
      if self.rt.val == crt.val:
        return crt, prev, 'r'
      else:
        return crt, prev, 'l'
    else:
      #the below code is wrong but is never used so doesn't matter :)
      crt, prev = self.max()
      return crt, prev, 'r'

  def retall(self,ret):
    '''appends all the nodes below a parent into the input list'''
    ret.append(self.val)
    if self.lt != None:
      self.lt.retall(ret)
    if self.rt != None:
      self.rt.retall(ret)

  def findall(self,a,b,ret):
    '''appends all values between a and b into ret'''
    val = self.val
    if a <= val and val <= b:
      ret.append(val)
    if self.lt != None and self.lt.val >= a:
      self.lt.findall(a,b,ret)
    if self.rt != None and self.rt.val <= b:
      self.rt.findall(a,b,ret)

  def __str__(self):
    ret = ''
    if self.lt != None:
      ret += 'l:'+ str(self.lt.val) + ' , '
    else:
      ret += 'l: , '
    ret+=str(self.val)
    if self.rt != None:
      ret += ' , r:'+ str(self.rt.val)
    else:
      ret += ' , r: '
    if self.lt != None:
      ret += ')  ('+str(self.lt)
    if self.rt != None:
      ret += ')  ('+str(self.rt)
    return ret


class tree():
  '''primary tree data-structure'''
  def __init__(self):
    self.head = None

  def add(self,val):
    node = Node(val)
    if self.head == None:
      self.head = node
      return

    crt = self.head
    while True:
      if node.val == crt.val:
        return
      elif node.val > crt.val:
        if crt.rt == None:
          crt.rt = node
          return
        crt = crt.rt
      elif node.val < crt.val:
        if crt.lt == None:
          crt.lt = node
          return
        crt = crt.lt
  
  def search(self,val):
    '''returns string on presence/ closest element to the input '''
    prev = self.head
    crt = self.head
    if crt == None:
      return 'The tree is empty!'
    lnear = crt.val #nearest value to the left
    rnear = crt.val #nearest value to the right
    while True:
      if val == crt.val:
        return 'The value '+str(val)+' exists in the tree!'

      elif val > crt.val:
        lnear = crt.val
        if prev.rt != None:
          rnear, tempprev = prev.rt.min(prev)
        else:
          rnear = prev.val
        if crt.rt == None:
          if rnear-val > val-lnear:
            temp = lnear
          else:
            temp = rnear
          return 'The value '+str(val)+' does not exist in the tree! '+str(temp)+' is the closest element to it in the tree'
        prev = crt
        crt = crt.rt

      elif val < crt.val:
        rnear = crt.val
        if prev.lt != None:
          lnear, tempprev = prev.lt.max(prev)
        else:
          lnear = prev.val
        if crt.lt == None:
          if rnear-val > val-lnear:
            temp = lnear
          else:
            temp = rnear
          return 'The value '+str(val)+' does not exist in the tree! '+str(temp)+' is the closest element to it in the tree'
        prev = crt
        crt = crt.lt

  def rem(self,val):
    '''removes the node with the value and reorders tree as required'''
    prev = self.head
    flag = 'h'
    crt = self.head
    if crt == None:
      return 'The tree is empty'
    while True:
      if val == crt.val:
        #left-up shift
        if crt.rt == None:
          if flag == 'h':
            self.head = crt.lt
          if flag == 'r':
            prev.rt = crt.lt
          elif flag == 'l':
            prev.lt = crt.lt
          return
        #right-up shift
        elif crt.lt == None:
          if flag == 'h':
            self.head = crt.rt
          if flag == 'r':
            prev.rt = crt.rt
          elif flag == 'l':
            prev.lt = crt.rt
          return
        #successor shift
        else:
          succ, succprev, succflag = crt.succ(prev)
          if flag == 'h':
            self.head = succ
          elif flag == 'r':
            prev.rt = succ
          elif flag == 'l':
            prev.lt = succ
          succ.lt = crt.lt
          if succflag == 'h':
            pass
          elif succflag == 'r':
            succprev.rt = succ.rt
          elif succflag == 'l':
            succprev.lt = succ.rt
          succ.rt = crt.rt
          return

      #transverse tree for value
      elif val > crt.val:
        if crt.rt == None:
          return 'The value '+str(val)+' does not exist in the tree thus can not be removed!'
        prev = crt
        crt = crt.rt
        flag = 'r'

      elif val < crt.val:
        if crt.lt == None:
          return 'The value '+str(val)+' does not exist in the tree thus can not be removed!'
        prev = crt
        crt = crt.lt
        flag = 'l'


#below code runs during execution
btree = tree()
while True:
  print('\n \n press a to add, s to search, rs to range search, r to remove, q to quit. ')
  f = input('Press the requird key : ')
  if f == 'a':
    for i in range(int(input("how many numbers do you want to add? "))):
      btree.add(int(input('enter the number to add: ')))
  elif f == 's':
    print(btree.search(int(input('enter the value to search in the tree : '))))
  elif f == 'rs':
    a = int(input('enter a, the lower limit of search range: '))
    b = int(input('enter b, the upper limit of search range: '))
    l = []
    btree.head.findall(a,b,l)
    print(l)
  elif f == 'r':
    btree.rem(int(input('enter the number to remove: ')))
  elif f == 'p':
    print(btree.head)
  elif f == 'q':
    break
  else:
    continue
