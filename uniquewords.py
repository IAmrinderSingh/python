from collections import Counter
textfile=input("Enter name of file: ")
f=open(textfile,'r')
words=f.read().split()
uniquewords=Counter(words)
for word,count in uniquewords.items():
    if count==1:
        print(word)