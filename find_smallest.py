import time

def time_func(func):
  t1 = time.time()
  func()
  t2 = time.time()
  print(int(t2 - t1))

a_lst = [ 1, 5, 2, 4 ]
b_lst = [ 5, 8, 4, 0 ]

@time_func
def find_smallest():
  a_l_c = a_lst[0]
  for i in a_lst:
    if i < a_l_c:
      a_l_c = i
  
  print(a_l_c) # O > 0

  b_l_c = b_lst[0]
  for i in b_lst:
    if i < b_l_c:
      b_l_c = i
  
  print(b_l_c) # O > 0

@time_func
def find_smallest_min():
  print(min(a_lst)) # O > 0
  print(min(b_lst)) # O > 0
