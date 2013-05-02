queen = 6
i=1

def back(path):
    global i
    if reject(path): return None 
    if issolution(path):
        print "Solucion: "+str(i)
        i+=1
        print path 
    for brother in makebrothers(path):
        if len(path)<queen:
            newpath = back(brother)
            if newpath: return newpath
    return None

def issolution(path):
    print path
    return len(path)>queen-1
     
def makebrothers(path):
    path = path +[0]
    while path[len(path)-1]<queen:
        yield path
        path[len(path)-1]= path[len(path)-1]+1
       
def reject(path):
    t = False
    for i in range(len(path)):
        for j in range(i+1,len(path)):
            if abs((path[j]-path[i])*1.0/(j-i))==1 or path[j]==path[i]: 
                return True
                
    return t
        
back([])
            
    

