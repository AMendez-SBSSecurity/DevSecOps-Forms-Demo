import forms
import git_operations
import app_logic
import os

def main():
    print("Menu:")
    print("1. First Form")
    print("2. Second Form")
    print("3. Third form")
    
    choice = int(input("Select a form (1 or 2): "))
    if choice == 1:
        name, food, email ,note = forms.first_form()
        app_logic.logic(False, name, food, email ,note)
    elif choice == 2:
        name, food, email, note = forms.first_form()
        app_logic.logic(True, name, food, email ,note)
    elif choice == 3:
        name, food, email, note = forms.first_form()
        app_logic.third_logic(name, food, email ,note)
    else:
        print("Invalid choice, please try again.")
        main()
    if os.path.exists("./WebApp"):
        os.system('cmd /c "rmdir /s /Q WebApp"')

if __name__ == "__main__":
    main()