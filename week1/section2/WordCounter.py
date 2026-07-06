text = 'to be or not to be that is the question whether tis nobler in the mind to suffer'
s=""
counter=dict()
for i in range(0,len(text)):
    if text[i]==' ':
        if s != "":
            if s in counter:
                counter[s]=counter.get(s, 0) + 1
            else:
                counter[s]=1
        s=""
    else:
        s+=text[i]
if s != "":
    if s in counter:
        counter[s] += 1
    else:
        counter[s] = 1
print(list(counter.items()))

sorted_dict=sorted(counter.items(),key=lambda x:x[1],reverse=True)
top3=sorted_dict[:3]
for word,count in top3:
    print(word,count)
just_once=list(filter(lambda x:x[1]==1,counter.items()))
just_once_sorted=sorted(just_once,key=lambda x:x[0])
print(just_once_sorted)
counter_appeared=[]
ok=False
for count in counter.values():
    if count in counter_appeared:
        ok=True
        break
    else:
        counter_appeared.append(count)
print(counter_appeared)
print(ok)

text = 'To be oR.. not to be .that is :the QUestion whether tis nobler in the mind to suffer'
s=""
counter2=dict()
for i in range(0,len(text)):
    if text[i]==' ':
        if s != "":
            if s in counter2:
                counter2[s]=counter2.get(s, 0) + 1
            else:
                counter2[s]=1
        s=""
    else:
        if text[i].isalnum():
            s+=text[i].lower()
if s != "":
    if s in counter2:
        counter2[s] += 1
    else:
        counter2[s] = 1
print(list(counter2.items()))