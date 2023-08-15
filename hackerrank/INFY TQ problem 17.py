train_nos=[16453,25627,22642,22905]
train_names={16453:"Prasanti Express",25627:"Karnataka Express",22642:"Trivandrum SF Express",22905:"Okha Howrah Express"}
from_list={16453:"SBC",25627:"SBC",22642:"VSKP",22905:"ST"}
to_list={16453:"BBS",25627:"DEC",22642:"TVM",22905:"KOAA"}
running_days={16453:['Mo','We','Th'],25627:['Su','Tu'],22642:['Mo','Tu','We','Th','Fr','Sa'],22905:['We','Sa']}
sleeper_fare={16453:600,25627:1600,22642:800,22905:987}
ac_fare={16453:987,25627:2500,22642:1256,22905:2879}

def get_train_name (train_no):
    if train_no in train_nos:
        return train_names[train_no]
    else:
        return "Invalid Train Number"

def get_trains_for_day(day_of_run):
    lst = []
    if day_of_run in ['Mo','Tu','We','Th','Fr','Sa','Su']:
        for train_no in train_nos:
            if day_of_run in running_days[train_no]:
                lst.append(train_no)    
        return lst
    else:
        return "Invalid Day"
    
def get_total_fare(train_no,passenger_dict):
    m, n = passenger_dict["sleeper"], passenger_dict["ac"]
    if m<0 or n<0 or (train_no not in train_nos):
        return "-1"
    else:
        return m*sleeper_fare[train_no]+n*ac_fare[train_no]
    
n=int(input())
l=[]
for i in range(n): 
    q=input().split()
    if(q[0]=='1'):   
        l.append(get_train_name(int(q[1])))
    elif(q[0]=='2'):
        l.append(get_trains_for_day(q[1]))
    elif(q[0]=='3'):
        l.append(get_total_fare(int(q[1]),{"sleeper":int(q[2]), "ac":int(q[3])}))
for i in l:
    if(type(i)==type([])):
        print(*i)
    else:
        print(i)
