import conf
def first_form():
    name = input("Enter your name: ")
    print("Select a food:")
    foods = list(conf.food.keys())
    for i, food in enumerate(foods, start=1):
        print(f"{i}. {food}")
    choice = int(input("Enter the number of your chosen food: "))
    selected_food = foods[choice - 1]
    note = input("Note: ")
    
    print(f"Name: {name}")
    print(f"Selected Food: {selected_food}")
    return name, selected_food, note
