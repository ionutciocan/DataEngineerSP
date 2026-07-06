def print_by_dept(listt):
    dept_index={}
    for l in listt:
        if l['dept'] not in dept_index:
            dept_index[l['dept']]=[]
        dept_index[l['dept']].append(l['name'])
    return dept_index
def list_of_salary(listt):
    salary_bracket={}
    stage=''
    for l in listt:
        if l['salary']<40000:
            stage='junior'
        elif l['salary']<70000:
            stage='mid'
        else:
            stage='senior'
        if stage not in salary_bracket:
            salary_bracket[stage]=[]
        salary_bracket[stage].append(l['name'])
    return salary_bracket


def highest_salary_dept(listt):
    totals = {}
    counts = {}
    for l in listt:
        dept = l['dept']
        if dept not in totals:
            totals[dept] = 0
            counts[dept] = 0
        totals[dept] += l['salary']
        counts[dept] += 1
    max_average = -1
    best_dept = ""
    for dept in totals.keys():
        average = totals[dept] / counts[dept]

        if average > max_average:
            max_average = average
            best_dept = dept

    print(f"Highest average salary is in {best_dept}: {max_average}")

def same_manager(listt):
    managers={}
    for l in listt:
        if l['manager'] not in managers:
            managers[l['manager']]=[]
        managers[l['manager']].append(l['name'])
    for m,n in managers.items():
        if len(n)>1:
            print(f"Manager:{m}-Employees:{n}")

def lookup_by_name(listt):
    lookup={}
    for l in listt:
        lookup[l['name']]={
            'dept':l['dept'],
            'salary':l['salary'],
            'manager':l['manager']
        }
    print(lookup)
employees = [
 {'name':'Alice', 'dept':'Engineering', 'salary':85000, 'manager':'Carol'},
 {'name':'Bob', 'dept':'Marketing', 'salary':52000, 'manager':'Dave'},
 {'name':'Carol', 'dept':'Engineering', 'salary':95000, 'manager':'Eve'},
 {'name':'Dave', 'dept':'Marketing', 'salary':61000, 'manager':'Eve'},
 {'name':'Frank', 'dept':'Engineering', 'salary':38000, 'manager':'Carol'},
 {'name':'Grace', 'dept':'Support', 'salary':41000, 'manager':'Dave'},
]

dept_index=print_by_dept(employees)
print(dept_index)
salary_bracket=list_of_salary(employees)
print(salary_bracket)
highest_salary_dept(employees)
same_manager(employees)
lookup_by_name(employees)