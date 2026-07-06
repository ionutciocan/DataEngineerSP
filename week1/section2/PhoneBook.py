def find_number(n,dicti):
    if n not in dicti.keys():
        print("This name doesn't exist")
    else:
        print(dicti[n])
def delete_number(n,dicti):
    print(dicti)
    dicti.pop(n,None)
    print(dicti)
def sort_numbers(dicti):
    temp=sorted(dicti,key=lambda x:x[0])
    print(temp)

def same_area(dicti):
    groups={}
    for k,v in dicti.items():
        zone=v[:3]
        if zone not in groups:
            groups[zone]=[]
        groups[zone].append((k,v))
    for zone,element in groups.items():
        print(f"Zone '{zone}' contain:{element}")

phone_book={}
phone_book["Alice"]="555-0101"
phone_book["Bob"]="555-0202"
phone_book["Carol"]="555-0101"
phone_book["Dave"]="444-0303"
phone_book["Eve"]="444-0404"

for name,number in phone_book.items():
    print(name,'-',number)

find_number("Raul",phone_book)
find_number("Carol",phone_book)
delete_number("Raul",phone_book)
delete_number("Carol",phone_book)
phone_book["Aurel"]="777-0101"
sort_numbers(phone_book)
same_area(phone_book)