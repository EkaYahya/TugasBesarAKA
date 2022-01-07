import time
from numpy import random

z = 0
while (z < 400):
    
    start_time = time.time()
    
    def gnomeSort( arr, n):
        index = 0
        while index < n:
            if index <= 0 :
                index = index + 1
            if arr[index] >=  arr[index - 1 ]:
                index = index + 1
            else :
                arr[index], arr[index - 1 ] = arr[index - 1 ], arr[index]
                index = index - 1
    
        return arr
            
    z = z + 50
    data = x=random.randint(100, size=(z))
    n = len (data)
    gnomeSort(data, n)
    
    print('Array tersortir :')
    print(data)
    print("Jumlah elemen : ", z)
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
   