'''
Created on 7 Mar 2013

@author: eidahil
'''
from __future__ import division
import personalSalary
import personalInflation
import personalTaxes
import pensionData

def main():
    ''' Set initial data '''
    salary_instance = []
    salary_instance.append(personalSalary.SalaryData(55000,3600,27000,0,2013,2006))
    salary_instance.append(personalSalary.SalaryData(56000,3700,28000,0,2013,2007))
    annual_inflation = personalInflation.InflationData(2) #2 percent inflation set
    
    ''' initialise variables used in loop '''
    num_year_in_service = []
    gross_salary = []
    monthly_take_home_pay =[]
    first_gross_salary =[]
    first_take_home_pay =[]
    pension_instance =[]
    monthly_gross_salary = []
    delta_wage_increase = []
    wage_increase = []
    inflation = []
    salary_increase_yoy = []
    monthly_tax = []
    
    for i in range(len(salary_instance)):    
        num_year_in_service.insert(i, (salary_instance[i].get_number_of_years_in_service()))
        gross_salary.insert(i, salary_instance[i].get_my_gross_salary())
        monthly_take_home_pay.insert(i, salary_instance[i].get_my_monthly_take_home_pay())
        first_gross_salary.insert(i, salary_instance[i].get_my_first_gross_salary())
        first_take_home_pay.insert(i, salary_instance[i].get_my_first_monthly_take_home_pay())
        pension_instance.insert(i, pensionData.MyPensionData(0,0))

        ''' calc my tax '''
        monthly_gross_salary.insert(i, gross_salary[i] / 12)
        print ("Gross salary per month: EUR", monthly_gross_salary[i])
        print ("Net Pay per month: EUR", monthly_take_home_pay[i])
        monthly_tax.insert(i,(((monthly_gross_salary[i] - monthly_take_home_pay[i])/monthly_gross_salary[i]*100)))
        print ("Net tax: ", round(monthly_tax[i]), "%")
    
        ''' Calc wage increase '''
        delta_wage_increase.insert(i,float(gross_salary[i] - first_gross_salary[i]))
        print ("delta_wage_increase: EUR", delta_wage_increase[i])
        wage_increase.insert(i, (delta_wage_increase[i] / gross_salary[i]) * 100) 
        print ("My wage increase: ", round(wage_increase[i]), "%")

        ''' calc inflation '''
        inflation.insert(i, annual_inflation.get_my_annual_inflation())
        print ("Year of service: ", num_year_in_service[i])

    
    ''' Per year of increment, calculate the increment, minus the inflation.'''
    for i in range(len(first_gross_salary)):
        salary_increase_yoy.insert(i, first_gross_salary[i])
        print ("index, first_gross_salary ", i, " ", first_gross_salary[i])

        for j in range(len(num_year_in_service)):
            print ("index, first_gross_salary ", j)
            #salary_increase_yoy[i] = salary_increase_yoy[i] - ((salary_increase_yoy[i] * inflation[i]) / 100)
            #salary_increase_yoy[i] = salary_increase_yoy[i] + (delta_wage_increase[i] / num_year_in_service[i])
        #print ("Salary post inflation: EUR", round(salary_increase_yoy))
        
    

    #''' calculate income and tax including pension'''
    #pension_contribution = gross_salary[i] * pension_instance[i].get_my_pension_contribution() / 100
    #gross_salary_w_deductions = gross_salary[i] - pension_contribution
    #monthly_gross_salary = gross_salary_w_deductions / 12
    #monthly_tax = float((monthly_gross_salary[i] - monthly_take_home_pay[i])/monthly_gross_salary)*100
    #print ("New net tax w/pension deduction: ", round(monthly_tax), "%")
    
    #''' TODO: add in other salary deductions and add benefits to salary like insurance and pension etc '''
    
if __name__ == "__main__":
    main()
    