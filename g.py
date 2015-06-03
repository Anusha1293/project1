def ash():
    t=raw_input()
    u=len(t)
    f=input()
    g=[]
    for i in range(f):
        v=raw_input()
        
        n=v.split(' ')
        
        for j in range(len(n)):
            n[j]=int(n[j])

        g.append(n)
    #print g
    for i in g:
        res=yesno(t,i)
        print res
def yesno(string, arr):
    string1=string*arr[1]
    p=arr[0]
    q=arr[1]
    if(string1[p-1]<=string1[q-1]):
        return "Yes yhis is one"
    else:
        return "No"
ash()

