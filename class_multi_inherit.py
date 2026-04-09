# logic - addMoney, withdraw money, bankAccIntrest 			

class Bank:
    def __init__(self,bName,bID):
        self.bank_name = bName
        self.bank_id = bID

class Customer(Bank):
    def __init__(self,bName,bID,custName,custAccount,custBalance):
        super().__init__(bName,bID)
        self.customer_name = custName
        self.customer_account = custAccount
        self.Balance = custBalance

    def getcustomerdetails(self):  ## this just for better understanding only final class prints are important
        return{
            'Bank_Name' : self.bank_name,
            'Bank_ID' : self.bank_id,
            'Customer_Name' : self.customer_name,
            'Customer_Account' : self.customer_account,
            'Main_Balance' : self.Balance
        }

class Deposit(Customer):
    def __init__(self,bName,bID,custName,custAccount,custBalance,depAmt):
        super().__init__(bName,bID,custName,custAccount,custBalance)
        self.deposit_amt = depAmt
        self.final_balance = custBalance+depAmt

    def getdepositdetails(self):
        print(f"Main Balance : {self.Balance}")
        print(f"After depositing {self.deposit_amt} final account balance is {self.final_balance}")

class Withdrawn(Deposit):
    def __init__(self,bName,bID,custName,custAccount,custBalance,depAmt,withAmt):
        super().__init__(bName,bID,custName,custAccount,custBalance,depAmt)
        self.withdraw_amt = withAmt
        self.final_balance1 = custBalance + depAmt
        self.final_balance = self.final_balance1 - withAmt
    
    def getwithdrawdetails(self):
        print(f"Main Balance : {self.Balance}")
        print(f"After deposit {self.deposit_amt} your final balance is {self.final_balance1}")
        print(f"After Withdrawing {self.withdraw_amt} your final balance is {self.final_balance}")

class Interest(Withdrawn):
    def __init__(self,details):
        super().__init__(details.get('bName'), details.get('bID'), details.get('custName'),
                         details.get('custAccount'), details.get('custBalance'), details.get('depAmt'),
                         details.get('withAmt'))
        self.rate = details.get('rate')
        self.years = details.get('years')
        self.interest = self.final_balance*self.rate*self.years
        self.total_balanace = self.interest + self.final_balance

    def getinterestdetails(self):   
        print(f"Main Balance : {self.Balance}")
        print(f"After deposit {self.deposit_amt} your final balance is {self.final_balance1}")
        print(f"After Withdrawing {self.withdraw_amt} your final balance is {self.final_balance}") 
        print(f'your Total balance is {self.total_balanace}')

# A simple dictionary to populate your class
bk_details = {
    'bName': "Global Bank",
    'bID': "GB101",
    'custName': "John Doe",
    'custAccount': 123456789,
    'custBalance': 1000.0,
    'depAmt': 200.0,
    'withAmt': 50.0,
    'rate': 0.05,  # 5% Interest
    'years': 3
}

ck = Interest(bk_details)
ck_Details = ck.getinterestdetails()




# dk = Deposit('xyz','bk0092','shah','GF23001',1000,200)
# dk.getdepositdetails()

# wk = Withdrawn('xyz','bk0092','shah','GF23001',1000,200,500)
# wk.getwithdrawdetails()
## deposit is not connecting with withdrawn class.