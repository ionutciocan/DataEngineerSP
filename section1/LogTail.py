logs = [
 'auth: User alice logged in',
 'db: Query executed in 12ms',
 'auth: ERROR invalid token for user bob',
 'api: GET /orders 200 OK',
 'db: ERROR connection timeout',
 'api: POST /checkout 201 Created',
 'auth: User carol logged in',
 'api: GET /products 200 OK',
]

for i in range(len(logs)-5,len(logs)):
    print(logs[i])
print(' ')
print(' ')
print(' ')
for i in range(0,len(logs)-5):
    print(logs[i])
print(' ')
print(' ')
print(' ')
logs=logs[::-1]
for l in logs:
    print(l)
print(' ')
print(' ')
print(' ')
newlogs=[]
for l in logs:
    if "ERROR" in l:
        newlogs.append(l)
for n in newlogs:
   print(n)
print(' ')
print(' ')
print(' ')
counts={}
for l in logs:
    word=l.split(':')[0]
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1

print(counts)