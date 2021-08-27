#----------------------------------------------------B-------------------------------------------------
annual_salary        = int (input("Enter your annual salary: "))
portion_saved        = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost           = int(input("Enter the cost of your dream home: "))
semi_annual_raise    = float(input("Enter the semi­annual raise, as a decimal: "))
r                    = 0.04
portion_down_payment = 0.25
current_savings      = 0
n_of_months          = 0
while True :
 current_savings = current_savings + (current_savings*r)/12
 current_savings = current_savings + (annual_salary/12)*portion_saved
 n_of_months +=1
 if current_savings>= 0.25*total_cost :
  break 
 if n_of_months % 6==0 :
      annual_salary = annual_salary + annual_salary*semi_annual_raise
print('Number of months: ' ,n_of_months)