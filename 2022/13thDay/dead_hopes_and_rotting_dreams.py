import time
def Comparex(a, b):
    return a < b

if True:
    def Partition(data, order):  # assuming all data being organized, via slicing in Qsort
        n = len(data)
        d = n//2
        pivot = data[d]
        #print(f'pivot of {data} is {pivot}')
        i, j = -1, n #0, n-1
        while True: #i < j:
            i +=1
            j -= 1
            time.sleep(0.1)
            while order(data[i], pivot):
                #print(f'{data[i]} smaller than pivot, next')
                i += 1
            while order(pivot, data[j]):
                #print(f'{data[j]} larger than pivot, next')
                j -= 1
            #print(f'swap happening at the ends of {data[i:j+1]}')
            if i >= j:
                return j
            data[i], data[j] = data[j], data[i]
            """
            print(data)
            if not pivot in [data[i], data[j]]:
                i += 1
                j -= 1
            elif data[i] == data[j] and data[i] == pivot:
                i += 1  # arbitrary choice between i and j, only one moves on
            print(f'now continuing comparing {data[i:j+1]} to {pivot}')
        print(f'partitioning done. final list: {data}')
        print(f'with pivot at position {j} which is {data[j]}')
        return data, j # j+1 is bigger than pivot for sure. similarly with i-1
                """

    def Qsort(data, order):
        n = len(data)
        print(n)
        p = Partition(data, order)
        Qsort(data[:p+1], order)
        Qsort(data[p+1:], order)
        return data
        if False:
            if n == 0 or n == 1:
                print("sorted segment")
                return data
            elif n == 2:
                print("sorted segment")
                if order(data[0], data[1]):
                    return data
                else:
                    return [data[1], data[0]]
            else:
                data1, q = Partition(data, order)
                print(data1)
                return Qsort(data1[:q+1], order) + Qsort(data1[q+1:], order) # maybe q better

else:
    def Qsort(A, lo, hi, to):
        if lo >= 0 and hi >= 0 and lo < hi:
            p = Partition(A, lo, hi, to)
            Qsort(A, lo, p, to)
            Qsort(A, p+1, hi, to)
        return A

    def Partition(A, lo, hi, to):
        pivot = A[(hi + lo)//2]
        i, j =  lo-1, hi+1
        while True:
            i += 1
            while to(A[i], pivot):
                i += 1 
            j -= 1
            while to(pivot, A[j]):
                j -= 1
            if i >= j:
                return j
            A[i], A[j] = A[j], A[i]

if False:
    qs = Quick_sort(rl, 0, len(rl)-1, Compare)
    print(qs)
    print("sorted" if is_sorted(qs) else "NOT SORTED")
