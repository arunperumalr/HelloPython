# Loan Calculator Program

# Function to calculate EMI
def calculate_emi(principal, annual_rate, months):
    monthly_rate = annual_rate / (12 * 100)

    if monthly_rate == 0:
        emi = principal / months
    else:
        emi = (
            principal
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months - 1)
        )

    return emi


# Main Program
print("====== Loan Calculator ======")

# User Inputs
principal = float(input("Enter Loan Amount: ₹ "))
annual_rate = float(input("Enter Annual Interest Rate (%): "))

# Choose tenure type
choice = input("Do you want to enter tenure in Years or Months? (Y/M): ").strip().upper()

if choice == "Y":
    years = int(input("Enter Loan Tenure (Years): "))
    months = years * 12
elif choice == "M":
    months = int(input("Enter Loan Tenure (Months): "))
else:
    print("Invalid choice! Please restart the program.")
    exit()

# EMI Calculation
emi = calculate_emi(principal, annual_rate, months)

# Total Payment and Interest
total_payment = emi * months
total_interest = total_payment - principal

# Display Results
print("\n====== Loan Details ======")
print(f"Loan Amount        : ₹ {principal:,.2f}")
print(f"Interest Rate      : {annual_rate:.2f}% per annum")
print(f"Loan Tenure        : {months} months")

print("\n====== Calculation Results ======")
print(f"Monthly EMI        : ₹ {emi:,.2f}")
print(f"Total Payment      : ₹ {total_payment:,.2f}")
print(f"Total Interest Paid: ₹ {total_interest:,.2f}")