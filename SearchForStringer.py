def StringerBell(listInput1, listInput2,listInput3,listInput4):
    length1 = len(listInput1)
    length2 = len(listInput2)
    length3 = len(listInput3)
    length4 = len(listInput4)
    for i in range(length1):
        for j in range(length2):
            for l in range(length3):
                for h in range(length4):
                    if listInput1[i]==listInput2[j]==listInput3[l]==listInput4[h]:
                        print('the name that is placed', i+1, 'is the target', ',the name is',(list1[i]))
                    else
                        print('we need more information or the data is incorrect')
list1 = ['Adrian','Avon', 'Stringer', 'WeeBay', 'Brandon', 'Omar', 'Brodey', 'Wallace']
list2 = ['RandomNigga','Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Stringer', 'Ava', 'William']
list3 = ['Emma','Oliver','Ava','January','February','Stringer','March','April','May','June','July','August','September','October','November','December']
list4 =  ['Tom', 'Snappy', 'Kitty','Stringer', 'Jessie', 'Chester','Catherine','Gingerbread Man','Andrew Parson']
list5 = ['test','one']
StringerBell(list1,list2,list3,list4)
