# A function to expand range of ZIP codes into a list
def expand_zip_code_ranges(zip_ranges):
    expanded_zip_codes = set()
    for zrange in zip_ranges:
        parts = zrange.split('-')
        if len(parts) == 2:
            start, end = map(int, parts)
            expanded_zip_codes.update(map(str, range(start, end + 1)))
        else:
            expanded_zip_codes.add(zrange)
    return expanded_zip_codes

# Define base premiums for industries
industry_base_premiums = {
    'construction': 1500,
    'retail': 1200,
    'manufacturing': 1400,
    'it': 1000,
}

# Define premium adjustments based on company size (number of employees)
company_size_premium_adjustments = {
    '1-5': 0.8,
    '6-10': 1.0,
    '11-50': 1.2,
    '51+': 1.5,
}

# Function to determine base premium based on industry and company size
def get_base_premium(industry, number_of_employees):
    # Get the base premium for the industry
    base = industry_base_premiums.get(industry, 1000)  # Default to 1000 if industry not found
    # Adjust base premium based on company size
    adjustment_factor = company_size_premium_adjustments.get(number_of_employees, 1.0)  # Default to no adjustment
    return base * adjustment_factor

# Function to calculate insurance premium based on user input
def calculate_insurance_premium(business_attributes, high_risk_zip_codes, base_premium):
    premium_multiplier = 1.0  # Start with a multiplier of 1.0
    
    # Risk multipliers based on business attributes
    risk_multipliers = {
        'industry': {
            # These are now unnecessary, as base premium changes with industry.
            # You can keep this if you want further industry-based adjustments.
        },
        'years_in_business': {
            '0-1': 1.3,
            '2-3': 1.2,
            '4-10': 1.1,
            '10+': 0.9,
        },
        # Size of company adjustments are now handled in the base premium
        'annual_revenue': {
            '0-100000': 1.0,
            '100001-500000': 1.1,
            '500001-1000000': 1.2,
            '1000001+': 1.3,
        }
    }
    
    # Apply the risk multipliers to the premium multiplier
    for attribute, risk_table in risk_multipliers.items():
        user_value = business_attributes[attribute]
        premium_multiplier *= risk_table.get(user_value, 1.0)
    
    # Increase the multiplier if the business is in a high-risk location
    if business_attributes['zip_code'] in high_risk_zip_codes:
        premium_multiplier *= 1.5

    # Calculate the final premium
    final_premium = base_premium * premium_multiplier

    return final_premium

# Function to get user input for business attributes
def get_business_attributes():
    print("Please enter the following details about your business to calculate the insurance premium:")
    industry = input("Industry (construction, retail, manufacturing, it): ").lower()
    years_in_business = input("Years in business (0-1, 2-3, 4-10, 10+): ")
    number_of_employees = input("Number of employees (1-5, 6-10, 11-50, 51+): ")
    annual_revenue = input("Annual revenue (0-100000, 100001-500000, 500001-1000000, 1000001+): ")
    zip_code = input("Business ZIP code: ")

    return {
        'industry': industry,
        'years_in_business': years_in_business,
        'number_of_employees': number_of_employees,
        'annual_revenue': annual_revenue,
        'zip_code': zip_code
    }

# Main function to run the insurance premium calculator
def main():
    # Get business attributes from user input
    business_attributes = get_business_attributes()

    # Calculate base premium based on industry and company size
    base_premium = get_base_premium(business_attributes['industry'], business_attributes['number_of_employees'])

    # Define high-risk ZIP codes (expand them from the ranges provided)
    high_risk_zip_codes_ranges = [
        '35020-35023', '35025-35029', '71201-71205', '71210', '71212', '71215',
    '48601-48607', '48609', '38101-38109', '38112-38128', '38130-38143',
    ]
    high_risk_zip_codes = expand_zip_code_ranges(high_risk_zip_codes_ranges)

    # Calculate the final insurance premium
    final_premium = calculate_insurance_premium(business_attributes, high_risk_zip_codes, base_premium)
    print(f"\nThe calculated insurance premium for your business is: ${final_premium:.2f}")

# Call the main function to start the program
if __name__ == "__main__":
    main()


