def KsmallestCountingSort(A,k):
    a = min(A)
    b = max(A)
    size = b - a + 1


    count = [0 for i in range(size)]
    output = [0 for i in range (len(A))]
    for i in range (len(A)):
        
        #count[A[i]- a] = count[A[i]- a] + 1
        count[A[i]-a] += 1
    print(count)
    for i in range (len(count)):
        count[i] += count[i-1]
    print(count)
    for i in reversed( range (len(A))):
        output[count[A[i]-a]-2] = A[i]
        count[A[i]- a] -= 1
    print( output)
    sum = 0
    for i in range(k):
        sum = output[i] + sum
    return sum



def test():
    A = [-1,0,0,0,0,0,0,1,2,10,6,-8,7]
    k = 2
    #print( Ksmallest(A,k))
    print(KsmallestCountingSort(A,k))

if __name__ == "__main__":
    test()



