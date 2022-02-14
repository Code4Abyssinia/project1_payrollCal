#"tabulate" is a module that allows you to display table data beautifully.
#It is not part of standard Python library, so it has to be installed. https://pyneng.read

#Payroll calculator ,01/28/2022, Naod Habte


from tabulate import tabulate

employees=[]
print("Hello, welcome, please enter below, \n the name of the employee, \n the numbers of hours worked and hourly rate")
for i in range (3):
       
        emp_name=input("Name of employee, please: ")
        hours_worked=float(input("Hours worked: "))
        pay_rate=float(input("Hourly rate: "))
        
        print("+*+*+*+*+*+*+*+*+")
        
                

        if hours_worked<=40:
                ot_pay = 0
                
                

        else:
                ot_pay =round( pay_rate * 1.5 * (hours_worked - 40), 2)

        regular_pay = round(hours_worked * pay_rate, 2)
        gross = round(regular_pay + ot_pay, 2)
        fed_tax = round(gross * 0.1, 2)
        state_tax = round( gross * 0.06, 2)
        fica_tax = round(gross * 0.03, 2)
        net =round( gross-fed_tax - state_tax - fica_tax, 2)
#i had to change my data into a str type to concatenate the dollar sign
        employee = emp_name ,str(hours_worked) + " $",str(pay_rate)+ " $",str(regular_pay) + " $",str(ot_pay)+" $",str(gross)+" $",str(fed_tax)+" $",str(state_tax)+" $",str(fica_tax)+" $",str(net)+" $"
        employees.append(employee)
        
col_name = ["Employee Name" ,"Hours Worked", "Pay Rate" , "Regular Pay", "OT Pay","Gross Pay","Fed Tax","State tax" , "FICA", "Net Pay"]


print(tabulate(employees, col_name, tablefmt="fancy_grid",showindex="always",floatfmt=".2f"))

