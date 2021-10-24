from collections import Counter
import collections
def revenue(shoe_stock,shoe_demand,shoe_demand_keys):
    tot=0
    key_lst_stock=list(shoe_stock.keys())
    for key in shoe_demand_keys:
        #print(key)
        if key in key_lst_stock and shoe_stock[key]!=0:
            tot=tot+shoe_demand[key][0]
            #print(shoe_demand[key][0])
            shoe_demand[key].pop(0)
            #print(shoe_demand[key])
            val=shoe_stock[key]
            val_new=val-1
            #print(val_new)
            shoe_stock[key]=val_new
    return tot

n=int(input())
lst=list(map(int,input().split()))
no=int(input())
lst1=[];shoe_demand=collections.defaultdict(list);shoe_demand_keys=[]
for i in range(no):
    lst1=list(map(int,input().split()))
    shoe_demand[lst1[0]].append(lst1[1])
    shoe_demand_keys.append(lst1[0])
shoe_stock=Counter(lst)
#print(shoe_stock)
total=revenue(shoe_stock,shoe_demand,shoe_demand_keys)
print(total)
