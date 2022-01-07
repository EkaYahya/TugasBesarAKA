import time
from numpy import random

z = 0
while (z < 500):
    
    start_time = time.time()

    def insertionSort(array):

        for step in range(1, len(array)):
            key = array[step]
            j = step - 1
        
      
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
        
            array[j + 1] = key
            
    z = z + 50
    data = x=random.randint(100, size=(z))
    insertionSort(data)
    print('Array tersortir :')
    print(data)
    print("Jumlah elemen : ", z)
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
   