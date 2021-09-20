exp=input().strip()
def minion_set(exp):
    exp_lst=list(exp)
    con_lst=[]
    vol_lst=[]
    count=0
    vowel=list("AEIOU")
    for ele in exp_lst:
       if ele not in vowel:
           for i in range(len(exp)):
               con_lst.append(exp[count:count+i+1])
           count+=1
       if ele in vowel:
            for j in range(len(exp)):
                vol_lst.append(exp[count:count+j])
            count+=1
    set_con=set(con_lst)
    set_vol=set(vol_lst)
    tup=(set_con,set_vol)
    return tup
def minion_count(exp):
    tup=minion_set(exp)
    vol=tup[0]
    con=tup[1]
    vol_set={}
    con_set={}
    count=0
    count1=0
    add_vol=0
    add_con=0
    for ele in vol:
        n=len(ele)
        for i in range(len(exp)-n+1):
            if ele==exp[i:i+n]:
                count+=1
        vol_set[ele]=count
        count=0
    for ele1 in con:
        n1=len(ele1)
        for j in range(len(exp)-n1+1):
            if ele1==exp[j:j+n1]:
                count1+=1
        con_set[ele1]=count1
        count1=0
    for k in vol:
        if k!='':
            add_vol=add_vol+vol_set[k]
    for l in con:
        if l!='':
            add_con=add_con+con_set[l]
    return add_con,add_vol
tup=minion_count(exp)
consonents=tup[1]
vowels=tup[0]
if consonents>vowels:
    print("Stuart",consonents)
else:
    print("kevin",vowels)
