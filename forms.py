import conf
def first_form():
    while True:
        name = input("Enter your name: ")
        if name.strip() == "":
            print("Name cannot be empty. Please try again")
        else:
            break
    print("Select a food:")
    foods = list(conf.food.keys())
    for i, food in enumerate(foods, start=1):
        print(f"{i}. {food}")
    choice = int(input("Enter the number of your chosen food: "))

    selected_food = foods[choice - 1]
    while True:
        email = input("Enter your email: ")
        if email.strip() == "":
            print("Email cannot be empty. Please try again")
        else:
            break
    note = input("Note: ")
    
    print(f"Name: {name}")
    print(f"Selected Food: {selected_food}")
    return name, selected_food, email ,note
