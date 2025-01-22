# 👇🏻 YOUR CODE 👇🏻:
def get_yearly_revenue(monthly_revenue):
    if monthly_revenue > 0:
        return monthly_revenue * 12
    else:
        return 0

def get_yearly_expenses(monthly_expenses):
    if monthly_expenses > 0:
        return monthly_expenses * 12
    else:
        return 0

def get_tax_amount(profit):
    tax_rate = 0

    if profit > 100000:
        tax_rate = 0.25
    else:
        tax_rate = 0.15
    
    return profit * tax_rate

def apply_tax_credits(tax_amount, tax_credits):
    return tax_amount * tax_credits


# /YOUR CODE

# BLUEPRINT | DONT EDIT

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

yearly_revenue = get_yearly_revenue(monthly_revenue)
yearly_expenses = get_yearly_expenses(monthly_expenses)

profit = yearly_revenue - yearly_expenses

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")

# /BLUEPRINT