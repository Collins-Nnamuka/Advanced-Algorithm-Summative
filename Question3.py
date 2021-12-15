text = 'Plain text'
key = 3

#Creating a function that will take two arguments which are the text and the key.
def encryption(text,key):
    #Creating a variable that will be used for storing the encrypted messages.
    encrypted_message = ""
    
    #Creating a variable start to help identify where to start and end based on the key.
    start = 0
    
    #Create a loop that loops through the key and the text and adds characters to our result variable. 
    #Then start a while loop for when the start variable is less than the key
    #Then get the result of the key of all the characters, including even the gaps using the loop.

    while start < key:
        for j in range(start,len(text),key):
            encrypted_message += text[j]
        #For increasing the start variable in order to get the following indexes.
        start += 1

    # returning the answer gotten from the encryption
    return encrypted_message

encrypted = encryption(text,key)


#Creating the decryption function that takes two arguments which are the text and the key. 
def decryption(encrypted,key):
    # initializing variables needed for the program
    start = 0
    #Creating a decrypt_message string that will be used to store the encrypted messages.
    decrypt_message = ''
    
#     checking for edges cases when the length of the 
#     text is even and the key is even 
    if len(encrypted) % 2 == 0 and key % 2 == 0: 
        
        #Creating a variable "divide" and assigning it to the division of length of the word and the key.
        divide = len(encrypted)//key 
        
        # While loop where the start variable is less than the variable divide.
        while start < divide:
            #This is used through the length of the word from the start
            for i in range(start,len(encrypted),divide):
                
                #Adding characters to the decrypt_message.
                decrypt_message += encrypted[i]
            #Incrementing the start variable to get the next index.
            start+=1 
            
    #Check for edges cases when the length of the text is even and the key is odd.
    if len(encrypted) % 2 == 0 and key % 2 != 0:
        #Dividing the length of the word by the key to know which partitions to start from
        divide = len(encrypted)//key 
        
       #Creating a while loop where the start variable is less than the divide variable
        while start < divide:
            divide += 1
            # adding the characters to the result variable
            decrypt_message += encrypted[start] 
            #loop through the length of the word from the start
            for i in range(start,len(encrypted)):
                # this is used for getting the next index to add to the answer
                n_index = i + divide
                decrypt_message += encrypted[n_index]
                decrypt_message += encrypted[n_index+key]
                # breaking out of the loop
                break
                
            # This is used to reset the divide to the partition
            divide = len(encrypted)//key 
            # increment incrementing the start to start at the next index
            start+=1 
        # adding the last character of divide to the answer
        decrypt_message+= encrypted[divide]

    # used for returning decrypted_message
    return decrypt_message
# calling the function decrypted
decrypted = decryption(encrypted,key)

#printing the result output
print("The plain text is: " + text)
print("The key is: " + str(key))
print("The encrypted text is: "+ encrypted)
print("The decrypted text is: "+ decrypted)
