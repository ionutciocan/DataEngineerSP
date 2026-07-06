def out_of_stock(dicti):
    ofs = list(filter(lambda x: x[1]['qty'] == 0, dicti.items()))
    print(ofs)

def make_restock(rst,dicti):
    for idp,quantity in rst:
        if idp in dicti.keys():
            dicti[idp]['qty']=dicti[idp]['qty']+quantity
    print(dicti)

def calculate_value(dicti):
    suma=0
    for idp in dicti.keys():
        suma+=dicti[idp]['qty']*dicti[idp]['price']
    print(suma)
def inverted_dict(dicti):
    inv_dict={}
    for idp in dicti:
        n=dicti[idp]['name']
        inv_dict[n] = {
            'id': idp,
            'qty': dicti[idp]['qty'],
            'price': dicti[idp]['price']
        }
    print(inv_dict)
def most_expensive(dicti):
    new_list=list(filter(lambda x:x[1]['qty']>0,dicti.items()))
    expensive_list=sorted(new_list,key=lambda x:x[1]['price'],reverse=True)
    print(expensive_list[:1])
inventory = {
 'P001': {'name': 'Notebook', 'qty': 50, 'price': 3.99},
 'P002': {'name': 'Pen', 'qty': 0, 'price': 0.99},
 'P003': {'name': 'Stapler', 'qty': 12, 'price': 7.49},
 'P004': {'name': 'Tape', 'qty': 0, 'price': 1.49},
 'P005': {'name': 'Highlighter','qty': 34, 'price': 2.29},
}
restock=[('P001',3),('P002',4),('P004',3),('P005',4)]
out_of_stock(inventory)
make_restock(restock,inventory)
calculate_value(inventory)
inverted_dict(inventory)
most_expensive(inventory)