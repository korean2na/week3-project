class Property():
    def __init__(self):
        # ADDRESS
        print("First, a few basic questions regarding your property.")
        self.street_address = input('\nWhat is the street address of your property?\n').lower()
        self.city = input('\nWhat city is your property located in?\n').lower()
        self.state = input('\nWhat state is your property located in?\n').lower()
        self.zip_code = abs(int(input('\nWhat ZIP code is your property located in?\n')))
        self.type = input('\nWhat type of property is it? (Condo, Duplex, House, Beach House, etc.)\n').lower()
        # INCOME
        print("\nThanks. Now let's get started with evaluating your property's return-on-investment (ROI).\nWe're going ask you a couple of questions regarding income from your property.")
        self.inc_rent = float(input("\nWhat will be the property's monthly income from RENT?\n"))
        self.inc_fees = float(input("\nWhat will be the property's monthly income from FEES?\n"))
            # TOTAL
        self.inc_total_monthly = self.inc_rent + self.inc_fees

        # EXPENSES
        print("\nNext, we're going ask you a series of questions regarding expenses incurred from your property.")
        self.exp_mortgage = float(input("\nHow much do you pay monthly in MORTGAGE on your property?\n"))
        self.exp_taxes = float(input("\nHow much do you pay monthly in TAXES on your property?\n"))
        self.exp_insurance = float(input("\nHow much do you pay monthly for INSURANCE on your property?\n"))
            # UTILITIES
        utilities_query = (input("\nDo you pay for any monthly utility for your property?\n(For this calculator, utilities include: electricity, water, gas, sewage, garbage)\n(Y)es | (N)o\n")).lower()
        if utilities_query == 'n' or utilities_query == 'no' or utilities_query == '(n)' or utilities_query == '(n)o' or utilities_query == '0':
            self.exp_electric = 0
            self.exp_water = 0
            self.exp_gas = 0
            self.exp_sewer = 0
            self.exp_garbage = 0
        else:
            self.exp_electric = float(input("\nHow much do you pay monthly for ELECTRICTY?\n"))
            self.exp_water = float(input("\nHow much do you pay monthly for WATER?\n"))
            self.exp_gas = float(input("\nHow much do you pay monthly for GAS?\n"))
            self.exp_sewer = float(input("\nHow much do you pay monthly for SEWAGE?\n"))
            self.exp_garbage = float(input("\nHow much do you pay monthly for GARBAGE REMOVAL?\n"))
            # OTHERS
        self.exp_hoa = float(input("\nHow much do you pay monthly in HOA FEES?\n"))
        self.exp_lawn = float(input("\nHow much do you pay monthly for LAWN CARE/SNOW REMOVAL?\n"))
        
            # PERCENT-BASED
        print("\nThe next few expenses covered are going to be based on a % of your property's total monthly income.\nFor these expenses, please provide a % from 1-100 of your total monthly income that will go towards that expense.\n(Example: If your total monthly income is $1000 and you put 5% towards repairs monthly, you will be putting $50/month towards repairs.")
                # PERCENTAGES
        self.exp_vacancy_p = float(input("\nWhat % of total monthly income will be put towards VACANCY CONTINGENCY?\n(5% is recommended)\n"))
        self.exp_repairs_p = float(input("\nWhat % of total monthly income will be put towards REPAIR FUNDS?\n(5% is recommended)\n"))
        self.exp_capex_p = float(input("\nWhat % of total monthly income will be put towards CAPITAL EXPENDITURE?\n(5% is recommended)\n"))
        self.exp_mgmt_p = float(input("\nWhat % of total monthly income will be put towards PROPERTY MANAGEMENT FEES?\n(10% is recommended)\n"))
                # DOLLAR AMOUNT
        self.exp_vacancy = self.exp_vacancy_p * self.inc_total_monthly / 100
        self.exp_repairs = self.exp_repairs_p * self.inc_total_monthly / 100
        self.exp_capex = self.exp_capex_p * self.inc_total_monthly / 100
        self.exp_mgmt = self.exp_mgmt_p * self.inc_total_monthly / 100
            # TOTAL
        self.exp_total_monthly = self.exp_mortgage + self.exp_taxes + self.exp_insurance + self.exp_electric + self.exp_water + self.exp_gas + self.exp_sewer + self.exp_garbage + self.exp_hoa + self.exp_lawn + self.exp_vacancy + self.exp_repairs + self.exp_capex + self.exp_mgmt
        
        # INVESTMENT EXPENSES
        print("\nFinally, we're going ask you a series of questions regarding investment expenses incurred from your property.")
        self.invest_down_pay = float(input("\nHow much did you pay in DOWN PAYMENT on your property?\n"))
        self.invest_closing = float(input("\nHow much did you pay in CLOSING COSTS on your property?\n"))
        self.invest_repairs = float(input("\nHow much did you set aside as REPAIR BUDGET for your property?\n"))
        self.invest_misc = float(input("\nHow much did you pay/set aside in MISCELLANEOUS INVESTMENTS for your property?\n"))
            # TOTAL
        self.invest_total = self.invest_down_pay + self.invest_closing + self.invest_repairs + self.invest_misc

        # CALCULATIONS
        self.cash_flow_monthly = self.inc_total_monthly - self.exp_total_monthly
        self.cash_flow_annual = self.cash_flow_monthly * 12
        self.roi_monthly = self.cash_flow_monthly / self.invest_total
        self.roi_annual = self.cash_flow_annual / self.invest_total
        self.roi_monthly_p = self.roi_monthly * 100
        self.roi_annual_p = self.roi_annual * 100
    
    def show_info(self):
        print(f"=~=~= INCOME =~=~=\nTotal Monthly Income: ${self.inc_total_monthly:.2f}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\n=~=~= EXPENSES =~=~=\nTotal Monthly Expenses: ${self.exp_total_monthly:.2f}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\n=~=~= INVESTMENT EXPENSES =~=~=\nTotal Investment: ${self.invest_total:.2f}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\n=~=~= ROI CALCULATIONS =~=~=\nMonthly Cash Flow: ${self.cash_flow_monthly:.2f}\nAnnual Cash Flow: ${self.cash_flow_annual:.2f}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\nMonthly Return-On-Investment (ROI): {self.roi_monthly_p:.2f}%\nAnnual Return-On-Investment (ROI): {self.roi_annual_p:.2f}%\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=")

    def __str__(self):
        return f"\nHere is a review of your property's information:\nAddress:\n{self.street_address.title()}\n{self.city.title()}, {self.state.upper()}, {self.zip_code}\n\nType: {self.type.title()}\n=~=~= INCOME =~=~=\nRent: ${self.inc_rent:.2f}\nFees: ${self.inc_fees:.2f}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\nTotal Monthly Income: ${self.inc_total_monthly:.2f}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\n=~=~= EXPENSES =~=~=\nMortgage: ${self.exp_mortgage:.2f}\nTaxes: ${self.exp_taxes:.2f}\nInsurance: ${self.exp_insurance:.2f}\nElectricity: ${self.exp_electric:.2f}\nWater: ${self.exp_water:.2f}\nGas: ${self.exp_gas:.2f}\nSewage: ${self.exp_sewer:.2f}\nGarbage Removal: ${self.exp_garbage:.2f}\nHOA Fees: ${self.exp_hoa:.2f}\nLawn Care/Snow Removal: ${self.exp_lawn:.2f}\nVacancy Contingency: ${self.exp_vacancy:.2f} ({self.exp_vacancy_p:.2f}% of total monthly income)\nRepair Funds: ${self.exp_repairs:.2f} ({self.exp_repairs_p:.2f}% of total monthly income)\nCapital Expenditure: ${self.exp_capex:.2f} ({self.exp_capex_p:.2f}% of total monthly income)\nProperty Management Fees: ${self.exp_mgmt:.2f} ({self.exp_mgmt_p:.2f}% of total monthly income)\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\nTotal Monthly Expenses: ${self.exp_total_monthly:.2f}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\n=~=~= INVESTMENT EXPENSES =~=~=\nDown Payment: ${self.invest_down_pay:.2f}\nClosing Costs: ${self.invest_closing:.2f}\nRepair Budget: ${self.invest_repairs:.2f}\nMiscellaneous Investments: ${self.invest_misc:.2f}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\nTotal Investment: ${self.invest_total:.2f}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\n=~=~= ROI CALCULATIONS =~=~=\nMonthly Cash Flow: ${self.cash_flow_monthly:.2f}\nAnnual Cash Flow: ${self.cash_flow_annual:.2f}\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\nMonthly Return-On-Investment (ROI): {self.roi_monthly_p:.2f}%\nAnnual Return-On-Investment (ROI): {self.roi_annual_p:.2f}%\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~="