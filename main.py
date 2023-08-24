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
    git_operations.clone_repo("./WebApp","github.com/AMendez-SBSSecurity/DevSecOps-WebApp-Demo.git")
    if choice == 1:
        name, food, note = forms.first_form()
        app_logic.logic(False, name, food, note)
    elif choice == 2:
        name, food, note = forms.first_form()
        app_logic.logic(True, name, food, note)
    elif choice == 3:
        name, food, note = forms.first_form()
        app_logic.third_logic(name, food, note)
    else:
        print("Invalid choice, please try again.")
        main()
    if os.path.exists("./WebApp"):
        os.system('cmd /c "rmdir /s /Q WebApp"')

if __name__ == "__main__":
    main()