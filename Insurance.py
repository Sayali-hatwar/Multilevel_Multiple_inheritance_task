# insurance => person details  insurance sum and cost calculate			


class Customer:
    def __init__(self,custName,acc_num,age,balance):
        self.customer_name = custName
        self.account_number = acc_num
        self.age = age
        self.balance = balance

class Insurance(Customer):
    def __init__(self, cust_details):
        super().__init__(cust_details.get("custName"), cust_details.get("acc_num"),
                         cust_details.get("age"), cust_details.get("balance"))
        self.insurance_name = cust_details.get("insur_name")
        self.insurance_id = cust_details.get("insur_id")
        self.rate = cust_details.get('rate')
        self.year = cust_details.get('year')
        self.insurance_value = cust_details.get("ins_value")
        
    def risk_level(self):    
        if self.age > 70 or self.year > 10:
            return "High Risk"
        elif self.age < 25:
            return "High Risk"
        elif self.age < 50:
            return "Low Risk"
        elif self.age < 70:
            return "Moderate Risk"
        else:
            return "High Risk"

    def risk_factor(self): 
        level = self.risk_level()
        if level == "High Risk":
            return self.rate * 1.5
        elif level == "Low Risk":
            return self.rate * 1.0 
        elif level == "Moderate Risk":
            return self.rate * 1.2
        else:
            return self.rate * 1.6   

bk_details = {
    'custName': "John Doe",
    'acc_num': 123456789,
    'age' : 34,
    'balance': 1000.0,
    'insur_name': "HealthUP",
    'insur_id': "BKID345001",
    'rate': 0.05,  # 5% Interest
    'year': 3,
    'ins_value' : 500000.0

}
        
st = Insurance(bk_details)
level = st.risk_level()
print(f"Risk Level: {level}")
factor = st.risk_factor()
print(f"Risk Factor: {factor}")