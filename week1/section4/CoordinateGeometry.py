import math

def find_the_closest(listt):
    min=math.hypot(listt[0][0],listt[0][1])
    min_ind=0
    for i in range(1,len(listt)):
        if math.hypot(listt[i][0],listt[i][1])<min:
            min = math.hypot(listt[i][0], listt[i][1])
            min_ind=i
    return listt[min_ind][0], listt[min_ind][1]


def lie_firstcdr(listt):
    res=[]
    for i in range(1,len(listt)):
        if listt[i][0]>0 and listt[i][1]>0:
            res.append(listt[i])
    return res

def sort_by_distance(listt):
    res=sorted(listt,key=lambda x:(x[0]**2+x[1]**2)**0.5,reverse=False)
    return res


def bounding_box(listt):
    res=sorted(listt,key=lambda x:x[0],reverse=False)
    minx=res[0][0]
    maxx=res[-1][0]
    res = sorted(listt, key=lambda x: x[1], reverse=False)
    miny = res[0][1]
    maxy = res[-1][1]
    return (minx,maxx),(miny,maxy)

def intersection(listt):
    used=[]
    res=[]
    for l in listt:
        if l in used:
            res.append(l)
        used.append(l)
    return res


points = [(3,4),(0,0),(-1,2),(5,-3),(3,4),(1,1),(-4,-4),(2,0)]

print(find_the_closest(points))
print(lie_firstcdr(points))
print(sort_by_distance(points))
print(bounding_box(points))
print(intersection(points))