def verify(heap,n):
  '''This function verifies the min heap property at the node n of the heap stored as an array'''
  l = len(heap) - 1
  if l == 2*n + 1:
    if heap[n] > heap[2*n + 1]:
      temp = heap[n]
      heap[n] = heap[2*n + 1]
      heap[2*n + 1] = temp
      verify(heap,2*n + 1)
      return

  if l > 2*n + 1:
    if heap[n] > heap[2*n + 1] and heap[2*n + 1] <= heap[2*n + 2]:
      temp = heap[n]
      heap[n] = heap[2*n + 1]
      heap[2*n + 1] = temp
      verify(heap,2*n + 1)
      return

    if heap[n] > heap[2*n + 2] and heap[2*n + 1] >= heap[2*n + 2]:
      temp = heap[n]
      heap[n] = heap[2*n + 2]
      heap[2*n + 2] = temp
      verify(heap,2*n + 2)
      return

def heap(heap):
  '''converts an array into min-heap'''
  for i in range(len(heap)-1,-1,-1):
    verify(heap,i)

def retmin(heap):
  '''returns the top element and rechecks heap property'''
  ret = heap[0]
  heap[0] = heap[len(heap)-1]
  del heap[len(heap)-1]
  verify(heap,0)
  return ret

n = int(input("How many numbers do you want in your heap structure?: "))
l = list(int(input('enter number: ')) for i in range(n))
heap(l)
print(l)
for i in range(n):
  print(retmin(l))
