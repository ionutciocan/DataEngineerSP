cart = [
 {'name': 'Headphones', 'price': 79.99, 'qty': 1},
 {'name': 'USB Cable', 'price': 9.99, 'qty': 3},
 {'name': 'Keyboard', 'price': 49.99, 'qty': 0},
 {'name': 'Mouse', 'price': 29.99, 'qty': 2},
 {'name': 'USB Cable', 'price': 9.99, 'qty': 2},
]
sum=0
for c in cart:
    sum+=c['price']*c['qty']
print("Suma:",sum)

for c in cart:
    if c['price']>50:
        c['price']=c['price']-c['price']/10

print(cart)

cart=list(filter(lambda x:x['qty']!=0,cart))
print(cart)

sorted_data=sorted(cart,key=lambda x:x['price']*x['qty'],reverse=True)
for s in sorted_data:
    print(s['price']*s['qty'],s)
merged={}
for c in cart:
    name=c['name']
    if name in merged:
        merged[name]['qty']+=c['qty']
    else:
        merged[name]=c.copy()
cart=list(merged.values())
print(cart)

