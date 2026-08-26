employees={}
departments={"IT","HR","Finance","Admin"}
working_days=[
    "MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY"
]
while True:
    print("1.Add Employee")
    print("2.Display All employees")
    print("3.Search Employee")
    print("4.Mark Attendence")
    print("5.Department Report")
    print("6.Delete Employee")
    print("7.Exit")
    op=input("Enter Option:")
    if op=="1":
        emp_id=input("Enter Emplpoyee Id:")
        if emp_id in employees:
            print("Employee ID already exit")
            break
        emp_name=input("Enter Employee Name:")
        emp_age=int(input("Enter Employee Age:"))
        salary=float(input("Enter Employee Salary:"))
        print("Available Departments:")
        for dept in departments:
            print(dept)
        departement=input("Enter Department:")
        if departement not in departments:
            print("Invalid Department")
            break
        skills=input("Enter Skills separated by comma:").split(",")
        skills=set(skills)
        employees[emp_id]={
            "name":emp_name,
            "age":emp_age,
            "salary":salary,
            "department":departement,
            "skills":skills,
            "attendences":{}
        }
        print("Added Succussfully")
    elif  op=="2":
        if not employees:
            print("Employees currently Not available")
            break
        for emp_id,employee_data in employees.items():
            print("Employee Id:",emp_id)
            print("Employee Name:",employee_data["name"])
            print("Employee Salary:",employee_data["salary"])
            print("Employee skills:",employee_data["skills"])
            print("Employee age:",employee_data["age"])
            print("Employee Department:",employee_data["department"])
            print("Employee Attendences:",employee_data["attendences"])

    elif op=="3":
        emp_id=input("Enter employee id to search:")
        if emp_id not in employees:
            print("Employee Not Found")
            break
        employee_data=employees[emp_id]
        print("Employee Id:",emp_id)
        print("Employee Name:",employee_data["name"])
        print("Employee Salary:",employee_data["salary"])
        print("Employee skills:",employee_data["skills"])
        print("Employee age:",employee_data["age"])
        print("Employee Department:",employee_data["department"])
        print("Employee Attendences:",employee_data["attendences"])
    elif op=="4":
        emp_id=input("Enter Employee Id:")
        if emp_id not in employees:
            print("Employee Not Found")
            break
        day=input("Enter day[Monday-Friday]:").upper()
        if day not in working_days:
            print("Invalid Working Day!")
            break
        attendence=employees[emp_id]["attendences"]
        if day in attendence:
            print("Attendence already Marked for day:",day)
            break
        status=input("Enter P for Present or A for  Absent:").upper()
        if status=="P":
            attendence[day]="Present"
        elif status=="A":
            attendence[day]="Absent"
        else:
            print("Invalid Status")
            break

        print("Attendence Marked Succuessfully")

    elif op=="5":
        print("Department Report")
        print("----------------------")
        for department in departments:
            count=0
            for employee in employees.values():
                if employee["department"]==department:
                    count+=1
            print(department,":",count,"employees")
    elif op=="6":
        emp_id=input("Enter Employee to delete:")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee Deleted Succussfully")
        else:
            print("Employee Not Found")
    elif op=="7":
        print("Thank you for using for application")
        break
    else:
        print("Invalid Option")
    



    
            





        





