students = [('Alice',92),('Bob',88),('Carol',74),('Dave',55),('Eve',61),('Frank',95),('Grace',48)]
rank={1:'1st',
      2:'2nd',
      3:'3rd',
      4:'4th',
      5:'5th',
      6:'6th',
      7:'7th',}

print(sorted(students,key=lambda x:x[1],reverse=True))
print(list(filter(lambda x:x[1]>=60,students)))
sorted_data=sorted(students,key=lambda x:x[1])
print('Highest=',sorted_data[-1],',','Lowest=',sorted_data[0])
total=0
nr=0
for s in students:
    total+=s[1]
    nr+=1
res=round(total/nr,1)
print('Average=',res)
sorted_data=sorted(students,key=lambda x:x[1],reverse=True)
for i in range(0,len(sorted_data)):
    name,score=sorted_data[i]
    print(rank[i+1],name,score)