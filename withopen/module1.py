


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



    #max_palk=max(p)#max salary
    #ind=p.index(max_palk) #where is the max salary
    #nimi=i[ind]# a person who stand on the position ind
    #print(f'{nimi}-l max salary {max_palk}')




    #map= tkaes all elements and change their format , can take some old mean, mean which it has and change it for different formats automatically



        

