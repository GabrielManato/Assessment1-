#04-PrimitiveQuiz

# List of countries and their capitals
countries_and_capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "Belgium": "Brussels",
    "Netherlands": "Amsterdam",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Portugal": "Lisbon"
}

# Loop through each country and ask the user for the capital
for country, capital in countries_and_capitals.items():
    answer = input(f"What is the capital of {country}? ").strip()
    
    # Check if the answer is correct (ignoring case)
    if answer.lower() == capital.lower():
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {capital}.")
