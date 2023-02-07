from module1 import*

#palgad=read_file('Palgad_file.txt')
#print(palgad)

#inimised=read_file('inimised_file.txt')
#print(inimised)


while True:
    print(f'-----------------------------------------------------------------------------------------------')
    print(f'0 read from file:\n1-data addition:\n2 save to file:\n3 delete a worker\n4 max salary,\n5 min salary,\n6 iqual salary,\n7 increase_waning,\n8 name_salary,\n9 top_salary\n10 average salary')
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
    elif v=='5':
        MIN(palgad,inimised) 
    elif v=='6':
        iqual_salary(inimised,palgad)

    elif v=='7':
        palgad,inimised=increase_waning(palgad,inimised,int(input('0 rise 1 waning >>:')))
        for i in range(len(palgad)): 
            print(f'{palgad[i]}- {inimised[i]}') 
    elif v=='8':
        name_salary(palgad,inimised)
    elif v=='9':
        top_salary(palgad,inimised)
    elif v=='10': 
        average(palgad,inimised)

