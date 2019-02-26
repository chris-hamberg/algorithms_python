M = [
    ['brad', 'jen', 'sarah', 'kim', 'jill'],
    ['luke', 'sarah', 'jen', 'jill', 'kim'],
    ['john', 'kim', 'jill', 'sarah', 'jen'],
    ['bill', 'kim', 'sarah', 'jill', 'jen']
    ]

women = [
        ['sarah', 'bill', 'brad', 'john', 'luke'],
        ['kim', 'brad', 'bill', 'luke', 'john'],
        ['jill', 'luke', 'brad', 'john', 'bill'],
        ['jen', 'john', 'luke', 'brad', 'bill']
        ]

C, T, x = list(), set(), -1
while x != len(M)-1:
    for i in range(len(M)):
        
        man = M[i][0]
        
        if man not in [c[0] for c in C]:
            
            lady = M[i][1]; del M[i][1]
            
            if lady in T:

                for i in range(len(C)):
                    if C[i][1] == lady:
                        cur_match = C[i]

                for j in range(len(women)):
                    if women[j][0] == lady:
                        break
                
                for k in range(len(women[j])-1):
                    if women[j][k+1] == cur_match[0]: break
                    elif women[j][k+1] == man: break
                
                preference = women[j][k+1]
                
                del C[i]
                C.append((preference, lady))
            
            else:
                x += 1
                C.append(None)
                C[x] = (man,lady)
                T.add(lady)

print(C)
