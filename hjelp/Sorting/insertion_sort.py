
def insertionSort(list):
    c = 0
    s = 0
    for i in range(1,len(list)):
        temp=list[i]
        j=i-1
        while temp<+list[j] and j>=0:
            list[j+1]=list[j]
            j=j-1
            s += 1
            c += 1
        list[j+1]=temp
        c += 1

    print ('Swap: ' + str(s))
    print ('Comp: ' + str(c))
    print(list)
    return list

insertionSort([6, 5, 4, 3, 2, 1])
