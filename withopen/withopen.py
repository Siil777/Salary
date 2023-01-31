from module1 import*

#palgad=read_file('Palgad_file.txt')
#print(palgad)

#inimised=read_file('inimised_file.txt')
#print(inimised)


while True:
    print(f'-----------------------------------------------------------------------------------------------')
    print(f'0 read from file:\n1-data addition:\n2 save to file:\n3 delete a worker\n4 max salary')
    v=input('>>:')
    if v=='0':
        palgad=[]
        inimised=[]# empty lists
        palgad=read_file('Palgad_file.txt')
        inimised=read_file('inimised_file.txt')
        #palgad=str_to_int(palgad)
        print(palgad)
        print(inimised)
        
    
    elif v=='1':
        palgad, inimised= elem_listisse(palgad,inimised)
        print(palgad)
        print(inimised)
    elif v=='2':
        list_to_file(palgad,'Palgad_file.txt' )
        list_to_file(inimised,'inimised_file.txt' )

    elif v=='3':
        palgad,inimised=delete(input('input name:'),palgad,inimised)
        print(palgad)
        print(inimised)
    elif v=='4':
        MAX(palgad,inimised)

