#03-Biography

name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)  
        break
    else:
        print("Invalid input. Please enter a numeric value for age.")
person_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}
print(person_info["name"], person_info["hometown"], person_info["age"], sep='\n')
