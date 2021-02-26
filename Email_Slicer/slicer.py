
email = input("Enter your email address: ")

if '@' in email and '.com' in email:

	user_name = email[:email.index('@')]
	domein_name = email[email.index('@')+1:]
	print(f"Your user name is {user_name} and your domain name is {domein_name}")
else:
	print("Please enter your email correctly")
