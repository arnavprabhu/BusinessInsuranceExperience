import openai

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

# Define an AI-driven risk assessment module
class RiskAssessment:
    @staticmethod
    def assess_risk(business_name, industry, location):
        # Simulate a basic risk assessment based on user inputs
        risk_score = 0
        
        # Assess risk based on industry
        if industry.lower() == "retail":
            risk_score += 10
        elif industry.lower() == "manufacturing":
            risk_score += 20
        elif industry.lower() == "technology":
            risk_score += 5

        # Assess risk based on location
        if location.lower() == "urban":
            risk_score += 15
        elif location.lower() == "suburban":
            risk_score += 10
        elif location.lower() == "rural":
            risk_score += 5

        return risk_score

# Function to generate AI responses
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose an appropriate engine
        prompt=prompt,
        max_tokens=50,  # Adjust this based on desired response length
        n=1,  # Number of responses to generate
        stop=None,  # Optional: Add a list of stop words to limit the response
    )
    
    return response.choices[0].text.strip()

# Update the SmallBusinessInsurance class to integrate AI and risk-based premiums
class SmallBusinessInsurance:
    def __init__(self, business_name, coverage_type, risk_score):
        self.business_name = business_name
        self.coverage_type = coverage_type
        self.claims = []
        self.risk_score = risk_score
        self.premium = self.calculate_premium()

    def calculate_premium(self):
        # Define a base premium
        base_premium = 500
        
        # Adjust the premium based on risk score
        premium = base_premium + self.risk_score
        
        return premium

    def file_claim(self, claim_description):
        self.claims.append(claim_description)
        print(f"Claim filed for {self.business_name}: {claim_description}")

    def display_policy_info(self):
        print(f"Business Name: {self.business_name}")
        print(f"Coverage Type: {self.coverage_type}")
        print(f"Premium: ${self.premium} per month")
        print(f"Risk Score: {self.risk_score}")
        print("Claims:")
        for i, claim in enumerate(self.claims, 1):
            print(f"{i}. {claim}")

# Example usage
if __name__ == "__main__":
    # Get user inputs for business attributes
    business_name = input("Enter your business name: ")
    industry = input("Enter your industry (e.g., retail, manufacturing, technology): ")
    location = input("Enter your business location (e.g., urban, suburban, rural): ")

    # Calculate the risk factor based on user inputs
    risk_score = RiskAssessment.assess_risk(business_name, industry, location)

    # Create a small business insurance policy with user-input risk factor
    policy1 = SmallBusinessInsurance(business_name, "General Liability", risk_score)
    
    # Display policy information, including user-defined risk assessment
    policy1.display_policy_info()
    
    # File a claim
    claim_description = input("Enter the claim description: ")
    policy1.file_claim(claim_description)

    # Display updated policy information with claims and adjusted premium
    policy1.display_policy_info()

    # Interact with the AI-powered chatbot
    user_question = input("Ask a question (e.g., 'What is my premium?'): ")
    chatbot_response = generate_response(user_question)
    print(f"Chatbot Response: {chatbot_response}")
