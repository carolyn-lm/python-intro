# Write function here
def calculate_pay(hours_worked, pay_per_hour):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_pay = 40 * pay_per_hour
        overtime_pay = overtime_hours * pay_per_hour * 2
        return overtime_pay + regular_pay
    return hours_worked * pay_per_hour

# Worked 40 hours at $20 an hour
print(calculate_pay(40,20))
# Worked 50 hours at $20 an hour
print(calculate_pay(50,20))
# Worked 40 hours at $12 an hour
print(calculate_pay(40,12))
