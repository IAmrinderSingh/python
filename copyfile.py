first_file,second_file=input("Enter name of file and destination of name of file ").split()
first=open(first_file,"r")
second=open(second_file,'w') 
second.write(first.read())
second.close()
second=open(second_file,'r')
print(second.read())
