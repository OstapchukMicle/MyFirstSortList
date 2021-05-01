m = [7,3,0,2,-1]
print(m)

for j in range(0,len(m)):
    temp = m[0]
    for i in range(1,len(m)-j,1):
        if temp>m[i]:
            m[i-1]=m[i]
            m[i]=temp
        else:
            temp=m[i]
        print("подход:",j+1," проход:",i," список: ",m)

    #print("подход:",j,"список:  ",m)
