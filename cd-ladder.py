def calculate_cd_ladder_return(cds, investment_amount):
    total_return = 0
    for cd in cds:
        principal = investment_amount / 4  # Equal investment in each CD
        duration_months, interest_rate = cd
        duration_years = duration_months / 12
        maturity_amount = principal * (1 + (interest_rate / 100) * duration_years)
        total_return += maturity_amount - principal
    return total_return


def get_cd_details():
    cds = []
    for i in range(1, 5):
        print(f"CD {i}")
        duration_months = int(input("Enter duration in months: "))
        interest_rate = float(input("Enter interest rate (%): "))
        cds.append((duration_months, interest_rate))
    return cds


def main():
    print("Welcome to CD Ladder Return Calculator")
    investment_amount = float(input("Enter the total investment amount: $"))
    cds = get_cd_details()
    total_return = calculate_cd_ladder_return(cds, investment_amount)
    print(f"The total return on your CD ladder is: ${total_return:.2f}")


if __name__ == "__main__":
    main()
