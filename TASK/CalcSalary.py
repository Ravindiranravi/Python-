# class Salary:
#     def __init__(self):
#         self.base_salary = 10000
    
#     def get_salary(self):
#         return self.base_salary
    
#     def get_allowance(self):
#         hra = 0.20 * self.base_salary  
#         da = 0.40 * self.base_salary   
#         ta = 0.25 * self.base_salary   
#         return hra + da + ta
    
#     def deduction(self):
#         insurance = 5000               
#         pf = 0.12 * self.base_salary   
#         gratuity = 0.05 * self.base_salary 
#         return insurance + pf + gratuity
    
#     def get_salary_step(self):
#         allowance = self.get_allowance()
#         deduction = self.deduction()
#         net_salary = self.base_salary + allowance - deduction
#         return net_salary

# # Example usage
# if __name__ == "__main__":
#     salary = Salary()
#     print(f"Base Salary: \u20B9{salary.get_salary()}")
#     print(f"Allowances: \u20B9{salary.get_allowance()}")
#     print(f"Deductions: \u20B9{salary.deduction()}")
#     print(f"Net Salary: \u20B9{salary.get_salary_step()}")




class Salary:
    def __init__(self, base_salary):
        self.base_salary = base_salary
    
    def get_salary(self):
        return self.base_salary
    
    def get_allowance(self):
        hra = 0.20 * self.base_salary  
        da = 0.40 * self.base_salary   
        ta = 0.25 * self.base_salary   
        return hra, da, ta
    
    def deduction(self):
        insurance = 5000              
        pf = 0.12 * self.base_salary  
        gratuity = 0.05 * self.base_salary 
        return insurance, pf, gratuity
    
    def get_salary_slip(self):
        hra, da, ta = self.get_allowance()
        insurance, pf, gratuity = self.deduction()
        total_allowance = hra + da + ta
        total_deduction = insurance + pf + gratuity
        net_salary = self.base_salary + total_allowance - total_deduction
        print('BASE SALARY =>')
        print(f"Base Salary: \u20B9{self.base_salary}")
        print('ALLOWANCE=>')
        print(f"HRA: \u20B9{hra}")
        print(f"DA: \u20B9{da}")
        print(f"TA: \u20B9{ta}")
        print('DEDUCTION=>')
        print(f"Insurance: \u20B9{insurance}")
        print(f"PF: \u20B9{pf}")
        print(f"Gratuity: \u20B9{gratuity}")
        print('TOTAL=>')
        print(f"Total Allowance: \u20B9{total_allowance}")
        print(f"Total Deduction: \u20B9{total_deduction}")
        print(f"Net Salary: \u20B9{net_salary}")

class EmployeeSalary(Salary):
    def __init__(self, base_salary, employee_id):
        super().__init__(base_salary)
        self.employee_id = employee_id
    
    def get_salary_slip(self):
        print(f"Employee ID: {self.employee_id}")
        super().get_salary_slip()

if __name__ == "__main__":
    emp_salary = EmployeeSalary(base_salary=15000, employee_id="101")
    emp_salary.get_salary_slip()
