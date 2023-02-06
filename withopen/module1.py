def read_file(file:str)->list:
    """
    loeme failist
    :param str file: faili nimi
    :param list mas: loetelu
    """
    fail=open(file,'r', encoding="utf-8-sig")
    mas=[]
    for row in fail:
        if row.isdigit():
             mas.append(int(row.strip()))#read each line separately
        else:
            mas.append(row.strip())
    fail.close()
    return mas

# what to add and where
def list_to_file(mas:list,file:str):
    """
    salvestame loetelu failisse
    :param str file: faili nimi
    :param list mas: loetelu
    """
    f=open(file,'w',encoding="utf-8-sig")
    for item in mas:
        f.write(item+'\n')
    f.close()


def elem_listisse(p:list,i:list):
    n=int(input('how a lot workers:'))
    for j in range(n):
        nimi=input('name:')
        i.append(nimi)
        palgad=input('salary:')
        p.append(palgad)
    return p,i


def delete(nimi:str,p:list,i:list):
    n=i.count(nimi)
    pos=0 #position to start
    print(nimi,n)
    for j in range(n): #count of repetition
        ind=i.index(nimi,pos) #find a person, what we are fainding, start = p, p:list, position where is being started count
        pos=ind #after that postion change for 1 position + 1
        i.remove(nimi)
        p.pop(ind) #salary through index
    return p,i

#def str_to_int(mas:list)->list:
#    for m in mas:
#        ind=mas.index(m)
#        m=mas.pop(ind) #where is m
#        mas.insert(m, ind)

    #return mas
def MAX(p:list,i:list):
     """ max calculates max value in the list
    :param p:list
    :param i:list
    """
    p=list(map(int,p))
    #for palk in p:
    max_palk=max(p)
    n=p.count(max_palk)
    pos=0
    print(f'max salary {max_palk}\n')
    for j in range(n):
        ind=p.index(max_palk,pos)
        nimi=i[ind]
        print(f'{nimi}')
        pos=ind+1
def MIN(p:list,i:list):
    p=list(map(int,p))
    min_palk=min(p)
    n=p.count(min_palk)
    pos=0
    print(f'min salary {min_palk}\n')
    for j in range(n):
        ind=p.index(min_palk,pos)
        nimi=i[ind]
        print(f'{nimi}')
        pos=ind+1

def iqual_salary(p:list,i:list):
     """min calculates min value in the list
    :param p:list
    :param i:list
    """
    palgad=read_file('Palgad_file.txt')
    inimised=read_file('inimised_file.txt')
    list1=[] 
    list2=[] 
    N=len(palgad) 
    for h in range(N+1):
        for j in range(h+1,N):
            if palgad[h]==palgad[j]:
                a=h
    b=palgad[a] 
    print(b) 
    for h in range(len(palgad)): 
        if b==palgad[h]: 
            list1.append(h)
    for h in range(len(list1)): 
        list2.append(inimised[list1[h]]) 
    print(f'repeat slary',b,h,'times')

def increase_waning(p:list,i:list): 
    """
    :param p:list
    :param i:list
    """
    p=list(map(int,p))
    i=list(map(str,i)) 
    print('rise')
    p.sort() 
    i.sort()
    print(p) 
    print(i)
    print('descending')
    p.sort(reverse=True) 
    i.sort(reverse=True) 
    print(p) 
    print(i)
 
    
    
       
        
       
   


def name_salary(p:list,i:list):
    """
    :param p:list
    :param i:list
    """
    p=list(map(int,p)) 
    pos=0 
    n=input('name:')
    ind=i.index(n,pos)  
    n=print(p[ind]) 
    pos=ind+1

def top_salary(p:list, i:list):
    """
    :param p:list
    :param i:list
    """
   
    p=list(map(int, p))
    l = p.copy()
    v = i.copy()

    vv = []
    vd =[]

    for j in range(0, 3):   
        y = p.index(max(p))
        v1 = l.index(min(l))
        vv.append(i[y])
        vd.append(v[v1])
        p.remove(max(p))
        l.remove(min(l))
        i.remove(i[y])
        v.remove(v[v1])
    print('top of rich workers:')
    for j in vv:
        print(j)
    print('top of poor workers:')
    for j in vd:
        print(j)
    return vv, vd

def average(p:list,i:list): 
    """
    :param p:list
    :param i:list
    """
    p=list(map(int,p)) 
    avg=sum(p)/len(p) 
    avg=int(avg)  
    if avg in p: 
        v=p.index(avg)  
        print(f'{avg} {i[v]}') 
    else: 
        print(f'average salary is {avg}')  
    return avg



    #max_palk=max(p)#max salary
    #ind=p.index(max_palk) #where is the max salary
    #nimi=i[ind]# a person who stand on the position ind
    #print(f'{nimi}-l max salary {max_palk}')




    #map= tkaes all elements and change their format , can take some old mean, mean which it has and change it for different formats automatically



        

