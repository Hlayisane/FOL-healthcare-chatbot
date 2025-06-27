# Knowledge base (aligned with recommendation keys)
condition_rules = {
    "influenza": {"fever", "cough", "sore_throat"},
    "cold": {"sneezing", "runny_nose", "mild_fever"},
    "malaria_infection": {"fever", "chills", "sweating", "headache"},
    "corona_virus": {"fever", "cough", "shortness_of_breath", "loss_of_taste"},
    "throat_infection": {"sore_throat", "swollen_lymph_nodes", "fever"}
}

# Advice base (matches keys above)
recommendations = {
    "influenza": [
        "Get plenty of rest and sleep.",
        "Drink lots of fluids to stay hydrated.",
        "Use over-the-counter medications like paracetamol for fever and pain relief."
    ],
    "cold": [
        "Stay hydrated by drinking warm fluids.",
        "Use a humidifier to ease congestion.",
        "Take vitamin C-rich foods to support your immune system."
    ],
    "malaria_infection": [
        "Seek immediate medical attention and take prescribed antimalarial drugs.",
        "Avoid physical exertion and rest as much as possible.",
        "Keep the room cool and use mosquito nets to avoid further bites."
    ],
    "corona_virus": [
        "Isolate yourself to prevent spreading the virus.",
        "Monitor oxygen levels and seek emergency care if breathing becomes difficult.",
        "Stay hydrated, rest, and follow your doctor's advice regarding antiviral medication."
    ],
    "throat_infection": [
        "Take the full course of antibiotics prescribed by your doctor.",
        "Gargle with warm salt water to ease throat pain.",
        "Avoid sharing utensils or drinks to prevent spreading the infection."
    ]
}

def collect_symptoms():
    print("Enter your symptoms, separated by commas (e.g., fever, cough, headache):")
    input_data = input().strip().lower()
    symptoms = [s.strip() for s in input_data.split(',') if s.strip()]
    return set(symptoms)

def identify_condition(symptoms_input, condition_rules):
    matches = []
    for condition, required_symptoms in condition_rules.items():
        if required_symptoms.issubset(symptoms_input):
            matches.append(condition)
    return matches

def fetch_recommendations(condition_name, recommendations):
    return recommendations.get(condition_name, ["No guidance found for this case."])

def healthbot_session(condition_rules, recommendations):
    print(" Welcome to MediBot!")
    print("Describe your symptoms, and I'll help identify common conditions.")


    while True:
        symptom_set = collect_symptoms()

        if not symptom_set:
            print("No symptoms detected. Try again.")
            continue

        print(f"\nYou mentioned: {', '.join(symptom_set)}")

        conditions_found = identify_condition(symptom_set, condition_rules)

        if conditions_found:
            print("\nPossible condition(s) based on your symptoms:")
            for condition in conditions_found:
                print(f"- {condition.replace('_', ' ').capitalize()}")
                suggestions = fetch_recommendations(condition, recommendations)
                print("  Suggested steps:")
                for tip in suggestions:
                    print(f"  • {tip}")
        else:
            print("\nI couldn't determine a condition based on the information provided.")
            print("Consider speaking to a healthcare professional.")

        again = input("\nWould you like to assess more symptoms? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print(" Thanks for using MediBot. Take care!")
            break

# Run the chatbot
if __name__ == "__main__":
    healthbot_session(condition_rules, recommendations)
