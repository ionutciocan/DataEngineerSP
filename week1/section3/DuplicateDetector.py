def more_than1(listt):
    repeated=set()
    res=[]
    for name in listt:
        if name in repeated:
            if name not in res:
                res.append(name)
        else:
            repeated.add(name)
    return res

def print_unique(listt):
    res=[]
    for name in listt:
        if name not in res:
            res.append(name)
    return res


def print_submitted(listt,times):
    time_submitted={}
    for name in listt:
        if name not in time_submitted.keys():
            time_submitted[name]=1
        else:
            time_submitted[name]+=1
    res=list(filter(lambda x:x[1]==times,time_submitted.items()))
    return res

def find_user(listt,n):
    res=set(listt)
    if n in res:
        return True
    else:
        return False

def count_unique(listt):
    repeated={}
    for name in listt:
        if name not in repeated:
            repeated[name]=1
        else:
            repeated[name]+=1
    res=list(filter(lambda x:x[1]==1,repeated.items()))
    return res

submissions = ['alice','bob','carol','alice','dave','bob','alice','eve','carol']
print(submissions)
print(more_than1(submissions))
print(print_unique(submissions))
print(print_submitted(submissions,2))
print(print_submitted(submissions,3))
print(print_submitted(submissions,4))
print(find_user(submissions,'bob'))
print(count_unique(submissions))