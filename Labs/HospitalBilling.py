#Hospital billing program

class patient:
    def __init__(self):
        self.total=0.0



    def details(self):
        self.no = input("Enter Patient Number: ")
        self.name =input("Enter Patient Name: ")
        print("\n=====================\n")
        print("Patient Number:", self.no)
        print("Patient Name:", self.name)

    #outpatient
    def billing(self, regfee =0.0, cons=0.0, labchar =0.0, phar=0.0):
        total = regfee + cons+ labchar+ phar
        return total
    #inpatient
    def billing(regfee=0.0, cons=0.0, days=0.0, charges=0.0, labchar=0.0, phar=0.0):
        total =regfee+cons+phar+(days*charges)
        return total



p1 =patient()
p1.details()

option =input("Is Patient Out-Patient (Y/N) :")
option=option.upper()
if option !='Y' and option !='N':
    option =input("Is Patient Out-Patient (Y/N) :")

if option =='Y':
    regfee=float(input("Enter Registration Fee:"))
    cons=float(input("Enter Consulation Fee:"))
    labchar=float(input("Enter Lab Charges:"))
    phar=float(input("Enter Pharmacy Charges:"))
    print("Total Charges :",p1.billing(regfee,cons,labchar,phar))

elif option =='N':
    regfee = float(input("Enter Registration Fee:"))
    cons = float(input("Enter Consulation Fee:"))
    days = float(input("Enter Number of Days:"))
    charges = float(input("Enter Charges per Day:"))
    labchar = float(input("Enter Lab Charges:"))
    phar = float(input("Enter Pharmacy Charges:"))
    print("Total Charges :", p1.billing(regfee, cons, days, charges, labchar, phar))