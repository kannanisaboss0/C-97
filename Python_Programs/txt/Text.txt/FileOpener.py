file_name=input("File name:")
f=open(file_name,'r')
count=0
for i in f:
    try:
        e=i.split()
        count=count+len(e)
        print(e)
    except:
        print(error)    
print(count)    

