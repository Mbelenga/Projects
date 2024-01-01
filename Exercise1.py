def calculate_pay(hourly_rate, hours_worked):
    """
    Function to calculate the employee's pay based on the hourly rate and hours worked.
    
    :param hourly_rate: The employee's hourly rate (float)
    :param hours_worked: The number of hours the employee worked (float)
    
    :return: The employee's total pay (float)
    """
    # Calculate the total pay by multiplying the hourly rate and the number of hours worked
    total_pay = hourly_rate * hours_worked

    # If the number of hours worked is greater than 40, calculate the overtime pay and add it to the total pay
    if hours_worked > 40:
        overtime_pay = (hourly_rate * 1.5) * (hours_worked - 40)
        total_pay += overtime_pay

    return total_pay

# Test the function with example values
hourly_rate = 10
hours_worked = 45

print(f"The employee's total pay is: ${calculate_pay(hourly_rate, hours_worked):.2f}")