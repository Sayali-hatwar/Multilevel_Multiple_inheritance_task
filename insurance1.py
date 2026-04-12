class Customer:
    def __init__(self,cust_name,cust_acc,age,balance):
        self.customer_name = cust_name
        self.customer_account = cust_acc
        self.customer_age = age
        self.main_balance = balance



class Insurance(Customer):
    def __init__(self, cust_details):
        super().__init__(cust_details.get('cust_name'), cust_details.get('cust_acc'),cust_details.get('age'), cust_details.get('balance'))
        self.insurance_name = cust_details.get('ins_name')
        self.insurance_id = cust_details.get('ins_id')
        self.standard_rate = cust_details.get('rate')
        self.insurance_value = cust_details.get('ins_val')
        self.experience_year = cust_details.get('exp_year',0)
        self.no_claim_year = cust_details.get('no_claim_yr',0)
        self.smoking = cust_details.get('smoking',False)
        self.drinking = cust_details.get('drinking',False)
        self.hazardous_habit = cust_details.get('hazardous_habit',False)
        
    def risk_level(self):
        if self.customer_age >= 70 or self.experience_year >= 10:
            return "High Risk"
        elif self.customer_age <= 25:
            return "Low Risk"
        elif self.customer_age <= 50:
            return "Moderate Risk"
        else:
            return "High Risk"
    
    def risk_factor(self):
        level = self.risk_level()
        if level == 'High Risk':
            return self.standard_rate*1.5
        elif level == 'Low Risk':
            return self.standard_rate*1.0
        elif level == 'Moderate Risk':
            return self.standard_rate*1.2
        else:
            return self.standard_rate*1.6
    
    def experience_discount(self):
        years = self.experience_year
        if years >= 6:
            return 0.15
        elif years >= 4:
            return 0.10
        elif years >= 2:
            return 0.07
        elif years >= 1:
            return 0.05
        else:
            return 0.0
    
    def no_claim_bonus(self):
        claim_year = self.no_claim_year
        if claim_year >= 5:
            return 0.20
        elif claim_year >=3:
            return 0.15
        elif claim_year >=1:
            return 0.10
        else:
            return 0.0
        
    def habit_penalty(self):
        penalty = 0.0
        if self.smoking:
            penalty += 0.10
        if self.drinking:
            penalty += 0.05
        if self.hazardous_habit:
            penalty += 0.08
        return min(penalty,0.25)
    
    def process_claim(self,damage_amount):
        print()
        print(f"========== Accident Alert : {self.customer_name} Hit the pole!!! ========")
        print(f"Damage amount : {damage_amount}")
        print(f"Deductable amount : {self.deductable_amount}")
    
        if damage_amount <= self.deductable_amount:
            user_pay = damage_amount
            # If the damage is less than the deductible, the company pays nothing!
            company_pays = 0
            print("Result: Damage is below deductible. Insurance covers $0.")
        else:
            user_pay = self.deductable_amount
            company_pays = damage_amount - self.deductable_amount
            print(f"Result: Insurance covers ${company_pays}!")
        print(f"User Pays : {user_pay}")

        # main balance after deducting user pay
        self.main_balance -= user_pay
        print(f"Your main balance : {self.main_balance}")
        
        # Reset no claim bonus after claiming the insurance 
        self.no_claim_year = 0

    
class Standardinsurance(Insurance):
    def __init__(self,cust_details):
        super().__init__(cust_details)
        self.deductable_amount = 500

    def calculate_standard_premium(self):
        current_rate = self.risk_factor()
        current_rate += self.habit_penalty()
        current_rate -= self.no_claim_bonus()
        # Final standard rate
        final_rate = max(current_rate,0.01)
        return round(self.insurance_value*final_rate,2)
    
    def display_receipt(self):
        print()
        print("=====================Standard Policy==================")
        print(f"Customer Name : {self.customer_name} | Customer Age : {self.customer_age}")
        print(f"Plan : {self.insurance_name} | ID : {self.insurance_id}")
        print(f"Risk-Level : {self.risk_level()}(Risk-Factor : {self.risk_factor()})")
        print(f"Deductable Amount : {self.deductable_amount}")
        print(f"Insurance Final Value : {self.calculate_standard_premium()}")
        print(f"Main Balance : {self.main_balance}")


class Premium(Insurance):
    def __init__(self, cust_details):
        super().__init__(cust_details)
        self.deductable_amount = 0

    def calculate_premium(self):
        premium_rate = self.risk_factor()
        premium_rate += self.habit_penalty()
        premium_rate -= self.no_claim_bonus()
        premium_rate -= self.experience_discount()
        # Final premium rate
        final_premium_rate = max(premium_rate,0.05)
        return round(self.insurance_value*final_premium_rate,2)
    
    def display_receipt(self):
        print("==================Premium Policy=================")
        print(f"Customer Name : {self.customer_name} | Customer Age : {self.customer_age}")
        print(f"Plan : {self.insurance_name} | ID : {self.insurance_id}")
        print(f"VIP Perks : Experience year bonus of {self.experience_discount()*100}% is applied")
        print(f"Deductable Amount : {self.deductable_amount}")
        print(f"Insurance final Value : {self.calculate_premium()}")
        print(f"Main Balance : {self.main_balance}")
        

    

cust_data = {
    'cust_name': "Alice Smith",
    'cust_acc': 987654321,
    'age': 35,
    'balance': 5000.0,
    'ins_name': "SafeGuard Standard",
    'ins_id': "STD-101",
    'rate': 0.05,            # 5% Base Rate
    'ins_val': 250000.0,      # $250,000 Insurance Value
    'exp_year': 4,           # 4 years experience
    'no_claim_yr': 3,        # 3 years no claims
    'smoking': False,
    'drinking': True,        # Adds penalty
    'hazardous_habit': False,
    'damage_amount':300
}

policy = Standardinsurance(cust_data)
standard_premium = policy.display_receipt()
print("--"*25)
std_claim = policy.process_claim(damage_amount=1200)
print()

premium_policy = Premium(cust_data)
premium = premium_policy.display_receipt()
print("--"*25)
prem_claim = premium_policy.process_claim(damage_amount=1200)

