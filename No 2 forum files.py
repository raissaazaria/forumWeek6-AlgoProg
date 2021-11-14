file =open("myVacation.txt","r") #open the text file which contain original text
myList = file.readlines() #output will turn into a list

count = 1 #start from number 1
newList=[] # add empty list 
for line in myList: #start looping
    count = count + 1 #add +1 in new line for looping
    formula = "{} {}".format(count,line) 
    newList.append(formula) #append formula to list

newListIntoStr= " ".join([str(list)for list in newList]) #transform list into string, because newFile.write doesnt accept list

newFile=open("myVacationResult.txt","w") #open new blank text file to write
newFile.write(newListIntoStr) #write the final result in newfile
file.close() 
