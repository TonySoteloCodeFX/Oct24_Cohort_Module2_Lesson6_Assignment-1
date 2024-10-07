def name_check():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Each name must have at least 2 characters.")
    elif not first_name.isalpha() or not last_name.isalpha():
        print("Error: Your name can only contain letters.")
    else:
        print("Your name checks out!")
    
name_check()

