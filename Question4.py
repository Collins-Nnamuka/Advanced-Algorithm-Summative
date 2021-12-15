
#Creating the superDigit function that takes in two arguments which are n and k

def superDigit(n, k):
    # creating a variable that will be used to calculate the super digit
    result = 0

    #creating a value p that will be used to concatenate n*k and convert it into an integer
    p = int(n * k)

    # Here we run a while loop while p is greater than zero and total is less than 9
    while (p > 0 or result > 9):
        # if statment for when p not equal 0 add the modulo of p to the total variable, 
        #divide it by 10, and get rid of the remainder.
        if (p != 0):
            result += p % 10
            p //= 10

        #exchange the current p with the total variable we have and continue searching for the super value.	
        else:
            p, result = result, p

    # Returning the result.
    return result
    
# These are the cases

n = '9875'
k = 4
print("n => " + str(n) + ', k => ' + str(k) + ', Concatenated value => ' + str(n * k) + " Super digit => " + str(superDigit(n, k)))

n = '148'
k = 3
print("n => " + str(n) + ', k => ' + str(k) + ', Concatenated value => ' + str(n * k) + " Super digit => " + str(superDigit(n, k)))


n = '28519'
k = 6
print("n => " + str(n) + ', k => ' + str(k) + ', Concatenated value => ' + str(n * k) + " Super digit => " + str(superDigit(n, k)))
