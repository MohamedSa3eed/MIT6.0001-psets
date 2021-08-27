annual_salary        = float (input("Enter your annual salary: "))
target               = 0.25 * 1000000
r =0.04
semi_annual_raise    = 0.07
portion_down_payment = 0.25 
current_savings      = 0
high =1000 
low =0 
portion_saved = (high - low )//2
steps =0
while abs (current_savings*portion_saved -target )>=100  :
 portion_saved = (high - low )//2
 current_savings      = 0
 n_of_months          = 1
 while n_of_months <= 36 :
   current_savings      = 0
   current_savings = current_savings + (current_savings*r)/12
   current_savings = current_savings + (annual_salary/12)*(portion_saved/float(10000))
   n_of_months +=1
   if n_of_months % 6==0 :
      annual_salary = annual_salary + annual_salary*semi_annual_raise
 if current_savings>= target :
   break 
 if current_savings < target :
     low =portion_saved
     steps += 1
 else :
     high= portion_saved    
     steps += 1

print("Best savings rate: {:.4f}".format(portion_saved / 10000))
print ('steps :',steps)

