

print("Welcome to Jonatas Flight Club.")
print("We find the best flight deals and email you.")
user_firstname = input("What is your first name?\n")
user_lastname = input("What is your last name?\n")
user_email = input("What is your email?\n")
user_email_confirmation = input("Please type your email again:\n")

while user_email != user_email_confirmation:
    print("Emails are not matching. Please try again.")
    user_email = input("What is your email?\n")
    user_email_confirmation = input("Please type your email again:\n")

print("You're in the club!")


