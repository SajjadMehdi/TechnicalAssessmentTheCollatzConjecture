#Author: Sajjad Mehdi

def printCollatzSequence(n):
#list to store the values of sequence
    c_list=list() 
    
    while (n!=1) :
        c_list.append(n) 
        #if n is even
        if (n%2==0) :
            n=n//2
        else:
          #if n is odd
            n=(3*n)+1
    c_list.append(1)  #print 1 in the end   
    l=len(c_list)

    print("Length of collatz sequence is", l)
    print("Sequence is :")
    for i in range(0,l):
      print(c_list[i])

#driver code
n = int(input("Enter the number to print collatz sequence: "))  
printCollatzSequence(n)