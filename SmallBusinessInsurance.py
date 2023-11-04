import random

# Define an AI-driven risk assessment module
class RiskAssessment:
    @staticmethod
    def assess_risk(business_name):
        # Simulate a basic risk assessment using random values
        risk_score = random.randint(1, 100)
        return risk_score

# Define an AI-powered chatbot for customer support
class Chatbot:
    @staticmethod
    def answer_question(question):
        # Simulate chatbot responses
        if "coverage" in question:
            return "Your coverage type is General Liability."
        elif "premium" in question:
            return "Your monthly premium is $500."
        else:
            return "I'm sorry, I cannot answer that question right now."

# Update the SmallBusinessInsurance class to integrate AI and risk-based premiums
class SmallBusinessInsurance:
    def __init__(self, business_name, coverage_type):
        self.business_name = business_name
        self.coverage_type = coverage_type
        self.claims = []
        self.risk_score = RiskAssessment.assess_risk(business_name)
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
    # Create a small business insurance policy
    policy1 = SmallBusinessInsurance("ABC Inc.", "General Liability")
    
    # Display policy information, including risk assessment and premium calculation
    policy1.display_policy_info()
    
    # File a claim
    policy1.file_claim("Property damage due to a fire")
    policy1.file_claim("Customer slip and fall accident")

    # Display updated policy information with claims and adjusted premium
    policy1.display_policy_info()

    # Interact with the AI-powered chatbot
    user_question = "What is my premium?"
    chatbot_response = Chatbot.answer_question(user_question)
    print(f"Chatbot Response: {chatbot_response}")
