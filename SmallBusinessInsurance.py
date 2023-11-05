class InsurancePolicy:
    def __init__(self, policy_holder, business_type, location, coverage_amount, years_in_business, employees, past_claims):
        self.policy_holder = policy_holder
        self.business_type = business_type
        self.location = location
        self.coverage_amount = coverage_amount
        self.years_in_business = years_in_business
        self.employees = employees
        self.past_claims = past_claims

    def calculate_base_premium(self):
        # Calculate a base premium based on business type and location
        base_premium = 0
        if self.business_type == "Retail":
            base_premium = 2000
        elif self.business_type == "Restaurant":
            base_premium = 3000
        elif self.business_type == "Technology":
            base_premium = 4000

        if self.location == "Urban":
            base_premium *= 1.2
        elif self.location == "Suburban":
            base_premium *= 1.1

        return base_premium

    def calculate_risk_factor(self):
        # Calculate a risk factor based on policy holder's history and years in business
        risk_factor = 1.0
        if self.policy_holder == "New Business":
            risk_factor *= 1.2
        elif self.policy_holder == "Experienced Business":
            risk_factor *= 0.9

        if self.years_in_business < 3:
            risk_factor *= 1.1  # Increase risk factor for newer businesses

        return risk_factor

    def calculate_coverage_factor(self):
        # Calculate a coverage factor based on coverage amount
        coverage_factor = 1.0
        if self.coverage_amount > 50000:
            coverage_factor *= 1.1  # Increase coverage factor for higher coverage

        return coverage_factor

    def calculate_employee_factor(self):
        # Calculate a factor based on the number of employees
        employee_factor = 1.0
        if self.employees > 10:
            employee_factor *= 1.2  # Increase factor for larger businesses

        return employee_factor

    def calculate_past_claim_factor(self):
        # Calculate a factor based on past claims history
        claim_factor = 1.0
        if self.past_claims > 0:
            claim_factor *= 1.5  # Increase factor for businesses with past claims

        # Ensure a minimum claim factor of 0.8, even if there are no past claims
        claim_factor = max(claim_factor, 0.8)

        return claim_factor

    def calculate_premium(self):
        # Calculate the final premium by combining all factors
        base_premium = self.calculate_base_premium()
        risk_factor = self.calculate_risk_factor()
        coverage_factor = self.calculate_coverage_factor()
        employee_factor = self.calculate_employee_factor()
        claim_factor = self.calculate_past_claim_factor()

        final_premium = base_premium * risk_factor * coverage_factor * employee_factor * claim_factor

        return final_premium

# Prompt the user for input
policy_holder = input("Enter the policy holder type (New Business/Experienced Business): ")
business_type = input("Enter the business type (Retail/Restaurant/Technology): ")
location = input("Enter the business location (Urban/Suburban): ")
coverage_amount = float(input("Enter the coverage amount (in USD): "))
years_in_business = int(input("Enter the years in business: "))
employees = int(input("Enter the number of employees: "))
past_claims = int(input("Enter the number of past claims: "))

# Calculate the premium based on user input
policy = InsurancePolicy(policy_holder, business_type, location, coverage_amount, years_in_business, employees, past_claims)
premium = policy.calculate_premium()

# Display the premium
print("\nInsurance Premium Calculation Results:")
print(f"Policy Holder: {policy_holder}")
print(f"Business Type: {business_type}")
print(f"Location: {location}")
print(f"Coverage Amount: ${coverage_amount:.2f}")
print(f"Years in Business: {years_in_business} years")
print(f"Number of Employees: {employees}")
print(f"Past Claims: {past_claims}")
print(f"Premium: ${premium:.2f}")
