monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses #calculates user monthly savings
annual_interest = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)#calculates savings over span of 1 year

print("Your monthly savings: ", "$",monthly_savings)
print("Your Projected savings after one year, with interest, is: ", "$", projected_savings)