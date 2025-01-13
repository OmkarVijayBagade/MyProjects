#email validator 
def validate_email(email):
    if "@" in email:
        return True
        
    else:
        return False


#phone validator
def validate_phone(phone):
    if len(phone) == 10 and phone.isdigit():
        return True
    else:
        return False

email = input("Enter your email:")
phone = input("Enter your phone number:")

if validate_email(email) and validate_phone(phone):
    print("Valid")
else:
    print("Not Valid")


