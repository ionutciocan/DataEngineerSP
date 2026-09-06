def intersect_posts(listt,l1,l2):
    s1=listt[l1]
    s2=listt[l2]
    res=s1.intersection(s2)
    return res

def difference_posts(listt,l1,l2):
    s1=listt[l1]
    s2=listt[l2]
    res=s1.difference(s2)
    return res

def union_posts(listt):
    res=set()
    for k in listt.keys():
        res=res.union(listt[k])
    return res

def intersect_all(listt):
    res=union_posts(listt)
    for v in listt.values():
        res=res.intersection(v)
    return res

def atleast2(listt,tag):
    s=listt[tag]
    for k in listt.keys():
        if k != tag:
            res=s.intersection(listt[k])
            if len(res)>=2:
                print(k)


posts = {
 'A': {'python', 'tutorial', 'beginner', 'coding'},
 'B': {'python', 'advanced', 'decorators', 'coding'},
 'C': {'javascript', 'tutorial', 'beginner', 'web'},
 'D': {'python', 'tutorial', 'coding', 'tips'},
}

print(intersect_posts(posts,'A','B'))
print(difference_posts(posts,'A','B'))
print(union_posts(posts))
print(intersect_all(posts))
atleast2(posts,'C')

