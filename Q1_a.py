
def BruteForceSumKElement(A,k):
    a = 0
    sum=0
    for j in range(len(A)):
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                a = A[i]
                A[i] = A[i+1]
                A[i+1] = a
    for i in range(k):
        sum = A[i] + sum
    return sum
def test():
    A= [6,-6,3,2,1,2,-5,4,3,5]
    print(BruteForceSumKElement(A,3))

if __name__ == "__main__":
    test()

