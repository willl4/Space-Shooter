from random import randint, shuffle

"""face = ['K','K','K','K','Q','Q','Q','Q','J','J','J','J']

failures = 0
trials = 100000
for i in range(trials):
    shuffle(face)
    #print(face)
    for j in range(8):
        if face[j] + face[j+1] + face[j+2] + face[j+3] == 'KKKK':
            failures += 1
            break
        if face[j] + face[j+1] + face[j+2] + face[j+3] == 'QQQQ':
            failures += 1
            break
        if face[j] + face[j+1] + face[j+2] + face[j+3] == 'JJJJ':
            failures += 1
            break
        
print((trials-failures)/trials*100,'%')"""

"""ppl = ['T','T','T','S','S','S','S','S','S','S','S','S','S','S','S']

failures = 0
trials = 100000
for i in range(trials):
    ko=0
    shuffle(ppl)
    #print(ppl)
    if ppl[0] == 'T' or ppl[1] == 'T' or ppl[13] == 'T' or ppl[14]=='T':
        failures+=1
        #print("i failed this", failures)
        ko=1
    if ko == 0:
        for j in range(13):
            if ppl[j] + ppl[j+1] == 'TT':
                failures += 1
                #print("i failed this", failures)
                ko=2
                break
    if ko==0:
        for j in range(12):
            if ppl[j] + ppl[j+1]+ppl[j+2] == 'TST':
                failures += 1
                #print("i failed this", failures)
                break
                
        

        
print((trials-failures)/trials*100,'%')"""

sib = ['A','A','B','B','C','C','D','D','E','E']

pairs = 0
trials = 1000
for i in range(trials):
    shuffle(sib)
    #print(sib)
    for j in range(9):
        if sib[j]+sib[j+1] == 'AA':
            pairs+=1
        if sib[j]+sib[j+1] == 'BB':
            pairs+=1
        if sib[j]+sib[j+1] == 'CC':
            pairs+=1
        if sib[j]+sib[j+1] == 'DD':
            pairs+=1
        if sib[j]+sib[j+1] == 'EE':
            pairs+=1

            
print(pairs/trials)

        
