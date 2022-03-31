class multi():
    def __init__(self,flag=True):
      self.n = 0
      self.data = {}
      if flag:
        self.build()
    
    def build(self):
      self.n = int(input("\nType the numbers of terms: "))
      for i in range(self.n):
        coeff = int(input("\nEnter coefficient of the term: "))
        self.data[(int(input('Enter power of x in the term: ')),int(input('Enter power of y in the term: ')))] = coeff
      
    def set(self,dict):
      self.data = dict

    def multiply(self,multi2):
      polydata = {}
      for (x1,y1) in self.data.keys():
        for (x2,y2) in multi2.data.keys():
          if (x1+x2,y1+y2) in polydata.keys():
            polydata[(x1+x2,y1+y2)] += self.data[(x1,y1)]*multi2.data[(x2,y2)]
          else:
            polydata[(x1+x2,y1+y2)] = self.data[(x1,y1)]*multi2.data[(x2,y2)]
      return(polydata)
    
    def __str__(self):
      ret = ''
      for (x,y) in self.data.keys():
        if x==0 and y==0:
          ret += str(self.data[(x,y)])+' + '
        elif x==0 and y!=1:
          ret += str(self.data[(x,y)])+'y^'+str(y)+' + '
        elif y==0 and x!=1:
          ret += str(self.data[(x,y)])+'x^'+str(x)+' + '
        elif x==1 and y!=1:
          ret += str(self.data[(x,y)])+'x'+'y^'+str(y)+' + '
        elif y==1 and x!=1:
          ret += str(self.data[(x,y)])+'x^'+str(x)+'y'+' + '
        elif x==1 and y==1:
          ret += str(self.data[(x,y)])+'xy'+' + '
        else:
          ret += str(self.data[(x,y)])+'x^'+str(x)+'y^'+str(y)+' + '
      ret = ret[:-3]
      return ret

class poly():
  def __init__(self,flag=True):
    self.n = 0
    self.data = {}
    if flag:
      self.build()

  def build(self):
    self.n = int(input("\nType the numbers of terms: "))
    for i in range(self.n):
      coeff = int(input("\nEnter coefficient of the term: "))
      self.data[int(input('Enter power of x in the term: '))] = coeff
  
  def multiply(self,poly2):
    polydata = {}
    for n1 in self.data.keys():
      for n2 in poly2.data.keys():
        if n1+n2 in polydata.keys():
          polydata[n1+n2] += self.data[n1]*poly2.data[n2]
        else:
          polydata[n1+n2] = self.data[n1]*poly2.data[n2]
    return(polydata)
    
  def set(self,dict):
    self.data = dict
  
  def __str__(self):
    ret = ''
    for n in self.data.keys():
      if n != 0:
        ret += str(self.data[n])+'X^'+str(n)+' + '
      elif n == 1:
        ret += str(self.data[n])+'X'+' + '
      else:
        ret += str(self.data[n])+' + '
    ret = ret[:-3]
    return ret

while True:
  inp = input('which type of multiplication do you want? multivariate(m) or univariate(u) : ')
  if inp.lower() == 'm':
    print('you have chosen multivariate(2 variable) multiplication. Please enter the polynomials next')
    p1 = multi()
    p2 = multi()
    p3 = multi(False)
    p3.set(p1.multiply(p2))
    print('The product is :')
    print(p3)
    break
  elif inp.lower() == 'u':
    print('you have chosen univariate multiplication. Please enter the polynomials next')
    p1 = poly()
    p2 = poly()
    p3 = poly(False)
    p3.set(p1.multiply(p2))
    print('The product is :')
    print(p3)
    break
  else:
    print('Please press m or u')
