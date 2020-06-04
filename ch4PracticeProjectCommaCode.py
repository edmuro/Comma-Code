#Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item.
#For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'
#Your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

def commaCode(someList):
    if someList != []:
        message = '' #Initialize string message
        for i in range(len(someList)):
            if i < len(someList)-1:
                message += someList[i]+', ' #Add a comma and a space for each list item that isn't the last
            else:
                message += 'and '+someList[i] #Add an 'and' and a space in front of the last list item
            
        print(message) #Print results
    else:
        print('Enter a non-empty list')

spam = ['apples','bananas','tofu','cats'] #Example list
commaCode(spam) #Call function
